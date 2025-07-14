from address import Address
from mailing import Mailing

to_address = Address("460093", "Вилючинск", "Крашенинникова", "22", "78")
from_address = Address("480000", "Оренбург", "Вагонная", "6", "8")


mailing = Mailing(to_address, from_address, 535, "TRK000056")

print(mailing)
