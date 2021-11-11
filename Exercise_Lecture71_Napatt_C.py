menuList = []
priceList = []

def showBill():
    print("----- P's Food ----")

    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

    print("Total price :" + str(sum(priceList)) + " THB")

while True:
    menuName = input("Please enter menu : ")
    totalPrice = 0
    if (menuName.lower() == "exit"):
        break
    else :
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)


showBill()


