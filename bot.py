import lightbulb
import hikari
import requests
from pprint import pprint
import urllib.parse

bot = lightbulb.BotApp(token='') #use default_enabled_guilds=() with the guild id of the servers you would like to run on for faster updating when making changes

#call to the random endpoint for a random joke
def call():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url).json()
    output = response['value']
    return output

#call to the catergory endpoint for the different catergory jokes
def catergory_call(arg):
    new_url = "https://api.chucknorris.io/jokes/random?category="+arg
    catergory_response = requests.get(new_url).json()
    catergory_output = catergory_response['value']
    return catergory_output

#print to comfirm the bot has started
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Chuck Norris Has Awoken')

#main bot command group
@bot.command
@lightbulb.command('chuck', 'Jokes group',)
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def command_group(context):
    pass

#subcommands for random & each catergory
@command_group.child
@lightbulb.command('random', 'Responds with a random chuck norris joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def random(context):
    value = call()
    await context.respond(value)


@command_group.child
@lightbulb.command('food', 'Responds with a chuck norris food joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def food(context):
    value = catergory_call('food')
    await context.respond(value)


@command_group.child
@lightbulb.command('career', 'Responds with a chuck norris career joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def career(context):
    value = catergory_call('career')
    await context.respond(value)


@command_group.child
@lightbulb.command('celebrity', 'Responds with a chuck norris celebrity joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def celebrity(context):
    value = catergory_call('celebrity')
    await context.respond(value)


@command_group.child
@lightbulb.command('dev', 'Responds with a chuck norris dev joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def dev(context):
    value = catergory_call('dev')
    await context.respond(value)


@command_group.child
@lightbulb.command('explicit', 'Responds with a chuck norris explicit joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def explicit(context):
    value = catergory_call('explicit')
    await context.respond(value)


@command_group.child
@lightbulb.command('fashion', 'Responds with a chuck norris fashion joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def fashion(context):
    value = catergory_call('fashion')
    await context.respond(value)


@command_group.child
@lightbulb.command('history', 'Responds with a chuck norris history joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def history(context):
    value = catergory_call('history')
    await context.respond(value)


@command_group.child
@lightbulb.command('money', 'Responds with a chuck norris money joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def money(context):
    value = catergory_call('money')
    await context.respond(value)


@command_group.child
@lightbulb.command('movie', 'Responds with a chuck norris movie joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def movie(context):
    value = catergory_call('movie')
    await context.respond(value)


@command_group.child
@lightbulb.command('music', 'Responds with a chuck norris music joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def music(context):
    value = catergory_call('music')
    await context.respond(value)


@command_group.child
@lightbulb.command('political', 'Responds with a chuck norris political joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def political(context):
    value = catergory_call('political')
    await context.respond(value)


@command_group.child
@lightbulb.command('religion', 'Responds with a chuck norris religion joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def religion(context):
    value = catergory_call('religion')
    await context.respond(value)


@command_group.child
@lightbulb.command('science', 'Responds with a chuck norris science joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def science(context):
    value = catergory_call('science')
    await context.respond(value)


@command_group.child
@lightbulb.command('sport', 'Responds with a chuck norris sport joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sport(context):
    value = catergory_call('sport')
    await context.respond(value)


@command_group.child
@lightbulb.command('travel', 'Responds with a chuck norris travel joke')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def travel(context):
    value = catergory_call('travel')
    await context.respond(value)

bot.run()
