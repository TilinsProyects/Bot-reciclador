import discord
import random

TOKEN = 'pon tu codigo aqui, no lo pongo io porque me lo roban XD'

links = {
    "vidrio": "https://www.youtube.com/watch?v=VrNNSYgTK5k",
    "papel": "https://crearyreciclar.com/mas-de-35-ideas-para-hacer-en-casa-con-materiales-reciclados/",
    "metal": "https://co.pinterest.com/rick0670rs/manualidades-en-metal/",
    "carton": "https://www.handfie.com/manualidades-con-cajas-de-carton/081/",
    "plastico": "https://www.educaciontrespuntocero.com/familias/manualidades-botellas-de-plastico/"
}

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!reciclar'):
        materiales = list(links.keys())
        material_aleatorio = random.choice(materiales)
        enlace = links[material_aleatorio]
        await message.channel.send(f'El material seleccionado es: {material_aleatorio}. Puedes reciclarlo aquí: {enlace}')

client.run(TOKEN)