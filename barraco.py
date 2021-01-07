import os
import discord
from env import TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print('A bicha logou como ' + str(self.user) + '! EU AMO')

    async def on_message(self, message):
        msg = message.content.lower().split()
        # don't respond to ourselves
        if message.author == self.user:
            return

        if 'oi' in msg:
            await message.channel.send('inhai mona')

        elif 'salada' in msg:
            await message.channel.send('tomate')

        elif 'utau' in msg:
            await message.channel.send('Enfim a falência')

        elif 'finalmente' in msg:
            await message.channel.send('FINALMENTE UM NOVO UTAU SURGE NO FANDOM')

        elif 'Boa noite' in msg:
            await message.channel.send('inhai mona')

        elif 'pururu' in msg:
            await message.channel.send('é cururu')

        elif 'agua' and 'mineral' in msg:
            await message.channel.send('DEIXA A VAIBE MORRE EM PAZ')

        elif '&help' in msg:
            await message.channel.send('Olá! Aqui estão todos os meus comandos:\nPor enquanto nada rs')
        
        elif 'vibe' in msg:
            await message.add_reaction('⚰')

client = MyClient()
client.run(TOKEN)