import discord
from bot_function_1 import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola deyus bot'):
        await message.channel.send("hola!")
    elif message.content.startswith('adios deyus bot'):
        await message.channel.send("adios😭")
    else:
        await message.channel.send("tu contraseña es " + gen_pass(int(message.content)))



client.run("MTI1MDYzMjY0NzEzNTQ2NTQ3Mg.GL9Bjr.a0oxki_03NCq7zpFsXddzYVGXIyhbfXGjjHfc0")
