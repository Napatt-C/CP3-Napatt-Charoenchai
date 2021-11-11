menuList = []

def showBill():
    print("----- P's Food ----")

    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])



while True:
    menuName = input("Please enter menu : ")
    totalPrice = 0
    if (menuName.lower() == "exit"):
        break
    else :
        menuPrice = int(input("Price :"))
        menuList.append([menuName, menuPrice])

showBill()


