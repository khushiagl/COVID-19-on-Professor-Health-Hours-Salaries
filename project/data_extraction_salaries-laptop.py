"""
CSC110 Project: How COVID - 19 Changed Post - Secondary Professors' Health, Hours, and Salaries

Module Description
===================
This module contains the functions for data extraction and organisation.

Copyright and Usage Information
=================================

This file is provided solely for the personal and private use of instructors and TAs of CSC110
at the University of Toronto St.George campus.All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

This file is Copyright(c) 2021 Kaylee Chan, Davit Barsamyan, Khushi Agrawal, and Meghan George.
"""
import csv


def process_data(file: str) -> tuple[list[str], list[list]]:
    """Return the headers and data stored in professors' salaries data set.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists, where each inner list stores a row in the csv file
    with appropriate data types.

     Preconditions:
      - filename refers to a valid csv file with headers
    """
    data = read_csv_file(file)
    cleaned_data = clean_data(data)
    rows_so_far = []

    for row in cleaned_data[1]:
        rows_so_far.append(process_row(row))

    return (data[0], rows_so_far)


def read_csv_file(filename: str) -> tuple[list[str], list[list[str]]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists of strings, where each inner list
      stores a row in the csv file.

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)
    """
    with open(filename) as file:
        reader = csv.reader(file)

        headers = next(reader)

        data = [row for row in reader]

    return (headers, data)


def clean_data(data: tuple[list[str], list[list[str]]]) -> tuple[list[str], list[list[str]]]:
    """Mutate and return the data by replacing or removing missing values.

        Preconditions:
        - row has the correct format for the professors' salaries data set
    """
    for row in data[1]:
        if row[4] == '-Inf':
            row[4] = '0'
    missing_obs = []
    for row in data[1]:
        for obs in row:
            if row not in missing_obs:
                if obs == '-Inf':
                    missing_obs.append(row)
    for row in missing_obs:
        data[1].remove(row)

    return data


def process_row(row: list[str]) -> list:
    """Convert a row of professors' salaries data to a list with more appropriate data types.

    Preconditions:
        - row has the correct format for the professors' salaries data set
    """
    return [
        str_to_date(row[0]),  # ref_date
        row[1],  # institution
        row[2],  # rank
        int(row[3]),  # total_teaching_staff
        int(row[4]),  # teaching_staff_excluded
        float(row[5]),  # avg salary
        float(row[6]),  # median salary
        float(row[7]),  # tenth_percentile_salaries
        float(row[8])  # nintyth_percentile_salaries
    ]


def str_to_date(date_string: str) -> tuple[int, int]:
    """Convert a string in yyyy/yyyy format to a (yyyy, yyyy).

    Preconditions:
    - date_string has format yyyy/yyyy
    """
    start, end = str.split(date_string, '/')
    academic_year = (int(start), int(end))

    return academic_year
