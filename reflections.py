# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api.network import Network
from typing import Generator
from piazza_api import Piazza
import re, csv
from time import sleep


# Reflection data
posts_csv = "posts.csv"
posts_tags = ["nr", "folders"] # This data is directly pulled from highest level of post data
posts_metadata = ["student uid", "section date", "uid+date", "date posted", "title"] # This data is pulled from post history
posts_titles = posts_metadata + posts_tags + ["post made"]


def get_posts(cs375 : Network, min_post=0, max_post=9999999) -> Generator:
    """ Gets posts based on a range
    """
    if not (max_post or min_post):
        return cs375.iter_all_posts()
    else:
        feed = cs375.get_feed(limit=999999, offset=0)
        cids = [post['id'] for post in feed["feed"] if min_post < int(post["nr"]) <= max_post]
        for cid in cids:
            yield cs375.get_post(cid)
            sleep(0.25)

"""
Self Reflections
"""

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
                        print(processed["nr"])
                    sleep(1)
                except Exception as e:
                    print(post["nr"], " ", e)
    except IOError:
        print("I/O error")

def process_post(post : dict) -> dict:
    """ Processes an individual post
    :param post: post metadata
    :returns: processed post metadata based on tags in posts_titles
    """
    metadata = {tag: post[tag] for tag in posts_tags}
    
    other_folders = ["logistics", "other", "survey", "peer_observation", "lecture_makeup", "self_reflection_makeup"]
    if True in [folder in other_folders for folder in metadata["folders"]]:
        raise Exception("is in folders ", metadata["folders"], " and was not included in csv")

    metadata.update(process_history(post["history"]))

    title_lower = metadata["title"].lower()

    if "video observation" in title_lower or "makeup" in title_lower or "make up" in title_lower:
        raise Exception("title is <", title_lower, "> and was not included in csv")

    metadata.update({"uid+date": metadata["student uid"]+metadata["section date"], "post made": 1})
    return metadata

def process_history(post_hist : list) -> dict:
    """Parses history metadata for title, date, student uid, and creation date.
    :param post_hist: post history 
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
    sect_date = re.search("([678]{1}\/\d+)", subject)
    sect_date = sect_date.group() if sect_date else "Error"
    if sect_date[2] == "0":
        sect_date = sect_date[:2] + sect_date[3:]

    hist_result.update({"section date": sect_date, "title": subject})
    return hist_result
