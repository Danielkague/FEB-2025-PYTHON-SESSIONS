class Pet:
    # This runs when you create a new pet
    def __init__(self, name):
        self.name = name
        self.hunger = 5      # How hungry your pet is (0-10)
        self.energy = 5      # How much energy your pet has (0-10)
        self.happiness = 5   # How happy your pet is (0-10)
        self.tricks = []     # List to store tricks your pet knows
    
    # Feed your pet to reduce hunger and increase happiness
    def eat(self):
        # Reduce hunger by 3, but don't go below 0
        if self.hunger >= 3:
            self.hunger = self.hunger - 3
        else:
            self.hunger = 0
        
        # Increase happiness by 1, but don't go above 10
        if self.happiness < 10:
            self.happiness = self.happiness + 1
    
    # Let your pet sleep to recover energy
    def sleep(self):
        # Increase energy by 5, but don't go above 10
        if self.energy <= 5:
            self.energy = self.energy + 5
        else:
            self.energy = 10
    
    # Play with your pet to make it happier
    def play(self):
        # Decrease energy by 2, but don't go below 0
        if self.energy >= 2:
            self.energy = self.energy - 2
        else:
            self.energy = 0
        
        # Increase happiness by 2, but don't go above 10
        if self.happiness <= 8:
            self.happiness = self.happiness + 2
        else:
            self.happiness = 10
        
        # Increase hunger by 1, but don't go above 10
        if self.hunger < 10:
            self.hunger = self.hunger + 1
    
    # Check how your pet is doing
    def get_status(self):
        print(f"Pet Name: {self.name}")
        print(f"Hunger Level: {self.hunger}/10")
        print(f"Energy Level: {self.energy}/10")
        print(f"Happiness Level: {self.happiness}/10")
    
    # Teach your pet a new trick
    def train(self, trick):
        # Check if pet already knows this trick
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
        else:
            # Add the new trick to the list
            self.tricks.append(trick)
            print(f"{self.name} learned how to {trick}!")
    
    # Show all tricks your pet knows
    def show_tricks(self):
        # Check if pet knows any tricks
        if len(self.tricks) == 0:
            print(f"{self.name} doesn't know any tricks yet!")
        else:
            print(f"{self.name} knows the following tricks:")
            # Loop through each trick and print it
            for trick in self.tricks:
                print(f"- {trick}")
