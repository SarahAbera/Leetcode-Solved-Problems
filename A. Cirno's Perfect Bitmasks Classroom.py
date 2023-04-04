testcases = int(input())
for _ in range(testcases):
    x = int(input())
    if x == 1:
        print(3)
    elif  x % 2 != 0:
        print(1)
    
    else:
        count = 0
        for i in range(32):
            if x & (1 << i):
                count += 1
        if count == 1:
            print(x + 1)
        else:
            powOfTwo = 2
            while powOfTwo <= 1073741824:
                if x & powOfTwo > 0:
                    print(powOfTwo)
                    break
                powOfTwo *= 2
            
