class Tree:
    def __init__(self, branches = [1]):
        self.branches = branches

    def tick(self):
        if len(self.branches) > 1:
            self.branches.append(self.branches[-1] + self.branches[-2])
        else: self.branches.append(1)
