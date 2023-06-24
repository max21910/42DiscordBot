# created with ❤️ by max21910 in 🇫🇷

import discord
import asyncio
import os
import random
from datetime import datetime, timedelta, time


# Private token ⚠️ do not share in public 
TOKEN = 'YOUR_DISCORD_TOKEN'  
CHANNEL_ID = 'YOUR_CHANEL_ID'
# End Private token ⚠️ do not share in public 

# configuring client
intents = discord.Intents.default()
intents.presences = True
client = discord.Client(intents=intents)

# connection du bot et démarrage de la boucle
@client.event
async def on_ready():
    print(f'✅ Succefully Logged in as {client.user.name} in the serveur ')
    print(f'✅ Start activity')
    print(f'✅ Listen commands start')
    activity=discord.Activity(type=discord.ActivityType.listening, name="Ecole42 Pool musique :-)")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    await schedule_daily_alldays_command() # Démarrer la boucle pour envoyer le message quotidien à 12h

# event date :
events = [
    {
        'name': 'juillet',
        'start_date': datetime(2023, 7, 3, 9, 42, 0),
        'end_date': datetime(2023, 7, 28, 18, 0, 0)
    },
    {
        'name': 'août',
        'start_date': datetime(2023, 8, 7, 9, 42, 0),
        'end_date': datetime(2023, 9, 1, 18, 0, 0)
    },
    {
        'name': 'septembre',
        'start_date': datetime(2023, 9, 1, 9, 42, 0),
        'end_date': datetime(2023, 10, 1, 18, 0, 0)
    }
]
# bot command :
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$42alldays'):
        for event in events:
            await send_countdown_message(message.channel, event, event['name'])
    elif message.content.startswith('$42'):
        command = message.content[3:]
        for event in events:
            if command.startswith(event['name']):
                await send_countdown_message(message.channel, event, command)
                break
    elif message.content.startswith('$Help'):
        await send_help_message(message.channel)
    elif message.content.startswith('$Easteregg'):
        await send_easteregg_message(message.channel)
    elif message.content.startswith('$Version'):
        await send_vers_message(message.channel)
    elif message.content.startswith('$Github'):
        await send_opensource_message(message.channel)

# send message to the channel 
async def send_countdown_message(channel, event, command):
    current_date = datetime.now()
    start_date = event['start_date']
    end_date = event['end_date']
    time_left = start_date - current_date if current_date < start_date else end_date - current_date
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_message = (
        f"⏳ Il reste **{days} jours, **  \n  **{hours} heures, ** \n **{minutes} minutes, ** et **{seconds} secondes**\n"
        f"avant la piscine de {command} à l'école 42! 🏊‍♂️\n"
        "Penser à prendre votre bonnet !💧 ")
    if current_date.date() >= start_date.date() and current_date.date() <= end_date.date():
        event_date_message = f"✅ La piscine de {command} a commencé !"
        await channel.send(event_date_message)
    if current_date.date() >= end_date.date() and current_date.date() <= start_date.date():
        event_date_message = f"🔴 La piscine de {command} est terminée !"
        await channel.send(event_date_message)
    if current_date.date() < start_date.date():
        await channel.send(countdown_message)

# help message
async def send_help_message(channel):
    help_message = (
        "Guide d'utilisation du bot :\n"
        "- Pour obtenir le décompte de toute les piscines de l'ecole 42, utilisez la commande `$42alldays`.\n"
        "- Pour obtenir le décompte jusqu'à la piscine de l'ecole 42, utilisez la commande `$42XX`.\n"
        "- Remplacer XX par le mois de votre piscine juillet, août, septembre.\n"
        "- si la piscine n'a pas encore commencer le décompte s'affiche\n"
        "- si la piscine a commencer le bot affiche: ✅ La piscine XX a commencer !\n"
        "- si la piscine est terminer le bot affiche: 🔴 La piscine de XX est terminer !\n"
        "- Pour afficher la version, utilisez la commande `$Version`.\n"
        "- Pour afficher ce message d'aide, utilisez la commande `$Help`.\n"
        "- Pour afficher le code open source, utilisez la commande `$Github`.\n"
        "- created and wrote in python with ❤️ by max21910 in 🇫🇷 \n")
    await channel.send(help_message)

# Version message :
async def send_vers_message(channel):
    vers_message = (
        "- V1.8(beta)\n"
        "- find me on Github :🌍 https://github.com/max21910/42DiscordBot)\n")
    await channel.send(vers_message)
    
# Message pour l'easter egg 
async def send_easteregg_message(channel):
  image_urls = [
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/Xavier.jpg?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/EasterEgg.jpg?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/3.png?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/2.JPG?raw=true',
        'https://github.com/max21910/42DiscordBot/blob/main/src/EasterEgg/1.jpg?raw=true',]
  selected_image_url = random.choice(image_urls)
  await channel.send(selected_image_url)
    
# Message pour open source 
async def send_opensource_message(channel):
    opensource_message = (
        "hey i'm open source \n find me in : 🌍 https://github.com/max21910/42DiscordBot")
    await channel.send(opensource_message)
    
# func to execute message at 12h every days 
async def schedule_daily_alldays_command():
    while True:
        current_datetime = datetime.now()
        current_time = current_datetime.time()
        target_time = time(11, 59, 45) 
         # Combinaison de la date actuelle avec l'heure cible
        target_datetime = datetime.combine(current_datetime.date(), target_time)
        # Si l'heure actuelle est supérieure à l'heure cible, ajoutez un jour à la date cible
        if current_time > target_time:
            target_datetime += timedelta(days=1)
         # Calcul du délai jusqu'à l'heure cible
        delay = (target_datetime - current_datetime).total_seconds()
        
        # Attendre jusqu'à l'heure cible
        await asyncio.sleep(delay)
        
        # Exécuter la commande $42alldays
        for event in events:
            await send_countdown_message(client.get_channel('YOUR_CHANEL_ID'), event, event['name'])
# run bot with the provided ''TOKEN''
client.run(TOKEN)