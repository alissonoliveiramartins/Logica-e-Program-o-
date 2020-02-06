bola = {'cor':'VERMELHA',
        'circunferencia':30,
        'material':'LINHO'}

def mudar_cor():
    bola['cor']=input('NOVA COR: ')
    
def mostrar_cor():
    print(bola['cor'])


quadrado = {'tamanho_lado':50}

def mudar_lado(quadrado):
    quadrado['tamanho_lado']= int(input('Digite o novo lado: '))
    quadrado['tamanho_lado']= quadrado['tamanho_lado']*2
    print(quadrado['tamanho_lado'])


retangulo = {'lado_a':'',
             'lado_b':''}

def mudar_lados(retangulo):
    retangulo['lado_a']= int(input('Digite o novo lado_A: '))
    retangulo['lado_b']= int(input('Digite o novo lado_B: '))

def calcular_area(retangulo):
    return retangulo['lado_a']*retangulo['lado_b']


                     
if __name__ == '__main__':
    mudar_cor()
    mostrar_cor()
    mudar_lado(quadrado)


    
