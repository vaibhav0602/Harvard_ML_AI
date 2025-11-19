from click.testing import Result

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

DAYS=["M","T","W"]

def backtrack(assignment=[]):
    if len(assignment)==len(VARIABLES):
        result=assignment
        return result
    if len(assignment)>0: var,day=assignment[-1]

    while len(assignment)<len(VARIABLES):
        a=0



