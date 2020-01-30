item = {'ide':'',
        'categ':'',
        'img':'',
        'nome':'',
        'aval':'',
        'n_ofe':'',
        'preco':'',
        'div':'',
        'c_base':''}

def new_item():
    item['ide'] = input('Digite ide : ')
    item['categ'] = input('Digite categ : ')
    item['img'] = input('Digite img : ')
    item['nome'] = input('Digite nome : ')
    item['aval'] = int(input('Digite aval : '))
    item['n_ofe'] = int(input('Digite n_ofer : '))
    item['preco'] = float(input('Digite preco : '))
    item['div'] = int(input('Digite div : '))
    item['c_base'] = input('Digite c_base : ')
    return item



def print_item(item):
    for i in item:        
        print(item[i])

if __name__ == '__main__' :
    meu_item = new_item()
    print_item(meu_item)
    
