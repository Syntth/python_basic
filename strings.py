import random
#Some excerxises with string methods
fer = 'fer'
fer.upper()
fer.capitalize()
fer.lower()
fer.casefold()

#Slices examples
word = 'ferrocarril'
word1 = word [1:4]
word2 = word [1:8]
word3 = word [::-1]
word4 = word [:8:3] #should print fra
word5 = word [::2]
word6 = word [:]
print(word)  #should print ferrocarril
print(word1) #should print err
print(word2) #should print errocar
print(word3) #should print ferrocarril mirrowed
print(word4) #should print fra
print(word5) #should print froarl
print(word6) #should print the entire word

#For loop range examples
rango = range (10) #generates a range object

for i in range(10): #prints i 10 times starting from 0
    print(i)


#List examples
countries = ['México', 'Venezuela', 'Colombia', 'Argentina']
ages = [12, 18, 24, 34, 50]

#List + * and append
a = [1,2]
b = [3,4]
c = a + b
d = a*2
print(c)    #Should print [1, 2, 3, 4]
print(d)    #Should print [1, 2, 1, 2]

rand = []
for i in range(0, 10):
    rand.append(random.randint(0, 15))

print(rand) #Should print a random list

ordered_num = sorted(rand)
print(ordered_num) #Should primt random list sorted


#Dictionaries examples
keys = ['a', 'b', 'c', 'd', 'e']

vowels = dict.fromkeys(keys)

print(vowels)   #Should print {'o': None, 'i': None, 'u': None, 'a': None, 'e': None}

