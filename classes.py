class string:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input() 

    def printString(self):
        print(self.text.upper())

x = string()
x.getString()
x.printString()
