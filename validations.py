import itertools
import pandas as pd

# This information is known beforehand
COLUMNS_INFO = {"DS": "object", "Y": "float64"}

default_params = {'columns': 2, 'column_info': COLUMNS_INFO}


def validate_csv(filepath, params=default_params):
    df = pd.read_csv(filepath)
    errors = []
    number_of_columns = params['columns']
    columns_info = params['column_info']
    errors += check_columns_types(df, columns_info)
    errors.append(has_valid_number_of_columns(df, number_of_columns))
    return [err[1] for err in errors if err is not True]


def check_columns_types(df, columns_info):
    errors = []
    for col_name, col_type in columns_info.items():
        errors.append(is_valid_column_type(df, (col_name, col_type)))
    return list(itertools.chain(errors))

def is_valid_column_type(df, col_info):
    col_name, col_type = col_info
    if col_name not in df:
        return False, '"{}" column must be present'.format(col_name)
    elif df[col_name].dtype.name == col_type:
        return True
    else:
        return False, '"{}" column has a wrong type'.format(col_name)

def has_valid_number_of_columns(df, number):
    if len(df.columns) == number:
        return True
    else:
        return False, 'Wrong number of columns, it must have {}'.format(number)
