class Archive:
    
    _instance = None
    archive_text = []
    archive_number = []
    text = ''
    number = 0

    def __new__(cls, text: str, number: int or float):
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
        
        else:
            cls.archive_number.append(cls._instance.number)
            cls.archive_text.append(cls._instance.text)
            # cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, text: str, number: int or float):
        self.number = number
        self.text = text
        
    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive('{self.text}', {self.number})"



archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive1)
print(archive3)
