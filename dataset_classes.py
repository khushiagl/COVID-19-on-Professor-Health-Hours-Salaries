"""
CSC110 Project: How COVID - 19 Changed Post - Secondary Professors' Health, Hours, and Salaries

Module Description
===================
This module contains the data classes for hours and salaries

Copyright and Usage Information
=================================

This file is provided solely for the personal and private use of instructors and TAs of CSC110
at the University of Toronto St.George campus.All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

This file is Copyright(c) 2021 Kaylee Chan, Davit Barsamyan, Khushi Agrawal, and Meghan George.
"""

from dataclasses import dataclass
import data_extraction_hours as hours
import data_extraction_salaries as salaries
import data_extraction_mental_health as health


@dataclass
class Hours:
    """A record of the number of hours a given individual delegated to certain parts of their job

    Instance Attributes:
    - classes
    - other_teaching
    - research
    - admin
    - total


    """
    classes: float
    other_teaching: float
    research: float
    admin: float


@dataclass
class Person:
    """a record of a teachers attributes

    Instance Attributes:
        - ref_date
        - role
        - classes, hours spent teaching classes
        - other_teaching, hpurs spent teaching other than classes
        - research, hours spent researching
        - admin hours spent doing admin work

    Representation Invariants:
        - self.classes >= 0
        - self.other_teaching >= 0
        - self.research >= 0
        - self.admin >= 0

    Sample Usage:
    >>> Person(ref_date=2019, role='College professor, instructor, teacher, or researcher',\
    classes=11.5, other_teaching=11.7, research=1.3, admin=1.4, average_hours=39)
    """
    ref_date: int
    role: str
    classes: float
    other_teaching: float
    research: float
    admin: float
    average_hours: float


@dataclass
class InstitutionSalaries:
    """A record of teacher salaries in terms of

    Instance Attributes:
        - ref_date
        - institution, the name of the post secondary institution
        - rank, rank of a given person i.e. professor, assistant professor etc
        - avg_salary average salary of a person with the given rank
        - median_salary
        - tenth_percentile_salaries
        - ninetieth_percentile_salaries

    Representation Invariants:
        - self.ref_date[0] < self.ref_date[1]

    """

    ref_date: tuple
    institution: str
    rank: str
    avg_salary: float
    median_salary: float
    tenth_percentile_salaries: float
    ninetieth_percentile_salaries: float


@dataclass
class MentalHealth:
    """ A record of the average response of teachers to a mental health poll

    Instance Attributes:
        - scale, a string indicating by which scale a category was measured i.e.
        Negative Effect Scale
        - item, a string indicating a statement in the poll i.e 'I am exhausted'
        - mean, the mean value of the responses
        - standard_deviation
        - score_corrected_correlations

    Representation invariants:
        - self.scale in ['Negative affect scale', 'Situational Loneliness scale',
        'Family and social support scale']
        - self.mean >= 0
        - self.standard_deviation >= 0
        - score_corrected_correlations >= 0
    """

    scale: str
    item: str
    mean: float
    standard_deviation: float
    score_corrected_correlations: float


def create_people_data(filename: str) -> list[Person]:
    """Return a list of Person data classes from the data set data"""

    data = hours.process_data(filename)
    data_classes = []
    for row in data[1]:
        row_data = Person(row[0], row[5], row[6], row[7], row[8], row[9], row[10])
        data_classes.append(row_data)
    return data_classes


def create_salary_data(filename: str) -> list[InstitutionSalaries]:
    """Return a list of InstitutionSalaries data classes from the data set data"""

    data = salaries.process_data(filename)
    data_classes = []
    for row in data[1]:
        row_data = InstitutionSalaries(row[0], row[1], row[2], row[5], row[6], row[7], row[8])
        data_classes.append(row_data)
    return data_classes


def create_health_data(filename: str) -> list[MentalHealth]:
    """Return a list of MentalHealth data classes from the data set data"""

    data = health.process_data(filename)
    data_classes = []
    for row in data[1]:
        row_data = MentalHealth(row[0], row[1], row[2], row[3], row[4])
        data_classes.append(row_data)
    return data_classes


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['dataclasses', 'data_extraction_hours', 'data_extraction_salaries',
                          'data_extraction_mental_health'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
