


class Queue(object):
    
    def __init__(self):
        self.vals = []

    def push(self, val):
        self.vals.append(val)

    def pop(self):
        # get value
        ret = self.vals[0]
        # delete of list & return
        self.vals.remove(self.vals[0])
        return ret

    def len(self):
        return len(self.vals)

    def empty(self):
        return len(self.vals) == 0


