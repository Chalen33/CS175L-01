#Chalen Bobish
#Resturant

vegetarian=False
vegan=False
gluten=False

response=input("Is anyone in your party a vegetarian?\n")
if response == 'yes':
    vegetarian= True

response=input("Is anyone in your party a Vegan?\n")
if response == 'yes':
    vegan= True

response=input("Is anyone in your party gluten-free?\n")
if response == 'yes':
    gluten= True

if vegan:
    print("Here are your resturant choices:"+
          "\nCorner Café\nThe Chef's Kitchen")

elif gluten:
    print("Here are your resturant choices:"+
          "\nMain Street Pizza Company\nCorner Café\nThe Chef's Kitchen")

elif vegetarian:
    print("Here are your resturant choices:"+
          "\nMain Street Pizza Company\nCorner Café\nMama's Fine Italian\nThe Chef's Kitchen")
    

