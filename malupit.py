cart = []

def addcart():
    while True:
        
        print("1. Jumbo Hotdog : 50 pesos")
        print("2. MalaJuicy Hamburger : 60 pesos")

        cart.append()

        pass
def merienda():
    while True:
        try:
            print("")
            print("1. Add to cart")
            print("2. Show cart")
            print("3. Remove item in the cart")
            print("4. Show price list")
            print("5. Purchase cart")
            print("6. Exit")
            print("")
            num = int(input("Enter a number from 1-6: "))

            match num:
                case "1":
                    addcart()
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    break

        except ValueError:
            print("")
            print("Invalid input, choose a numbers 1-6")
            continue

merienda()
