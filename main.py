import os
import discord
import requests
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

# news, ar, ffi, merch, test
channelId = [722163183409954848, 849887600327262208, 746738363427717193, 934836304955457536, 932742493999616080]

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
        case 722163183409954848:
            return "<@&935865359762878485>"
        # ar 
        case 849887600327262208:
            return "<@&935865535638433822>"
        # ffi 
        case 746738363427717193:
            return "<@&935865453807554561>"
        # merch 
        case 934836304955457536:
            return "<@&935865603103809596>"
        # test 
        case 932742493999616080:
            return "<@&935967437151686687>" 
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

        await message.delete()
        await message.channel.send("🎶🌮  " + news + " " + tag + "  🌮🎶")

        if (message.attachments):
            for img in message.attachments:
                await message.channel.send(img)


client.run(os.getenv('TOKEN'))