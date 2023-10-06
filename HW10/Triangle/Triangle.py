class Triangle:

    
    def check(self):
        if ((self.size_a + self.size_b) > self.size_c) & ((self.size_b + self.size_c) > self.size_a) & ((self.size_c + self.size_a) > self.size_b):
            if self.size_a == self.size_b & self.size_b == self.size_c:
                return'Равносторонний'
            elif (self.size_a == self.size_b) | (self.size_b == self.size_c) | (self.size_a == self.size_c):
                return 'Равнобедренный'
            else:
                return 'Разносторонний'
        else:
            return None

    def __init__(self, a, b=None, c=None):
        self.size_a = a
        self.size_b = b if b else a
        self.size_c = c if c else a
        self.name = check()
    