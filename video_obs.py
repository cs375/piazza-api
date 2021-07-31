# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api.network import Network
from typing import Generator
from piazza_api import Piazza
import re, csv
from time import sleep

# Video Observation data
obs_csv = "obs.csv"
obs_tags = ["nr", "folders"]
obs_metadata = ["student uid", "section date", "uid+date", "title", "responded"]
obs_titles = obs_metadata + obs_tags


"""
Video Observations
"""

def process_all_vid_obs(obs : list) -> None:
    """ Processes and writes video observations to csv
    :param obs: list of processed video observation metadata
    """
    try:
        with open(obs_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=obs_titles)
            writer.writeheader()
            for ob in obs:
                try:
                    processed = process_ob(ob)
                    if processed:
                        if processed["nr"] < 391:
                            break
                        writer.writerow(processed)
                        print(processed["nr"])
                    sleep(0.5)
                except Exception as e:
                    print(ob["nr"], " ", e)
    except IOError:
        print("I/O error")


def process_ob(obs : dict) -> dict:
    """ Processes an individual post
    :param obs: video observation metadata
    :returns: processed post metadata based on tags in posts_titles
    """
    metadata = {tag: obs[tag] for tag in obs_tags}

    metadata.update(process_obs(obs["children"], obs["history"]))

    metadata.update({"uid+date": metadata["student uid"] + metadata["section date"]})

    # for k,v in metadata.items():
    #     print(k, v)

    folders = metadata["folders"]

    if "peer_observation" in folders or "video observation" in metadata["title"].lower():
        if "logistics" not in folders and "self_reflection_makeup" not in folders :
            return metadata
    raise Exception(metadata["title"], " is in folders ", metadata["folders"], " and was not included in csv")

def process_obs(obs_children : dict, obs_hist : list) -> dict:
    """Parses history metadata for title, date, student uid, and creation date.
    :param post_hist: post history 
    :returns: dictionary with relevant history data pulled.
    """
    result = {}
    latest = obs_hist[0]
    result["student uid"] = obs_hist[-1]["uid"]
    subject = latest["subject"]

    # Date of section, in m/dd format
    sect_date = re.search("([678]{1}\/\d+)", subject)
    sect_date = sect_date.group() if sect_date else "Error"

    # Checks for student response or response in comments
    # print(obs_children[0].keys())
    student_response = [response["history"][0]["uid"] for response in obs_children if response["type"]=="s_answer"]

    try:
        student_response += [response["uid"] for response in obs_children if response["type"]=="followup"]
    except:
        if len(student_response) == 0:
            student_response += ["manual check required"]

    result.update({"section date": sect_date, "title": subject, "responded": student_response})
    return result