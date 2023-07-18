import string as st
import random as rd


def letra_minuscula():
    alfabeto_min = st.ascii_lowercase
    letras_minúsculas = list()

    for i in alfabeto_min:
        letras_minúsculas.append(i)
   
    return rd.choice(letras_minúsculas)

def letra_maiuscula():
    alfabeto_maius = st.ascii_uppercase
    letras_maiusculas = list()
    
    for i in alfabeto_maius:
        letras_maiusculas.append(i)
        
    return rd.choice(letras_maiusculas)


def digito():
    digitos = st.digits
    lista_de_digitos = list()
    
    for i in digitos:
        lista_de_digitos.append(i)
        
    return rd.choice(lista_de_digitos)

def caractere_especial():
    caracteres_especiais = st.punctuation
    lista_de_caracteres = list()
    
    for i in caracteres_especiais:
        lista_de_caracteres.append(i)
        
    return rd.choice(lista_de_caracteres)

def gerar_senha(lista):
    
    rd.shuffle(lista)
    senha = ''
    for char in lista:
        senha += char
    return senha

