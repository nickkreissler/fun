def manhatten(int,inte):
    l = getgrid(int,inte)

    x=0
    y_position = 0
    x_position = 0
    l1 = ['y_position', 'x_position']
    l2= [1,-1]
    while(x < 10000):
        x+=1
        y = random.choice(l1)
        z = random.choice(l2)
        if y == 'y_position':
            if y_position == 0 and z == -1:
                y_position = int-1
                l[y_position][x_position]+=1
            elif y_position == int-1 and z == 1:
                y_position = 0
                l[y_position][x_position] = 1
            else:
                y_position += z
                l[y_position][x_position] = 1
        if y == 'x_position':
            if x_position == 0 and z == -1:
                x_position = inte - 1
                l[y_position][x_position]=1
            elif x_position == inte - 1 and z == 1:
                x_position = 0
                l[y_position][x_position] = 1
            else:
                x_position += z
                l[y_position][x_position] = 1
    for i in l:
        print('{}'.format(l[i]))
    print('\n')



def getgrid(x,y):
    l = {}
    for i in range(x):
        l[i] = []
        for z in range(y):
            l[i] += [0]

    return l
