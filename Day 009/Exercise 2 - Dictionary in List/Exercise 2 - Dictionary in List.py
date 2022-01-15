travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    travel_logUser = {}
    travel_logUser["country"] = country
    travel_logUser["visits"] = visits
    travel_logUser["cities"] = cities
    travel_log.append(travel_logUser)
    print(travel_log)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])