import pandas as pd

data = pd.read_excel('/TestData.xlsx', sheet_name='Sheet1')


def print_data():
    d = data
    print(d)
