# bot.py
import os
import random
from gettext import find

import discord
from dotenv import load_dotenv
import ssl

import time

import asyncio

import trials

ssl._create_default_https_context = ssl._create_unverified_context
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

vip = ['K2-18B#6152', 'Venus#1759', 'MEE6#4876', 'Nilsnils9#0522', 'viggope#6217']
betatesters = ['LarsTu#3458', 'K2-18B#6152', 'viggope#6217']
notif = 0
shift: int = 1
version = 1.0
update = 'Easter spring'
neversion = 'Admin update'
neversion2 = 'Trials of Venus'

VipError = 'You dont have that permission'
VipError: PermissionError
JukeError = 'Thats impossible'
JukeError: IndexError




myscore = 1271892
galascore = 1163064
sunscore = 951106


commands = ['freeze', 'flash', 'luck?', 'show memes', 'meme', 'throw dice',
            'throw multi dice', 'throw infinity dice', 'throw mega dice',
            'throw anti dice', 'relax', '8', 'joker', 'heart', 'diamond',
            'spader', 'clover', 'show commands', 'tetris', 'connect',
            'scratch', 'self destruct', 'edit test', 'stonks', 'air',
            '19 dollars', 'citat', 'Q', 'e', 'play game', 'buy pack',
            'buy spacepack', 'buy characterpack', 'mega Q',
            'status', 'my solar system', 'leaderboard', 'price wheel',
            'info', 'pack info']

loot = ['50 coins', '0 coins', '1 multi dice', '1 mega dice', '1 coin dice']

spaceloot = ['100 coins', '0 coins', '1 planet', '1 moon', '3 moons!', '75 coins', '0 coins', '0 coins',
             '0 coins', '0 coins', '0 coins', '100 coins', '100 coins', '75 coins', '75 coins', '75 coins',
             '75 coins', '1 moon', '3 moons!', '1 moon', '1 antidice', '1 coindice', '1 coindice'] # '1 space dice',

wheel = ['5 coins', '5 coins', '5 coins', '5 coins', '10 coins', '10 coins', '10 coins', '15 coins',
         '15 coins', '15 coins', '1 mega dice', '1 mega dice', '3 multidices', '3 multidices',
         '3 multidices', '**1 0 0 0 C O I N S!**', '20 coins', '50 coins', '20 coins', '50 coins', '3 coindices', '3 coindices', '3 coindices']

pack = ['3 Mega dices, 5 Multidices']

srare = ['Euanthe', 'Erinome', 'Polydeuces']
rare = ['Aitne', 'Sponde', 'Kallichore', 'Megaclite', 'Mundilfari', 'Arche', 'Helike']
#parts#


class Botten(discord.Client):

    shift = shift

    notif = notif
    alfa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    client = discord.Client()
    imonline = 0
    coins: int
    dicesthrown: int
    multidices: int
    megadices: int

    a = 0

    copy = 'Empty'

    news: list

    sender = ""

    beta = ""
    paste = copy

    def saveCoins(self):
        file = open("coins.txt", "w")
        file.write(str(self.coins))
        file.close()

    def readCoins(self):
        try:
            file = open("coins.txt", "r")
            self.coins = int(file.read())
            file.close()
        except:
            self.coins = 0

    def saveDices(self):
        file = open("dicesthrown.txt", "w")
        file.write(str(self.dicesthrown))
        file.close()

    def readDices(self):
        try:
            file = open("dicesthrown.txt", "r")
            self.dicesthrown = int(file.read())
            file.close()
        except:
            self.dicesthrown = 0

    def saveMultidice(self):
        file = open("multidices.txt", "w")
        file.write(str(self.multidices))
        file.close()

    def readMultidice(self):
        try:
            file = open("multidices.txt", "r")
            self.multidices = int(file.read())
            file.close()
        except:
            self.multidices = 0

    def saveMegadice(self):
        file = open("megadices.txt", "w")
        file.write(str(self.megadices))
        file.close()

    def readMegadice(self):
        try:
            file = open("megadices.txt", "r")
            self.megadices = int(file.read())
            file.close()
        except:
            self.megadices = 0

    def saveRank(self):
        file = open("rank.txt", "w")
        file.write(str(self.rank))
        file.close()

    def readRank(self):
        try:
            file = open("rank.txt", "r")
            self.rank = file.read()
            file.close()
        except:
            self.rank = 'Tellus'

    def savePlanets(self):
        file = open("planets.txt", "w")
        file.write(str(self.planets))
        file.close()

    def readPlanets(self):
        try:
            file = open("planets.txt", "r")
            self.planets = int(file.read())
            file.close()
        except:
            self.planets = 0

    def saveMoons(self):
        file = open("moons.txt", "w")
        file.write(str(self.moons))
        file.close()

    def readMoons(self):
        try:
            file = open("moons.txt", "r")
            self.moons = int(file.read())
            file.close()
        except:
            self.moons = 0

    def saveLvl(self):
        file = open("lvl.txt", "w")
        file.write(str(self.lvl))
        file.close()

    def readLvl(self):
        try:
            file = open("lvl.txt", "r")
            self.lvl = int(file.read())
            file.close()
        except:
            self.lvl = 0

    def saveAntidices(self):
        file = open("antidices.txt", "w")
        file.write(str(self.antidices))
        file.close()

    def readAntidices(self):
        try:
            file = open("antidices.txt", "r")
            self.antidices = int(file.read())
            file.close()
        except:
            self.antidices = 0

    def saveCoindices(self):
        file = open("coindices.txt", "w")
        file.write(str(self.coindices))
        file.close()

    def readCoindices(self):
        try:
            file = open("coindices.txt", "r")
            self.coindices = int(file.read())
            file.close()
        except:
            self.coindices = 0

    def saveCharacters(self):
        file = open("characters.txt", "w")
        file.write(str(self.characters[0:len(self.characters)]))
        file.close()
        file = open("srare.txt", "w")
        file.write(str(self.srare[0:len(self.srare)]))
        file.close()
        file = open("rare.txt", "w")
        file.write(str(self.rare[0:len(self.rare)]))
        file.close()

    def readCharacters(self):
        try:
            file = open("characters.txt", "r")
            self.characters[0:len(self.characters)] = int(file.read())
            file.close()
            file = open("srare.txt", "r")
            self.srare[0:len(self.srare)] = int(file.read())
            file.close()
            file = open("rare.txt", "r")
            self.rare[0:len(self.rare)] = int(file.read())
            file.close()
        except:
            self.characters = ['']
            self.srare = ['']
            self.rare = ['']

    def saveMailbox(self):
        file = open("news.txt", "w")
        file.write(str(self.news))
        file.close()

    def readMailbox(self):
        try:
            file = open("news.txt", "r")
            self.news = file.read()
            file.close()
        except:
            self.news = ['']

    def __init__(self):
        self.readCoins()
        self.readDices()
        self.readMultidice()
        self.readMegadice()
        self.readRank()
        self.readPlanets()
        self.readMoons()
        self.readLvl()
        self.readAntidices()
        self.readCoindices()
        self.readCharacters()
        self.readMailbox()
        super().__init__()

    def save(self):
        self.saveMultidice()
        self.saveMegadice()
        self.saveAntidices()
        self.saveRank()
        self.saveCoins()
        self.saveDices()
        self.saveLvl()
        self.saveMoons()
        self.savePlanets()
        self.saveCoindices()
        self.saveCharacters()
        self.saveMailbox()




    @client.event
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        # await message.channel.send('**Hellu**, Im finally online!\n')
        activity = discord.Game(name="Spacex", type=1)
        await bot.change_presence(status=discord.Status.idle, activity=activity)

    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'**Hi {member.name}**, welcome to this Discord server!'
        )

    async def on_guild_join(guild):
        general = find(lambda x: x.name == 'chat', guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send('Hello {}!'.format(guild.name))

    async def kick(ctx, member: discord.Member, *, reason=None):
        await client.kick(member)
        await ctx.send(f'User {member} has been kick')

    @client.event
    async def on_message(self, message):
        #await message.channel.send('Im going to be offline for a while')
        message.content = message.content.lower()
        if str(message.author) == str(client.user):
            return
        #self.coins = 25
        #self.saveCoins()
        #self.multidices= 1
        #self.megadices= 1



        # print("Bot is ready!")
        # print(message)

        if message.content.startswith('empty embed'):
            embedVar = discord.Embed(title="** **", description="** **", color=0x00ff00)
            embedVar.add_field(name="** **", value="** **", inline=False)
            embedVar.add_field(name="** **", value="** **", inline=False)
            await message.channel.send(embed=embedVar)
        score = self.moons * 1 + self.planets * 5
        def pack1():  # 200
            if self.coins >= 200:
                self.coins -= 200
                self.multidices += 5
                self.megadices += 3
                self.save()
                #message.channel.send('You got: 5 multi dices, 3 mega dices')
            #else:
               # message.channel.send('You dont have enough coins ('+self.coins+'/200)')

        def pack2():  # 400
            if self.coins >= 400:
                self.coins -= 400
                self.multidices += 10
                self.megadices += 5
                self.moons += 1
                self.save()
                #message.channel.send('You got: 10 multi dices, 5 mega dices, 1 moon')
            #else:
                #message.channel.send('You dont have enough coins ('+self.coins+'/400)')

        def pack3():  # 1500
            if self.coins >= 1500:
                self.coins -= 1500
                self.multidices += 25
                self.megadices += 10
                self.moons += 4
                self.planets += 1
                self.save()
                #message.channel.send('You got: 25 multi dices, 10 mega dices, 4 moons, 1 planet')
            #else:
                #message.channel.send('You dont have enough coins (' + self.coins + '/1500)')

        def pack4():  # 5000
            if self.coins >= 5000:
                self.coins -= 5000
                self.multidices += 50
                self.megadices += 25
                self.moons += 7
                self.planets += 2
                self.antidices += 1
                self.save()
               # message.channel.send('You got: 50 multi dices, 25 mega dices, 7 moons, 2 planets and 1 **Anti dice**')
            #else:
               # message.channel.send('You dont have enough coins ('+self.coins+'/5000)')

        def spacepack1():  # 1200
            if self.coins >= 1200:
                self.coins -= 1200
                self.moons += 5
                self.planets += 1
                self.coindices += 1
                self.save()

        def spacepack2():  # 1750
            if self.coins >= 1750:
                self.coins -= 1750
                self.moons += 7
                self.planets += 3
                self.antidices += 1
                self.coindices += 1
                self.save()

        def characterpack1():  # 1000
            if self.coins >= 1000:
                self.coins -= 1000
                ran = random.randint(1, 3)
                #print(ran)
                if ran == 1:
                    ran = srare
                else:
                    ran = rare
                got = random.choices(ran)
                #print(ran)
                #print(str(got[0]))
                self.characters.insert(1, got)
                if str(got[0]) in srare:
                    self.srare.insert(1, got)
                else:
                    self.rare.insert(1, got)
                self.save()
                #print(got)
                #await message.channel.send('You got ' + got + '!')

        # message.content = message.content.islower()
        #        bot.remove_command('help')  # Removes default help command

        if notif == 1:
            rander = random.randint(1, 200)
            # if rander == 1:
            #   await message.channel.send(
            #      '**Tip of the day:**\n Be friend with my creator\n ||viggope#6127||\n** **\n**if youre already:**\nBe friend with me!\n')

            if rander == 2:
                await message.channel.send(
                    '**Tip of the day:**\n Try this command!\n **' + random.choice(self.commands) + '**\n')

            if rander == 3:
                await message.channel.send(
                    '**Hi ** @everyone !\n Add this member! I mean, why not?\n' + str(message.author))

            if rander == 4:
                await message.channel.send(
                    '@everyone ** 💡 I got an idea!**\n 💵 You pay me 100$ every months, and I give you 1000$ every YEAR!\n *Deal?*')

            if rander == 5:
                await message.channel.send(
                    '**Am I right?**\n 1+1 = 11')

            if rander == 6:
                await message.channel.send(
                    '@everyone **Lets celebrate the flying pigs day!**\n🐽')

            if rander == 7:
                await message.channel.send(
                    '**Check this amazing game made of my creator!**\n'
                    'https://scratch.mit.edu/projects/487823170/')

            if rander == 8:
                await message.channel.send(
                    '**Bored?**\nTry this command and tooo many bots will spawn!\n||**create agario bot**||')

            if message.author == self.user:
                return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        scratch = [
            'https://scratch.mit.edu/projects/504980803/fullscreen/',
            'https://scratch.mit.edu/projects/424695861/fullscreen/',
            'https://scratch.mit.edu/projects/487823170/fullscreen/',
            'https://scratch.mit.edu/projects/491750081/fullscreen/',
            'https://scratch.mit.edu/projects/404468703/fullscreen/',
            'https://scratch.mit.edu/projects/454060301/fullscreen/',
            'https://scratch.mit.edu/projects/411743330/fullscreen/',
            'https://scratch.mit.edu/projects/374161087/fullscreen/',
            'https://scratch.mit.edu/projects/428222435/fullscreen/',
            'https://scratch.mit.edu/projects/364226698/fullscreen/',
            'https://scratch.mit.edu/projects/400711411/fullscreen/'
            ]


        memes = [
            'recoverymeme.png',
            'BUNS.png',
            'head.jpeg',
            'stonks.jpg',
            'Spookmine.png',
            'thomas.jpg',
            'Venus.jpg',
            'Giraff.jpg',
            'bedrock.png',
            'memememe.png',

        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

        if message.content == 'show commands':
            await message.channel.send(commands)

        if message.content == 'show id' or message.content == 'show nametag':
            response = message.author
            await message.channel.send(response)

        if message.content == 'luck?':
            ran = random.randint(1, 7)
            if ran == 1:
                await message.channel.send('actually, **yes**')
                ran = 0
            elif ran == 2 or ran == 3:
                await message.channel.send('**maybe**...')
                ran = 0
            else:
                await message.channel.send('**nope**')

        if message.content == 'throw dice':
            ran = random.randint(1, 6)
            await message.channel.send('🎲 **Dice thrown**\n It says: ' + str(ran))
            self.dicesthrown += 1
            self.saveDices()

        # if 'say' in message.content:
        #   await message.channel.send(message.content[4:len(message.content)])

        # print(message.author)
        # if message.content == 'Venus, turn off' and message.author == 'viggope#6217':
        # exit(on_message)
        # print(message.author.id)

        # if message.content == 'create password':

        if message.content == 'eatsnail':
            await message.channel.send('Snail eaten. **BURP!**')

        # if message.content == 'ring phone':
        # await message.channel.send('**📞 A phone is ringing!** \n Type 1 to answer\n Type 2 to ignore')
        # if message.content == '1':
        # await message.channel.send('**Hello?**')
        # time.sleep(3)
        #  await message.channel.send('Oops. The call ended because he died')

        if 'sweden' in message.content:
            await message.channel.send('Yay! Sweden! 🇸🇪🇸🇪🇸🇪❤️')

        if 'you sucks' in message.content:
            if not 'rasmus' in message.content:
                await message.channel.send('Baldie is angry 😠')
            else:
                await message.channel.send('Baldie agrees 😼')

        if 'stonks' in message.content:
            await message.channel.send(file=discord.File("stonks.jpg"))

        if 'bigbrain' in message.content:
            await message.channel.send(file=discord.File("head.jpeg"))

        if 'giraff' in message.content:
            await message.channel.send(file=discord.File("Giraff.jpg"))
            await message.channel.send(file=discord.File("images.jpg"))

        if 'spook' in message.content:
            await message.channel.send(file=discord.File("Spookmine.png"))

        #if 'venus' in message.content:
         #   await message.channel.send(file=discord.File("Venus.jpg"))

        if 'buns' in message.content:
            await message.channel.send(file=discord.File("buns.jpg"))
            await message.channel.send(file=discord.File("BUNS.png"))

        if message.content == 'meme':
            response = random.choice(memes)
            await message.channel.send(file=discord.File(str(response)))

        if message.content == 'show memes':
            response = memes
            num = 1
            for i in range(len(memes) - 1):
                await message.channel.send(file=discord.File(str(response[num])))
                num += 1

        if message.content[0:4] == 'copy':
            await message.channel.send(message.content[5:len(message.content)] + ' successfully copied!')
            self.copy = message.content[5:len(message.content)]

        if message.content == 'paste':
            await message.channel.send(str(self.copy))


        '''if message.content == 'party':

            for i in range(10):
                ran = random.randint(0, len(self.alfa) - 1)
                self.beta += (self.alfa[ran])
            await message.channel.send('Finally; 🎉🎊Party time!️\nType ||' + str(self.beta) + '|| to win')
            time.sleep(10)
            if message.content == str(self.beta):
                await message.channel.send(message.author, 'Won! Id: ||', message.author.id, '||')
                '''
        if message.content == 'test':
            mes = await message.channel.send("Type *666* fast!")
            time.sleep(5)
            if message.content == '666':
                await mes.edit(content="Nice! You won!")
            else:
                await mes.edit(content="Tooooooooooooooooo late")

        ### Mini commands ###

        if message.content == 'idk':
            await message.channel.send('¯\_(ツ)_/¯')

        if message.content == 'relax':
            await message.channel.send('😎')

        if message.content == 'your so smart':
            await message.channel.send('Finally, somebody is trusting me. 🧠')

        if 'pigbrain' in message.content:
            await message.channel.send('🐽🧠')

        if 'pigrain' in message.content:
            await message.channel.send('🐖🐖🐖🐖🐖🐖🐖🐖🐖🐖🐖🐖🐖🐖🐖🐷🌧')

        if 'big grain' in message.content:
            await message.channel.send('🌾')

        if 'pig grain' in message.content:
            await message.channel.send('🌾🐷')

        if 'big rain' in message.content:
            await message.channel.send('🌧')

        if 'grain rain' in message.content:
            await message.channel.send('🌾🌧')

        if 'rainbow' in message.content:
            await message.channel.send('🌈')

        if 'grainbow' in message.content:
            await message.channel.send('🏹🌾')

        if 'trig rain' in message.content:
            await message.channel.send('**WARNING** ')
            await message.channel.send(file=discord.File("thomas.jpg"))

        if 'ping pong' in message.content:
            await message.channel.send('🏓')

        if 'censured sushi' in message.content:
            await message.channel.send('🍙')

        if 'china town' in message.content:
            await message.channel.send('⛩')

        if 'spader' in message.content:
            await message.channel.send('♠️')

        if 'diamond' in message.content:
            await message.channel.send('♦️️')

        if 'clover' in message.content:
            await message.channel.send('♣️️')

        if 'heart' in message.content:
            await message.channel.send('♥️️')

        if 'joker' in message.content:
            await message.channel.send('️🃏')

        if 'uno stop card' in message.content:
            await message.channel.send('️⦸')

        if 'air' in message.content:
            await message.channel.send('     ️')

        if '19 dollars' in message.content:
            await message.channel.send('£$¥¢️')

        if message.content == 'e':
            await message.channel.send('recovery')

        if message.content == 'q':
            self.coins += 1
            self.saveCoins()
            await message.channel.send('Successfully gained 1 coin')

        if message.content == 'create agario bot':
            await message.channel.send('Bots created. It will now appear "AGAR BOT OVH" in agar.io')

        if message.content == 'friend meme':
            await message.channel.send(
                'GRAMMAR WITH ME!  \nTodays grammar:   One friendship, two **FRIENDSHIPS** \nGRAMMAR WITH ME!  ')

        if 'tetris' in message.content:
            await message.channel.send('▗▘▙▞▛▙▘▟▖▜')

        if 'connect' in message.content:
            await message.channel.send('***WARNING***    B a d   c o n n e c t i o n   📡')

        if 'self destruct' in message.content:
            counter = 3
            response = f'THIS MESSAGE WILL SELF DELETE IN 3'
            msger = await message.channel.send(response)
            for i in range(2):
                counter -= 1
                await msger.edit(content='THIS MESSAGE WILL SELF DELETE IN ' + str(counter) + ' ')
                time.sleep(1)
            await asyncio.sleep(1)
            await msger.delete()

        if 'scratch' in message.content:
            await message.channel.send('Here is a suggestion for a scratch game:\n'+random.choice(scratch))


        if str(message.author) == 'MEE6#4876':
            ran = random.randint(1, 5)
            if ran == 1:
                await message.channel.send('Wait a minute. . .\nIS THAT **MEE6**? Im a big fan of you!\n Can I get your signature please???')


        if message.content[0:4] == 'spam':
            for i in range(5):
                await message.channel.send(message.content[5:len(message.content)])

        if message.content == '8':
            await message.channel.send('🎱')

        if 'molang' in message.content:
            await message.channel.send('https://media.discordapp.net/attachments/723169651105988690/824723029610594324/unknown.png?width=510&height=765')

        if message.content[0:10] == 'ghost spam':
            for i in range(5):
                await message.channel.send(message.content[11:len(message.content)])
                msg = await message.channel.send(message.content[11:len(message.content)])
                await asyncio.sleep(0)
                await msg.delete()

        if message.content == 'edit test':
            counter = 1
            edi = await message.channel.send(str(counter))
            for counter in range(10):
                counter += 1
                await edi.edit(content=counter)
                time.sleep(1)

        if message.content == 'create password':
            for i in range(10):
                ran = random.randint(0, len(self.alfa) - 1)
                self.beta += (self.alfa[ran])
            passwordmes = await message.channel.send('Your new password is: ' + str(self.beta))
            time.sleep(5)
            await passwordmes.edit(content='**NOTHING HERE**')
            password = self.beta

        # Rule
        if message.content == 'print rule 1':
            await message.channel.send(
                '**Man får inte använda botar i #nyheter , #diskussion (om inte i nödfall), #idéer-och-förslag, #rapport eller #röstning**')
        if message.content == 'print rule 2':
            await message.channel.send('**Ingen spam om inte du heter Venus och är verifierad som bot**')

        if message.content == 'play game':
            Msg = await message.channel.send('Game starts in 3')
            time.sleep(1)
            await Msg.edit(content='Game starts in 2')
            time.sleep(1)
            await Msg.edit(content='Game starts in 1')
            time.sleep(1)
            await message.channel.send('https://www.youtube.com/watch?v=cvh0nX08nRw')
        ###
        # if str(message.author.id) == str('656595397472550933'):

        if message.content == 'reset coins' and message.author.id == int(656595397472550933):
            await message.channel.send('reseting score. . .')
            self.coins = 0
            self.saveCoins()
        elif message.content == 'reset coins' and not message.author.id == int(656595397472550933):
            await message.channel.send(
                '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')

        if message.content == 'throw multi dice':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                if self.multidices >= 1:
                    self.dicesthrown += 1
                    self.saveDices()
                    self.multidices -= 1
                    self.saveMultidice()
                    ran = random.randint(1, 25)
                    await message.channel.send('🎲 **Multi dice thrown**\n It says: ' + str(ran))
                elif not self.multidices >= 1:
                    await message.channel.send('You dont have enough **resources** to do that')
            elif message.content == 'throw multi dice':
                if not message.author.id == int(656595397472550933) or str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')
                    print(message.author.id)

        if message.content == 'throw mega dice':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                if self.megadices >= 1:
                    self.dicesthrown += 1
                    self.saveDices()
                    self.megadices -= 1
                    self.saveMegadice()
                    ran = random.randint(1, 250)
                    await message.channel.send('♻️ **MEGA dice thrown**\n It says: ' + str(ran))
                elif not self.megadices >= 1:
                    await message.channel.send('You dont have enough **resources** to do that')
            elif message.content == 'throw mega dice':
                if not message.author.id == int(656595397472550933) or str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')
                    print(message.author.id)

        if message.content == 'throw infinity dice':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                self.dicesthrown += 1
                self.saveDices()
                ran = random.randint(1, 10000)
                await message.channel.send('∞️ ***I N F I N I T Y* dice thrown**\n It says: ' + str(ran))
            elif message.content == 'throw infinity dice':
                if not message.author.id == int(656595397472550933) or not str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')
                    print(message.author.id)

        if message.content == 'throw anti dice':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                self.dicesthrown += 1
                self.saveDices()
                ran = random.randint(-100000000, 0)
                await message.channel.send('◼️**⤺A=N=T=I⤻ dice thrown**\n It says: ' + str(ran))
            elif message.content == 'throw anti dice':
                if not message.author.id == int(656595397472550933) or not str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')
                    print(message.author.id)

        if message.content == 'freeze':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                await message.channel.send('❄️ **Brr. Its cold. Isnt it?**')
            elif message.content == 'freeze':
                if not message.author.id == int(656595397472550933) or not str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')
                    print(message.author)

        if message.content == 'citat':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                await message.channel.send('ADA ÄR INTE VIGGOS SYSTER')
            elif message.content == 'citat':
                if not message.author.id == int(656595397472550933) or not str(message.author) in vip:
                    await message.channel.send(
                        '**Man**  \nThose sentences doesnt concern you\n **- - - - - - - - - - - -** \n')

        if message.content == 'flash':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                await message.channel.send('⚡️ **FLASH** ⚡️')
            elif message.content == 'flash':
                if not message.author.id == int(656595397472550933) or not str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')

        if message.content == 'message id' and message.author.id == int(656595397472550933):
            await message.channel.send(message.id)
            await message.channel.send(message)
        elif message.content == 'message id' and not message.author.id == int(656595397472550933):
            await message.channel.send(
                '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')

        if message.content == 'venus' and str(message.author.id) == int(656595397472550933):
            await message.channel.send('*Yes, my master*')
        elif message.content == 'venus' and not (message.author) == int(656595397472550933):
            await message.channel.send('**YOUR NOT MY MASTER!!!**')
            print('imposter alert')

        if message.content == 'throw coindice':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                if self.coindices >= 1:
                    self.dicesthrown += 1
                    self.saveDices()
                    self.coindices -= 1
                    self.saveCoindices()
                    ran = random.randint(10, 50)
                    await message.channel.send('💰🎲💰 **Coin dice thrown**\n It says: ' + str(ran) + ' coins')
                elif not self.coindices >= 1:
                    await message.channel.send('You dont have enough **resources** to do that')
            elif message.content == 'throw coindice':
                if not message.author.id == int(656595397472550933) or str(message.author) in vip:
                    await message.channel.send(
                        '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')
                    print(message.author.id)

        if message.content == 'mjöl' or message.content == 'grotesco':
            await message.channel.send('https://www.youtube.com/watch?v=AQIxZMUWUpU')

        if message.content == 'bestefar' or message.content == 'grotesco2':
            await message.channel.send('https: // www.youtube.com / watch?v = 4YFmCAdhdNQ')

        if message.content == 'head shot' or message.content == 'ryggskott':
            await message.channel.send('')

        if message.content == 'phone':
            mes = await message.channel.send("123 456 789")
            time.sleep(5)
            await mes.edit(content="SIKE\n **THATS THE WRONG NUMBER**")

        if message.content == 'toggle notifications' and message.author.id == int(656595397472550933):
            if self.notif == 1 and self.shift == 1:
                self.notif = 0
            elif self.notif == 0 and self.shift == 0:
                self.notif = 1
                self.shift = 1
            await message.channel.send('Notifications changed √️   (' + str(notif) + ')')
        elif message.content == 'toggle notifications' and not message.author.id == int(656595397472550933):
            await message.channel.send(
                '**Whoops!**  \nYou dont have that permission\n **- - - - - - - - - - - -** \n')

        if message.content[0:17] == 'set notifications' and message.author.id == int(656595397472550933):
            self.notif = message.content[18:19]
            if self.notif == 1:
                self.shift = 1
            else:
                self.shift = 0
            await message.channel.send('Notifications successfully changed to ' + self.notif)

        if message.content == 'mega q':
            if message.author.id == int(656595397472550933) or str(message.author) in vip:
                self.coins += 5
                self.saveCoins()
                await message.channel.send('Successfully gained 5 coins')
            elif message.content == 'mega q':
                if not message.author.id == int(656595397472550933) or not str(message.author) in vip:
                    await message.channel.send(
                        '**Wowsa**  \nThats a bunt of coins. I dont think you can controll it.\n **- - - - - - - - - '
                        '- - -** \n')

        ### Embeds ###
        if message.content == 'status':
            self.save
            if not str(message.author) in vip:
                embedVar = discord.Embed(title="**"+str(message.author)[0:len(str(message.author))-5]+"'s Status**", description='= = = = = =', color=0x00ff00)
            else:
                embedVar = discord.Embed(
                    title="**" + str(message.author)[0:len(str(message.author)) - 5] + "'s Status**",
                    description='*=* *=* *=* *=* *=* *=*', color=0x00ff00)
            embedVar.add_field(name="Id:", value=str(message.author.id), inline=False)
            embedVar.add_field(name="Tag:", value=str(message.author)[len(str(message.author))-5:len(str(message.author))], inline=False)
            embedVar.add_field(name="Dices thrown:", value=str(self.dicesthrown), inline=True)
            embedVar.add_field(name="Coins:", value=str(self.coins), inline=True)
            embedVar.add_field(name="Multi dices:", value=str(self.multidices), inline=False)
            embedVar.add_field(name="Mega dices:", value=str(self.megadices), inline=True)
            embedVar.add_field(name="Coindices:", value=str(self.coindices), inline=True)
            embedVar.add_field(name="Anti dices:", value=str(self.antidices), inline=False)
            embedVar.add_field(name="––––––––––––––––––––––––––––––––", value='** **', inline=False)
            if str(message.author) in betatesters:
                embedVar.add_field(name='Beta tester', value='Verified √')
            if str(message.author) in vip:
                embedVar.add_field(name='** V.I.P **', value='Verified √')
            if str(message.author.id).__contains__(str(trials.user_trials)):
                embedVar.add_field(name='**◊ Trials opened ◊**', value='Verified √ ***∑***')


            #print(self.multidices, self.megadices)

            await message.channel.send(embed=embedVar)

        if message.content == 'my solarsystem' or message.content == 'my solar system' or message.content == 'solarsystem':
            if self.planets >= 1 and self.moons >= 3:
                self.rank = 'Merkurius <2>'
                self.saveRank()
            if self.planets >= 3 and self.moons >= 10:
                self.rank = 'Ceres <3>'
                self.saveRank()
            if self.planets >= 10 and self.moons >= 20:
                self.rank = 'Neptunus <4>'
                self.saveRank()
            if self.planets >= 15 and self.moons >= 35:
                self.rank = 'Pluto <5>'
                self.saveRank()
            if self.planets >= 24 and self.moons >= 50:
                self.rank = '*Uranus <6>*'
                self.saveRank()
            if self.planets >= 35 and self.moons >= 79:
                self.rank = '*Jupiter <7>*'
                self.saveRank()
            if self.planets >= 50 and self.moons >= 100:
                self.rank = '*Mars <8>*'
                self.saveRank()
            if self.planets >= 75 and self.moons >= 125:
                self.rank = '**Venus <9>**'
                self.saveRank()
            if self.planets >= 100 and self.moons >= 150:
                self.rank = '**Callisto <10>**'
                self.saveRank()
            if self.planets >= 125 and self.moons >= 235:
                self.rank = '**Europa <11>**'
                self.saveRank()
            if self.planets >= 150 and self.moons >= 280:
                self.rank = '**SUN**'
                self.saveRank()
            if self.planets >= 250 and self.moons >= 450:
                self.rank = '***GALAXY***'
                self.saveRank()
            if self.planets >= 500 and self.moons >= 750:
                self.rank = '***U N I V E R S U M***'
                self.saveRank()
            if self.planets >= 1000 and self.moons >= 1000 and self.antidices >= 1:
                self.rank = '◼️B l a c k h ◉ l e◼️'
                self.saveRank()

            self.saveCoins()
            self.saveDices()
            self.saveMultidice()
            self.saveMegadice()
            self.readCoins()
            self.readDices()
            self.readMegadice()
            self.readMultidice()
            embedVar = discord.Embed(
                title="**" + str(message.author)[0:len(str(message.author)) - 5] + "'s Solar system**",
                description='** **', color=0x00ff00)
            embedVar.add_field(name="Rank:", value=str(self.rank), inline=False)
            embedVar.add_field(name="Planets:",
                               value=str(self.planets),
                               inline=False)
            embedVar.add_field(name="Moons", value=str(self.moons), inline=True)
            embedVar.add_field(name="Spacex ID:", value=str(message.author.id*2), inline=True)
            embedVar.add_field(name="Coins:", value=str(self.coins), inline=True)
            embedVar.add_field(name="Anti dices:", value=str(self.antidices), inline=False)
            embedVar.add_field(name="Total space score:", value=score, inline=False)
            #embedVar.add_field(name="Level:", value=str(self.level), inline=False)

            await message.channel.send(embed=embedVar)
            ran = random.randint(1, 10)
            if ran == 1:
                await message.channel.send('**Tip:**\nDid you know that the best way to get planets and moons is to buy packs or playing spacex?\nWell, now you do.')

        if message.content == 'characters':
            self.save
            embedVar = discord.Embed(
                title="**" + str(message.author)[0:len(str(message.author)) - 5] + "'s Characters**",
                description='= = = = = =', color=0x00ff00)
            embedVar.add_field(name="Rank:", value=str(self.rank), inline=False)
            embedVar.add_field(name="Characters:", value=self.characters, inline=False)
            embedVar.add_field(name="Rare characters:", value=self.rare, inline=True)
            embedVar.add_field(name="Super rare characters:", value=self.srare, inline=False)
            await message.channel.send(embed=embedVar)


        if message.content == 'leaderboard':
            self.save
            embedVar = discord.Embed(title="**Global rank leaderboard**", description='= = = = = =', color=0x00ff00)
            embedVar.add_field(name="1. ", value='Venus#1759 '+str(myscore), inline=False)
            embedVar.add_field(name="2. ", value='Galaxymaster2007#1524 '+str(galascore), inline=False)
            embedVar.add_field(name="3. ", value='Sunbeamer#3382 '+str(sunscore), inline=False)
            embedVar.add_field(name="Your rank:", value=str(message.author)+' '+str(score), inline=True)


            #print(self.multidices, self.megadices)

            await message.channel.send(embed=embedVar)

        ### Shop och ekonomi ###
        if message.content.startswith('buy'):
            if 'chest' in message.content:
                if self.coins >= 25:
                    self.coins -= 25
                    self.saveCoins()
                    randloot = random.choices(loot)
                    if randloot[0] == '50 coins':
                        #print('success')
                        self.coins = self.coins + 50
                        self.saveCoins()
                    if randloot[0] == '0 coins':
                        #print('success')
                        self.coins += 0
                        self.saveCoins()
                    if randloot[0] == '1 multi dice':
                        #print('success')
                        self.multidices = self.multidices + 1
                        self.saveMultidice()
                    if randloot[0] == '1 mega dice':
                        #print('success')
                        self.megadices = self.megadices + 1
                        self.saveMegadice()
                    if randloot[0] == '1 coindice':
                        #print('success')
                        self.coindices += 1
                        self.saveCoindices()
                    #print(self.coins+50)
                    #print(self.multidices, self.megadices)
                    #print(randloot)
                    self.readCoins()
                    self.readDices()
                    self.readMegadice()
                    self.readMultidice()
                    await message.channel.send('**Successfully bought a chest**\nYou got:  '+str(randloot[0]))

        if 'pack1' in message.content:
            pack1()
        if 'pack2' in message.content:
            pack2()
        if 'pack3' in message.content:
            pack3()
        if 'pack4' in message.content:
            pack4()
        if 'spacepack1' in message.content:
            spacepack1()
        if 'spacepack2' in message.content:
            spacepack2()
        if 'characterpack1' in message.content:
            characterpack1()


#50 coins', '0 coins', '1 multi dice', '1 mega dice
        ### Minigames med priser ###
        if message.content.startswith('play'):
            if message.content[5:len(message.content)] == 'spacex':
                spacex = random.choices(spaceloot)
                if self.coins >= 75:
                    self.coins -= 75
                    self.saveCoins()
                    if spacex[0] == '100 coins':
                        #print('success')
                        self.coins = self.coins + 100
                        self.saveCoins()
                    if spacex[0] == '0 coins':
                        #print('success')
                        self.coins += 0
                        self.saveCoins()
                    if spacex[0] == '1 planet':
                        #print('success')
                        self.planets = self.planets + 1
                        self.savePlanets()
                    if spacex[0] == '1 moon':
                        #print('success')
                        self.moons = self.moons + 1
                        self.saveMoons()
                    if spacex[0] == '3 moons!':
                        #print('success')
                        self.moons += 3
                        self.saveMoons()
                    if spacex[0] == '75 coins':
                        #print('success')
                        self.coins = self.coins + 75
                        self.saveCoins()
                    if spacex[0] == '1 antidice':
                        #print('success')
                        self.antidices += 1
                        self.saveAntidices()
                    if spacex[0] == '1 coindices':
                        # print('success')
                        self.coindices += 1
                        self.saveCoindices()
                    #print(spacex)
                    self.readCoins()
                    self.readRank()
                    self.readPlanets()
                    self.readMoons()
                    await message.channel.send('**Successfully played *S P A C E X***\nYou earned:  '+str(spacex[0]))

            if message.content[5:len(message.content)] == 'price wheel':
                price = random.choices(wheel)
                if self.coins >= 50:
                    self.coins -= 50
                    self.saveCoins()
                    if price[0] == '5 coins':
                        # print('success')
                        self.coins = self.coins + 5
                        self.saveCoins()
                    if price[0] == '10 coins':
                        # print('success')
                        self.coins += 10
                        self.saveCoins()
                    if price[0] == '15 coins':
                        # print('success')
                        self.coins += 15
                        self.saveCoins()
                    if price[0] == '20 coins':
                        # print('success')
                        self.coins += 20
                        self.saveCoins()
                    if price[0] == '50 coins':
                        # print('success')
                        self.coins += 50
                        self.saveCoins()
                    if price[0] == '**1 0 0 0 C O I N S!**':
                        # print('success')
                        self.coins += 1000
                        self.saveCoins()
                    if price[0] == '1 mega dice':
                        # print('success')
                        self.megadices += 1
                        self.saveMegadice()
                    if price[0] == '3 multi dices':
                        # print('success')
                        self.multidicesdices += 1
                        self.saveMultidice()
                    if price[0] == '3 coindices':
                        # print('success')
                        self.coindices += 3
                        self.saveCoindices()

                    # print(spacex)
                    self.readCoins()
                    self.readMegadice()
                    self.readMultidice()
                    await message.channel.send(
                        '**Wheel spinned. . .***\nYou got:  ' + str(price[0]))
                    ran = random.randint(1, 10)
                    if ran == 1:
                        await message.channel.send(
                            '**Tip:**\nSpinning price wheels is not the best way to get coins in, we performs chests or spacex\'s.')



        ###data###
        if message.content == 'info':
            self.save
            embedVar = discord.Embed(
                title="**VENUS INFO**",
                description='+=+ +=+ +=+ +=+ +=+ +=+', color=0x00ff00)
            embedVar.add_field(name="Version", value=version, inline=True)
            embedVar.add_field(name="Version name", value=update, inline=True)
            embedVar.add_field(name="** **", value='** **', inline=False)
            embedVar.add_field(name="Creator", value='viggope#6217', inline=True)
            embedVar.add_field(name="Creator id", value='656595397472550933', inline=True)
            embedVar.add_field(name="** **", value='** **', inline=False)
            embedVar.add_field(name="Next update", value='Unknown', inline=True)
            embedVar.add_field(name="Next update name", value=neversion, inline=True)
            embedVar.add_field(name="Coming update name", value=neversion2, inline=True)
            embedVar.add_field(name="Update info", value='Added easter pack\nAdded commands', inline=False)
            embedVar.add_field(name="################", value='** **', inline=True)
            embedVar.add_field(name="My score", value=myscore, inline=False)
            embedVar.add_field(name="My tag", value='Venus#1759', inline=False)
            embedVar.add_field(name="My id", value='808405969703796807', inline=False)
            embedVar.add_field(name='Client id', value=id(client), inline=False)
            embedVar.add_field(name="Lines of code programmed", value='>1200', inline=False)
            embedVar.add_field(name="Message id", value=message.id, inline=False)
            embedVar.add_field(name="Message info", value=message, inline=False)
            embedVar.add_field(name="Some commands", value=commands, inline=False)
            embedVar.fields.reverse()
            await message.channel.send(embed=embedVar)
        if message.content == 'pack info':
            self.save
            embedVar = discord.Embed(
                title="Pack info",
                description='= = = = = = = =', color=0x00ff00)
            embedVar.add_field(name="Pack1 content", value='You get 5 multidices and 3 megadices\nPrice: 200 coins', inline=False)
            embedVar.add_field(name="Pack2 content", value='You get 10 multidices, 5 megadices and 1 moon\nPrice: 400 coins', inline=False)
            embedVar.add_field(name="Pack3 content", value='You get 25 multidices, 10 megadices, 4 moons and 1 *planet*\nPrice: 400 coins', inline=False)
            embedVar.add_field(name="Pack4 content", value='You get 50 multidices, 25 megadices, 7 moons 2 *planet* and 1 *antidice\nPrice: 5000 coins',inline=False)
            embedVar.add_field(name="** **", value='** **', inline=False)
            embedVar.add_field(name="Spacepack1 content", value='You get 5 moons, 1 *planet* and 1 coindice\nPrice: 1200 coins',inline=False)
            embedVar.add_field(name="Spacepack2 content", value='You get 7 moons, 3 *planets*, 1 coindice and 1 *antidice*\nPrice: 1750 coins',inline=False)
            embedVar.add_field(name="** **", value='** **', inline=False)
            embedVar.add_field(name="Characterpack1 content", value='You have a chance to get 1 rare or super rare character when you buy this pack\nPrice: 1000 coins',inline=False)
            await message.channel.send(embed=embedVar)

        if message.content == 'rank info':
            self.save
            embedVar = discord.Embed(
                title="Rank info",
                description='-=- -=- -=- -=- -=- -=- -=- -=-', color=0x00ff00)
            embedVar.add_field(name="Merkurius <2> Requirements", value='You need 1 planet and 3 moons', inline=False)
            embedVar.add_field(name="Ceres <3> Requirements", value='You need 3 planets and 10 moons', inline=False)
            embedVar.add_field(name="Neptunus <4> Requirements", value='You need 10 planet and 20 moons', inline=False)
            embedVar.add_field(name="Pluto <5> Requirements", value='You need 15 planets and 35 moons', inline=False)
            embedVar.add_field(name="Uranus <6> Requirements", value='You need 24 planets and 50 moons', inline=False)
            embedVar.add_field(name="Jupiter <7> Requirements", value='You need 35 planets and 79 moons', inline=False)
            embedVar.add_field(name="Mars <8> Requirements", value='You need 50 planets and 100 moons', inline=False)
            embedVar.add_field(name="Venus <9> Requirements", value='You need 75 planets and 125 moons', inline=False)
            embedVar.add_field(name="Callisto <10> Requirements", value='You need 100 planets and 150 moons', inline=False)
            embedVar.add_field(name="Europa <11> Requirements", value='You need 125 planets and 235 moons', inline=False)
            embedVar.add_field(name="Sun <12> Requirements", value='You need 150 planets and 280 moons', inline=False)
            embedVar.add_field(name="Galaxy <13> Requirements", value='You need 250 planets and 450 moons',inline=False)
            embedVar.add_field(name="Universum <14> Requirements", value='You need 500 planets and 750 moons', inline=False)
            embedVar.add_field(name="||Locked|| <15> Requirements", value='You need 1000 planets, 1000 moons and 1 anti dice',inline=False)
            await message.channel.send(embed=embedVar)


        if message.content == 'mailbox':
            embedVar = discord.Embed(
                title="**"+str(message.author)[0:len(str(message.author))-5]+"'s Mailbox**", #("+str(len(list(self.news)))+")",
                description='= = = = = = = =', color=0x00ff00)
            embedVar.add_field(name='** **', value=self.news)
            await message.channel.send(embed=embedVar)
            #self.saveMailbox()
            #await message.channel.send(embed=embedVar)

    ### Admin update ###

        if message.content.startswith('kick'):
            if message.author in vip:
                for user in message.mentions:
                    try:
                        await user.kick(reason="Youve been kicked out by "+message.author)
                    except discord.errors.Forbidden as err:
                        await message.channel.send('**Whoops!**')
                        await message.channel.send(err.text)
            else:
                await message.channel.send('**Stop dreaming!** You dont have that permission')

        if message.content.startswith('admin'):
            if message.author in vip:
                for user in message.mentions:
                    try:
                        vip.insert(1, message.author)
                    except VipError as err:
                        await message.channel.send('**Whoops!**')
                        await message.channel.send(err.text)
            else:
                await message.channel.send('**Stop dreaming!** You dont have that permission')

    ## Trials of Venus update ##
        if message.content == 'trials begin':
            await trials.handle(message)
            #time.sleep(10)

            '''async def greet(ctx):
                await ctx.send("Select portal 1 or 2")

                def check(m):
                    return m.content == "1" or "2" and m.channel == channel

                await client.wait_for("message", check=check)
                await ctx.send("hi")
            await greet(ctx=message.channel)'''


bot = Botten()
bot.run(TOKEN)