import random
import discord
from discord import member
from discord.ext.commands import BucketType, cooldown
from discord.ext import commands
import os
from discord.utils import get
import youtube_dl



# =================================================================================

client = commands.Bot(command_prefix="=", case_insensitive=True)


# ==================================================================================
@client.event
async def on_ready():
    guild = client.get_guild(631556614465257505)
    canal = guild.get_channel(765657391457894420)
    print('Entramos como {0.user})'.format(client))
    await client.change_presence(
        activity=discord.Streaming(name="Roleplay de UBER 24/7", url='https://www.twitch.tv/foxinho'))
    await canal.send(f'TO ONLINE CARALHOOOOOOOOOOOOOO   '
                     f' https://cdn.discordapp.com/attachments/765657391457894420/850058318542405682/pressao.mp4')

    @client.event
    async def on_command_error(ctx, error):
        message = (f"{ctx.message.author.mention}, Este comando não existe, ou está errado.")
        await ctx.reply(f"{message}")

    # ======================================================================================================================

    @client.command()
    @cooldown(1, 3, BucketType.user)
    async def perguntar(ctx, *, question):
        responses = ['Estou certo disto.',
                     'Definitivamente.',
                     'Sem sombra de duvidas.',
                     'Sim.',
                     'Estou em duvida.',
                     'Pergunta depois to com sono.',
                     'Não posso dizer agora.',
                     'É melhor você nem saber...',
                     'Não conte com isso.',
                     'Nem fudendo.',
                     'Meus recursos dizem que não.',
                     'Não.',
                     'Ok.',
                     'Roberto Souza Soares.',
                     'Pergunta pro Bolsonaro mlk.',
                     'Não quero falar agora to ocupado filho da puta.',
                     'Não quero falar.',
                     'Ele não...', ]
        await ctx.reply(f'{random.choice(responses)}')

    # ======================================================================================================================
    @client.command(aliases=['online'])
    async def status(ctx):
        respostas = ['TO ACORDADO PORRA.',
                     'Que foi arrombado?',
                     'Hmm?',
                     'https://tenor.com/view/dia-gif-9323851',
                     'To online.',
                     'Roberto Souza Soares.',
                     'Bom dia.',
                     'EDIT BASED!  https://cdn.discordapp.com/attachments/765657391457894420/850052072899739709/Heathens_Centuries_Heavens_Feel_II_Saber_Alter_AMV_EDIT.mp4',
                     'GELADEIRA TSUNAMI!!'
                     ' https://cdn.discordapp.com/attachments/765657391457894420/850052549335711794/geladeira_tsunami.mp4',
                     'https://tenor.com/view/clubpenguim-joiner-gif-19009876',
                     ':cricket: grelo',
                     f':flag_br: BOLSONARO'
                     f' https://tenor.com/view/presitendete-do-brasil-jair-bolsonaro-sparkle-smile-gif-16870246',
                     f'Não olha pra janela, e nem atenda a porta.'
                     f' https://tenor.com/view/troll-face-creepy-smile-gif-18297390',
                     f':heart: Caminhões'
                     f' https://cdn.discordapp.com/attachments/765657391457894420/850058318542405682/pressao.mp4',
                     f'https://cdn.discordapp.com/attachments/765657391457894420/865283590207963137/ronaldo_1.mp4']
        await ctx.reply(f'{random.choice(respostas)}')

        # ======================================================================================================================

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=11):
        await ctx.channel.purge(limit=amount)
        await ctx.reply(f"10 Mensagens apagadas", delete_after=amount)


# ======================================================================================================================

@client.command(aliases=["peido"])
@cooldown(1, 3, BucketType.user)
async def trava(ctx):
    await ctx.reply(f'https://tenor.com/view/dr-nefario-fart-gun-gif-20054143')


# ======================================================================================================================

@client.command()
@cooldown(1, 3, BucketType.user)
async def melhormusica(ctx):
    await ctx.reply(f'https://www.youtube.com/watch?v=LYVAVlYIzpk')


# ======================================================================================================================

@client.command(aliases=["macaco"])
@cooldown(1, 5, BucketType.user)
async def mansk(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/668213885534339113/668214201222955018/Screenshot_649.png')
    await ctx.send(f'https://cdn.discordapp.com/attachments/668213885534339113/668214877260742697/Screenshot_790.png')
    await ctx.send(f'https://cdn.discordapp.com/emojis/616204066564866058.png?v=1')
    await ctx.send(
        f'https://media.discordapp.net/attachments/401857210122240017/593952605936418836/unknown.png?width=432&height=243')
    await ctx.send(f'https://cdn.discordapp.com/attachments/668213885534339113/681714455633330254/unknown.png')
    await ctx.send(f'https://media.discordapp.net/attachments/540707303976992778/541528940339003393/Screenshot_3.png')
    await ctx.send(f'https://media.discordapp.net/attachments/506288332477562880/540746530261565461/unknown.png')
    await ctx.send(f'https://media.discordapp.net/attachments/451136369213833226/645062749289971712/unknown.png')


# ======================================================================================================================

@client.command(aliases=["pong"])
@cooldown(1, 3, BucketType.user)
async def ping(ctx, arg=None):
    if arg == "pong":
        await ctx.reply("Nice job, you just ponged yourself")
    else:
        await ctx.reply(f'Pong! ai está o meu ping amigo: {round(client.latency * 100)}ms')


# ======================================================================================================================

@client.command(pass_context=True, aliases=['j', 'comeback', "joi"])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"O bot foi conectado em {channel}\n")

    await ctx.send(f"Entrei em {channel}")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Audio pausado.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("O audio não está pausado.")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Sai de {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Eu não estou em um canal")


@client.command(aliases=['skip', 's'])
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Ja tem uma musica tocando!")
        return

    await ctx.send("Tudo está ficando pronto, aguarde.")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Baixando o audio\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Tocando: {nname[0]}")
    print("playing\n")


# ======================================================================================================================

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.reply(f"{member} foi banido!")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.reply(f"{member} foi kickado!")


# ======================================================================================================================
@client.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.reply(f"Avatar de: {avamember.mention} "
                   f"{userAvatarUrl}")


# ======================================================================================================================
@client.command(aliases=['say'])
async def falar(ctx, *, message):
    await ctx.message.delete()
    await ctx.reply(f"{message}".format(message))


# ======================================================================================================================

@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    time = ctx.guild.created_at.strftime("%Y-%m-%d")

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name,
        color=discord.Color.blue()

    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Dono", value=owner, inline=True)
    embed.add_field(name="ID do server", value=id, inline=True)
    embed.add_field(name="Região", value=region, inline=True)
    embed.add_field(name="Membros", value=memberCount, inline=True)
    embed.add_field(name="Criado em", value=time, inline=True)

    await ctx.reply(embed=embed)


@client.command()
async def ronaldo(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/765657391457894420/865283590207963137/ronaldo_1.mp4")


# ======================================================================================================================

@client.command()
@cooldown(1, 3, BucketType.user)
async def foinao(ctx):
    await ctx.send("FOI um não.")
    await ctx.send("Infelizmente")
    await ctx.send("Depois de tudo")
    await ctx.send("Ele quer fazer isso consigo mesmo")
    await ctx.send("Ela n me escolheu")
    await ctx.send("Eu me dedicando")
    await ctx.send("Pra caralho")
    await ctx.send("Que raiva")


# ======================================================================================================================

@client.command()
@cooldown(1, 3, BucketType.user)
async def ouvidizer(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/765657391457894420/875177217213214751/ouvidizer_m.mp4")


# ======================================================================================================================


@client.command(aliases=['ui'])
async def userinfo(ctx, member: discord.Member):
    color = member.top_role.color
    embed = discord.Embed(title=f"Informação de {member.name}", color=color)
    embed.add_field(name="Criado em", value=f"{member.created_at.strftime('%d/%m/%Y  %H:%M:%S')}")
    embed.add_field(name="Entrou em", value=f"{member.joined_at.strftime('%d/%m/%Y  %H:%M:%S')}")
    embed.add_field(name="Apelido", value=f"{member.nick}")
    embed.add_field(name="Cargo", value=f"{member.top_role}")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_footer(text="Isso é apenas uma moldura")

    await ctx.reply(embed=embed)





client.run("token")
