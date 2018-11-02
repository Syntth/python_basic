import random
#La búsqueda binaria recive 4 parámetros:
#El primero es una lista de datos = data
#El segundo es el número a buscar = target
#el cuarto y quinto son los indices primero y último de la lista = i,j
def binary_search(data, target, i, j):
    if i > j:
        return False

    mid = (i+j) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, i, mid - 1)
    else:
        return binary_search(data, target, mid+1, j)

if __name__ == '__main__':
    data = [random.randint(0,100) for i in range (10)]

    data.sort()

    print (data)
    target =int(input('Que numero deseas encontrar?'))
    found = binary_search(data, target, 0, len(data)-1)
    print (found)