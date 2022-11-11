User = input("User Name")
Password = input("Password")
if User == "1234" and Password == "1234":
    print("----------------------------------")
    print("ฺBJA Shop VAT INVOICE")
    print("----------------------------------")
    print("1 CPU case  X 1   :  1000 THB")
    print("2 Keyboard  X 1   :  1200 THB")
    print("3 Mouse     X 1   :  400 THB")
    print("----------------------------------")
    buy = input("what you want to buy(type the number)")
    if buy == "1":
        amount=int(input("how much do you want"))
        Toltal = int((amount * 1000))
        print("CPU cause",Toltal,"Bath")
    elif buy == "2":
        amount=int(input("how much do you want"))
        Toltal = int((amount * 1200))
        print("Keyboard",Toltal,"Bath")
    elif buy == "3":
        amount = int(input("how much do you want"))
        Toltal = int((amount * 1400))
        print("Keyboard", Toltal, "Bath")

else: print("Login fail")


