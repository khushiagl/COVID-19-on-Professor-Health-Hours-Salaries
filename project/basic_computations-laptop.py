"""
CSC110 Project: How COVID - 19 Changed Post - Secondary Professors' Health, Hours, and Salaries

Module Description
===================
This module contains the functions that compute on the data classes

Copyright and Usage Information
=================================

This file is provided solely for the personal and private use of instructors and TAs of CSC110
at the University of Toronto St.George campus.All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

This file is Copyright(c) 2021 Kaylee Chan, Davit Barsamyan, Khushi Agrawal, and Meghan George.
"""
from hours_data_class import InstitutionSalaries

years = [(2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]


def return_max_salary(data: list[InstitutionSalaries], salary_type: str) -> list:
    """Return the max salary in data of the given salary_type.

    Preconditions:
        -salary_type == 'Median' or 'Average' or 'Tenth Percentile' or 'Ninetieth Percentile'
    """
    # ACCUMULATOR list_so_far: List of max_salaries so far
    list_so_far = []

    if salary_type == 'Median':
        for date in years:
            max_salary = max(salaries.median_salary for salaries in data if salaries.ref_date == date)
            list_so_far.append(max_salary)
        return list_so_far
    elif salary_type == 'Average':
        for date in years:
            max_salary = max(salaries.avg_salary for salaries in data if salaries.ref_date == date)
            list_so_far.append(max_salary)
        return list_so_far
    elif salary_type == 'Tenth Percentile':
        for date in years:
            max_salary = max(salaries.tenth_percentile_salaries for salaries in data if salaries.ref_date == date)
            list_so_far.append(max_salary)
        return list_so_far
    elif salary_type == 'Ninetieth Percentile':
        for date in years:
            max_salary = max(salaries.ninetieth_percentile_salaries for salaries in data if salaries.ref_date == date)
            list_so_far.append(max_salary)
        return list_so_far


def return_min_salary(data: list[InstitutionSalaries], salary_type: str) -> list:
    """Return the min salary in data of the given salary_type.

    Preconditions:
        -salary_type == 'Median' or 'Average' or 'Tenth Percentile' or 'Ninetieth Percentile'
    """
    # ACCUMULATOR list_so_far: List of min_salaries so far
    list_so_far = []

    if salary_type == 'Median':
        for date in years:
            min_salary = min(salaries.median_salary for salaries in data if salaries.ref_date == date)
            list_so_far.append(min_salary)
        return list_so_far
    elif salary_type == 'Average':
        for date in years:
            min_salary = min(salaries.avg_salary for salaries in data if salaries.ref_date == date)
            list_so_far.append(min_salary)
        return list_so_far
    elif salary_type == 'Tenth Percentile':
        for date in years:
            min_salary = min(salaries.tenth_percentile_salaries for salaries in data if salaries.ref_date == date)
            list_so_far.append(min_salary)
        return list_so_far
    elif salary_type == 'Ninetieth Percentile':
        for date in years:
            min_salary = min(salaries.ninetieth_percentile_salaries for salaries in data if salaries.ref_date == date)
            list_so_far.append(min_salary)
        return list_so_far


def calculate_salary_percentage_difference(list_of_institutions: list[InstitutionSalaries],
                                           salary_type: str) -> list[float]:
    """Calculate the percentage change between consecutive schoolyears.

    Preconditions:
        -salary_type == 'Median' or 'Average' or 'Tenth Percentile' or 'Ninetieth Percentile'
    """
    percentages = []
    for i in range(len(list_of_institutions) - 1):
        if salary_type == 'Average':
            percentage = calculate_percentage_difference(list_of_institutions[i].avg_salary,
                                                         list_of_institutions[i + 1].avg_salary)
            percentages.append(percentage)
        elif salary_type == 'Median':
            percentage = calculate_percentage_difference(list_of_institutions[i].median_salary,
                                                         list_of_institutions[i + 1].median_salary)
            percentages.append(percentage)
        elif salary_type == 'Tenth Percentile':
            percentage = calculate_percentage_difference(list_of_institutions[i].tenth_percentile_salaries,
                                                         list_of_institutions[i + 1].tenth_percentile_salaries)
            percentages.append(percentage)
        elif salary_type == 'Ninetieth Percentile':
            percentage = calculate_percentage_difference(list_of_institutions[i].ninetieth_percentile_salaries,
                                                         list_of_institutions[i + 1].ninetieth_percentile_salaries)
            percentages.append(percentage)
    return percentages


def calculate_percentage_difference(value1: float, value2: float) -> float:
    """Calculate the percentage change between two given float values."""
    return ((value2 - value1) / value1) * 100
