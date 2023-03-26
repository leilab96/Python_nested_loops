#Third Excercise
# in the cars list, finds the cars where the price is in EUR and change it to USD, then it writes it out
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

def currency_changer(cars):
  conversion_rate=1.2
  for car in cars:
    if car["currency"] == "EUR":
      car["price"] *= conversion_rate
      car["currency"] = "USD"
    name = car["type"]
    price = car["price"]
    currency = car["currency"]
    print(f"{name}: {price:.2f} {currency}")
  return cars


currency_changer(cars)

