"""
CSC110 Project: How COVID - 19 Changed Post - Secondary Professors' Health, Hours, and Salaries

Module Description
===================
This module contains functions that graph the relationships between health, hours, and salaries.

Copyright and Usage Information
=================================

This file is provided solely for the personal and private use of instructors and TAs of CSC110
at the University of Toronto St.George campus.All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

This file is Copyright(c) 2021 Kaylee Chan, Davit Barsamyan, Khushi Agrawal, and Meghan George.
"""
import plotly.express as px
import pandas as pd
import hours_data_class

list_of_salaries = hours_data_class.create_salary_data('prof_salaries.csv')
list_of_hours = hours_data_class.create_people_data('prof_hours.csv')
years = [(2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]


# helper function
def all_ranks_only(lst):
    for obj in list_of_salaries:
        if obj.rank == 'All ranks combined (including deans)':
            lst.append(obj)
    return lst


# helper function
def all_institutions(lst):
    for obj in list_of_salaries:
        if obj.institution not in lst:
            lst.append(obj.institution)
    return lst


def graph_function1():
    dict_of_uni_salaries = {}
    list_of_institutions = []
    list_of_institutions_ranks = []
    list_of_institutions_ranks = all_ranks_only(list_of_institutions_ranks)
    list_of_institutions = all_institutions(list_of_institutions)
    for year in years:
        temp_universities = [x for x in list_of_institutions]
        for obj1 in list_of_institutions_ranks:
            if year == obj1.ref_date:
                for uni in list_of_institutions:
                    if uni == obj1.institution:
                        if uni in temp_universities:
                            temp_universities.remove(uni)
                        if uni in dict_of_uni_salaries:
                            dict_of_uni_salaries[uni].append(obj1.avg_salary)
                            break
                        else:
                            dict_of_uni_salaries[uni] = [obj1.avg_salary]
                            break
        if len(temp_universities) > 0:
            for tuni in temp_universities:
                if tuni in dict_of_uni_salaries:
                    dict_of_uni_salaries[tuni] += [None]
                else:
                    dict_of_uni_salaries[tuni] = [None]

    df = pd.DataFrame(dict_of_uni_salaries)
    print(df)
    graph = px.line(df, y=dict_of_uni_salaries, x=['2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021'],
                    labels={'value': 'Average Salaries($)', 'x': 'Academic Years(yr)'},
                    title='Average Salary Change per Year in Canadian Universities', markers=True)
    graph.show()


# helper function
def possible_ranks():
    list_of_ranks = []
    for obj in list_of_salaries:
        if obj.rank not in list_of_ranks:
            list_of_ranks.append(obj.rank)

    return list_of_ranks


# helper function
def average_ranks_year(year, rank):
    list_of_nums = []
    for obj in list_of_salaries:
        if obj.ref_date == year and obj.rank == rank:
            list_of_nums.append(obj.avg_salary)

    return sum(list_of_nums) / len(list_of_nums)


def graph_function2():
    rank_list = possible_ranks()
    avg_in_year = []
    dict_rank_avg = {}
    for year in years:
        for rank in rank_list:
            avg_in_year.append(average_ranks_year(year, rank))
            if rank in dict_rank_avg:
                dict_rank_avg[rank] += avg_in_year
                avg_in_year = []
            else:
                dict_rank_avg[rank] = avg_in_year
                avg_in_year = []

    print(dict_rank_avg)
    print(len(dict_rank_avg))

    df = pd.DataFrame(dict_rank_avg)
    print(df)
    graph = px.line(df, y=dict_rank_avg, x=['2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021'],
                    labels={'value': 'Average Salaries($)', 'x': 'Academic Years(yr)', 'variable': 'Academic Ranks'},
                    title='Average Salary Change per Year for Academic Ranks', markers=True)
    graph.show()


graph_function2()
graph_function1()
