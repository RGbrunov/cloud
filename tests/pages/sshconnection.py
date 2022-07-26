from sys import stdout

import paramiko

command = "df"

# Update the next three lines with your
# server's information

host = "52.118.63.110"
username = "root"
password = "dmf2HUCuE85s"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command("df")
print(stdout.read().decode())
client.close()
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(host, username, password)
#
# stdin, stdout, stderr = ssh.exec_command(command)
# lines = stdout.readlines()
# print(lines)
