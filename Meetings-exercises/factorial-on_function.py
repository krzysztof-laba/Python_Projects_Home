

def factorial(n):
    n=int(n)
    if n > 1:
        #print(n)
        #print("*")
        return (n*factorial(n - 1))
    else:
        print(n)
        print("--")
        return(1)




print (factorial(n = input("Podaj liczbe: ")))



