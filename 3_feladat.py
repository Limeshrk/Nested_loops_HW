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

arfolyam = 1.1 #EUR - USD árfolyam ~1.1 körül mozog
def car_currency_converter(cars):
  for i in range(0,len(cars)):
    if cars[i]['currency'] == "EUR":
      cars[i]['price'] = cars[i]['price'] * arfolyam
      cars[i]['currency'] = "USD"
        ##print(cars[i]['type'], cars[i]['price'], cars[i]['currency']) #csak az átváltottak
    print(cars[i]['type'], cars[i]['price'], cars[i]['currency']) #Teljes lista EUR-ban

car_currency_converter(cars)