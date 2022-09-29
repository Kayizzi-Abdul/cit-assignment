# # # # # # END OF WEEK 7 QUIZ

# # # # # 1. Your task is to create slightly different animals, which should have the same properties and methods, 
# # # # # but should implement the talk() method in different ways. 
# # # # # For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". 
# # # # # They should all share the following (private) properties: name (string), age (number), food (list of strings),
# # # # #  and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food.
# # # # #  Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, 
# # # # # as the animals have different sounds.
# # # # # When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)


class Animals:
    def __init__(self,name,age,food):
        self.__name = name
        self.__age = age
        self.__food = []
    
    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age = new_age

    def get_food(self):
        return self.__food

    def add_food(self,new_food):
        self.__food.append(new_food)

    def remove__food(self):
        food_to_remove = input("Enter food to remove")
        if food_to_remove in self.__food:
            self.__food.remove(food_to_remove)
            print(f"{food_to_remove} has been removed succesfully")
        else:
            print(f"{food_to_remove} has not been found")

    def Cat_sound(self):
        return "Meow"

    def Dog_sound(self):
        return "Woff"

    def Fish_sound(self):
        return "Blub"

    def Cow_sound(self):
        return "Muuu"


cow = Animals("Cow",23,"grass")
cow.add_food("greens")
cow.add_food("grass")
print(cow.get_food())
print(f"{cow.Cow_sound()} is sound of a cow")
cow.remove__food()
print(cow.get_food())


# # # # # 2. The snail climbs up 7 feet each day and slips back 2 feet each night. 
# # # # # How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem.
# # # # # Sample Input: 31
# # # # # Sample Output: 6


def Snail(self,depth):
    self.depth = depth
    self.days = days
    i = 0
    days = 0
    while depth > i:
        i += 7
        i -= 2
        days += 1
        return days

# # # print(f"{Snail(31)} are the days it takes the snail to climb")


# # # # # 3. Write a function that takes a list of numbers and returns the largest number in the list.

def readvalues():
    list = []
    

    while True:
        numbers = int(input("Enter values or a to quit"))
        if numbers == 'a':
            break
        else:
            list.append(numbers)
    return list

def largest(list):
    Largest = max[list]
    return Largest






# # # # # 4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# # # # # Suppose the following input is supplied to the program:
# # # # # `Hello world!`
# # # # # Then, the output should be:
# # # # # `UPPER CASE 1`
# # # # # `LOWER CASE 9`

word = input("Enter your word")

def String(word):
    l = u = 0
    for i in word:
        if i.isupper():
            u += 1
        else:
            l += 1
    return print(f"Upper letters are {u} and lower letters are {l}")

String(word)


# # # # # 5. Using Object Oriented Programming, write a program that implements
# # # # # a dice game. The game should have two players, and each player
# # # # # should have a name and a score. The game should have a method
# # # # # called `play` that takes two players as arguments and simulates
# # # # # the game. The game should be played as follows:
# # # # #     - Each player rolls a die.
# # # # #     - The player with the highest roll wins the round.
# # # # #     - The winner gets one point added to their score.
# # # # #     - The game ends when one player has 5 points.
# # # # #     - The player with the most points at the end of the game wins.
# # # # #     - The program should print out the winner's name and score.
# # # # #     - If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time,
# # # # #  they get an extra roll, but their turn ends.

# # # # # 6. Write a Python program that lists out all the default as well as custom properties of the class.

class Name:
    '''This is a sample class'''
    pass

print(Name)


# # # # # 7. Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.

# # # # # 8. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.

# # # # # 9. Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size.
# # # # #  The queue should be "first-in-first-out" (FIFO).

# # # # # 10. Using a while loop, implement merge sort algorithm.