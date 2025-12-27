import pandas as pd

cars_data = {'model': ['Audi A1', 'Audi A6', 'Audi A4', 'Audi A3','Audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol']}

# Write your code below
audi_cars = pd.DataFrame(cars_data)
audi_cars.insert(2, 'price', [12500, 16500, 16800, 17300, 13900])

# Testing the result
print(audi_cars)