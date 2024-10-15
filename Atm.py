count = 0
while True:
    count += 1
    if count<=3:
        y = input("enter username : ")
        if y == "Pawan@":
            z = input("enter password : ")
            if y == "Pawan@" and z == "1234":
                print("welcome what you want")
                x = ("a) balance check","b) deposit amount","c) withdraw amount ")
                print(x)
                n = input("press : ")
                a, b, c = x
                if n == "a":
                    print("5000")
                    g = ("a) exit","b) continue")
                    print(g)
                    h = input("press : ")
                    a, b = g
                    if h == "a":
                        print("thank you")
                        break
                elif n == "b":
                    q = int(input("how much deposit : "))
                    print(5000+q)
                    print("thank you")
                    break
                elif n == "c":
                    print("how much : ")
                    w = int(input("how much withdraw : "))
                    print(5000-w)
                    print("thank you")
                    break
                else:
                    print("please enter correct character")
            else:
                print("error")
        else:
            print("enter correct details")
    else:
        print("Try again after 24 hours")
        break