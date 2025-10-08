while True:
    n = int(input("enter the number: "))
    for i in range(0, 11):
        print(n, "*", i, "=", n*i)

    again = input("again? (y/n): ")
    if again.lower() == "n":
        break

