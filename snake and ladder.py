import random

class snakesandladder(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.ladders = {3:38,24:33,42:93,72:84}
        self.snakes = {17:7,54:34,62:19,98:79}

    def check_for_snakes_and_ladders(self):
        if self.ladders.__contains__(self.position):
            print("It's a Ladder, Climb Up")
            self.position = self.ladders[self.position]
        elif self.snakes.__contains__(self.position):
            print("It's a Snake, Move Down")
            self.position = self.snakes[self.position]
        return self

    def roll(self):
        x=random.randint(1,6)
        print("You got a " + str(x))
        self.position=self.position + x
        return self

print("##### Welcome to Snakes & Ladders Game #####")
p1 = input("Enter the name of Player 1 :")
p1 = snakesandladder(p1,0)
p2 = input("Enter the name of Player 2 :")
p2 = snakesandladder(p2,0)
print("##### Let us Start #####")

while p1.position < 100 or p2.position < 100:
    dice = input("Player 1 : ")
    if dice.isdigit():
        val=int(dice)
    if dice == "roll":
        p1 = p1.roll()
        p1 = p1.check_for_snakes_and_ladders()
    elif val>=1 and val<=20:
        p1.position=p1.position + val
        p1 = p1.check_for_snakes_and_ladders()
    else:
        print("Invalid Move")
    print(" Your final position is " + str(p1.position))

    if p1.position > 99:
        print("\nPlayer 1 won the game")
        print("##### Game Successfully Finished #####")
        break

    dice = input("Player 2 : ")
    if dice.isdigit():
        val=int(dice)
    if dice == "roll":
        p2 = p2.roll()
        p2 = p2.check_for_snakes_and_ladders()
    elif val>=1 and val<=20:
        p2.position=p2.position + val
        p2 = p2.check_for_snakes_and_ladders()
    else:
        print("Invalid Move")
    print(" Your final position is " + str(p2.position))

    if p2.position > 99:
        print("\nPlayer 2 won the game")
        print("##### Game Successfully Finished #####")
        break