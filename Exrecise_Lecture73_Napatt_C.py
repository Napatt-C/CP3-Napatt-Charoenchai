systemMenu = {"Pizza" : 259,
              "Chicken" : 79,
              "Spagetti" : 80,
              "Soup" : 50,
              "Water" : 10}
menuList = []

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

def showBill():
    print("--- P's food ---")
    sum_price = 0
    total_price = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        sum_price = menuList[number][1]
        total_price = sum_price + total_price
    print("Total price : ", total_price, " THB")


showBill()