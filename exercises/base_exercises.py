# import area

from typing import List
import re
import pandas as pd
import requests

"""
- Please do not change the the name of the already defined functions from below.
- For all the functions consider Exception Handling(if applicable).
- For all the functions consider doing validations of the input parameters - when applicable, of course
- Feel free to add additional functions if you need them.
"""


def parse_dictionary(input_dict: dict) -> list:
    """
    Given a dictionary with several keys and possible duplicated values(two keys might have the same value),
    identify the duplicated values.
    E.g. input:
     - {'a': 47, 'b': 52, 'c': 47, 'd': 44, 'e': 52, 'f': 53, 'g': 54, 'h': 44, 'i': 54}
     - {'z': 47, 'y': 52, 'x': 47, 'w': 44, 'v': 52, 'u': 53, 't': 54, 's': 44, 'r': 54}
    !!! Be aware that the name of the keys is IRRELEVANT and they should not be considered in the code - the response should be the same for both sample dicts from above
    :param input_dict:
    :return: list:
        - for the example dictionary from above the result should be: [47, 52, 44, 53, 54]
    """
    empty_list = []
    try:
        for key, value in input_dict.items():
            x = value
            if x not in empty_list:
                empty_list.append(x)
        return empty_list
    except AttributeError:
        return 'Error: The input is not a dictionary!'


a = parse_dictionary(
    {'a': 47, 'b': 52, 'c': 47, 'd': 44, 'e': 52, 'f': 53, 'g': 54, 'h': 44, 'i': 54, 'z': 47, 'y': 52, 'x': 47,
     'w': 44, 'v': 52, 'u': 53, 't': 54, 's': 44, 'r': 54})
# b = parse_dictionary(['52', '5253'])
print(a)


def identify_missing_students(all_students: list, students_who_completed: list) -> list:
    """
    Given the list of all students and the list of students who completed the assessment, identify the students who did not complete the assessment
    :param all_students: list - all the students who should have completed the assessment
    :param students_who_completed: - students who already completed the assessment
    :return: list - students who have not already completed the assessment
    """
    assessment_not_completed = []
    duplicate_name_all_students = set(all_students)

    for student in all_students:
        duplicate_name_all_students.add(student)
        if len(duplicate_name_all_students) != len(all_students):
            return 'Error: There are students with the same name, please add last name!'
        if student not in students_who_completed:
            assessment_not_completed.append(student)

    return assessment_not_completed


c = identify_missing_students(['vlad', 'mircea', 'alex', 'mihai'], ['alex', 'mihai'])
print(c)


def identify_numbers_v1(possible_numbers: list) -> list:
    """
    Given an input list which can contain both numeric and alphanumeric chars, identify a list numbers based on condition:
        - list element > 1.4
    The function can contain multiple instructions in multiple lines.
    The function should be done before idenfify_numbers_v2
    :param possible_numbers: list - containing both numbers and strings
    :return: list - containing the numbers from the input list which matched the condition from above; if no entry matches the condition return an empty list
    """
    number_list = []
    for element in possible_numbers:
        if ((type(element) == int) or (type(element) == float)) and (element > 1.4):
            number_list.append(element)

    return number_list


d = identify_numbers_v1(['vlad', 1.2, 2.4])
print(d)


def identify_substring(full_message: str, strings_to_find: list) -> dict():
    """
    Identifies in a string message the number of occurrences for specific strings
    :param full_message: str - contains the full message string which needs to be searched for the input substrings
    :param strings_to_find: list(str) - strings to be searched in the full message
    :return: dict("substring": "no_occurrences") - if none of the strings in the list will e found in the full message, return None
    """
    empty_dict = {}
    comparative_list = []

    try:
        for string in strings_to_find:
            number_of_occurrences = full_message.count(string)
            empty_dict[string] = number_of_occurrences
            if string not in full_message:
                comparative_list.append(string)

        if len(comparative_list) == len(strings_to_find):
            return None

    except TypeError:
        return "The substring list contains other types than str"

    else:
        return empty_dict


e = identify_substring('welcome to my python exercises', ['q', 'b'])
print(e)


def validate_password(input_pwd: str) -> bool:
    """
    Validates a password sent by the user
    :param input_pwd: str - input password to be validated cross the following rules:
        - should be between 10 and 15 chars
        - should contain at least one number
        - should contain at least one special character
        - should contain at least 1 uppercase/lowercase letter
    :return: bool - True/False depending on the validity of the input string
    """

    password = re.search("^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{10,15}$", input_pwd)
    if password:
        return True
    print(
        'Password must contain between 10 and 15 chars, one number, one special character and at least one uppercase/lowercase letter')
    return False


f = validate_password('Vlad123!zavate')
print(f)


def footbal_championship_winner(input_file: str) -> str:
    """
    Find the football championship winner.
    Assumption 1: Input file can be in CSV or JSON format.
    Assumption 2: If input file is csv, on the first row the headers are present
    Each team is granted with points based on the following rules:
     - 0 points for lose
     - 1 point for a draw
     - 3 points for a win
    If, multiple team have the same number of points, the winner is decided
        based on the average goals per match. Higher scoring team wins!
    If, there is still equality, choose a method of your own to decide
        the winner.
    Test files must be provided for all scenarios.
    :param input_file: str - input file containing matches results
    :return str - name of the winning team
    """

    championship = pd.read_csv(input_file)
    championship['home_score'] = championship['score'].apply(lambda x: x[0] if x[2] != '-' else x[:2])
    championship['away_score'] = championship['score'].apply(lambda x: x[-1] if x[-3] != '-' else x[-2:])

    championship['Points'] = 0
    team_name = dict(zip(championship['home_team'], championship['Points']))

    for index, row in championship.iterrows():
        if row['home_score'] > row['away_score']:
            team_name[row['home_team']] += 3
        elif row['home_score'] == row['away_score']:
            team_name[row['home_team']] += 1
            team_name[row['away_team']] += 1
        elif row['home_score'] < row['away_score']:
            team_name[row['away_team']] += 3

    winner = max(team_name, key=team_name.get)

    return winner


h = footbal_championship_winner(
    'C:/Users/ZZ03NO826/PycharmProjects/Python-Upskill/python-core-de-training-refactored/app/datasets/football_championship_input.csv')
print(h)


def fetch_data_from_url(url: str):
    """
    Fetch data from a given URL using HTTP GET request.

    Args:
    - url (str): The URL to make the request to.

    Returns:
    - tuple: (status_code, response_content)
    """
    try:
        response = requests.get(url=url)
        return (response.status_code, response.content)
    except requests.RequestException:
        return 'Error with the request'


i = fetch_data_from_url('https://www.google.co.uk/')
print(i)


