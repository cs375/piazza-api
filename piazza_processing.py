# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api.network import Network
from typing import Generator
from piazza_api import Piazza
import re, csv
from time import sleep


# Create csv for reflection data
posts_csv = "posts.csv"
posts_tags = ["nr", "folders"] # This data is directly pulled from highest level of post data
posts_metadata = ["student uid", "section date", "date posted", "title"] # This data is pulled from post history
posts_titles = posts_metadata + posts_tags + ["post made"]

# Initialize csv for students
users_csv = "users.csv"
users_tags = ["id", "name", "email"]
users_titles = users_tags


"""
Posts
"""

def get_posts(cs375 : Network, min_post=None, max_post=None) -> Generator:
    """ Gets posts based on a range
    """
    if not (max_post or min_post):
        return cs375.iter_all_posts()
    else:
        feed = cs375.get_feed(limit=999999, offset=0)
        cids = [post['id'] for post in feed["feed"]]
        if max_post is not None:
            min_post = 0 if min_post is None else min_post
            cids = cids[::-1][min_post:max_post]
        for cid in cids:
            yield cs375.get_post(cid) 


def process_all_posts(posts : list) -> None:
    """ Processes and writes posts to post csv
    :param posts: list of processed post metadata
    """
    try:
        with open(posts_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=posts_titles)
            writer.writeheader()
            for post in posts:
                try:
                    processed = process_post(post)
                    if processed:
                        writer.writerow(processed)
                    sleep(1)
                except Exception:
                    print(Exception)
                    print(post["nr"])
    except IOError:
        print("I/O error")

def process_post(post : dict) -> dict:
    """ Processes an individual post
    :param post: post metadata
    :returns: processed post metadata based on tags in posts_titles
    """
    metadata = {tag: post[tag] for tag in posts_tags}
    
    other_folders = ["logistics", "other", "survey", "peer_observation"]
    if True in [folder in other_folders for folder in metadata["folders"]]:
        print(str(metadata["nr"]) + " " + str(metadata["folders"]))
        return

    metadata.update(process_history(post["history"]))
    metadata.update({"post made": 1})
    return metadata


def process_history(post_hist : dict) -> dict:
    """Parses history metadata for title, date, student uid, and creation date.
    :param post_hist: earliest post history 
    :returns: dictionary with relevant history data pulled.
    """
    hist_result = {}
    init_post = post_hist[-1]
    hist_result["student uid"] = init_post["uid"]

    # Fetch creation date and convert from m-dd to m/dd form
    date = init_post["created"]
    hist_result["date posted"] = date[6:7] + "/" + date[8:10]
    subject = post_hist[0]["subject"]

    # Date of section, in m/dd format
    date = re.search("(\d{1}\/\d+)", subject)
    date = date.group() if date else "Error"

    hist_result.update({"section date": date, "title": subject})
    return hist_result

    

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


