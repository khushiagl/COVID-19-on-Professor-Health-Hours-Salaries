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
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import dataset_classes
import basic_computations as cmp

list_of_salaries = dataset_classes.create_salary_data('prof_salaries.csv')
list_of_hours = dataset_classes.create_people_data('prof_hours.csv')
years = [(2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]
salary_types = ['Average', 'Median', 'Tenth Percentile', 'Ninetieth Percentile']
scale_types = ['Negative affect scale', 'Situational Loneliness scale',
               'Family and social support scale']


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

    graph.update_layout(title='Average Percentage Salary Change per Year in Canadian Universities',
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

    create_min_max_data(x_values, y_values, bar_data)

    graph = go.Figure(data=bar_data)
    # Create dropdown menu
    starting_graph_button = dict(label="All",
                                 method="update",
                                 args=[{"visible": [True] * len(bar_data)},
                                       {"title": "Minimum and Maximum Salaries per Year of Canadian"
                                                 " Universities (All Salary Types)"}])
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

    graph.update_layout(title='Minimum and Maximum Salaries per Year of Canadian Universities',
        updatemenus=[dict(active=0, buttons=list(menu_list))],
        yaxis=dict(title='Salary($)'), xaxis=dict(title='Academic Years(yr)'), barmode='group')
    graph.show()


def graph_avg_role_hours() -> None:
    """ Plot a bar graph of the average hours worked for different academic roles
    using plotly.express."""
    role_list = possible_roles()
    avg_for_role = []
    for role in role_list:
        avg_for_role.append(average_hours_role(role))

    dict_role_avgs = {'Roles': role_list, 'Hours': avg_for_role}

    df = pd.DataFrame(dict_role_avgs)
    graph = px.bar(df, y='Hours', x='Roles', title='Average Hours Worked per Academic Role',
                   color='Hours')
    graph.show()


def graph_avg_salary_ranks() -> None:
    """" Plot a line graph of the change in average salaries per year for different academic ranks
    using plotly.express."""
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
    df = pd.DataFrame(dict_rank_avg)
    graph = px.line(df, y=dict_rank_avg,
                    x=['2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021'],
                    labels={'value': 'Average Salaries($)', 'x': 'Academic Years(yr)',
                            'variable': 'Academic Ranks'},
                    title='Average Salary Change per Year for Academic Ranks', markers=True)
    graph.show()


def graph_avg_salaries() -> None:
    """ Plot a line graph of the change in average salaries per year for Canadian universities
    using plotly.express."""
    dict_of_uni_salaries = {}
    list_of_institutions = []
    list_of_institutions_ranks = []
    list_of_institutions_ranks = all_ranks_only(list_of_institutions_ranks)
    list_of_institutions = all_institutions(list_of_institutions)

    create_dict_dataframe(list_of_institutions, list_of_institutions_ranks, dict_of_uni_salaries)

    df = pd.DataFrame(dict_of_uni_salaries)

    graph = px.line(df, y=dict_of_uni_salaries,
                    x=['2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021'],
                    labels={'value': 'Average Salaries($)', 'x': 'Academic Years(yr)',
                            'variable': 'Canadian Universities'},
                    title='Average Salary Change per Year in Canadian Universities', markers=True)

    # create list of menu items for each university
    all_true = [True] * len(dict_of_uni_salaries)
    list_of_buttons = [dict(label='All Universities',
                            method="update",
                            args=[{"visible": all_true}])]
    index = 0
    for uniname in dict_of_uni_salaries:
        graph_booleans = [False] * len(dict_of_uni_salaries)
        graph_booleans.pop(index)
        graph_booleans.insert(index, True)
        button = dict(label=uniname,
                      method="update",
                      args=[{"visible": graph_booleans}])
        list_of_buttons.append(button)
        index += 1

    graph.update_layout(updatemenus=[
        dict(
            active=0,
            buttons=list(list_of_buttons)
        ),
    ], )
    graph.show()


def graph_mental_health() -> None:
    """Represent mental health data through a bar graph using plotly express."""
    data = dataset_classes.create_health_data('prof_mental_health.csv')
    bar_data = []
    create_mental_health_data(data, bar_data)

    graph = go.Figure(data=bar_data)
    # Create dropdown menu
    starting_graph_button = dict(label="All",
                                 method="update",
                                 args=[{"visible": [True] * len(bar_data)},
                                       {"title": "Responses to Mental Health Survey (All Scales)"}])
    menu_list = [starting_graph_button]

    for i in range(len(scale_types)):
        graph_booleans = [False] * len(bar_data)
        graph_booleans.pop(i)
        graph_booleans.insert(i, True)
        button = dict(label=scale_types[i],
                      method="update",
                      args=[{"visible": graph_booleans},
                            {"title": "Responses to Mental Health Survey (" + scale_types[i]
                                      + " Scale)"}])
        menu_list.append(button)

    graph.update_layout(title='Responses to Mental Health Survey',
        updatemenus=[dict(active=0, buttons=list(menu_list))],
        yaxis=dict(title='Likert Scale Mean Score'), xaxis=dict(title='Item'), barmode='group')
    graph.show()


# Helper functions
def all_ranks_only_specific_uni(lst: list, inst: str) -> list:
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
        percentages = cmp.calculate_salary_percentage(list_of_institutions_ranks,
                                                      'Average')
        line_data.append(go.Line(name=institution, x=x_values, y=percentages))


def create_min_max_data(x_values: list, y_values: dict, bar_data: list) -> None:
    """Mutate the list bar_data to contain go.Bars for each salary type"""
    for salary_type in salary_types:
        min_salary = cmp.return_min_salary(list_of_salaries, salary_type)
        max_salary = cmp.return_max_salary(list_of_salaries, salary_type)
        y_values[salary_type] = (min_salary, max_salary)
        bar_data.append(go.Bar(name='Minimum ' + salary_type + ' Salary', x=x_values,
                               y=y_values[salary_type][0]))
        bar_data.append(go.Bar(name='Maximum ' + salary_type + ' Salary', x=x_values,
                               y=y_values[salary_type][1]))


def possible_roles() -> list[str]:
    """ Return list of all possible roles in hours dataset."""
    list_of_roles = []
    for obj in list_of_hours:
        if obj.role not in list_of_roles:
            list_of_roles.append(obj.role)

    return list_of_roles


def average_hours_role(role: str) -> float:
    """ Return the average salary for the given role."""
    list_of_hours_avg = []
    for obj in list_of_hours:
        if obj.role == role:
            list_of_hours_avg.append(obj.average_hours)

    return sum(list_of_hours_avg) / len(list_of_hours_avg)


def possible_ranks() -> list[str]:
    """ Return list of all possible academic ranks in salaries dataset."""
    list_of_ranks = []
    for obj in list_of_salaries:
        if obj.rank not in list_of_ranks:
            list_of_ranks.append(obj.rank)

    return list_of_ranks


def average_ranks_year(year: tuple[int, int], rank: str) -> float:
    """ Return the average salary for a given rank during a given year."""
    list_of_nums = []
    for obj in list_of_salaries:
        if obj.ref_date == year and obj.rank == rank:
            list_of_nums.append(obj.avg_salary)

    return sum(list_of_nums) / len(list_of_nums)


def all_ranks_only(lst: list) -> list:
    """ Return list of only Person objects with rank 'All ranks combined (including deans)'."""
    for obj in list_of_salaries:
        if obj.rank == 'All ranks combined (including deans)':
            lst.append(obj)
    return lst


def create_dict_dataframe(list_of_institutions: list, list_of_institutions_ranks: list,
                          dict_of_uni_salaries: dict) -> None:
    """Mutate given dictionary for graph dataframe using data from the given lists."""
    for year in years:
        temp_universities = list(list_of_institutions)
        for obj1 in list_of_institutions_ranks:
            if year == obj1.ref_date:
                mutate_dict_dataframe(list_of_institutions, dict_of_uni_salaries, obj1,
                                      temp_universities)
        if len(temp_universities) > 0:
            fill_incomplete_data(dict_of_uni_salaries, temp_universities)


def mutate_dict_dataframe(list_of_institutions: list, dict_of_uni_salaries: dict,
                          obj1: dataset_classes.InstitutionSalaries, temp_uni: list) -> None:
    """Helper function for mutating dictionary for dataframe."""
    for uni in list_of_institutions:
        if uni == obj1.institution:
            if uni in temp_uni:
                temp_uni.remove(uni)
            if uni in dict_of_uni_salaries:
                dict_of_uni_salaries[uni].append(obj1.avg_salary)
                break
            else:
                dict_of_uni_salaries[uni] = [obj1.avg_salary]
                break


def fill_incomplete_data(dict_of_uni_salaries: dict, temp_uni: list) -> None:
    """Helper function for filling incomplete data in dataframe dictionary"""
    for tuni in temp_uni:
        if tuni in dict_of_uni_salaries:
            dict_of_uni_salaries[tuni] += [None]
        else:
            dict_of_uni_salaries[tuni] = [None]


def create_mental_health_data(data: list, bar_data: list) -> None:
    """Mutate the list pie_data to contain go.Bars for each scale"""
    for scale in scale_types:
        x_values = [health.item for health in data if health.scale == scale]
        y_values = [health.mean for health in data if health.scale == scale]
        bar_data.append(go.Bar(name=scale, x=x_values, y=y_values))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['dataset_classes', 'basic_computations', 'plotly.graph_objs',
                          'plotly.express', 'pandas'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
