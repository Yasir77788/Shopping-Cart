# shopping cart to perform adding, removing, 
# clearing, and showing the items within the cart

# import functions
from IPython.display import clear_output
# global list variable
cart = []

# create function to add items to cart
def addItem(item):

    clear_output()
    cart.append(item)
    print("{} has been added.".format(item))


# create function to remove item from cart
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print("{} has been removed.".format(item))
    except ValueError as e:
        print("Sorry we could not remove that item.")
        print(e)


# create fucntio to show items int cart
def showCart():
    clear_output()
    if cart:
        print("Here is your cart:")
        for item in cart:
            print("- {}".format(item))
    else:
        print("Your cart is empty.")


# create function to clear itmes from the cart
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty")


# creat main function that loops until the user quit
def main():
    done = False
    while not done:
        print("\nPlease, select one option from the following:")
        ans = input("\nquit/add/remove/show/clear: ").lower()
        if ans == "quit":
            print("Thanks for using...")
            showCart()
            done = True

        elif ans == "add":
            item = input("What would you like to add? ").title()
            addItem(item)

        elif ans == "remove":
            showCart()
            item = input("What item would u like to remove? ").title()
            removeItem(item)

        elif ans == "show":
            showCart()

        elif ans == "clear":
            clearCart()
            print("Cart has been cleared.")

        else:
            print("Sorry that was not an option.")

# run the programm
if __name__ == "__main__":
    main()





