# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api.network import Network
from typing import Generator
from piazza_api import Piazza
import csv
from time import sleep

# Survey data
survey_csv = "surveys.csv"
survey_tags = ["nr", "folders"]
survey_metadata = ["student uid", "title"]
survey_titles = survey_metadata + survey_tags


"""
Surveys
"""

def process_all_surveys(surveys : list) -> None:
    """ Processes and writes surveys to csv
    :param survey: list of processed survey metadata
    """
    try:
        with open(survey_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=survey_titles)
            writer.writeheader()
            for s in surveys:
                try:
                    processed = process_surveys(s)
                    if processed:
                        writer.writerow(processed)
                        print(processed["nr"])
                    sleep(0.5)
                except Exception as e:
                    print(s["nr"], " ", e)
    except IOError:
        print("I/O error")


def process_surveys(survey : dict) -> dict:
    """ Processes an individual post
    :param survey: survey metadata
    :returns: processed post metadata based on tags in posts_titles
    """
    metadata = {tag: survey[tag] for tag in survey_tags}

    metadata.update(process_survey_hist(survey["children"], survey["history"]))

    # for k,v in metadata.items():
    #     print(k, v)

    folders = metadata["folders"]

    if "survey" in folders or "survey" in metadata["title"].lower():
        if "logistics" not in folders and "other" not in folders:
            return metadata
    raise Exception(metadata["title"], " is in folders ", metadata["folders"], " and was not included in csv")

def process_survey_hist(survey_children : dict, survey_hist : list) -> dict:
    """Parses history metadata for title, date, student uid, and creation date.
    :param post_hist: post history 
    :returns: dictionary with relevant history data pulled.
    """
    result = {}
    latest = survey_hist[0]
    result["student uid"] = survey_hist[-1]["uid"]
    subject = latest["subject"]

    result.update({"title": subject})
    return result