#import area

from typing import List

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
    pass


def identify_missing_students(all_students: list, students_who_completed: list) -> list:
    """
    Given the list of all students and the list of students who completed the assessment, identify the students who did not complete the assessment
    :param all_students: list - all the students who should have completed the assessment
    :param students_who_completed: - students who already completed the assessment
    :return: list - students who have not already completed the assessment
    """
    pass


def identify_numbers_v1(possible_numbers: list) -> list:
    """
    Given an input list which can contain both numeric and alphanumeric chars, identify a list numbers based on condition:
        - list element > 1.4
    The function can contain multiple instructions in multiple lines.
    The function should be done before idenfify_numbers_v2
    :param possible_numbers: list - containing both numbers and strings
    :return: list - containing the numbers from the input list which matched the condition from above; if no entry matches the condition return an empty list
    """
    pass


def identify_substring(full_message: str, strings_to_find: list) -> dict():
    """
    Identifies in a string message the number of occurrences for specific strings
    :param full_message: str - contains the full message string which needs to be searched for the input substrings
    :param strings_to_find: list(str) - strings to be searched in the full message
    :return: dict("substring": "no_occurrences") - if none of the strings in the list will e found in the full message, return None
    """
    pass


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
    pass


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
    pass


def fetch_data_from_url(url: str):
    """
    Fetch data from a given URL using HTTP GET request.

    Args:
    - url (str): The URL to make the request to.

    Returns:
    - tuple: (status_code, response_content)
    """
    pass


