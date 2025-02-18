class Human():
    def __init__(self, name , age):
            self.name = name
            self.age  = age
    
    def printinfo(self):
          print(self.name)
          print(self.age)

contents = Human("名前", "年齢")

contents.printinfo()