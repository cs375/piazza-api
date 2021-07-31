# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api import Piazza
from piazza_api.network import FolderFilter
from reflections import *
from video_obs import *
from surveys import *
from users import *

# Initialize Piazza instance and login
p = Piazza()
p.user_login("yolanda.shen.3@gmail.com", "") # Remove PW when committing
user_profile = p.get_user_profile()

# Access 375 Summer 2021 Piazza data (posts and users)
cs375 = p.network("kp3aw8qu5pkm9")

# Generate CSVs
generate_posts = True
generate_obs = False
generate_surveys = False
generate_users = False

if generate_posts:
    posts = get_posts(cs375, min_post=719, max_post=721)
    process_all_posts(posts)
if generate_obs:
    obs = get_posts(cs375, min_post=340, max_post=None)
    # for k,v in next(obs).items():#["feed"][5].items():
    #     print(k, " ", v)

    # for i in next(obs)["children"]:
    #     if i["type"] == "i_answer":
    #         continue
    #     for k, v in i.items():
    #         print(k, " ", v)
    #     print("\n")

    process_all_vid_obs(obs)
if generate_surveys:
    surveys = get_posts(cs375, min_post=550, max_post=None)
    process_all_surveys(surveys)
if generate_users:
    users = cs375.get_all_users()        
    write_csv_users(process_all_users(users, users_tags))

