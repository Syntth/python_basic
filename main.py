import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _init_clients():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients():
    tmp_table = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames= CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table, CLIENT_TABLE)


#Crea un cliente, si el cliente ya existe regresa una excepcion
def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already exists')

#Muestra la lista de clientes
def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

#Recibe 2 parametros para actualizar un cliente, si el cliente no está en la lista manda excepción
def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client is not in the list')

#Funcion para borrar cliente
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in the list')

#Funcion para buscar un cliente de la lista
def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True

#Da bienvenida y muestra un menu de opciones
def _print_welcome():
    print('Hi! Welcome to my program')
    print('*' * 50)
    print('What would you like to do?')
    print('[C] Create client')
    print('[L] List client')
    print('[U] Update client')
    print('[D] Delete client')
    print('[S] Search client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field

#Obtiene el nombre del cliente
def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name



if __name__ == '__main__':
    _init_clients()
    _print_welcome()

#Guarda el valor ingresado por el usuario y lo pasa a mayus
    command = input()
    command = command.upper()

#Determina que accion tomará dependiendo del input, sino es opción válida regresa una excepción
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)


    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        updated_name = str.lower(input('What is the new client name:'))

        update_client(client_name, updated_name)

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('Client is on the client\'s list')
        else:
            print('Client: {} is not in the client\'s list'.format(client_name))
    else:
        print('Invalid command')

    _save_clients()