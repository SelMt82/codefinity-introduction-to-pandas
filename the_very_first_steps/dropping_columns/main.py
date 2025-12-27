import pandas as pd

cars_data = {'model': ['Audi A1', 'Audi A6', 'Audi A4', 'Audi A3','Audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'capital': ['Manila', 'Monaco', 'Bangkok', 'Stockhol', 'Valletta']}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
# audi_cars = audi_cars.drop(columns=['capital'], axis=1) # using columns= for deleting columns followed with ['columnname'], axis=1
# audi_cars = audi_cars.drop(index=audi_cars.index[[1,2]]) use this to delete rows by df index
# How to drop rows which is including 
# Example 1 with boolean mask
# audi_cars = audi_cars[audi_cars['capital'] != 'Monaco']
# Example 2 with indexvalue of filtered rows
# first find label-rows, where capital == 'Monaco'
idx = audi_cars[audi_cars['capital'] == 'Monaco'].index
# drop those labels
audi_cars = audi_cars.drop(index=idx)

# Testing the result
print(audi_cars)