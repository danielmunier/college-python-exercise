#not finished
from random import randint
from os import system as sys


inscricoesDB = dict()

#Função na qual irá armazenar inscrições para dentro de um dicionário/txt
def new_registry():
    try:
        while True:  
                #Recebe as entradas do usuário
                user_name = str(input('Digite o nome do usuário: '))
                email = str(input('Digite o email do usuário: ')).replace(' ','')
                telefone = (input('Digite o telefone do usuário: ')).replace(' ','')
                curso = str(input('Qual é o curso do usuário? '))
                telefone = int(telefone)

                #Gera um número entre 0 e 999 para cada usuário cadastrado
                voucher = randint(100,999)

                #Envia para um txt
                with open('dados.txt','a') as file:
                    file.write(f'"Voucher: {voucher}, Nome: {user_name}, email:{email}, telefone: {telefone}, curso:{curso}",\n')
                    file.close()

                #Caso o Voucher gerado já se encontra no dicionário, então o programa iniciará um loop até gerar um Voucher totalmente novo
                if voucher in inscricoesDB:
                    while voucher in inscricoesDB:
                        voucher = randint(0,999)
                        if voucher in inscricoesDB:
                         continue
                        else:
                            break

                #Envia as informações para o dicionário
                inscricoesDB[voucher] = {'Voucher': voucher,'Nome': user_name,'email':email,'telefone': telefone,'curso':curso}
               
                #Verifica a necessidade do usuário de cadastrar mais pessoas no dicionário
                continuar = int(input('Deseja continuar? 1 - Sim  2 - Não'))
                sys('cls')

                if continuar == 1:
                    continue
                elif continuar == 2:
                    return ''

    except ValueError:
            print('Valor inválido')
    except:
            print('Algo inesperado aconteceu...')
    
def show_registry(): #Função na qual irá mostrar os cadastrados presentes no dicionário
    sys('cls')
    if len(inscricoesDB) == 0: #Caso não tenha nenhum elemento dentro do dicionário
        print('Nenhuma inscrição cadastrada')
        
    else:
        print(f'Total de {len(inscricoesDB)} usuários cadastrados!') #Mostra o total de usuários cadastrados no dicionário
        for i in inscricoesDB:
           print(f'''
            Voucher:  {i}
            Nome: {inscricoesDB[i]['Nome']}
            Email: {inscricoesDB[i]['email']}
            Telefone: {inscricoesDB[i]['telefone']}
            Curso: {inscricoesDB[i]['curso']}''')

    input('Aperte qualquer tecla para continuar...')
    sys('cls')
        
#Menu de opções para chamar as funçoes do programa
def menu():
    
        while True:
            try:
                print('--'*10,'MENU','--'*10)
                print('1  -  Nova inscrição\n'
                    '2  -  Visualizar inscrições\n'
                    '0  -  Sair\n')

                #Recebe a escolha do usuário
                user_choice = int(input('Escolha: : '))
                if user_choice not in [1,2,0]: #CASO A ESCOLHA DO USUÁRIO NÃO ESTEJA ENTRE AS OPÇÕES DO MENU
                    sys('cls')
                    print('Erro: Opção inválida!')
                    continue

                elif user_choice == 1:#Chama a função inscrição para cadastramento de usuários no dicionário
                    new_registry() 

                elif user_choice == 2:#Chama a função que irá mostrar todos os usuários cadastrados
                    show_registry()

                elif user_choice == 0:#Encerra o programa
                    sys('cls')
                    print('Programa encerrado. Até mais!')
                    break

            except ValueError:  #CASO O USUÁRIO PASSE UMA OPÇÃO INVÁLIDA
                sys('cls')
                print('Erro: Opção inválida!')
                continue

            except KeyboardInterrupt: #CASO O USUÁRIO ENCERRE O PROGRAMA VIA TERMINAL
                sys('cls')
                print('Programa encerrado pelo usuário!')
                break

            except: #CASO OCORRA QUALQUER ERRO
                print('Algo inesperado aconteceu...')

        
def delete_registry():
    pass

def search_registry():
    pass
    

menu()









