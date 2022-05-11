import discord


TOKEN='OTczNDQ0Mzc1MzgyMjIwODMx.GN7gQl.AAsBqwntOTeUx8fMWVpCWBU8G5_6xSF8UpFDZo'

client =discord.Client()


@client.event
async def on_ready():
  print(f'{client.user} is online!!!')
  general=client.get_channel(973444776982630422)
  await general.send("Hello there!!")

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(f'Hi {member.name}, Welcome to my Youtube channel')
  general=client.get_channel(973444776982630422)
  await general.send(f'A new member {member.name} has appeared!!')
  


@client.event
async def on_message(message):
  #general=client.get_channel(973444776982630422)
  if message.author==client.user:
    return
  msg=message.content.split()
  if message.author.id==432610292342587392:
    emoji=client.get_emoji(973494869169414184)
    if msg==[]:
      await message.add_reaction(emoji)
    
  #if (message.author.id==729607695895887882):
  #  emoji=client.get_emoji(973494869169414184)
  #  response = "Whats up"
  #  await general.send(response)
  #  await message.add_reaction(emoji)

  #msg=message.content.split(' ')
  #if len(msg) > 10:
  #  response='Msg too long to send'
  #  await message.delete()
  #  await message.channel.send(response)



client.run(TOKEN)
