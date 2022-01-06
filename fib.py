#Write a program for fibonacci numbers

def fib(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Using recursion value of fib({num}) is {fib(num)}")
