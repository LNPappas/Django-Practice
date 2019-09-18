from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():

    def __init__(self):
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def cut(self):
        return self.allcards[:26], self.allcards[26:]

class Hand():

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, new_cards):
        self.cards.extend(new_cards)

    def remove_card(self):
        return self.cards.pop()


class Player():

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def play(self):
        drawn = self.hand.remove_card()
        print(f'{self.name} has placed: {drawn} \n')
        return drawn

    def draw_war(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for _ in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def not_empty(self):
        return len(self.hand.cards) != 0



d = Deck()
d.shuffle()
half1,half2 = d.cut()

comp = Player("Computer", Hand(half1))
name = input("What's your name? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.not_empty() and comp.not_empty():
    total_rounds +=1
    print("Next Round!")
    print("Current Standings:")
    print('{}: {}'.format(user.name, str(len(user.hand.cards))))
    print('{}: {}'.format(comp.name, str(len(comp.hand.cards))))
    print('Play! \n')
    
    table = []
    c_card = comp.play()
    p_card = user.play()

    table.append(c_card)
    table.append(p_card)

    if c_card[1] == p_card[1]:
        war_count+=1
        print("WAR!!")

        table.extend(user.draw_war())
        table.extend(comp.draw_war())

        c_card = comp.play()
        p_card = user.play()

        table.append(c_card)
        table.append(p_card)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table)
        else:
            comp.hand.add(table)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table)
        else:
            comp.hand.add(table)

print("GAME OVER!")
print(f"Rounds: {war_count}")
print("War {} time(s)".format(str(war_count)))

if comp.not_empty() == True:
    print(f'{user.name} wins!!')
elif user.not_empty() == True:
    print(f'{comp.name} wins!!')