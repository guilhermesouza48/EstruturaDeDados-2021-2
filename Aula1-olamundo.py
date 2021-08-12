# print () : exibe informações
print("Hello world!!!")

# input () : permite entrada de informações
name = input("Your name? ")

print (f"Name: {name}")

# int () converte o que foi informado no input () de texto para numero inteiro
years = int (input ("How old are you? "))

if years >= 18:
    print("Can drink!")
    print("Can be arrested!")
else:
    print("Can't drink!")
    print("Cannot be arrested!")