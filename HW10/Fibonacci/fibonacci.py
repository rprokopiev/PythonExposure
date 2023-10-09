class Fibonacci:


    def __init__(self, number: int):
        self.number = number
        def fibonacci(num):
            positive_list = [0, 1]
            for i in range(num):
                positive_list.append(positive_list[-2]+positive_list[-1])
            return positive_list
        self.result = fibonacci(number)

f1 = Fibonacci(10)
print(f1.result)