#!/usr/bin/python

import sys
import time
import select
import paramiko

host = 'root@66.228.54.140'
#username = input('What is your username?')
password = input('Please enter your password:')
i = 1

#
# Try to connect to the host.
# Retry a few times if it fails.
#
while True:
    print "Trying to connect to %s (%i/30)" % (host, i)

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host)
        print "Connected to %s" % host
        break
    except paramiko.AuthenticationException:
        print "Authentication failed when connecting to %s" % host
        sys.exit(1)
    except:
        print "Could not SSH to %s, waiting for it to start" % host
        i += 1
        time.sleep(2)

    # If we could not connect within time limit
    if i == 30:
        print "Could not connect to %s. Giving up" % host
        sys.exit(1)

# Send the command (non-blocking)
stdin, stdout, stderr = ssh.exec_command("my_long_command --arg 1 --arg 2")

# Wait for the command to terminate
while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        if len(rl) > 0:
            # Print data from stdout
            print stdout.channel.recv(1024),

#
# Disconnect from the host
#
print "Command done, closing SSH connection"
ssh.close()