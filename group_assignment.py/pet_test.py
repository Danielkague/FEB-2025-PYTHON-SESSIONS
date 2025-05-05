# Import the Pet class from the pet module
from pet import Pet

# Test script starts here
def test_pet_class():
    print("=" * 50)
    print("STARTING PET CLASS TESTS")
    print("=" * 50)
    
    # Test 1: Creating a pet
    print("\nTest 1: Creating a new pet")
    print("-" * 30)
    dog = Pet("Buddy")
    print(f"Created pet named: {dog.name}")
    dog.get_status()
    
    # Test 2: Feeding the pet
    print("\nTest 2: Testing the eat() method")
    print("-" * 30)
    print("Before eating:")
    print(f"Hunger: {dog.hunger}, Happiness: {dog.happiness}")
    dog.eat()
    print("After eating once:")
    print(f"Hunger: {dog.hunger}, Happiness: {dog.happiness}")
    dog.eat()
    print("After eating twice:")
    print(f"Hunger: {dog.hunger}, Happiness: {dog.happiness}")
    
    # Test 3: Testing sleep method
    print("\nTest 3: Testing the sleep() method")
    print("-" * 30)
    print("Before sleeping:")
    print(f"Energy: {dog.energy}")
    dog.sleep()
    print("After sleeping:")
    print(f"Energy: {dog.energy}")
    
    # Test 4: Testing play method
    print("\nTest 4: Testing the play() method")
    print("-" * 30)
    print("Before playing:")
    print(f"Energy: {dog.energy}, Happiness: {dog.happiness}, Hunger: {dog.hunger}")
    dog.play()
    print("After playing once:")
    print(f"Energy: {dog.energy}, Happiness: {dog.happiness}, Hunger: {dog.hunger}")
    dog.play()
    print("After playing twice:")
    print(f"Energy: {dog.energy}, Happiness: {dog.happiness}, Hunger: {dog.hunger}")
    
    # Test 5: Testing limits (make sure values don't go below 0 or above 10)
    print("\nTest 5: Testing attribute limits")
    print("-" * 30)
    
    # Test hunger minimum limit (0)
    print("Testing minimum hunger limit:")
    cat = Pet("Whiskers")
    cat.hunger = 2  # Set hunger to 2
    print(f"Hunger before eating: {cat.hunger}")
    cat.eat()  # Should reduce to 0, not -1
    print(f"Hunger after eating: {cat.hunger}")
    
    # Test energy maximum limit (10)
    print("\nTesting maximum energy limit:")
    cat.energy = 8  # Set energy to 8
    print(f"Energy before sleeping: {cat.energy}")
    cat.sleep()  # Should increase to 10, not 13
    print(f"Energy after sleeping: {cat.energy}")
    
    # Test happiness maximum limit (10)
    print("\nTesting maximum happiness limit:")
    cat.happiness = 9  # Set happiness to 9
    print(f"Happiness before playing: {cat.happiness}")
    cat.play()  # Should increase to 10, not 11
    print(f"Happiness after playing: {cat.happiness}")
    
    # Test 6: Testing trick learning
    print("\nTest 6: Testing the train() and show_tricks() methods")
    print("-" * 30)
    
    # First check with no tricks
    fish = Pet("Bubbles")
    print("Before learning any tricks:")
    fish.show_tricks()
    
    # Learn some tricks
    print("\nLearning tricks:")
    fish.train("swim in circles")
    fish.train("jump out of water")
    fish.train("bubble blowing")
    
    # Show all tricks
    print("\nAfter learning tricks:")
    fish.show_tricks()
    
    # Try to learn the same trick again
    print("\nTrying to learn the same trick again:")
    fish.train("swim in circles")
    
    # Final check of pet status
    print("\nFinal Pet Status:")
    print("-" * 30)
    dog.get_status()
    
    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)

# Run the test function
if __name__ == "__main__":
    test_pet_class()