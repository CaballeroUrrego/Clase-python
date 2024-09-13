
#Dia 1 3
# /07/24

# Variables 
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable =5
print(my_int_variable)

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables y un print
print(my_string_variable ,str (my_int_to_str_variable),my_bool_variable)
print("Este es el valor de:",my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))


#variables en una sola linea ¡Cuidado con abusar de esta sintaxis 
name, surname, alias, age ="Sebastian","Urrego","Caballero",24
print("Me llamo:",name, surname,".Mi edad es: " ,age,". y mi alias es",alias)

#Inputs
#name = input('¿Cuál es tu nombre? ')
#age = input('¿Cuántos años tienes? ')
#print(name)
#print(age)

#Cambiamos su tipo
name = 35
age ="Urrego"
print(name)
print(age)

#Forzamos el tipo
address: str= "My dirrecion"
address = 32
print(type(address))