# 42DiscordBot
!!!!!This project is no longer  maintained. !!!!!!
## Hi 👋, I'm a Discord Bot

![Profile views](https://komarev.com/ghpvc/?username=max21910&label=Profile%20views&color=0e75b6&style=flat)

![Chat Image](https://github.com/max21910/42DiscordBot/blob/main/src/images/chat.png?raw=true)
![Profile Image](https://github.com/max21910/42DiscordBot/blob/main/src/images/profile.png?raw=true)

## Discord Bot for 42 School Piscines

This Discord bot was created to display the countdown for 42 School piscines. It also provides information about ongoing piscines and upcoming ones.

### Installation

#### On a Discord Server

[Click here to invite the bot to your server](https://discord.com/api/oauth2/authorize?client_id=1118602481434361886&permissions=8&scope=bot)

**Note:**
You won't be able to modify the bot if you invite it to the server.

#### On a Linux Server

To install and run this bot on a Linux server, follow these steps:

1. Make sure you have Python 3.8 or a later version installed on your Linux server.
2. Clone this GitHub repository to your server using the following command:

   ```
   git clone https://github.com/max21910/42DiscordBot.git
Navigate to the bot directory:


   ```
cd 42DiscordBot
   ```
Install the dependencies by running the following command:
   ```
pip install -r requirements.txt
   ```
Obtain a token for your Discord bot by following the instructions in the official Discord documentation: Creating a Bot Account.

Replace the value of TOKEN in the bot.py file with your own token.

Configuring the Bot on the Discord Developer Portal
Go to the Discord Developer Portal and log in with your Discord account.
Click on "New Application" to create a new application.
Give your application a name (e.g., "42DiscordBot") and click "Create."
In the left menu, select "Bot."
Click on "Add Bot" to add a bot to your application.
Under the "Token" section, click "Copy" to copy the bot token.
Replace the value of TOKEN in the bot.py file with the token you copied.
Usage
Once the bot is installed and configured, you can run it using the following command:

   ```
python3 42DiscordBot.py
   ```
Linux Server
If the installation is on a Linux server, run the command:
   ```
screen python3 path/to/file
   ```
Example:
   ```
screen python3 path/file/42DiscordBot.py
   ```
The bot will connect to your Discord server and be ready to receive commands.

Available Commands
$42alldays: Displays the countdown for all 42 School piscines.
$42july: Displays the countdown until the July piscine.
$42august: Displays the countdown until the August piscine.
$42september: Displays the countdown until the September piscine.
$Help: Displays a help message with available commands.
$Easteregg: Displays a surprise image.
$Version: Displays the bot version.
$Github: Displays the link to the bot's source code.
If the piscine has not started, the bot displays: Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes avant la piscine de septembre à l'école 42!
If the piscine has started, the bot displays: ✅ La piscine de XX a commencé!
If the piscine is finished, the bot displays: 🔴 La piscine de XX est terminée!
XX corresponds to the month of the piscine.
Contributors
Created by max21910
Note
Feel free to contribute to the project by submitting pull requests or reporting issues. Any contribution is welcome!

⚠️ Note:
Every day at 12 PM, the bot automatically sends a message in the specified channel ID.

Connect with me:
Twitter
Instagram
Medium
YouTube
