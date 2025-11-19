from termcolor import cprint

from logic import *
from puzzle import knowledge

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
symbols=[]



for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

knowledge=And()

for person in people:
    knowledge.add(Or(Symbol(f"{person}{houses[0]}"),
                     Symbol(f"{person}{houses[1]}"),
                     Symbol(f"{person}{houses[2]}"),
                     Symbol(f"{person}{houses[3]}")
                     ))

for person in people:
    for house1 in houses:
        for house2 in houses:
            if house1!=house2:
                knowledge.add(
                    Implication(Symbol(f"{person}{house1}"),Not(Symbol(f"{person}{house2}")))
                            )


def knowledge_check(self, knowledge):
    for symbol in symbols:
        if model_check(knowledge,symbol):
            cprint('YES','green')

print(knowledge_check(knowledge))
