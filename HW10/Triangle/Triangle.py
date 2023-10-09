class Triangle:

    def __init__(self, a, b=None, c=None):
        self.size_a = a
        self.size_b = b if b else a
        self.size_c = c if c else a

    def triangle_check(self):
            if ((self.size_a + self.size_b) > self.size_c) & ((self.size_b + self.size_c) > self.size_a) & ((self.size_c + self.size_a) > self.size_b):
                if self.size_a == self.size_b & self.size_b == self.size_c:
                    return 'Равносторонний'
                elif (self.size_a == self.size_b) | (self.size_b == self.size_c) | (self.size_a == self.size_c):
                    return 'Равнобедренный'
                else:
                    return 'Разносторонний'
            else:
                return 'Несуществующий'

t1 = Triangle(3, 4, 5)
t2 = Triangle(3)
t3 = Triangle(3, 4)
t4 = Triangle(3, 4, 40)

print(t1.triangle_check())
print(t2.triangle_check())
print(t3.triangle_check())
print(t4.triangle_check())