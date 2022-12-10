"""
CSC110 Project: How COVID - 19 Changed Post - Secondary Professors' Health, Hours, and Salaries

Module Description
===================
This module contains the functions that graph computations on the data classes.

Copyright and Usage Information
=================================

This file is provided solely for the personal and private use of instructors and TAs of CSC110
at the University of Toronto St.George campus.All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

This file is Copyright(c) 2021 Kaylee Chan, Davit Barsamyan, Khushi Agrawal, and Meghan George.
"""
import hours_data_class
import basic_computations as cmp
import plotly.graph_objs as go

list_of_salaries = hours_data_class.create_salary_data('prof_salaries.csv')
list_of_hours = hours_data_class.create_people_data('prof_hours.csv')
years = [(2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]
salary_types = ['Average', 'Median', 'Tenth Percentile', 'Ninetieth Percentile']


def graph_average_salary_change() -> None:
    """Plot a line graph of the percentage change between average salaries for each schoolyear
    for Canadian Universities."""
    list_of_institutions = []
    list_of_institutions = all_institutions(list_of_institutions)
    line_data = []

    create_line_data(list_of_institutions, line_data)

    graph = go.Figure(data=line_data)

    starting_graph_button = dict(label="All",
                                 method="update",
                                 args=[{"visible": [True] * len(line_data)}])

    institute_menu_list = [starting_graph_button]

    # Buttons for Dropdown List
    for i in range(len(line_data)):
        graph_booleans = [False] * len(line_data)
        graph_booleans.pop(i)
        graph_booleans.insert(i, True)
        button = dict(label=list_of_institutions[i],
                      method="update",
                      args=[{"visible": graph_booleans}])
        institute_menu_list.append(button)

    graph.update_layout(
        updatemenus=[dict(active=0, buttons=list(institute_menu_list))],
        yaxis=dict(title='Average Salary Change per Year(%)'),
        xaxis=dict(title='Academic Years(yr)'), barmode='group')
    graph.show()


def graph_max_min_salaries() -> None:
    """Build a bar graph representing the maximum and minimum salaries of all types between Canadian
    Universities for each schoolyear."""
    y_values = {}
    x_values = ['2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021']
    bar_data = []

    create_bar_data(x_values, y_values, bar_data)

    graph = go.Figure(data=bar_data)
    # Create dropdown menu
    starting_graph_button = dict(label="All",
                                 method="update",
                                 args=[{"visible": [True] * len(bar_data)},
                                       {"title": "Minimum and Maximum Salaries per Year of Canadian "
                                                 "Universities (All Salary Types)"}])
    menu_list = [starting_graph_button]

    for i in range(len(salary_types)):
        graph_booleans = [False] * len(bar_data)
        indices = [i * 2, (i * 2) + 1]
        for x in indices:
            graph_booleans.pop(x)
            graph_booleans.insert(x, True)
        button = dict(label=salary_types[i] + " Salaries",
                      method="update",
                      args=[{"visible": graph_booleans},
                            {"title": "Minimum and Maximum Salaries per Year of Canadian "
                                      "Universities (" + salary_types[i] + " Type)"}])
        menu_list.append(button)

    graph.update_layout(
        updatemenus=[dict(active=0, buttons=list(menu_list))],
        yaxis=dict(title='Salary($)'), xaxis=dict(title='Academic Years(yr)'), barmode='group')
    graph.show()


# Helper functions
def all_ranks_only_specific_uni(lst, inst: str):
    """Return list of only Person objects with rank 'All ranks combined (including deans)'."""
    for obj in list_of_salaries:
        if obj.rank == 'All ranks combined (including deans)' and obj.institution == inst:
            lst.append(obj)
    return lst


def all_institutions(lst: list) -> list:
    """Return list of all institutions in salaries dataset."""
    for obj in list_of_salaries:
        if obj.institution not in lst:
            lst.append(obj.institution)
    return lst


def create_line_data(list_of_institutions: list, line_data: list) -> None:
    """Mutate the list line_data to contain go.Lines for each institution in list_of_institutions"""
    for institution in list_of_institutions:
        list_of_institutions_ranks = []
        list_of_institutions_ranks = all_ranks_only_specific_uni(list_of_institutions_ranks,
                                                                 institution)
        x_values = [str(list_of_institutions_ranks[x].ref_date) for x in
                    range(1, len(list_of_institutions_ranks))]
        percentages = cmp.calculate_salary_percentage_difference(list_of_institutions_ranks,
                                                                 'Average')
        line_data.append(go.Line(name=institution, x=x_values, y=percentages))


def create_bar_data(x_values: list, y_values: dict, bar_data: list) -> None:
    """Mutate the list bar_data to contain go.Bars for each salary type"""
    for salary_type in salary_types:
        min_salary = cmp.return_min_salary(list_of_salaries, salary_type)
        max_salary = cmp.return_max_salary(list_of_salaries, salary_type)
        y_values[salary_type] = (min_salary, max_salary)
        bar_data.append(go.Bar(name='Minimum ' + salary_type + ' Salary', x=x_values, y=y_values[salary_type][0]))
        bar_data.append(go.Bar(name='Maximum ' + salary_type + ' Salary', x=x_values, y=y_values[salary_type][1]))
