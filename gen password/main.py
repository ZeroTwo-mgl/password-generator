from random import *

caractère=['A','B','C','D','E','F','ù','%','$','/','w','z','y','1','9','3']

print("""

░██╗░░░░░░░██╗░█████╗░██╗░░██╗███████╗██╗░░██╗░░░██████╗░██╗░░░██╗
░██║░░██╗░░██║██╔══██╗██║░██╔╝██╔════╝██║░██╔╝░░░██╔══██╗╚██╗░██╔╝
░╚██╗████╗██╔╝███████║█████═╝░█████╗░░█████═╝░░░░██████╔╝░╚████╔╝░
░░████╔═████║░██╔══██║██╔═██╗░██╔══╝░░██╔═██╗░░░░██╔═══╝░░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║░╚██╗███████╗██║░╚██╗██╗██║░░░░░░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░""")
 
longueur= int (input ('enter the length of the passwords :  '))

nb_pwd=int (input('how many passwords do you want to generate : '))

def pwd (longueur) :
	pwd=str()
	shuffle (caractère)
	for x in range (longueur):
	    pwd+=caractère [x]

	print (pwd)

for x in range(nb_pwd):
	pwd (longueur)

input ()