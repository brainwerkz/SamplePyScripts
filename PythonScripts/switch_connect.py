#!/usr/bin/python2.7

__author__ = 'timmattison'

import pyuda
import re
import paramiko
import sys
import time
import calendar
from calandar import timegm

# For debugging only
# paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

# This is part of the regex we use to look for the interfaces we care about
interface_regex = "Fe1\/0\/"

# These are the operation we support
status_operation = "status"
on_operation = "on"
off_operation = "off"
valid_operations = [status_operation, on_operation, off_operation]

def send_string_and_wait_for_string(command, wait_string, should_print):
    # Send the su command
    shell.send(command)

    # Create a new receive buffer
    receive_buffer = ""

    while not wait_string in receive_buffer:
        # Flush the receive buffer
        receive_buffer += shell.recv(1024)

    # Print the receive buffer, if necessary
    if should_print:
        print (receive_buffer)

    return receive_buffer

def validate_operation(operation):
    # Is this an operation we support?
    if(not operation in valid_operations):
        # No, tell them and bail out
        print (operation) + (" is not a valid operation")
        sys.exit(-1)

# Get the command-line arguments
switch_ip_address, username, password, operation, port_number = pyuda.get_command_line_arguments(["Switch IP address", "Admin username", "Admin password", status_operation + ", " + on_operation + ", or " + off_operation, "Port number"])

# Make sure the operation makes sense
validate_operation(operation)

# Create an SSH client
client = paramiko.SSHClient()

# Make sure that we add the remote server's SSH key automatically
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the client
client.connect(switch_ip_address, username=username, password=password, allow_agent=False, look_for_keys=False)

# Create a raw shell
shell = client.invoke_shell()

# Wait for the prompt
send_string_and_wait_for_string("", "#", False)

# Disable more
send_string_and_wait_for_string("terminal length 0\n", "#", False)

# Which command are we trying to run?
if((operation == on_operation) or (operation == off_operation)):
    # Trying to do on or off

    # Send the "conf t" command
    send_string_and_wait_for_string("conf t\n", "(config)#", False)

    # Send the interface command
    send_string_and_wait_for_string("interface Gi1/0/" + str(port_number) + "\n", "(config-if)#", False)

    # Build the power command
    power_command = "power inline "

    # What kind of operation is this?
    if(operation == off_operation):
        # Power off, "never" means off
        power_command += "never"
    else:
        # Power on, "auto" means on (there are other options but this is the simplest)
        power_command += "auto"

    # Add the carriage return
    power_command += "\n"

    # Send the power command
    send_string_and_wait_for_string(power_command, "(config-if)#", False)
elif(operation == status_operation):
    # Get the status of all of the PoE ports
    power_data = send_string_and_wait_for_string("show power inline\n", "#", False)

    # Split the data into lines
    power_data_lines = power_data.splitlines()

    # We haven't found what we're looking for yet
    found = False

    # Loop through all of the lines
    for power_data_line in power_data_lines:
        # Does this look like the interface we want?
        if(not re.match("^" + interface_regex + port_number + "\s", power_data_line)):
            # No, keep going
            continue

        # Found the interface we want, split up the fields
        power_data_fields = power_data_line.split()

        # Get the second field which is the power state field and print it
        print (power_data_fields[1])

        # We found what we needed
        found = True

        # Get out of the for loop
        break

    # Did we find what we needed?
    if not found:
        # No, let the user know
        print ("Did not find port ") + port_number

else:
    # This is an operation we didn't handle
    print (operation) + (" not handled")

# Close the SSH connection
client.close()
