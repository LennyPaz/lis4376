"""SS6 - Functions for Pandas DataFrames and Series Data Structures"""
import pandas as pd


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
    print("4. Using multiple conditions: not, and, or.")
    print("5. Logical operators, numeric comparisons, NaN handling.")
    print()
    print("Note: not, and, or statements require truth-values.")
    print("Pandas requires \"bitwise\" (overloaded operators): not(~), and (&), or (|).")
    print()


def get_data():
    """loads and displays Titanic data"""
    print("Print pandas version:")
    print(pd.__version__)
    print()

    df = pd.read_csv('titanic.csv', encoding='utf-8')
    print("Display data:")
    print(df)
    print()

    print("Display type:")
    print(type(df))
    print()

    print("Total number of passengers: ", end="")
    print(len(df))
    print()

    return df


def and_operator(my_titanic_df):
    """demonstrates bitwise AND operator"""
    total_non_survivors = (my_titanic_df['survived'] == 'no').sum()
    print("Total number perished: ", end="")
    print(total_non_survivors)
    print()

    male_non_survivors = ((my_titanic_df['gender'] == 'male') & (my_titanic_df['survived'] == 'no')).sum()
    print("Total males perished: ", end="")
    print(male_non_survivors)
    print()

    num_deceased_males_to_total_deceased = male_non_survivors / total_non_survivors
    print("Percentage of males who died from total perished: ", end="")
    print(f"{num_deceased_males_to_total_deceased:.2%}")
    print()


def convert_data(my_titanic_df):
    """converts age column to numeric, identifying non-numeric values"""
    titanic_series = my_titanic_df['age']
    numeric_and_non_numeric_data = pd.to_numeric(titanic_series, errors='coerce')
    non_numeric_data = titanic_series[numeric_and_non_numeric_data.isna()]
    numeric_data = titanic_series[~numeric_and_non_numeric_data.isna()]

    return numeric_and_non_numeric_data, numeric_and_non_numeric_data, numeric_data


def or_operator(my_titanic_series):
    """demonstrates bitwise OR operator"""
    titanic_series = pd.Series(my_titanic_series, name='age')
    my_titanic_df = titanic_series.to_frame()

    old_young_passengers = my_titanic_df[(my_titanic_df['age'] > 70) | (my_titanic_df['age'] < 5)]
    print("Total number of passengers older than 70 OR younger than 5: ", end="")
    print(len(old_young_passengers))
    print()


def not_operator(my_titanic_df):
    """demonstrates bitwise NOT with .isin()"""
    unique_countries = my_titanic_df['country'].drop_duplicates()
    print("Total number of unique home countries: ", end="")
    print(len(unique_countries))
    print()

    titanic_series = pd.Series(unique_countries, name='country')
    countries_df = titanic_series.to_frame()

    excluded_countries = ['England', 'France']
    non_excluded_countries = countries_df[~countries_df['country'].isin(excluded_countries)]
    print("Total number of unique home countries, not including England or France: ", end="")
    print(len(non_excluded_countries))
    print()
