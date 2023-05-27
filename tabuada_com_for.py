num = int(input('De qual número você deseja a tabuada: '))
for contador in range(10):
    print('{} x {} = {}'.format(num, contador+1, num * (contador +1)))