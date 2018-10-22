clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already exists')

def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('Hi! Welcome to my program')
    print('*' * 50)
    print('What would you like to do?')
    print('[C] Create client')
    print('[D] Delete client')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command.capitalize()

    if command == 'C' or command == 'c':
        client_name = input('Type new client name: ')
        create_client(client_name)
        list_clients()
    elif command == 'D' or command == 'd':
        pass
    else:
        print('Invalid command')
