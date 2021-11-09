user_input = int(input("Number :"))

for i in range(user_input):
    ast = "*"
    create_aster = ast * (2 * i + 1)
    space_ast = " " * (user_input - (i+1))
    print(space_ast, create_aster)

