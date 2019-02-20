import pizza as p
#A way to import other modules
#Can use Alias to make it easier to use other modules

p.make_pizza("16", "Pepperoni")
p.make_pizza("23", "Cheese", "hAMEs")

#from pizza import make_pizza
#Another way to import a function from another modules

#from module_name import function1, function2, function3
#A way to import multiple functions and not the whole module


#from pizza import *
#this imports all of the functions from the module pizza
#Might cause confusion as multiple functions might have the same names
