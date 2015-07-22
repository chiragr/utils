utils
=====

Small utilities that simplify life!

1) mailer/mailer.js

Built to be used with NodeJS, mailer.js sends personalized emails to a group of recipients.

Emails have a customized message as well as a common message.

Great utility for sending farewell/keep_in_touch emails while resigning from a job! :-)

Steps to execute:
  1. Install node.js (http://nodejs.org/)
  2. Copy this file to a directory of your choice E.g.: ~/mailer.js
  3. Update sections that have comments starting with "Setup"
  4. Execute: node mailer.js
  
2) food/food.py

"food.py" tells you what breakfast you should cook tomorrow morning. It randomly selects a breakfast item from the list of breakfast items provided in "food.json" and prints the name on screen. Once selected, the item will not repeat untill you have eaten all the items listed!

Wrote this after I got tired of replying to my wife's perpetual question, "What should we have for breakfast tomorrow?"

Steps to execute:
  1. Install Python
  2. Copy food.py and food.json in a directory of your choice
  3. Check the list of breakfast items in food.json and add/remove items based on your liking
  3. Execute: python food.py
  4. Cook the breakitem listed next morning
  5. Stay healthy!

3) airtel/data-bal.py

"data-bal.py" prints/mails you your balance data and days for the current billing cycle. It is a good idea to add this script as a cron job.

NOTE 1: This script is only for the Indian Airtel customers.
NOTE 2: Currently it only prints the results. Mailing functionality can be added by the users.

Steps to execute:
  1. Install Python
  2. Copy data-bal.py in a directory of your choice
  3. Execute: data-bal.py
