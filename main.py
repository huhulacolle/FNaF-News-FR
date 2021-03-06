import os
import discord
import random
import requests
from dotenv import load_dotenv
from munch import DefaultMunch
load_dotenv()

client = discord.Client()

MP = "Si vous savez créer et maintenir un bot Discord, préviens le staff ! le développeur principal de ce bot a quitté ce serveur.\n"
MP += "Si tu veux voir le code source du bot, le voici : <https://github.com/huhulacolle/FNaF-News-FR/blob/main/main.py>"

# news, ar, ffi, merch, test
channelId = [995357878850433075, 995358682260971520, 995358418426662967, 995358782064431144, 932742493999616080]

def deleteChannelTag(text):
    if "#" in text:
        return text.replace("#", "")
    return text

def translation(text):
    text = deleteChannelTag(text)
    auth_key = os.getenv('KEY')
    api = requests.get(f"https://api-free.deepl.com/v2/translate?auth_key={auth_key}&text={text}&target_lang=FR")
    json = DefaultMunch.fromDict(api.json())
    return json.translations[0].text

def getInfo(id):
    match id:
        # news 
        case 995357878850433075:
            return {
                "tag": "<@&935865359762878485>",
                "id": 722163183409954848
            }
        # ar 
        case 995358682260971520:
           return {
                "tag": "<@&935865535638433822>",
                "id": 849887600327262208
            }
        # ffi 
        case 995358418426662967:
           return {
                "tag": "<@&935865453807554561>",
                "id": 746738363427717193
            }
        # merch 
        case 995358782064431144:
           return {
                "tag": "<@&935865603103809596>",
                "id": 934836304955457536
            }
        # test 
        case 932742493999616080:
           return {
                "tag": "<@&935967437151686687>",
                "id": 995370251321618464
            }
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
        info = DefaultMunch.fromDict(getInfo(message.channel.id))
        channel = client.get_channel(info.id)

        img = ""

        if(message.attachments):
            img += "\n"
            for m in message.attachments:
                img += f"{str(m)}\n"

        await channel.send(f"🎶🌮  {news} {info.tag}  🌮🎶{img}")

        if (bool(random.getrandbits(1))):
            await channel.send(MP)

    # MP
    # MP = [
    #     "Je ne suis qu'un bot je ne peux pas te répondre désolé :(",
    #     "k",
    #     "Parler à un bot est une perte de temps",
    #     "je sais",
    #     "Oofy's",
    #     "Je suis une erreur",
    #     "Achete toi une vie",
    #     "Lilian est un furry",
    #     "J'ai envoyé ton adresse IP au Dark net",
    #     "William Afton n'était pas en tort",
    #     "Michael est Springtrap",
    #     "Shadow Lolbit est un Yes",
    #     "Let's try with another controlled shock",
    #     "Les NFTs c'est le cancer mais la NFT, y a pas mieux",
    # ]

    if ("Direct Message" in str(message.channel)):
        # await message.channel.send(random.choice(MP))
        await message.channel.send(MP)


client.run(os.getenv('TOKEN'))