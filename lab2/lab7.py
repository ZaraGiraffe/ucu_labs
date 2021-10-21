

def test(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    try:
        a = int(input())
    except:
        print("Error")
        return 
    if (a <= 2):
        print("Error")
        return
    
    i = 2
    while(True):
        if (test(i) and a % i):
            print(i)
            return
        i += 1
        
main()




    



