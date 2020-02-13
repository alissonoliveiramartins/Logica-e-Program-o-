pessoa = {'nome':''}

def new_pessoa():
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['idade'] = int(input('Digite  a idade: '))
    pessoa['peso'] = float(input('Digite o peso: '))
    pessoa['altura'] = float(input('Digite a altura: '))
    return pessoa

def envelhecer(pessoa,anos=1):
    pessoa['idade'] += anos
    if idade > 21 :
        pessoa['altura'] -= 0.5

def engordar(pessoa, peso=2):
    pessoa['peso'] += peso
    if pessoa['peso'] > 80:
        print('Você preciade de uma dieta ')
    

def emagrecer(pessoa, peso=1):
    pessoa['peso'] -= 1
    if pessoa['peso'] < 45 and pessoa['idade'] > 17:
        print('Você precisa comer mais')

def crescer(pessoa, centimentros=1):
    pessoa['altura'] += centimentros
    
    
def infitos_args(*args):
    print('menu')
    for i in args:
        print(i, ': ')

def mostrar_pessoa(pessoa):
    #for i in pessoa:
    #print(f'{i} = {pessoa[i]}')
    print(pessoa)

me = ['NOVA PESSOA','ENVELHECER','ENGORDAR','EMAGRECER','CRESCER','MOSTRAR PESSOA',]

def menu(tam=20):
    print('='*tam)
    print('Menu'.upper().center(tam, '_'))

    for i in range(len(me)):
        print('{} => {}'.format(i+1, me[i]))
        
    print('='*tam)
    
    

pessoas = []
op = 1
while 1 <= op <= 6:
    menu(30)
    op = int(input(' > '))
    
    if op == 1:
        x = new_pessoa()
       
        print(('\n DESEJA SALVAR ? \n S/N :')
        xop = input(' > ')
        if xop.upper() == 'S':
            pessoas.append(x)
        else:
            pass
        
    if op == 6:
        mostrar_pessoa(pessoas)
        
    



#if __name__ == '__main__' :
    
    

    
#  Argumentos INFINITOS  
#infitos_args()
#infitos_args(1)
#infitos_args(1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0, 1, 1, 312, 3123,1, 3,1, 2
