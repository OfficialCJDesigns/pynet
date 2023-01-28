import paramiko

# create an SSH client
client = paramiko.SSHClient()

# add the host key automatically
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connected server counter
counter = 0

try:
    # connect to the main server
    client.connect(hostname='main_server.com', username='main_user', password='main_password')
    counter += 1
    print(f'Connected to main server, connected servers: {counter}')
    # listen for commands
    while True:
        # get the command
        stdin, stdout, stderr = client.exec_command('read command')
        command = stdout.read().decode().strip()

        # check if command is 'exit'
        if command == 'exit':
            counter -= 1
            print(f'Exiting, connected servers: {counter}')
            break

        # execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # print the output
        print(stdout.read().decode())
except Exception as e:
    print(f'Error connecting to main server: {e}')
finally:
    # close the connection
    client
