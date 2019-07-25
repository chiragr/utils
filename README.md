# utils

Small utilities that simplify life!

## mailer/mailer.js

Built to be used with NodeJS, mailer.js sends personalized emails to a group of recipients.

Emails have a customized message as well as a common message.

Great utility for sending farewell/keep_in_touch emails while resigning from a job! :-)

Steps to execute:
- Install node.js (http://nodejs.org/)
- Copy this file to a directory of your choice E.g.: ~/mailer.js
- Update sections that have comments starting with "Setup"
- Execute: node mailer.js
  
## food/food.py

"food.py" tells you what breakfast you should cook tomorrow morning. It randomly selects a breakfast item from the list of breakfast items provided in "food.json" and prints the name on screen. Once selected, the item will not repeat untill you have eaten all the items listed!

Wrote this after I got tired of replying to my wife's perpetual question, "What should we have for breakfast tomorrow?"

Steps to execute:
- Install Python
- Copy food.py and food.json in a directory of your choice
- Check the list of breakfast items in food.json and add/remove items based on your liking
- Execute: python food.py
- Cook the breakitem listed next morning
- Stay healthy!

## airtel/data-bal.py

"data-bal.py" prints/mails you your balance data and days for the current billing cycle. It is a good idea to add this script as a cron job.

NOTE 1: This script is only for the Indian Airtel customers.
NOTE 2: Currently it only prints the results. Mailing functionality can be added by the users.

Steps to execute:
- Install Python
- Copy data-bal.py in a directory of your choice
- Execute: data-bal.py

## scrabble/scrabblescore.py

While we love to play Scrabble, it is a pain to keep track of the score. So I created a Scrabble Score keeper. It takes care of blanks, double/triple letters, double/triple words and bonus points.

