#!/usr/bin/python3

import paramiko
from contextlib import contextmanager
host = '66.228.54.140'
username = input('What is your username?')
password = input('Please enter your password:')
#def create_ssh(host=host, username=username, password=password):
#   ssh = paramiko.SSHClient()
#    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#    try:
#       print ("creating connection")
#       ssh.connect(host, username=username, password=password)
#       print ("connected")
#       yield ssh
#    finally:
#       print ("closing connection")
#       ssh.close()
#       print ("closed")
       
# create_ssh

ssh = paramiko.SSHClient()
#ssh.connect(server=host, username=username, password=password)
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(pwd + "/n")

