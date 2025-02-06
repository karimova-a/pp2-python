class string_methods:
    def __init__(self, sstring=""):
        self.sstring = sstring
    
    def getString(self):
        self.sstring = input()

    def printString(self):
        self.sstring = self.sstring.upper()
        print(self.sstring)

st1 = string_methods()
st1.getString()
st1.printString()