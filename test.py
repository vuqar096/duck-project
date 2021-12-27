def decode(*args):
    inputx = None
    result = None
    if len(args)%2!=1:
        inputx = args[0:len(args)-1]
    else:
        inputx = args
    for arg_a,arg_b in zip(inputx[1::2],inputx[2::2]):
        if arg_a == inputx[0]:
            result = arg_b
            break
    if len(args)%2!=1 and result == None:
        result = args[-1]
    return result

# name='esed'
# print(decode(name,'vuqar',5,'sefer',3,'esed',8,10))

xdic = {'name':'Vuqar','yas':'30'}
print(','.join([key+'=\''+value+'\'' for key,value in xdic.items()]))