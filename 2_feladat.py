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

def passenger_check(cars):
  for i in range(0,len(cars)):
    if cars[i]['passengerQty'] < len(cars[i]['passengers']):
      print(f"a(z) {cars[i]['type']} típusú autóban túl sok az utas")

passenger_check(cars)