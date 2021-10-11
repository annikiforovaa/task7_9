def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def schot (user):
    if (isint(user)):
        user = int(user)
    else:
        schot (input("Введите целое десятичное число: "))
        return
    
    k = 0
    N = user
    
    if user < 0:
        user *=-1
    
    while user > 0:
        x = user % 10
        user = user // 10
        if (x!=0) and (x%2==0):
            k = k+1
            
    print("Сумма четных цифр в числе ", N ," равна ", k)
schot (input("Введите целое десятичное число: "))