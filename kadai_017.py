class Human():
    def __init__(self,age, name):
        self.age = age
        self.name = name
    def check_adult(self):
        if self.age > 19:
            print(f"{self.name}さんは{self.age}歳で成人です")
        else:
            print(f"{self.name}さんは{self.age}歳で未成年です")

Human_check = [
    Human(18,"寺地"),
    Human(19,"荻野"),
    Human(20,"佐藤"),
    Human(21,"国吉"),
    Human(22,"平沢"),
]       
for i in Human_check:
    i.check_adult()