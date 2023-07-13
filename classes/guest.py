class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
    
    def pay_money(self, amount):
        self.wallet -= amount
        return self.wallet
    
    def buy_drink(self, drink):
        self.pay_money(drink.price)
        return drink.price
    
    def rent_room(self, room):
        self.pay_money(room.price)
        return room.price