"""pessoa = {'nome':'',
          'idade':'',
          'peso':'',
          'altura':''}"""

def new_pessoa(identificador):
    print('='*30)
    print('NOVA PESSOA'.center(30,'_'))
    pessoa = {}
    pessoa['id'] = identificador
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['idade'] = int(input('Digite  a idade: '))
    pessoa['peso'] = float(input('Digite o peso: '))
    pessoa['altura'] = float(input('Digite a altura: '))
    print('='*30)
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
    print('='*30)
    print('PESSOAS:'.center(30,'_'))
    print()
    for i in pessoa:
        for c,v in i.items():
            print(f'{c} = {v}')
    print('='*30)    
    #print(pessoa)

def buscar():
    n = 0
    for dic in pessoas:
        print('BUSCAR POR: '.center(30, '_'))
        for chave in dic.keys():
            n += 1
            print(f'{n} => {chave}')
        break
            
    num = int(input('> '))
    if num == 1:
        chave = 'id'
    elif num == 2:
        chave = 'nome'
    elif num == 3:
        chave = 'idade'
    elif num == 4:
        chave = 'peso'
    elif num == 5:
        chave = 'altura'
    else:
      return 0       
    valor = input(f'Digite o  {chave}\n> ')

    for dic in pessoas:
        if str(dic[chave]).upper().startswith(str(valor).upper()):
            print(dic)    

def deletar():
  ide = int(input('DIGITE O ID PARA PROSEGUIR\n> '))

  for dic in pessoas:
    if str(dic['id']).upper().startswith(str(ide).upper()):
            
      for c,v in dic.items():
        print(f'{c} = {v}')
      print()
      print('DESEJA DELETAR ?'.center(30))
      print('sim(S) | não(N)'.center(30))
      deleta = input('> ')
      if deleta.upper() == 'S':
        pessoas.remove(dic)
      else:
        pass  

def atualizar():
    print('='*30)
    print('ATUALIZAR'.center(30,'_'))
    n = 1
    ide = int(input('DIGITE O ID\n> '))
    
    for dic in pessoas:
        print('='*30)
        print('O QUE DESEJA ATUZALIZAR ?'.center(30, '_'))
        for chave, valor in dic.items():
            if dic['id'] == ide:
                print(f'{n} => {chave.upper()} : {valor}')
            
    atualizar = int(input('> '))
    if atualizar == 1:
        dic['nome'] = input('Digite o novo nome da pessoa: ')
    elif atualizar == 2:
        dic['idade'] = int(input('Digite a nova idade da pessoa: '))
    elif atualizar == 3:
        dic['peso'] = float(input('Digite o novo peso da pessoa: '))
    elif atualizar == 4:
        dic['altura'] = float(input('Digite a nova altura da pessoa: '))
                               

def menu(tam=30):
    print('='*tam)
    print('Menu'.upper().center(tam, '_'))

    for i in range(len(me)):
        print('{} => {}'.format(i+1, me[i]))
        
    print('='*tam)
       
if __name__ == '__main__' :
    
    me = ['NOVA PESSOA','ENVELHECER','ENGORDAR','EMAGRECER','CRESCER','MOSTRAR PESSOAS','BUSCAR','DELETAR','ATUALIZAR']
    pessoas = []
    op = 1
    identificador = 0
    while 1 <= op <= len(me):
        menu()
        op = int(input(' > '))
        if op == 1:
            identificador += 1 #O identificador é o numero do ID da pessoa, A cada nova pessoa criada é icrementado 1 no id
            x = new_pessoa(identificador)
            print('DESEJA SALVAR ?'.center(30,'_'))
            print('sim(S) | não(N)'.center(30))
            xop = input(' > ')
                  
            if xop.upper() == 'S':
                pessoas.append(x)
                print()   
            else:
                pass
            
        if op == 6:
            mostrar_pessoa(pessoas)
            ficar = 1
            while ficar == 1:
              ficar=int(input('0 => MENU PRINCIPAL\n'))
        elif op == 7:
            buscar()
        elif op == 8:
            deletar()
        elif op == 9:
            atualizar()
            

