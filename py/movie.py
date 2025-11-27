movie  = input("What's your favorite Movie? ")
#?
 #if movie == "The 400 Blows" or movie == "Breathless":
#      print("French New Wave") 

# elif movie == "Woman in the Dunes" or movie == "Pale Flower":
#      print("Japanese New Wave")

# elif movie == "Taxi Driver" or movie == "The Graduate":
#      print("New Hollywood")

# elif movie == "La Dolce Vita" or movie == "L'aventura":
#      print("Italian New Wave")

# else:
#      print("Who???")*
#?
match movie:
     case "The 400 Blows" | "Breathless":
          print("French New Wave")

     case "Woman in the Dunes" | "Pale Flower": 
          print("Japanese New Wave")

     case "Taxi Driver" | "The Graduate":
          print("New Hollywood")

     case "La Dolce Vita" | "L'aventura":
          print("Italian New Wave")

     case _:
          print("Who??")