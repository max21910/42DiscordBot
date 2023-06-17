# 42DiscordBot
<h1 align="center">Hi 👋, I'm a Discord Bot</h1>


<p align="left"> <img src="https://komarev.com/ghpvc/?username=max21910&label=Profile%20views&color=0e75b6&style=flat" alt="max21910" /> </p>


# Bot Discord pour les piscines de l'école 42

Ce bot Discord a été créé pour afficher le décompte des piscines de l'école 42. Il fournit également des informations sur les piscines en cours, les piscines à venir et les commandes disponibles.

## Installation

### Sur un serveur Linux

Pour installer et exécuter ce bot sur un serveur Linux, suivez les étapes suivantes :

1. Assurez-vous d'avoir Python 3.8 ou une version ultérieure installée sur votre serveur Linux.
2. Clonez ce dépôt GitHub sur votre serveur en utilisant la commande suivante :

   ```shell
   git clone https://github.com/max21910/42DiscordBot.git
   ```

3. Accédez au répertoire du bot :

   ```shell
   cd 42DiscordBot
   ```

4. Installez les dépendances en exécutant la commande suivante :

   ```shell
   pip install -r requirements.txt
   ```

5. Obtenez un token pour votre bot Discord en suivant les instructions de la documentation officielle de Discord : [Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html).
6. Remplacez la valeur du `TOKEN` dans le fichier `bot.py` par votre propre token.

### Configuration du bot sur le portail développeur de Discord

1. Accédez au [portail développeur de Discord](https://discord.com/developers/applications) et connectez-vous avec votre compte Discord.
2. Cliquez sur "New Application" pour créer une nouvelle application.
3. Donnez un nom à votre application (par exemple, "42DiscordBot") et cliquez sur "Create".
4. Dans le menu de gauche, sélectionnez "Bot".
5. Cliquez sur "Add Bot" pour ajouter un bot à votre application.
6. Sous la section "Token", cliquez sur "Copy" pour copier le token du bot.
7. Remplacez la valeur du `TOKEN` dans le fichier `bot.py` par le token que vous avez copié.

## Utilisation

Une fois le bot installé et configuré, vous pouvez l'exécuter en utilisant la commande suivante :

```shell
python 42DiscordBot.py
```

Le bot se connectera à votre serveur Discord et sera prêt à recevoir des commandes.

### Commandes disponibles

- `$42alldays` : Affiche le décompte de toutes les piscines de l'école 42.
- `$42julydays` : Affiche le décompte jusqu'à la piscine de juillet.
- `$42augustdays` : Affiche le décompte jusqu'à la piscine d'août.
- `$42septemberdays` : Affiche le décompte jusqu'à la piscine de septembre.
- `$Help` : Affiche un message d'aide avec les commandes disponibles.
- `$Easteregg` : Affiche une image surprise.
- `$Version` : Affiche la version du bot.
- `$Github` : Affiche le lien vers le code source du bot.
- If the pool did not start the bot displays: `Il reste {days} jours, {hours} heures, {minutes} minutes et {seconds} secondes "
        "avant la piscine de septembre à l'école 42 ! `  
-If the pool has started the bot displays: `✅ La piscine de XX a commencer ! `    
Iif the pool is finished the bot displays: `🔴 La piscine de XX est terminer ! `    
XX correspond to the month of the pool 

## Contributeurs

- Created by [max21910](https://github.com/max21910)

## Remarque

 N'hésitez pas à contribuer au projet en soumettant des pull requests ou en signalant des problèmes. Toute contribution est la bienvenue !



Assurez-vous de remplacer la valeur du token dans le fichier `bot.py` par votre propre token Discord pour que le bot fonctionne correctement.
## ⚠️ Note :
every 12 pm the bot automaticly send message in the specify chanel id 
<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/max21160" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="max21160" height="30" width="40" /></a>
<a href="https://instagram.com/maxime_dpj" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="maxime_dpj" height="30" width="40" /></a>
<a href="https://medium.com/max21160" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="max21160" height="30" width="40" /></a>
<a href="https://www.youtube.com/c/max_studio" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="max_studio" height="30" width="40" /></a>
</p>
