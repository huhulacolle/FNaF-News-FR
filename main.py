import os
import discord
import random
import requests
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

# news, ar, ffi, merch, test
channelId = [995357878850433075, 995358682260971520, 995358418426662967, 995358782064431144, 932742493999616080]

def deleteChannelTag(text):
    if "#" in text:
        return text.replace("#", "")
    return text

def translation(text):
    text = deleteChannelTag(text)
    auth_key = os.getenv('KEY')
    apiDeepl = requests.get("https://api-free.deepl.com/v2/translate?auth_key=" + auth_key + "&text=" + text +"&target_lang=FR")
    json = apiDeepl.json()
    return json['translations'][0]['text']

def TagChannel(id):
    match id:
        # news 
        case 995357878850433075:
            return "<@&935865359762878485>"
        # ar 
        case 995358682260971520:
            return "<@&935865535638433822>"
        # ffi 
        case 995358418426662967:
            return "<@&935865453807554561>"
        # merch 
        case 995358782064431144:
            return "<@&935865603103809596>"
        # test 
        case 932742493999616080:
            return "<@&935967437151686687>" 
        case _:
            return None

def channelIdAnnounce(id):
    match id:
        # news 
        case 995357878850433075:
            return 722163183409954848
        # ar 
        case 995358682260971520:
            return 849887600327262208
        # ffi 
        case 995358418426662967:
            return 746738363427717193
        # merch 
        case 995358782064431144:
            return 934836304955457536
        # test 
        case 932742493999616080:
            return 995370251321618464
        case _:
            return None

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    
    # News automatique
    if message.channel.id in channelId:
        news = translation(message.content)
        tag = TagChannel(message.channel.id)
        channel = client.get_channel(channelIdAnnounce(message.channel.id))
        await channel.send("🎶🌮  " + news + " " + tag + "  🌮🎶")

        if (message.attachments):
            for img in message.attachments:
                await channel.send(img)

    # MP
    MP = [
        "Je ne suis qu'un bot je ne peux pas te répondre désolé :(",
        "k",
        "Parler à un bot est une perte de temps",
        "je sais",
        "Oofy's",
        "Je suis une erreur",
        "Achete toi une vie",
        "Lilian est un furry",
        "J'ai envoyé ton adresse IP au Dark net",
        "William Afton n'était pas en tort",
        "Michael est Springtrap",
        "Shadow Lolbit est un Yes",
        "Let's try with another controlled shock",
        "Les NFTs c'est le cancer mais la NFT, y a pas mieux",
    ]

    if ("Direct Message" in str(message.channel)):
        await message.channel.send(random.choice(MP))


client.run(os.getenv('TOKEN'))