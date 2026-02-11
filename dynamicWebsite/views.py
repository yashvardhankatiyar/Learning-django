from django.shortcuts import render
from .models import Destination



def index(request) :
    dest1 = Destination(id=1, name="Mumbai", desc="City of dreams & Marine Drive vibes", img="image1.jpg", price=999, isOffer= True)
    dest2 = Destination(id=2, name="Kolkata", desc="Cultural capital with iconic Howrah Bridge", img="image2.jpg", price=899, isOffer= True)
    dest3 = Destination(id=3, name="Bangalore", desc="India's IT hub with pleasant weather", img="image3.jpg", price=1299, isOffer= False)
    dest4 = Destination(id=4, name="Delhi", desc="Historic monuments & street food paradise", img="image4.jpg", price=1099, isOffer= True)
    dest5 = Destination(id=5, name="Jaipur", desc="Pink City full of royal palaces", img="image5.jpg", price=1199, isOffer= False)
    dest6 = Destination(id=6, name="Goa", desc="Beaches, nightlife & chill vibes", img="image6.jpg", price=1599, isOffer= True)
    dest7 = Destination(id=7, name="Manali", desc="Snowy mountains & adventure sports", img="image7.jpg", price=1799, isOffer= False)
    dest8 = Destination(id=8, name="Kerala", desc="Backwaters, greenery & houseboats", img="image8.jpg", price=1499, isOffer= False)



    dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8]
    dests = sorted(dests, key = lambda x : x.isOffer, reverse= True)
    return render(request, "TournTravelIndexPage.HTML", {"dests" : dests})