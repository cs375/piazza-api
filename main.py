# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api import Piazza
import re, csv
from time import sleep

# Initialize Piazza instance and login
p = Piazza()
p.user_login("yolanda.shen.3@gmail.com", "cs375su2021")
user_profile = p.get_user_profile()

# Access 375 Summer 2021 Piazza data (posts and users)

cs375 = p.network("kp3aw8qu5pkm9")
posts = cs375.iter_all_posts(limit = 100) # TODO: no limit causes post-fetching error, annoyingly
users = cs375.get_all_users()

# Generate CSVs
generate_posts = True
generate_users = False

# Create csv for reflection data
# Metadata: post number, folders, student uid, date of section, title of post
# FIXME: also track date of original post
posts_csv = "posts.csv"
posts_tags = ["nr", "folders"]
posts_metadata = ["student uid", "date", "title"]
posts_titles = posts_metadata + posts_tags

# Initialize csv for students
# Metadata: student uid, student name, email
users_csv = "users.csv"
users_tags = ["id", "name", "email"]
users_titles = users_tags


"""
Posts
"""

# Writes to posts csv (writes after all posts have been processed rather than after each post)
# 
# def write_csv_posts(posts):
#     try:
#         with open(posts_csv, 'w') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=posts_titles)
#             writer.writeheader()
#             for data in posts:
#                 writer.writerow(data)
#     except IOError:
#         print("I/O error")

# Processes all fetched posts and writes each post to the csv as a row
def process_all_posts(posts):
    #return [process_post(post) for post in posts]
    try:
        with open(posts_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=posts_titles)
            writer.writeheader()
            for data in posts:
                writer.writerow(process_post(data))
                sleep(1)
    except IOError:
        print("I/O error")

# Processes an individual post
def process_post(post):
    dict = {tag: post[tag] for tag in posts_tags}
    dict["student uid"] = post["history"][-1]["uid"]
    dict.update(process_title(post["history"][0]["subject"]))
    return dict

# Parses a title for a date of format m/dd
def process_title(subject):
    date = re.search("(\d+\/\d+)", subject)
    if not date:
        date = "Error"
    else:
        date = date.group()
    return {"date": date, "title": subject}


"""
Users
"""

# Writes to user csv
def write_csv_users(users):
    try:
        with open(users_csv, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=users_titles)
            writer.writeheader()
            for data in users:
                writer.writerow(data)
                sleep(1)
    except IOError:
        print("I/O error")

# Process all users
def process_all_users(users):
    return [process_user(user) for user in users]

# Process individual user
def process_user(user):
    return {tag: user[tag] for tag in users_tags}


"""
CSV creation
"""

if generate_posts:
    process_all_posts(process_all_posts(posts))
if generate_users:
    write_csv_users(process_all_users(users))