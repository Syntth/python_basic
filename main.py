clients = 'pablo,ricardo,'
#Crea un cliente, si el cliente ya existe regresa una excepcion
def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already exists')

#Muestra la lista de clientes
def list_clients():
    global clients
    print(clients)

#Recibe 2 parametros para actualizar un cliente, si el cliente no está en la lista manda excepción
def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        print('Client is not in the list')

#Funcion para borrar cliente
def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in the list')

#añade una coma al final del nombre de cada cliente
def _add_comma():
    global clients
    clients += ','

#Da bienvenida y muestra un menu de opciones
def _print_welcome():
    print('Hi! Welcome to my program')
    print('*' * 50)
    print('What would you like to do?')
    print('[C] Create client')
    print('[D] Delete client')
    print('[U] Update client')

#Obtiene el nombre del cliente
def _get_client_name():
    return input('What is the client name: ')


if __name__ == '__main__':
    _print_welcome()

#Guarda el valor ingresado por el usuario y lo pasa a mayus
    command = input()
    command = command.upper()

#Determina que accion tomará dependiendo del input, sino es opción válida regresa una excepción
    if command == 'C':
        client_name = input('Type new client name: ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name: ')
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command')