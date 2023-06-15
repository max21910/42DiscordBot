import discord
import asyncio
from datetime import datetime, timedelta

# Private token ⚠️ do not share in public 
TOKEN = 'YOUR-DISCORD-TOKEN-HERE'   
CHANNEL_ID = 'YOUR_CHANEL_ID_HERE'
CHANNEL_ID_test ='TEST_CHANEL_ID_HERE'
# End Private token ⚠️ do not share in public 

intents = discord.Intents.default()
intents.message_content = False

# configuring client

client = discord.Client(intents=intents)


# connection du bot et démarrage de la boucle
@client.event
async def on_ready():
    
    print(f'✅ Logged in as {client.user.name} in the serveur Listen commands start')
    # Démarrer la boucle pour envoyer le message quotidien à 12h
    await send_daily_message()
    
# Event listen commands in channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$42julydays'):
        await julydate(message.channel)
    if message.content.startswith('$42augustdays'):
        await augustdate(message.channel)
    if message.content.startswith('$42septemberdays'):
        await septemberdate(message.channel)
    if message.content.startswith('$Help'):
        await send_help_message(message.channel)
    if message.content.startswith('$Easteregg'):
        await send_easteregg_message(message.channel)
    if message.content.startswith('$Version'):
        await send_vers_message(message.channel)
    if message.content.startswith('$Github'):
        await send_opensource_message(message.channel)
        
# Date et heure de l'événement de la piscine le 3 juillet 2023 a 8h00  et fin le 28 juillet à 18h00    
async def julydate(channel):
    event_date = datetime(2023, 7, 3, 8, 0, 0)  
    end_event_date = datetime(2023, 7, 28, 18, 0, 0)  
    current_date = datetime.now()
    time_left = event_date - current_date
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    july_countdown_message = (
        f"Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine d'août à l'école 42 !")
    if current_date.date() >= event_date.date() and current_date.date() <= end_event_date.date():
        event_date_message = "✅ La piscine de septembre a commencer !"
        await channel.send(event_date_message)
    if current_date.date() >= end_event_date.date() and current_date.date() <= event_date.date():
        event_date_message = "🔴 La piscine de septembre est terminer !"
        await channel.send(event_date_message)
    if current_date.date() < event_date.date():
        await channel.send(july_countdown_message)
    
  # Date et heure de l'événement de la piscine le 7 août 2023 a 8h00  et fin le 1er septembre à 18h00 
async def augustdate(channel):
    event_date = datetime(2023, 8, 7, 8, 0, 0)
    end_event_date = datetime(2023, 9, 1, 18, 0, 0)
    current_date = datetime.now()
    time_left = event_date - current_date
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    august_countdown_message = (
        f"Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine d'août à l'école 42 !")
    if current_date.date() >= event_date.date() and current_date.date() <= end_event_date.date():
        event_date_message = "✅ La piscine de septembre a commencer !"
        await channel.send(event_date_message)
    if current_date.date() >= end_event_date.date() and current_date.date() <= event_date.date():
        event_date_message = "🔴 La piscine de septembre est terminer !"
        await channel.send(event_date_message)
    if current_date.date() < event_date.date():
        await channel.send(august_countdown_message)
    
   
# Date et heure de l'événement de la piscine le 11 septembre 2023 a 8h00  et fin le 1er octobre à 18h00    
async def septemberdate(channel):
    event_date = datetime(2023, 9, 1, 8, 0, 0)  
    end_event_date = datetime(2023, 10, 1, 18, 0, 0) 
    current_date = datetime.now()
    time_left = event_date - current_date
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    september_countdown_message = (
        f"Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine de septembre à l'école 42 !")
    if current_date.date() >= event_date.date() and current_date.date() <= end_event_date.date():
        event_date_message = "✅ La piscine de septembre a commencer !"
        await channel.send(event_date_message)
    if current_date.date() >= end_event_date.date() and current_date.date() <= event_date.date():
        event_date_message = "🔴 La piscine de septembre est terminer !"
        await channel.send(event_date_message)
    if current_date.date() < event_date.date():
        await channel.send(september_countdown_message)
    
# Message pour l'aide
async def send_help_message(channel):
    help_message = (
        "Guide d'utilisation du bot :\n"
        "- Pour obtenir le décompte jusqu'à la piscine de l'ecole 42, utilisez la commande `$42XXdays`.\n"
        "- Remplacer XX par le mois de votre piscine july, august, september.\n"
        "- si la piscine n'a pas encore commencer le décompte s'affiche\n"
        "- si la piscine a commencer le bot affiche: ✅ La piscine XX a commencer !\n"
        "- si la piscine est terminer le bot affiche: 🔴 La piscine de septembre est terminer !\n"
        "- Pour afficher la version, utilisez la commande `$Version`.\n"
        "- Pour afficher ce message d'aide, utilisez la commande `$Help`.\n"
        "- Pour afficher le code, utilisez la commande `$Github`.\n"
        "- created with ❤️ by max21910 in 🇫🇷 \n"
    )
    await channel.send(help_message)

    
    
# Message pour la version
async def send_vers_message(channel):
    vers_message = (
        "- V1.4 (beta)\n"
        "- find me on Github :🌍 https://github.com/max21910/42DiscordBot)\n"
        "- created with ❤️ by max21910 in 🇫🇷 \n")
    await channel.send(vers_message)
    
    # Message pour l'easter egg 
async def send_easteregg_message(channel):
    help_message = (
        "EasterEgg")# need more work here  
    await channel.send(help_message)
   
# Message pour open source 
async def send_opensource_message(channel):
    opensource_message = (
        "hey i'm open source find me in : 🌍 https://github.com/max21910/42DiscordBot")
    await channel.send(opensource_message)

# func to execute message at a precise date 

async def execute_julydate():
    channel = client.get_channel(YOUR_CHANEL_ID_HERE) 
    await julydate(channel)

async def execute_augustdate():
    channel = client.get_channel(YOUR_CHANEL_ID_HERE)  
    await augustdate(channel)  
    
async def execute_septemberdate():
    channel = client.get_channel(YOUR_CHANEL_ID_HERE)  
    await septemberdate(channel)  
    


# send a message every day at 12 am of all pool dates times remaining add 15 sec for calculate and display message
async def send_daily_message():
    while True:
        now = datetime.now()
        target_time = now.replace(hour=11, minute=59, second=40)
        if now > target_time:
            target_time += timedelta(days=1)
        time_to_wait = (target_time - now).total_seconds()
        await asyncio.sleep(time_to_wait)
        channel = client.get_channel(CHANNEL_ID) 
        channeltest = client.get_channel(CHANNEL_ID_test)
        await asyncio.sleep(time_to_wait)
# Wait until the bot is ready
        await client.wait_until_ready() 
# execute func to send message
        await execute_julydate()
        await execute_augustdate()
        await execute_septemberdate()
# run bot 
client.run(TOKEN)