import sys

clients = [
	{
		'name': 'Pablo',
		'company': 'Google',
		'email':'pablo@google.com',
		'position':'Software engineer',
	},
	{
		'name': 'Ricardo',
		'company': 'Facebook',
		'email':'rica@facebook.com',
		'position':'Data engineer',
	}
]


def create_client(name):
	global clients

	if client_name not in clients:
		clients.append(name)
	else:
		print('Client already is in the client\'s list')


def list_clients():
	for idx, client in enumerate(clients):
		print('{}: {}'.format(idx, client))


def update_client(client_name, updated_client_name):
	global clients
	if client_name in clients:
		# clients = clients.replace(client_name + ',', updated_client_name)
		index = clients.index(client_name)
		clients[index] = updated_client_name
	else:
		print('Client is not in clients list')


def delete_client(client_name):
	global clients 
	if client_name in clients:
		# clients = clients.replace(client_name + ',','')
		clients.remove(client_name)
	else:
		print('Client does not exists')


def search_client(client_name):
	# clients_list = clients.split(',')
	#for client in clients_list:
	for client in clients:
		if client != client_name:
			continue
		else:
			return True

#   def _add_comma():
# 	global clients
# 	clients += ','


def _print_welcome():
	print('WELCOME TO MY WORLD')
	print('*'*50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[L]ist client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


def _get_client_name():
	client_name = None
	while not client_name:
		client_name = input('What is the client name? ')
		if client_name == 'exit':
			break
	if not client_name:
		client_name: None
		sys.exit()

	return client_name

if __name__ == '__main__':
	_print_welcome()
	command = input()
	command = command.upper();

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		updated_client_name = input('What is the updated client name? ')
		update_client(client_name, updated_client_name)
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print('The client is in the client\'s list')
		else:
			print('The client: {} is not in our client\'s list'.format(client_name))
	else:
		print('Invalid command')


# USO DE LISTAS
# import copy
# countries = ['Ecuador','Venezuela','Colombia','Argentina']
# global_countries = None
# global_countries = copy.copy(countries)
# countries[0] = 'Honduras'

# Suma (+) Concatena dos o más listas:
# a=[1,2]
# b=[3,4]
# a + b --> [1,2,3,4]
# Multiplicación (*) Repite la misma lista:
# a=[1,2]
# a * 2 —> [1,2,1,2]
# Añadir elemento al final de la lista:
# a=[1]
# a.append(2)=[1,2]
# Eliminar elemento al final de la lista:
# a=[1,2]
# b=a.pop()
# a=[1]
# Eliminar elemento dado un indice:
# a=[1,2]
# b=a.pop(1)
# a=[2]
# Ordenar lista de menor a mayor, esto modifica la lista inicial
# a=[3,8,1]
# a.sort() —> [1,3,8]
# Ordenar lista de menor a mayor, esto NO modifica la lista inicial
# a=[3,8,1]
# a.sorted() —> [1,3,8]
# Eliminar elementos de lista Elimina el elemento de la lista dado su indice
# a=[1,2,3]
# del a[0] —> a[2,3]
# Eliminar elementos de lista Elimina el elemento de la lista dado su valor
# a=[0, 2, 4, 6, 8]
# a.remove(6)
# a=[0, 2, 4, 8]
# Range creacion de listas en un rango determinado
# a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
# a=[0,2,4,6,8]
# Tamaño lista len Devuelve el valor del tamaño de la lista:
# a=[0,2,4,6,8]
# len(a)=5

# DICCIONARIOS
# carros = {}
# carros['mercedes'] = 'carros europeo'
# carros['honda'] = 'carros japones'
# carros.keys()   devuelve los id
# carros.values() 
# carros.items() devuelve las llaves y sus valores