import random
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_lenght = int(input("porfavor ingresar la longitud de su contraseña"))
password = ""
for i in range (pass_lenght):
    password += random.choice(elementos)
    
print(password)

