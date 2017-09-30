from search import Problem


class Vacuum(Problem):
    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        super().__init__(initial, goal)
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def value(self, state):
        pass
