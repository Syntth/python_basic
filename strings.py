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
print(word)  #should print ferrocarril
print(word1) #should print err
print(word2) #should print errocar
print(word3) #should print ferrocarril mirrowed
print(word4) #should print fra
print(word5) #should print froarl