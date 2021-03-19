'''

When Boredom kicks u better Toss it away as TossGod says 😁!
A Program that reads the number of tosses to be performed along with the user
intent upon success and gives a success result with dynamic success headers!

'''
import random as rand


class TossGod:
    def __init__(self, n, headEvent, tailEvent):
        self.events = ["Heads", "Tails"]
        self.headEvent = headEvent
        self.tailEvent = tailEvent
        self.tosses = n

    def toss(self):
        print("Occurrences:", end=" ")
        draw, ct_draw = True, 1

        while draw is True:
            count_heads, count_tails = 0, 0
            for i in range(self.tosses):
                occured = rand.sample(self.events, 1)
                print(str(occured).strip("[']"), end=" ")
                count_heads = count_heads + 1 if "Heads" in occured else count_heads + 0
            count_tails = self.tosses - count_heads
            draw = True if count_heads == count_tails else False
            if draw: print(
                f"\nDraw!({count_tails}/{count_heads})" + self.describerDraw() + f" Draw {ct_draw}!"); ct_draw += 1

        if count_tails > count_heads:
            print(f"\nTails Win! ({count_tails}/{count_heads})")
            print(self.describerBeginning() + self.tailEvent + self.describerEnd())
        else:
            print(f"\nHeads Win! ({count_heads}/{count_tails})")
            print(self.describerBeginning() + self.headEvent + self.describerEnd())

    def describerDraw(self):
        messages = [" Not a gud day to Draw! Lets go Again!", " Oh Drat! Go Again u Moron!", " Tough to Decide Eh!",
                    " U better start figuring it out yourself!"]
        return str(rand.sample(messages, 1)).strip("[']")

    def describerBeginning(self):
        messages = ["You better ", "Oh it says u better ", "Well u should ", "It's a gud day to "]
        return str(rand.sample(messages, 1)).strip("['\"]")

    def describerEnd(self):
        messages = [" for now!", " though!", " as the Toss God says!", " for time being!"]
        return str(rand.sample(messages, 1)).strip("[']")


if __name__ == '__main__':
    n = int(input("Enter the number of Tosses:"))
    headEvent = input("Enter the head event:")
    tailEvent = input("Enter the tail event:")
    T = TossGod(n, headEvent, tailEvent)
    T.toss()
