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


@dataclass
class Person:
    """a record of a teachers attributes

    Instance Attributes:
        - ref_date
        - GEO the general location of the teacher in terms of province in Canada
        - CIP the classification of instructional program
        - population_characteristics
        - employment, whether a person works one job or several or none
        - role
        - classes, hours spent teaching classes
        - other_teaching, hpurs spent teaching other than classes
        - research, hours spent researching
        - admin hours spent doing admin work

    Representation Invariants:
        - self.geo in ['Atlantic provinces', 'British Columbia', 'Canada', 'Ontario', 'Prairie provinces'
    'Quebec', 'Territories']
        - self.classes >= 0
        - self.other_teaching >= 0
        - self.research >= 0
        - self.admin >= 0
        - isalnum(self.cip) == True

    Sample Usage:
    >>> Person(ref_date=2019, geo='Atlantic provinces', cip='BHASE [b]',\
    population_characteristics='Female gender [F]', employment='More than one job or business',\
    role='College professor, instructor, teacher, or researcher', classes=11.5, other_teaching=11.7,\
     research=1.3, admin=1.4)
    """
    ref_date: int
    geo: str
    cip: str
    population_characteristics: str
    employment: str
    role: str
    classes: float
    other_teaching: float
    research: float
    admin: float


def create_people_data(filename: str) -> list[Person]:
    """Return a list of Person data classes from the data set data"""

    data = hours.process_data(filename)
    data_classes = []
    for row in data[1]:
        row_data = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        data_classes.append(row_data)
    return data_classes


@dataclass
class InstitutionSalaries:
    """A record of teacher salaries in terms of

    Instance Attributes:
        - ref_date
        - institution, the name of the post secondary institution
        - rank, rank of a given person i.e. professor, assistant professor etc
        - total_teaching_staff, total number of teaching staff of the given rank
        - teaching_staff_excluded
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
    total_teaching_staff: int
    teaching_staff_excluded: int
    avg_salary: float
    median_salary: float
    tenth_percentile_salaries: float
    ninetieth_percentile_salaries: float


def create_salary_data(filename: str) -> list[InstitutionSalaries]:
    """Return a list of InstitutionSalaries data classes from the data set data"""

    data = salaries.process_data(filename)
    data_classes = []
    for row in data[1]:
        row_data = InstitutionSalaries(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        data_classes.append(row_data)
    return data_classes
