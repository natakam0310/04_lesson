from smartphone import Smartphone


catalog = [
    Smartphone(brand="Samsung", model="Galaxy", number="+79146252225"),
    Smartphone(brand="LG", model="AH", number="+79146250000"),
    Smartphone(brand="Sony", model="S15", number="+79146666225"),
    Smartphone(brand="Aplle", model="RL", number="+79146250000"),
    Smartphone(brand="realme", model="dk", number="+73536252225")
    ]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")
