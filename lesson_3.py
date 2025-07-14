from user import User
from card import Card 

Alex = User("Alex")

Alex.sayName()
Alex.setAge(35)
Alex.sayAge()


card = Card ("1236 1236 5489 8642", "08/26", "Alex U")

Alex.addCard (card)

Alex.getCard().ply(2000)
