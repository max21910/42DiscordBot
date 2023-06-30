# created with ❤️ by max21910 in 🇫🇷
#this program is written in python
import discord
import asyncio
import random
from datetime import datetime, timedelta, time
#--------->  Private token ⚠️ do not share in public 
DISCORD_TOKEN = 'DISCORD_TOKEN'  
CHANNEL_ID = 'CHANNEL_ID' #---------> this is the channel where the bot send message 
#---------> configuring client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
my_Activity_Status = "6 x 7 = 42" #---------> discord Status 
my_Status = discord.Status.online
#---------> connection du bot et démarrage de la boucle
@client.event
async def on_ready():
    print(f'✅ Succefully Logged in as {client.user.name} in the serveur ')
    print(f'✅ Succefully launch discord activity')
    print(f'✅ Listen commands start')
    activity=discord.Activity(type=discord.ActivityType.listening, name=my_Activity_Status)
    await client.change_presence(status=my_Status, activity=activity)  # online status 
    await all_date_reminders() # Démarrer la boucle pour envoyer le message quotidien à 12h
#---------> event date :
events = [
    {
        'name': 'juillet',
        'start_Date': datetime(2023, 7, 3, 9, 42, 0),
        'end_Date': datetime(2023, 7, 28, 18, 0, 0),
        'id_Check_Date': datetime(2023, 6, 28, 15, 0, 0),
        'id_Check_End_Date': datetime(2023, 7, 2, 15, 0, 0)
    },
    {
        'name': 'août',
        'start_Date': datetime(2023, 8, 7, 9, 42, 0),
        'end_Date': datetime(2023, 9, 1, 18, 0, 0),
        'id_Check_Date': datetime(2023, 8, 2, 15, 0, 0),
        'id_Check_End_Date': datetime(2023, 8, 3, 15, 0, 0)
    },
    {
        'name': 'septembre',
        'start_Date': datetime(2023, 9, 1, 9, 42, 0),
        'end_Date': datetime(2023, 10, 1, 18, 0, 0),
        'id_Check_Date': datetime(2023, 9, 1, 15, 0, 0),
        'id_Check_End_Date': datetime(2023, 9, 3, 15, 0, 0)
    }
]
#---------> bot command :
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$42alldays'):
        for event in events:
            await send_countdown_Message(message.channel, event, event['name'])
    elif message.content.startswith('$42'):
        command = message.content[3:]
        for event in events:
            if command.startswith(event['name']):
                await send_countdown_Message(message.channel, event, command)
                break
    elif message.content.startswith('$Help'):
        await send_help_message(message.channel)
    elif message.content.startswith('$Easteregg'):
        await send_easteregg_message(message.channel)
    elif message.content.startswith('$Version'):
        await send_vers_message(message.channel)
    elif message.content.startswith('$Github'):
        await send_opensource_message(message.channel)
#---------> send message to the channel 
async def send_countdown_Message(channel, event, command):
    current_Date = datetime.now()
    start_Date = event['start_Date']
    end_Date = event['end_Date']
    id_Check_Date = event['id_Check_Date']
    id_Check_End_Date = event['id_Check_End_Date']
    time_Left = start_Date - current_Date if current_Date < start_Date else end_Date - current_Date
    days = time_Left.days
    hours, remainder = divmod(time_Left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_Message = (
        f"⏳ Il reste **{days} jours, **  \n  **{hours} heures, ** \n **{minutes} minutes, ** et **{seconds} secondes**\n"
        f"avant la piscine de {command} à l'école 42! 🏊‍♂️\n"
        "Pensez à prendre votre bonnet !💧 ")
    if current_Date.date() >= start_Date.date() and current_Date.date() <= end_Date.date():
        event_Date_Message = f"✅ La piscine de {command} a commencé !"
        await channel.send(event_Date_Message)
    if current_Date.date() >= end_Date.date() and current_Date.date() <= D.date():
        event_Date_Message = f"🔴 La piscine de {command} est terminée !"
        await channel.send(event_Date_Message)
    if current_Date.date() >= id_Check_Date.date() and current_Date.date() <= id_Check_End_Date.date():
        id_Check_Message = f"⚠️ N'oubliez pas de vérifier votre identité pour la piscine de {command} à l'école 42 !"
        await channel.send(id_Check_Message)
    if current_Date.date() < id_Check_Date.date() or current_Date.date() > id_Check_End_Date.date():
        id_check_End_Message = f"🔴 La vérification de  votre identité pour la piscine de {command} n'a pas encore commencé ou est terminée à l'école 42 !"
        await channel.send(id_check_End_Message)
    if current_Date.date() < start_Date.date():
        await channel.send(countdown_Message)
#---------> help message
async def send_help_message(channel):
    help_Message = (
        "Guide d'utilisation du bot :\n"
        "- Pour obtenir le décompte de toute les piscines de l'ecole 42, utilisez la commande `$42alldays`.\n"
        "- Pour obtenir le décompte jusqu'à la piscine de l'ecole 42, utilisez la commande `$42XX`.\n"
        "- Remplacer XX par le mois de votre piscine juillet, août, septembre.\n"
        "- si la piscine n'a pas encore commencer le décompte s'affiche\n"
        "- si la piscine a commencer le bot affiche: ✅ La piscine XX a commencer !\n"
        "- si la piscine est terminer le bot affiche: 🔴 La piscine de XX est terminer !\n"
        "- Pour afficher la version, utilisez la commande `$Version`.\n"
        "- Pour afficher ce message d'aide, utilisez la commande `$Help`.\n"
        "- Pour afficher le code, utilisez la commande `$Github`.\n"
        "- created with ❤️ by max21910 in 🇫🇷 \n"
    )
    await channel.send(help_Message)
#---------> Message pour la version
async def send_vers_message(channel):
    vers_Message = (
        "- V1.8(beta)\n"
        "- find me on Github :🌍 https://github.com/max21910/42DiscordBot)\n"
        "- created with ❤️ by max21910 in 🇫🇷 \n")
    await channel.send(vers_Message)
async def send_online_message(channel):
    vers_message = (
        "⚠️ Hey , im back online 🌍 ✅ sorry for the delay\n")
    await channel.send(vers_message)
async def send_night_message():
    night_message = "⚠️ It's time to go to bed 🛌 ⚠️\nGood night 🌃"
    await client.get_channel(CHANNEL_ID).send(night_message)
#---------> Message pour l'easter egg 
async def send_easteregg_message(channel):
  image_urls = [
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/Xavier.jpg?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/EasterEgg.jpg?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/3.png?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/2.JPG?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/1.jpg?raw=true',]
  selected_image_url = random.choice(image_urls)
  await channel.send(selected_image_url)
#---------> Message pour open source 
async def send_opensource_message(channel):
    opensource_message = (
        "hey i'm open source \n find me in : 🌍 https://github.com/max21910/42DiscordBot")
    await channel.send(opensource_message)
#---------> func to execute message at a precise date 
async def all_date_reminders():
    while True:
        Current_sleep_time = datetime.now()
        current_time_sleep = Current_sleep_time.time()
        target_sleep = time(12, 00, 00)
        #---------> Combinaison de la date actuelle avec l'heure cible
        target_datetime = datetime.combine(Current_sleep_time.date(), target_sleep)
        #---------> Si l'heure actuelle est supérieure à l'heure cible, ajoutez un jour à la date cible
        if current_time_sleep > target_sleep:
            target_datetime += timedelta(days=1)
        #---------> Calcul du délai jusqu'à l'heure cible
        delay = (target_datetime - Current_sleep_time).total_seconds()
        #---------> Attendre jusqu'à l'heure cible
        await asyncio.sleep(delay)
         #---------> Exécuter la commande $42alldays
        for event in events:
            await send_countdown_Message(client.get_channel(CHANNEL_ID), event, event['name'])
#--------->run bot 
client.run(DISCORD_TOKEN)