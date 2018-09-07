
import pandas as pd
import itertools

df = pd.DataFrame({"pear": [1,2,3], "apple": [2,3,"hola"], "orange": [3,4,5]})

# This information is known beforehand
COLUMNS_INFO = {"pear": "object", "apple": "object", "orange": "object"}

default_params = {'columns': 2, 'column_info': COLUMNS_INFO}

def validate(df, params=default_params):
    errors = []
    number_of_columns = params['columns']
    columns_info = params['column_info'] 
    errors += check_columns_types(df, columns_info)
    errors.append(check_number_of_columns(df, number_of_columns))
    return list(filter(lambda err: err != '', errors))

def check_columns_types(df, columns_info):
    errors = []
    for col_name, col_type in columns_info.items():
        errors.append(check_column_type(df, (col_name, col_type)))
    return list(itertools.chain(errors))

def check_column_type(df, col_info):
    col_name, col_type = col_info
    if df[col_name].dtype.name == col_type:
        return ''
    else:
        return ': '.join([col_name, 'wrong type'])

def check_number_of_columns(df, number):
    if len(df.columns) == number:
        return ''
    else: 
        return 'Wrong number of columns'
