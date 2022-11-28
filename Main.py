import random

kids = ["rey", "jesse", "lukas", "dom", "kevin", "xitlali", "adrian", "dulce", "sayid", "Caine"]
location = ["mo", "cafeteria", "pines", "backrooms", "spanns"]


def Clue():
    print(kids[rand.randrange(10)])
    num=rand.randrange(0,100)
    victim = random.randrange#not finished
    if num<10:
        print("ballooned")
        print(kids[rand.randrange(10)])
        print("in")
    elif num<20:
        print("pied")
        print(kids[rand.randrange(10)])
        print("in")
    elif num<35:
        print("got chocolate chip cookies (actually raisins) by")
        print(kids[rand.randrange(10)])
        print("in")
    elif num <= 15:
        print("got their shoelaces tied by")
        print(kids[rand.randrange(10)])
        print("in")
    else:
        print("got turned into a bunny with a raygun by")
        print(kids[rand.randrange(10)])
        print("in")
    print(location[rand.randrange(5)])
    
Clue()
