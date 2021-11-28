a=0
while a==0:
    x = (input('Введите два слова через пробел: '))
    m=str(' ')
    d=x.find(m)
    if ( d != -1 and x[0]!=m and x[(len(x))-1]!=m and x[d+1:(len(x))-1].find(m)==-1):
        # print('подходит')
        # print(x[0:d][::-1]+m+x[d+1:len(x)][::-1])
        text1=x[0:d][::-1]
        text2=x[d+1:len(x)][::-1]
        print (text1.capitalize()+m+text2.capitalize())
        break
    else:
        print('Вы ввели не правильно. Повторите.')
