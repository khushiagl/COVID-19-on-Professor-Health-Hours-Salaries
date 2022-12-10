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
import data_extraction_salaries as salaries


def process_data(file: str) -> tuple[list[str], list[list]]:
    """Return the headers and data stored in professors' mental health data set.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists, where each inner list stores a row in the csv file
    with appropriate data types.

     Preconditions:
      - filename refers to a valid csv file with headers
    """
    data = salaries.read_csv_file(file)
    rows_so_far = []

    for row in data[1]:
        rows_so_far.append(process_row(row))

    return (data[0], rows_so_far)


def process_row(row: list[str]) -> list:
    """Convert a row of professors' mental health data to a list with more appropriate data types.

    Preconditions:
        - row has the correct format for the professors' mental health data set
    """
    return [
        row[0],  # scale
        row[1],  # item
        float(row[2]),  # mean
        float(row[3]),  # standard deviation
        float(row[4]),  # item-total score-corrected correlations
    ]
