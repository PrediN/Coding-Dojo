# importação de bibilioptecas

import time
import random

# Declaração de variaveis

y = 0

# Declaração de função

def explorarPlaneta(iniciar):
    print()
    while iniciar != 's':
        if iniciar == 's':
            print()
            print('Viagem iniciar com sucesso!')
            print()
            for i in range (10,0,-1):
                print(f"Despressurição em: {i}")
                time.sleep(1) 
            break
        
        elif iniciar == 'n':
            iniciar = str(input('Desejar iniciar? (S/N) ')).lower().strip()
            print()
            
        
        else:
            print('Insira uma confirmação valida')
            iniciar = str(input('Deseja iniciar a viagem?  (S/N) ')).lower().strip()
            print()

    if iniciar == 's':
        print('Viagem iniciar com sucesso!')
        for i in range (10,0,-1):
            print(f"Despressurição em: {i}")
            time.sleep(1)
        print()
            
def obstaculo(confirmacao):
    print()
    print("Obstáculo encontrado")
    print("Opção 1: Escalar")
    print("Opção 2: Contornar")
    print()
    confirmacao = int(input("Qual a opção desejada? "))
    
    if confirmacao == 1:
        escalada()
    else:
        contornar()

def escalada():
    x = random.randint(1, 2)
    if x == 1:
        print()
        print(10*'=')
        print("Parabéns passaram o obstaculo!")
        print(10*'=')
        print()
        a = random.randint(1, 2)
        if a == 1:
            minerais()
        else:
            vida()
    else:
        print("Que pena, não passaram")
        obstaculo(y)
            

def contornar():
    obstaculo(y)

def minerais():
    print()
    print(10*"=")
    print("Encontrado minerais")
    print("Realizado a coleta de dados da area")
    print(10*"=")
    print()
    retorno = str(input('Deseja retornar?  (S/N) : ')).strip().lower()

    if retorno == 's':
        print()
        print('Viagem finalizada')
        print()
                
    else: 
        obstaculo(y)

def vida():
    print()
    print(10*"=")
    print("Encontrada formas de vida")
    print("Realizado a coleta de dados da area")
    print(10*"=")
    print()
    retorno = str(input('Deseja retornar?  (S/N): ')).strip().lower()
    if retorno == 's':
        print()
        print('Viagem finalizada')
        print()
    else: 
        obstaculo(y)
           

# APRESENTAÇÃO DE RESULTADOS

init = str(input("Deseja iniciar a viagem? ")).lower().strip()
explorarPlaneta(init)
obstaculo(y)







