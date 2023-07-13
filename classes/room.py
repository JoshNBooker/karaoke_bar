class Room:

    def __init__(self, name, price, guests, songs, free_space, bar_tab):
        self.name = name
        self.price = price
        self.guests = guests
        self.songs = songs
        self.free_space = free_space
        self.bar_tab = bar_tab

    def sell_drink(self, guest, drink):
        profit = guest.buy_drink(drink)
        self.bar_tab += profit
        return self.bar_tab
    
    def check_in_guest(self, guest):
        self.guests.append(guest)
        return self.guests