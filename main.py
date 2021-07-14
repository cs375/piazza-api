# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api import Piazza
from piazza_processing import *

# Initialize Piazza instance and login
p = Piazza()
p.user_login("yolanda.shen.3@gmail.com", "") # Remove PW when committing
user_profile = p.get_user_profile()

# Access 375 Summer 2021 Piazza data (posts and users)
cs375 = p.network("kp3aw8qu5pkm9")
posts = get_posts(cs375, min_post=None, max_post=78)
users = cs375.get_all_users()

# Generate CSVs
generate_posts = True
generate_users = False

"""
CSV creation
"""

if generate_posts:
    process_all_posts(posts)
if generate_users:
    write_csv_users(process_all_users(users, users_tags))

