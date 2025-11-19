class TicTacToe():

    def __init__(self,cross=True,start_position=(1,1)):
        self.cross=cross
        self.start_position=start_position
        self.turn_counter=1
        self.state:dict= dict()

        for i in range(3):
            for j in range(3):
                self.state[i,j]=""
                if (i,j)==start_position:
                    self.state[start_position]='X'

    def player_turn(self, state):
        X_count=0
        O_count=0
        for i in range(3):
            for j in range(3):
                if state[(i, j)] == 'X':
                    X_count+=1
                if state[(i, j)] == 'O':
                    O_count+=1
        return not (X_count>O_count)

    def actions(self,state):
        actions=[]
        for i in range(3):
            for j in range(3):
                if state[(i, j)] =="":
                    actions.append((i,j))
        return actions

    def result(self,state,action):
        try :
            if self.player_turn(state):
                state[action]='X'
            else:
                state[action] = 'O'
        except IndexError:
            print("Index Out of Range")

        return state

    def terminal(self, state):
        terminal_state=False
        if state[(1,1)]!="":
            if (state[(0, 0)] == state[(1, 1)]) and (state[(0, 0)] == state[(2, 2)]) :
                terminal_state=True
            if (state[(0, 2)] == state[(1, 1)]) and (state[(0, 2)] == state[(2, 0)]) :
                terminal_state = True

        for i in range(3):
            if state[(i, 0)] != "":
                if (state[(i, 0)] == state[(i, 1)]) and (state[(i, 0)] == state[(i, 2)]):
                    terminal_state = True
            if state[(0, i)] != "":
                if (state[(0, i)] == state[(1, i)]) and (state[(0, i)] == state[(2, i)]):
                    terminal_state = True

        if terminal_state:
            return terminal_state
        else:
            if self.turn_counter==9:
                return True
            else:
                return False

    def utility(self,state):
        utility=0

        if (state[(0, 0)] =='X') and state[(1, 1)]=='X' and ( state[(2, 2)]=='X') :
            utility=1

        if (state[(0, 2)] =='X') and state[(1, 1)]=='X' and ( state[(2, 0)]=='X') :
            utility=1

        for i in range(3):
            if (state[(i, 0)] == 'X') and (state[(i, 1)] =='X') and (state[(i, 2)]=='X'):
                utility=1

            if (state[(0, i)] == 'X') and (state[(1, i)] =='X') and (state[(2, i)]=='X'):
                utility=1

        if (state[(0, 0)] =='O') and state[(1, 1)]=='O' and ( state[(2, 2)]=='O') :
            utility=-1

        if (state[(0, 2)] =='O') and state[(1, 1)]=='O' and ( state[(2, 0)]=='O') :
            utility=-1

        for i in range(3):
            if (state[(i, 0)] == 'O') and (state[(i, 1)] =='O') and (state[(i, 2)]=='O'):
                utility=-1

            if (state[(0, i)] == 'O') and (state[(1, i)] =='O') and (state[(2, i)]=='O'):
                utility=-1

        return utility

    def max_value(self,s):
        if self.terminal(s):
            return self.utility(s)
        v = float('-inf')
        for action in self.actions(s):
            v = max(v, self.min_value(self.result(s, action)))
        return v

    def min_value(self,s):
        if self.terminal(s):
            return self.utility(s)
        v = float('inf')
        for action in self.actions(s):
            min(v, self.max_value(self.result(s, action)))
        return v


t=TicTacToe(start_position=(0,0))
t.max_value(s=t.state)