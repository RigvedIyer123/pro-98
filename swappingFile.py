def swapFile():
    #fileName = input("enter name of file 1")
    #fileName2 = input("enter name of the file 2")

    with open("text1.txt","r") as a:
        dataA = a.read()
    with open("text2.txt","r") as b:
        dataB = b.read()
    with open("text1.txt","w") as a:
        a.write(dataB)
    with open("text2.txt","w") as b:
        b.write(dataA)
swapFile()