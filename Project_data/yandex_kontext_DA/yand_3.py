def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def check_win(n, k):
    while True:
        for i in range(k):
            if is_prime(n + i + 1):
                return 'YES'                
        
        plus = 0

        if is_prime(n + k + 1) or (not is_prime(n + k) and is_prime(n + 3*k)):
                return 'NO'

        for i in range(k):
            # проверяем след. интервал n + k где есть вариант сделать простое число            
            if not is_prime(n + k + i + 1):
                plus += 1
            else:
                break
        
        if not is_prime(n + k + k):
            n += 1
        else:
            n += (plus + k)
            

input_str = input()
n, k = input_str.split()
n = int(n)
k = int(k)

print(check_win(n, k))


'''
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

def check_win(n, k):
    while True:
        for i in range(k):
            if is_prime(n + i + 1):
                return 'YES'                
     
        if not is_prime(n + k + 1):
            n += 2
        else:
            return 'NO'
         
input_str = input()
n, k = input_str.split()
n = int(n)
k = int(k)

print(check_win(n, k))

'''