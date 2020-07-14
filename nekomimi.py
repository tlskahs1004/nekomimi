import discord
import os
import random

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("뿅뿅❤/Made by 시나몬")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!네코'):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed2 = discord.Embed(
            colour=discord.Colour.green()
        )
        embed3 = discord.Embed(
            colour=discord.Colour.green()
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1, 3)
        print('?번째사진 : ' + str(randomnumber))
        print('기호 : ' + str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho == 1:
            urlbase1 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            await message.channel.send(embed=embed3)
        else:
            urlbase_1 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await message.channel.send(embed=embed)
            await message.channel.send(embed=embed2)
            await message.channel.send(embed=embed3)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
