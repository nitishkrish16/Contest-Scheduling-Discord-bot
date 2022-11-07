import discord
import datetime

client = discord.Client()

welcomeMessage = # Enter your welcome message here.
welcomeChannelID = # Enter the welcome channel's ID here.
botToken = # Enter your bot's token here.

# Logging information for start-up.
@client.event
async def on_ready():
    print("I'm all set as {0.user}.".format(client))
    if len(client.guilds) == 0:
        print("I'm not in any servers.")
    else:
        print("I'm in the server/servers:", end = "")
        for item in client.guilds:
            print(" " + item.name, end = "")
        print(".")

# Logs new users and sends the welcome message.
@client.event
async def on_member_join(member):
    print(f"Recognized {member.name} joined a server on {datetime.datetime.now(datetime.timezone.utc)}.")
    await client.get_channel(TestBotInfo.getWelcomeID()).send(welcomeMessage) # Add any formatting here. Example: welcomeMessage.format(member.name) will display the new users name in place of a set of {}.

# A help message.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('!help'):
        await client.get_user(message.author.id).send("") # Enter what you would like your help message to be here.

client.run(botToken)
