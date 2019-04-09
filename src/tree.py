class Tree:
    def __init__(self, branches = [1]):
        self.branches = branches

    def first_tick(self):
        self.branches.append(1)

    def tick(self):
        self.branches.append(self.branches[-1] + self.branches[-2])
