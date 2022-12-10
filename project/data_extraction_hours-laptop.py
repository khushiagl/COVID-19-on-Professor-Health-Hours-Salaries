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
    """Return the headers and data stored in professors' hours data set.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists, where each inner list stores a row in the csv file
    with appropriate data types.

     Preconditions:
      - filename refers to a valid csv file with headers
    """
    data = salaries.read_csv_file(file)
    cleaned_data = clean_data(data)
    rows_so_far = []

    for row in cleaned_data[1]:
        rows_so_far.append(process_row(row))

    return (data[0], rows_so_far)


def clean_data(data: tuple[list[str], list[list[str]]]) -> tuple[list[str], list[list[str]]]:
    """Mutate and return the data by removing missing values.

    Preconditions:
        - row has the correct format for the professors' hours data set
    """

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
    """Convert a row of professors' hours data to a list with more appropriate data types.

    Preconditions:
        - row has the correct format for the professors' hours data set
    """
    return [
        int(row[0]),  # ref_date
        row[1],  # GEO
        row[3],  # CIP
        row[4],  # population characteristics
        row[5],  # employment
        row[6],  # role
        float(row[7]),  # avg_hours_class_teaching
        float(row[8]),  # avg_hours_other_teaching
        float(row[9]),  # avg_hours_research
        float(row[10]),  # avg_hours_administrative
        float(row[11])  # avg_hours_total
    ]
