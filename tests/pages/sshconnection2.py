# -*- coding: utf-8 -*-
import paramiko
# Server related information, below enter your personal username, password, IP and other information
ip = "52.118.63.110"
port = 22
user = "root"
password = "dmf2HUCuE85s"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Establish a connection
ssh.connect(ip, port, user, password, timeout=10)
# Enter the Linux command
stdin, stdout, stderr = ssh.exec_command("pwd")
# Output command execution results
result = stdout.read()
print(result)
# Close the connection
ssh.close()
