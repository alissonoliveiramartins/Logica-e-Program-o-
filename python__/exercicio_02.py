user = {'msg':'',
        'comments':[],
        'r_twt':'',
        'likes':''}

def new_twt():
    #devereceber dois comentarios
    user['msg']=input('Digite a msg: ')
    user['comments']=[]
    for i in range(2):
        user['comments'].append(input(f'Comentario {i+1}: '))
        
    user['r_twt']=int(input('Digite r_twt: '))
    user['likes']=int(input('Quantidade de likes: '))
    return user

    
def print_twt(user):
    print(user['msg'])
    print(len(user['comments']),'\t', user['r_twt'],'\t S2',user['likes'])

if __name__ == '__main__' :
    twt = new_twt()
    print_twt(twt)
