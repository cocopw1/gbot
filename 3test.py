import discord
from discord import *
from random import *
import requests as rq
from time import *
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import PIL.ImageOps
def tri_bulle(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j][1] < tab[j+1][1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab
global stop
bot = commands.Bot('!', help_command=None)
@bot.command()
async def roll(ctx,chifre):
    try:
        chifre = int(chifre)
        await ctx.send(randint(0,chifre))
    except:
        await ctx.send("n'est pas un int")
@bot.command()
async def ts(ctx,arg1:int):
    global stop
    stop = False
    a = 0
    arg1=int(arg1/5)
    while ((a<arg1)and(not stop)):
        a+=1
        sleep(2)
        print(a,stop)
        await ctx.send('Je suis le chien qui spam')
        await ctx.send('Je suis le chien qui spam')
        await ctx.send('Je suis le chien qui spam')
        await ctx.send('Je suis le chien qui spam')
        await ctx.send('Je suis le chien qui spam')
    print("j'ai fini")
@bot.command()
async def stop(ctx):
    global stop
    stop =True
@bot.command()
async def reveil(ctx, membre:Member):
    global stop
    stop = False
    while(not stop):
        await ctx.send(f"{membre.mention}")
@bot.command()
async def evil(ctx,membre:Member, **args):
    img = rq.get(membre.avatar_url)
    file = open("avatar.png", "wb")
    file.write(img.content)
    file.close()
    text = ctx.message.content
    text=text.replace(str(membre.id),membre.name)
    text=text.replace('!','').replace('<','').replace('>','').replace('@','')
    tlist = text.split(' ')
    lenlist =[]
    for word in tlist:
        lenlist.append(len(word)+1)
    recap =""
    lettercount = 0
    for i in range(len(tlist)):
        if (lettercount+lenlist[i]>20):
            recap+='\n'
            lettercount = 0
        recap+=tlist[i]+' '
        lettercount+=lenlist[i]
    
    try :
        image = Image.open('avatar.png')
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save('invertavatar.png')
        img = Image.open('invertavatar.png')
    except:
        img = Image.open('avatar.png')
    title_font = ImageFont.truetype('Roboto-Regular.ttf', int(img.size[1]/10))
    contour_font = ImageFont.truetype('Roboto-Regular.ttf', int(img.size[1]/10)+5)
    image_editable = ImageDraw.Draw(img)
    image_editable.multiline_text((15,15), recap, (255, 255, 255), font=title_font,stroke_width=5,stroke_fill = (0,0,0))
    img.save("result2.png")
    img = [discord.File('result2.png')]
    await ctx.send(files=img)
@bot.command()
async def prank(ctx):
    emb= Embed(title = 'A wild pokémon has appeared!', description = 'Guess the pokémon and type `p!catch <pokémon>` to catch it!',color=0xF446FF)
    emb.set_image(url="https://cdn.discordapp.com/attachments/973562809231220737/973565367999922236/pokemon.jpg")
    await ctx.send(embed= emb)
@bot.command()
async def off(ctx):
    if (ctx.author.id == 410566152394244106):
        await bot.close()
    else:
        await ctx.send("pas autorisé")
@bot.command()
async def leaderboard(ctx):
    file = open( "ratio.csv","r")
    content = file.read()
    listcontent = content.split('\n')
    listcont = []
    for i in range(len(listcontent)):
        listcont.append(listcontent[i].split(';'))
        try:
            listcont[i][0]=int(listcont[i][0])
            listcont[i][1]=int(listcont[i][1])
        except:
            print("err")
            listcont.pop(i)
    print(listcont)
    listcont = tri_bulle(listcont)

    print ('\n')
    print(listcont)
    des = ''
    for i in range(len(listcont)):
        des+=str(i+1)+' <@!'+str(listcont[i][0]) +'> ' + str(listcont[i][1])+'\n'
    emb = Embed(title = 'leaderboard', description = des)
    await ctx.send(embed =emb)
        
    
bot.run('OTQ4MTUxMjg1MzU2NTc2Nzc4.Yh3osg.amx2jTpA3THSOu-T7qpACZjjOmQ')
