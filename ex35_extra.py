#-*-encoding:utf-8-*-
from sys import exit

def gold_room():
    print "this room is full of gold. how much do you take?"
    new_next = []

    while True:
        next = raw_input('> ')
        for i in next:
            if not "0" <= i <= "9":
                gold_room()
            else:
                print i

        if int(next) < 50:
            print "nice, you're not greedy, you win!"
            exit()
        else:
            print "you greedy bastard!"
            exit()

gold_room()
