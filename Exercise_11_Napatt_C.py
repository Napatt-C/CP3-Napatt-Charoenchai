user_input = int(input("Number :"))

for i in range(user_input):
    create_aster = "*" * (2 * i + 1)
    space_ast = " " * (user_input - (i+1))
    print(space_ast, create_aster)

