from django.db import models

class Destination():
    name : str
    img : str
    desc : str
    price : float
    isOffer : bool

    def __init__(self, id : int, name : str, img : str, desc : str, price : float, isOffer : bool) : 
        self.id = id
        self.name = name
        self.img = img
        self.desc = desc
        self.price = price
        self.isOffer = isOffer

