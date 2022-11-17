import discord
from discord import *
from random import *
from time import *
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw 
global stop
bot = commands.Bot('!', help_command=None)
debug_mode = True
def ratioadd(author):
    file = open("ratio.csv", 'r')
    text =file.read()
    liness=[]
    lines =text.split('\n')
    for i in range(len(lines)):
        liness.append( lines[i].split(';'))
        print(liness[i])
        try:
            liness[i][1]= int(liness[i][1])
        except:
            liness.pop(i)
    find = False
    for i in range(len(liness)):
        if (int(liness[i][0])==author):
            liness[i][1]+=1
            find =True
            print("find")
    if (not find):
        print("not find")
        liness.append([author, 1])
    linesstr= str( liness)
    print (linesstr+'\n')
    linesstr=linesstr.replace('], [', '''
''').replace(',',';').replace('[[','').replace(']]','')
    linesstr=linesstr.replace("'","").replace('"',"").replace('\\','').replace(']','').replace('[','')
    print(linesstr)
    file.close()
    file =open("ratio.csv","w")
    file.write(linesstr)
    file.close()
@bot.event
async def on_message_delete(message):
    print(52)
    if (message.author.id == 948151285356576778):
        re = await message.channel.send(message.content +' + ratio')
        await re.add_reaction('<:NotFunnyDidntLaugh:937741166194077759>')
'''@bot.event
async def on_error(event, *args, **kwargs):
    channel = discord.utils.get(bot.get_all_channels(), guild__name='pw', name='g')
    re = [event,args,kwargs]
    await channel.send(re)'''
@bot.event
async def on_message(message):
    global debug_mode
    if (message.channel.id != 935807417516720219):
        rand = randint(0,100)
        a = message.content.split(' ')
        if (message.channel.id == 973916311170220042)or(message.channel.id ==1022152605880819762):
            if message.author.id != 948151285356576778:
                await message.channel.send(message.content)
        if (a[0] == 'stopd'):
            if message.author.id == 410566152394244106:
                debug_mode = False
        if (a[0] =='error'):
            r=re
        if (a[-1]=='quoi')or(a[-1]=='pourquoi'):
           await message.channel.send('feur')
        if (a[-1]=='oui')or (a[-1]=='Oui')or(a[-1]=='OUI'):
            if(rand <= 12):
                await message.channel.send('stiti')
        if (a[-1]=='non')or (a[-1]=='Non')or(a[-1]=='NON'):
            if(rand <= 12):
                await message.channel.send('bril')
        if (a[-1] == '?'):
            if (a[-2]=='quoi')or(a[-2]=='pourquoi'):
                await message.channel.send('feur')
        if (a[0]=='no'):
            img = Image.open('no.png')
            title_font = ImageFont.truetype('Roboto-Regular.ttf', 25)
            image_editable = ImageDraw.Draw(img)
            image_editable.text((15,15), message.content, (237, 230, 211), font=title_font)
            img.save("result.png")
            no= [discord.File('result.png')]
            await message.channel.send(files=no)
        if debug_mode:
            print(message.content)
        if rand ==1:
            if message.author.id != 477593635358113792:
                re =  await message.channel.send("ratio",reference=message)
                ratioadd(message.author.id)
                await re.add_reaction('<:NotFunnyDidntLaugh:937741166194077759>')
            else :
                ran = randint(0 ,3)
                if ran == 1:
                     re =  await message.channel.send("ratio",reference=message)
                     ratioadd(message.author.id)
                     await re.add_reaction('<:NotFunnyDidntLaugh:937741166194077759>')

        

bot.run("you won't get that")
