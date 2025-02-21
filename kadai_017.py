class Human():
    def __init__(self,age):
        self.age = age
    def check_adult(self):
        if self.age > 19:
            print(f"{self.age}歳で成人です")
        else:
            print(f"{self.age}歳で未成年です")

Human_check = [
    Human(18),
    Human(19),
    Human(20),
    Human(21),
    Human(22)
]       
for i in Human_check:
    i.check_adult()