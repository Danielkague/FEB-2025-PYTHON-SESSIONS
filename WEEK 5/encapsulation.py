class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # private variable

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("Chocolate taken!")
        else:
            print("No chocolates left!")


# Create an instance of SecretStash
stash = SecretStash()

# Take chocolates until none are left
for _ in range(20):  # Attempt to take more chocolates than available
    stash.take_chocolate()  # Properly indented
