#Second excercise
#Prints out the name of the cars where there are too much passengers 
def count_passengers(cars):
    for car in cars:
        passengerQty = car["passengerQty"]
        passengers = len(car["passengers"])
        type = car["type"]
        if passengers > passengerQty:
          print(f"A(z) {type} típusú autóban túl sok az utas.")
        
cars = [
    {"price": 1549,
     "passengerQty": 4,
     "currency": "EUR",
     "type": "Kia",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 1954,
     "passengerQty": 5,
     "currency": "EUR",
     "type": "Suzuki",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 5,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 2,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
    {"price": 9542,
     "passengerQty": 4,
     "currency": "USD",
     "type": "Ford",
     "transmission": "automatic",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
]

count_passengers(cars)