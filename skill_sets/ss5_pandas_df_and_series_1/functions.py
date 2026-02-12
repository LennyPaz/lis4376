"""SS5 - Functions for Pandas DataFrames and Series Data Structures"""
import pandas as pd

# read data into pandas "global" DataFrame (for access in functions below)
df = pd.read_csv('us_data.csv')


def get_requirements():
    """prints the program requirements"""
    print("Pandas DataFrames and Series Data Structures")
    print()
    print("Program Requirements:")
    print("Developer: Lenny Paz")
    print()
    print("1. Working with DataFrames and Series for tabular data handling.")
    print("2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols).")
    print("3. DataFrame: Collection of Series objects sharing same index.")
    print("4. Isolating rows and columns.")
    print("5. Series: One-dimensional labeled array.")
    print("6. Working with Boolean data.")
    print()


def get_data():
    """displays pandas version and loaded data"""
    print("Print pandas version:")
    print(pd.__version__)
    print()

    print("Display data:")
    print(df)
    print("Display type:")
    print(type(df))
    print()


def get_bool_data():
    """creates Boolean DataFrame from comparison"""
    print("Print Boolean data:")
    print("Note: Comparison operator returns Boolean value, parentheses () optional.")
    df_bool = (df == 'DE')
    print(df_bool)
    print()

    print("Display type:")
    print(type(df_bool))

    return df_bool


def count_bool_cols(your_bool):
    """counts True values by column"""
    bool_sum_cols = your_bool.sum()
    print("\nPrint Boolean cols:")
    print("Note: Using sum() method on DataFrame returns Series.")
    print(bool_sum_cols)
    print()

    print("Display type:")
    print(type(bool_sum_cols))
    print()


def count_bool_rows(your_bool):
    """counts True values by row"""
    bool_sum_rows = your_bool.sum(axis=1)
    print("Print Boolean rows:")
    print("Note: Using sum() method on DataFrame returns Series.")
    print(bool_sum_rows)
    print()

    print("Display type:")
    print(type(bool_sum_rows))
    print()


def count_bool_total(your_bool):
    """counts total True values"""
    bool_sum_total = your_bool.sum().sum()
    print("Print Boolean total:")
    print("Note: Calling sum() on Series returns total count (also, implicitly converts to numpy.int64).")
    print(bool_sum_total)
    print()

    print("Display type:")
    print(type(bool_sum_total))
    print()


def get_series_data():
    """extracts Series from DataFrame"""
    print("Print Square Miles as Series:")
    print("Note: Calling one column in DataFrame returns Series object.")
    my_series = df['total square miles']
    print(my_series)
    print()

    print("Display type:")
    print(type(my_series))

    return my_series


def evaluate_series_data(s_data):
    """filters and counts Series values"""
    num_states = (s_data >= 100000).sum()
    print("\nPrint number of states with 100,000 or more square miles:")
    print(num_states)
    print()

    print("Display type:")
    print(type(num_states))
    print("Note: sum() used on series object implicitly converts to numpy.int64 (i.e., scalar value/single number)")
    print()


def convert_dataframe_to_numpy_array(your_bool):
    """demonstrates DataFrame to NumPy conversion"""
    print("DataFrame converted to NumPy array (ndarray) using \"values\" attribute:")
    print()

    print("Display your_bool type:")
    print(type(your_bool))
    print()

    print("Display your_bool using \"values\" attribute:")
    print(your_bool.values)
    print()

    print("Display NumPy array using \"to_numpy()\" method:")
    print(your_bool.to_numpy())
    print()

    print("Print total number of states with two-letter abbreviation == to \"DE\":")
    print("Note: Calling sum() method of ndarray calculates sum across entire array.")
    print(your_bool.values.sum())
    print()
