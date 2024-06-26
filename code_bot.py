import discord
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola deyus bot'):
        await message.channel.send('¡Hola!')
    elif message.content.startswith('adios deyus bot'):
        await message.channel.send("adios😭")
    elif message.content.startswith('voltea una moneda'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send("tu contraseña es " + gen_pass(int(message.content)))

client.run("put here your token")
