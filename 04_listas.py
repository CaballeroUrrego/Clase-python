### Listas ###

my_list = list()
my_other_list =  []

print(len(my_list))

my_list = [35, 24 ,62 ,52, 30, 30,17]

print(my_list)
print(len(my_list))

my_other_list=[23,1.60, "Sebastian","Urrego"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#Contar elementos dentro de la propia lista
print(my_list.count(30))


age,height,name,surname=my_other_list
print(name)

name, height, age, surname=my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3],

print(age)

print(my_list +my_other_list )