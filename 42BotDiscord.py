import discord
import asyncio
from datetime import datetime, timedelta

# Private token ⚠️ do not share in public 
TOKEN = 'TOKEN'  
CHANNEL_ID = 'CHANNEL_ID'
intents = discord.Intents.default()
intents.message_content = True


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# connection du bot et démarrage de la boucle
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    # Démarrer la boucle pour envoyer le message quotidien à 9h
    await send_daily_message()
    print('start daily message')

# Event in channel
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

        
    if message.content.startswith('$help'):
        await send_help_message(message.channel)

        
    if message.content.startswith('$easteregg'):
        await send_easteregg_message(message.channel)
    
        
    if message.content.startswith('$version'):
        await send_vers_message(message.channel)
      
       
        

    
async def julydate(channel):
    event_date = datetime(2023, 7, 3, 8, 0, 0)  # Date et heure de l'événement de la piscine le 3 juillet 2023
    current_date = datetime.now()
    time_left = event_date - current_date

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    july_countdown_message = (
        f"Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine de juillet à l'école 42 !"
    )
    await channel.send(july_countdown_message)
  
    
    
async def augustdate(channel):
    event_date = datetime(2023, 8, 7, 8, 0, 0)  # Date et heure de l'événement de la piscine le 7 august 2023
    current_date = datetime.now()
    time_left = event_date - current_date

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
# Message pour le temp avant le debut de la piscine de septembre 
    august_countdown_message = (
        f"Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine de aout à l'école 42 !"
    )
    await channel.send(august_countdown_message)
   
async def septemberdate(channel):
    event_date = datetime(2023, 9, 11, 8, 0, 0)  # Date et heure de l'événement de la piscine le 11 septembre 2023
    current_date = datetime.now()
    time_left = event_date - current_date

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
# Message pour le temp avant le debut de la piscine de septembre 
    september_countdown_message = (
        f"Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine de septembre à l'école 42 !"
    )
    await channel.send(september_countdown_message)

# Message pour l'aide
async def send_help_message(channel):
    help_message = (
        "Guide d'utilisation du bot :\n"
        "- Pour obtenir le décompte jusqu'à la piscine de l'ecole 42, utilisez la commande `$42XXdays`.\n"
        "- Remplacer XX par le mois de votre piscine july, august, september.\n"
        "- Pour afficher la version, utilisez la commande `$version`.\n"
        "- Pour afficher ce message d'aide, utilisez la commande `$help`.\n"
        "- created with ❤️ by max21910 in 🇫🇷 \n"
    )
    await channel.send(help_message)
    print('send help message')
    
    
# Message pour la version
async def send_vers_message(channel):
    vers_message = (
        "- V1.3 (beta)\n"
        "- created with ❤️ by max21910 in 🇫🇷 \n"
    )
    await channel.send(vers_message)
    
# Message pour l'easter egg 
async def send_easteregg_message(channel):
    help_message = (
        "EasterEgg"
       
    )
    await channel.send(help_message)
   
    print('Easter egg')

async def execute_julydate():
    channel = client.get_channel(CHANNEL_ID) 
    await julydate(channel)

async def execute_augustdate():
    channel = client.get_channel(CHANNEL_ID)  
    await augustdate(channel)  
    
async def execute_septemberdate():
    channel = client.get_channel(CHANNEL_ID)  
    await septemberdate(channel)  
    




# send a message every day at 12 am of all pool dates times remaining 
async def send_daily_message():
    while True:
        now = datetime.now()
        target_time = now.replace(hour=12, minute=0, second=0)

        if now > target_time:
            target_time += timedelta(days=1)

        time_to_wait = (target_time - now).total_seconds()
        await asyncio.sleep(time_to_wait)

        channel = client.get_channel(CHANNEL_ID) 
        channeltest = client.get_channel(CHANNEL_ID_test)
        await asyncio.sleep(time_to_wait)
        await client.wait_until_ready()  # Wait until the bot is ready
        await execute_julydate()
        await execute_augustdate()
        await execute_septemberdate()
        

client.run(TOKEN)