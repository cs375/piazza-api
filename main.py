# Author: Yolanda Shen
# CS375 Summer 2021

from piazza_api import Piazza
from piazza_processing import *

# Initialize Piazza instance and login
p = Piazza()
p.user_login("yolanda.shen.3@gmail.com", "")
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


# print(process_history([{'anon': 'no', 'uid': 'jzqdjhlqvpz5kr', 'subject': 'Brianna Fan, CS 70, 07/01 [Discussion]', 'created': '2021-07-05T20:39:55Z', 'content': '<p><span style="text-decoration:underline">Before your section</span><br /> <br /><strong>What are the learning goals of the discussion section or lab?</strong><br />- continuing modular arithmetic, more focus on equations and chinese remainder theorem<br /><br /><strong>Which topic do you predict will be the most difficult for the students to learn?</strong><br />- how chinese remainder theorem works, what modular equivalencies mean<br /><br/><strong>What is one thing about your teaching that you want to focus on during this class?</strong><br />- being more encouraging, saying &#34;great question&#34; per this week&#39;s 375 class<br /><br /><strong>What activities will you do during class? (e.g. Group work? Pair work? Lecture? Physical demo?)</strong><br />- breakout rooms, group solving of the last CRT question<br /><br /><span style="text-decoration:underline">Immediately after your section</span><br /> <br /><strong>First things first I’m the realest</strong><br /> <br /><strong>What went really well today? :)</strong><br />- Students were very engaged, especially in the second section. They made some jokes and participated in the chat as well, seemed like they were comfortable with each other as well. Someone even asked where another student was bc they had an excused absence.<br /><br /><strong>What didn’t go so well?</strong><br />- Didn&#39;t get to the last question for the first section, but I got to it in the second and it went well.</p>\n<p>- Fireworks were going off (Canada Day) which was slightly disruptive but I think it actually made the atmosphere more relaxed and was fun for the students.<br /><br /><strong>Presentation</strong><br /> <br />Did you:</p>\n<ul><li>speak in a clear voice that could be easily heard?\xa0<strong>Yes</strong></li><li dir="ltr">write clearly?\xa0<strong>Yes</strong></li><li dir="ltr">listen carefully to students’ comments and questions without interrupting?\xa0<strong>Yes</strong></li><li dir="ltr">appear confident?\xa0<strong>Yes</strong></li><li dir="ltr">appear enthusiastic?\xa0<strong>Yes</strong></li><li dir="ltr">provide clear explanations?\xa0<strong>Yes</strong></li><li dir="ltr">explain terminology?\xa0<strong>Yes</strong></li></ul>\n<p> <br /><strong>Ideas for improving your presentation:</strong><br />- Noting the times for how long it takes to go over stuff, as it always varies and one section may be slower than another<br /><br /><strong>Classroom Climate</strong><br /> <br />Did you:</p>\n<ul><li dir="ltr">address students of all genders equally?\xa0<strong>Yes</strong></li><li dir="ltr">address students of different ethnic groups equally?\xa0<strong>Yes</strong></li><li dir="ltr">address shy and forthcoming students equally?\xa0<strong>Yes</strong></li><li dir="ltr">feel like students were generally happy (e.g. no angry students)?\xa0<strong>Yes</strong></li><li dir="ltr">take the time to learn your students’ names?\xa0<strong>Yes</strong></li></ul>\n<p> <br /><strong>Ideas for improving the classroom climate:</strong><br />- More fun things at the beginning of class for those who come early, especially to engage the 1st section<br /><br /><strong>Student Participation</strong><br /> </p>\n<ul><li dir="ltr">Are students comfortable interacting with you?\xa0<strong>Yes</strong></li><li dir="ltr">Are the students comfortable interacting with each other?\xa0<strong>Yes</strong></li><li dir="ltr">How often were you talking versus the students?\xa0<strong>More student talking now but still mainly me</strong></li><li dir="ltr">Did you encourage the students to ask questions?\xa0<strong>Yes</strong></li><li dir="ltr">Are students comfortable asking “stupid” questions?\xa0<strong>Yes</strong></li><li dir="ltr">Were you happy with how long it took for students to answer your questions?\xa0<strong>Yes</strong></li><li dir="ltr">Did the students seem interested and engaged?\xa0<strong>Yes</strong></li></ul>\n<p> <br /><strong>Ideas for improving student participation:</strong><br />- Doing more of the group problem solving, but me stepping back/turning video off to let them brainstorm for a bit without me<br /><br /><strong>Focusing on Students</strong><br /> <br />Did you:</p>\n<ul><li dir="ltr">try to answer a student’s question with a question?\xa0<strong>Yes</strong></li><li dir="ltr">try to find out what the students knew before giving an explanation?\xa0<strong>Yes</strong></li><li dir="ltr">provide explanations to address both struggling and excelling students?\xa0<strong>Yes</strong></li><li dir="ltr">feel like students understood your explanations?\xa0<strong>Yes</strong></li><li dir="ltr">feel like students, in general, really understand with the material?\xa0<strong>Yes</strong></li></ul>\n<p> <br /><strong>Ideas for tailoring your teaching to the needs of your students:</strong><br />- Continuing to take their feedback, focusing on areas where it seems like they&#39;re struggling more--especially for the midterm</p>\n<p> <br /><strong>Link to previous self-reflection: @380</strong><br /> </p>'}]))