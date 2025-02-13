def identificador(*args):
    i = 0
    status = False
    for val in args:
        if  args[i] == 0 and args[i+1] == 0:
            status = True
            print(f"{args} >>> {status}")
            break
        i +=1
    if status == False:
            print(f"{args} >>> {status}")

identificador(1,2,6,2,6,9,8,7,4,5,0,0)