import pandas as pd

file_url = 'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/pandas.txt'

# Write your code below
text_data = pd.read_csv(file_url, sep='\r', header=None)
first_row = text_data.iloc[0]

# Testing the result
print(first_row)