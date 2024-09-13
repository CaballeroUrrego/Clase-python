## Strings ##
my_string="Mi String"
my_other_sting= 'Mi otro String'
print (len(my_string))
print (len(my_other_sting))

print(my_string + " " +my_other_sting )   

my_new_line_string = "Este es un String \n Con salto de linea"

print(my_new_line_string )

my_tab_string = "\t Este es un String con tabulacion"

print(my_new_line_string )
print(my_tab_string )

my_scape_string ="\tEste es un String \nEscapado"
print(my_scape_string)

#Formateo


name,surname ,age = "Caballero", "Urrego",23

print("Mi nombre es {} {}y mi edad es {}".format(name,surname ,age))
print("Mi nombre es %s %s y mi edad es %s"%(name,surname ,age))
print("Mi nombre es" + name+ "" + surname + "y mi edad es " + str(age))
print(f"Mi nombre es{name}{surname}y mi edad es {age}")

#Desempaquetado de caracteres 
lenguage="python"
a, b, c, d, e, f =lenguage
print(a)
print(e)

#Division

lenguage_slice=lenguage[1:3] 
print(lenguage_slice[0])

lenguage_slice=lenguage[1:] 
print(lenguage_slice[0])
