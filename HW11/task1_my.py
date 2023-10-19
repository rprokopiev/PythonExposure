import time

import datetime

class MyStr(str):
    
    
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.author = author
        instance.record_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
        return instance
    
    
    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.record_time})'
    
    
    def __repr__(self):
        return f'MyStr({str(self.value)}, {str(self.author)})'
    

event = MyStr("Мама мыла раму", "Маршак")
print(repr(event))