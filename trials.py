import jsonpickle
import time
import random

# from bot import client

from discord import channel

alfabeta = '!"#€%&/()=?+0V<>A'
right = alfabeta[random.randint(0, len(alfabeta)-1)]
print(right)


def saveTrialusers():
    file = open("trialusers.txt", "w")
    file.write(jsonpickle.encode(user_trials))
    file.close()


def readTrialusers():
    try:
        file = open("trialusers.txt", "r")
        trials: dict = jsonpickle.decode(file.read())
        file.close()
        return trials
    except:
        print("failed to read trialusers.txt, zeroing")
        return dict()
        pass


class Trials:
    step: int
    guessing = False
    def __init__(self):
        self.step = 0

    def start(self):
        self.step = 1
        saveTrialusers()
        return


async def handle(message, guessing=None):
    ut: Trials = None
    if message.content.startswith("trial"):
        ut = user_trials.get(message.author.id)
    if not ut:
         print("no trial for user yet")
         ut = Trials()
         user_trials[message.author.id] = ut
    else:
        print("found ongoing trial for user")

    if "begin" in message.content:
        ut.start()
        await message.channel.send('The portal opens. . .')
        time.sleep(2)
        await message.channel.send('. . .')
        time.sleep(2)
        await message.channel.send("You are now in the hall of portals")
        time.sleep(2)
        await message.channel.send('Interacting with portal 1. . .')
        time.sleep(2)
        await message.channel.send(
            'An encrypted code appears 3 meters in front of you but you cant understand what it means')
        time.sleep(2)
        await message.channel.send(
            'On the left, a complicated puzzle appears. 🧩')
        puzzle = 'V'

        # async def greet():
        await message.channel.send("V0" + puzzle)
        guessing = True
        # def check(m):
        #   return m.content == "%" and m.channel == channel
        # while not message.content == '%':

                # message.content("%", check=check)
                # await message.channel.send("V0A")

        # await greet()

        portal_selection = 1, 2, 3


    else:
        if guessing == True:
            if message.content == right:
                guessing = False
#  return None


user_trials = readTrialusers()
