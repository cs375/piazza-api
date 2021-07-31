# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api.network import Network
import csv
from time import sleep

# User data
users_csv = "users.csv"
users_tags = ["id", "name", "email"]
users_titles = users_tags


"""
Users
"""

def write_csv_users(users : list) -> None:
    """ Writes users to user csv
    :param users: list of processed user metadata
    """
    try:
        with open(users_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=users_titles)
            writer.writeheader()
            for data in users:
                writer.writerow(data)
                sleep(1)
    except IOError:
        print("I/O error")

def process_all_users(users : list, users_tags : list) -> list:
    """ Processes all users
    :param users: list of users (each user is a dictionary with metadata)
    :returns: list of users filtered for specific metadata 
    """
    return [process_user(user, users_tags) for user in users]

def process_user(user : dict, users_tags : list) -> dict:
    """ Processes individual user
    :param user: user with metadata
    :returns: filtered dictionary of user metadata based on users_tags
    """
    return {tag: user[tag] for tag in users_tags}


