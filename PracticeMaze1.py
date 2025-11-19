import sys

class Node():
    def __init__(self,state, action, parent):
        self.state=state
        self.action = action
        self.parent=parent

class StackFrontier():
    def __init__(self):
        self.frontier=[]

    def add(self,node):
        self.frontier.append(node)

    def empty(self):
        return len(self.frontier)==0

    def remove(self):
        if self.empty:
            raise Exception("empty frontier")

        else:
            node=self.frontier[-1]
            self.frontier=self.frontier[:-1]
            return node

    def is_state(self,state):
        return any(state==node.state for node in self.frontier)

    class Maze():
        def __init__(self):
            fr=StackFrontier()

            with open('maze1.txt') as f:
                content=f.read()

            content=content.splitlines()
            self.height=len(content)
            self.width=max(len(lines) for lines in content)
            self.walls=[]
            for i in range(self.height):
                row=[]
                for j in range(self.width):
                    try:
                        if content[i][j]=='A':
                            self.start=(i,j)
                            row.append('False')
                        elif content[i][j]=='B':
                            self.goal = (i, j)
                            row.append('False')
                        elif content[i][j]==' ':
                            row.append('False')
                        else:
                            row.append('True')
                    except IndexError:
                        row.append('False')

                self.walls.append(row)
            self.solution=[]


        def neighbour(self,state):
            neighbour=[]
            x,y=state

            if x+1<=self.width and not self.walls[x+1][y]: neighbour.append({'right',(x+1,y)})
            if x-1>=0and not self.walls[x+1][y]: neighbour.append({'left', (x - 1, y)})
            if y + 1 <= self.height and not self.walls[x][y+1]: neighbour.append({'up', (x, y+1)})
            if y - 1 >= 0 and not self.walls[x][y - 1]: neighbour.append({'down', (x, y - 1)})

            return neighbour

        def solve(self):
            start=Node(state=self.start,action=None,parent=None)
            fr=StackFrontier
            fr.add(start)
            self.explored=set()

            while True:
                if fr.empty():
                    raise Exception('No Solution')

                node=fr.remove()
                if node.state==self.goal:
                    print('solution found')
                    action=[]
                    state=[]

                else:
                    self.explored.add(node.state)
                    for action,state in self.neighbour(node.state):
                        if  (not fr.is_state(state)) and state not in self.explored :
                            childnode=Node(state,action,node)
                            fr.add(childnode)



