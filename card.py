class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknown'


    def __init__(self, number, date, holder):
        self.number = number
        self.holder = holder
        self.validDate = date

    def ply (self, amount):
        print("с карты", self.number, "списали", amount)    
        
		