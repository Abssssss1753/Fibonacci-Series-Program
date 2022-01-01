import time

def Fibo_Iterative(n):
    prev_Num = 0
    current_Num = 1
    for i in range(1,n):
        perpre_Num = prev_Num
        prev_Num = current_Num
        current_Num = perpre_Num + prev_Num
    return current_Num

def Fibo_Recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibo_Recursive(n-1) + Fibo_Recursive(n-2)

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    init = time.time()
    print(f"1) Using iterative value of fib({num}) is {Fibo_Iterative(num)}")
    print(f"It took {time.time() - init} second for iterative operation")
    print()
    print(f"2) Using recursive value of fib({num}) is {Fibo_Recursive(num)}")
    print(f"It took {time.time() - init} second for recursive operation")

