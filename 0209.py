def notation(base, n):
    if n < base:
        print(numberChart[n], end = ' ')
    else:
        notation(base, n//base)
        print(numberChart[n%base],end= ' ')


numberChart = ['0','1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F"]

