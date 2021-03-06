import datetime

import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, MissingRequiredArgument
from discord_components import Button, ButtonStyle
from cogs.core.config.config_trigger import get_trigger_list, add_trigger
from cogs.core.functions.functions import log, get_author, get_prefix_string, get_botc, get_colour


class trigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def trigger(self, ctx):
        if ctx.invoked_subcommand is None:
            ...

    @trigger.command()
    @commands.has_permissions(administrator=True)
    async def add(self, ctx):
        time = datetime.datetime.now()
        user = ctx.author.name
        name = ctx.channel.name
        msg2 = ctx.message
        mention = ctx.author.mention
        botchannel = get_botc(message=ctx.message)
        if name == botchannel or botchannel == 'None':
            cmsg = ctx.message.content[15:]
            word = cmsg.split(" : ")[0]
            msg = cmsg.split(" : ")[1]
            if trigger in get_trigger_list(guildid=ctx.guild.id):
                embed = discord.Embed(title=f"**Fehler**", description=f"Der Trigger {word} existiert bereits!"
                                                                       f"Wenn du ihn verändern möchtest, nutze "
                                                                       f"```trigger edit {word}``` oder klicke auf "
                                                                       f"den unteren Knopf. Wenn du ihn komplett "
                                                                       f"entfernen möchtest, "
                                                                       f"nutze ```trigger remove {word}```",
                                      colour=get_colour(ctx.message))
                embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' +
                                      get_prefix_string(message=ctx.message),
                                 icon_url='https://media.discordapp.net/attachments/645276319311200286'
                                          '/803322491480178739/winging-easy.png?width=676&height=676')
                await ctx.send(embed=embed)  # todo add components
                log(f'{time}: Der Spieler {user} hat versucht den Befehl {get_prefix_string(ctx.message)}'
                    f'trigger add zu benutzen und damit den Trigger {word} hinzuzufügen, konnte'
                    f' es aber nicht da dieser bereits existiert hat!', id=ctx.guild.id)
                return
            add_trigger(guildid=ctx.guild.id, trigger=word, msg=msg)
            embed = discord.Embed(title=f"**Trigger Add**",
                                  description=f"Der Bot reagiert nun auf ```{word}``` mit der Nachricht:"
                                              f"```{msg}```",
                                  colour=get_colour(ctx.message))
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/645276319311200286/803322491480178739/winging-easy'
                    '.png?width=676&height=676')
            embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' +
                                  get_prefix_string(message=ctx.message),
                             icon_url='https://media.discordapp.net/attachments/645276319311200286'
                                      '/803322491480178739/winging-easy.png?width=676&height=676')
            await ctx.send(embed=embed)
            log(f'{time}: Der Spieler {user} hat den Befehl {get_prefix_string(ctx.message)}'
                f'trigger add benutzt und damit den Trigger {word} hinzugefügt.!', id=ctx.guild.id)

        else:
            log(input=f'{time}: Der Spieler {user} hat probiert den Befehl {get_prefix_string(ctx.message)}'
                      f'trigger add im Channel #{name} zu benutzen!', id=ctx.guild.id)
            await ctx.send(f'{mention}, dieser Befehl kann nur im Kanal #{botchannel} genutzt werden.',
                           delete_after=3)
            await msg2.delete()

    @add.error
    async def handle_error(self, ctx, error):
        time = datetime.datetime.now()
        user = ctx.author.name
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title='**Fehler**', colour=get_colour(ctx.message))
            embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' + get_prefix_string(
                message=ctx.message),
                             icon_url='https://media.discordapp.net/attachments/645276319311200286/803322491480178739'
                                      '/winging-easy.png?width=676&height=676')
            embed.add_field(name='‎',
                            value='Dir fehlt folgende Berrechtigung um den Befehl auszuführen: '
                                  '```administrator```',
                            inline=False)
            await ctx.send(embed=embed)
            log(input=str(time) + ': Der Spieler ' + str(
                user) + ' hatte nicht die nötigen Berrechtigungen um ' +
                      get_prefix_string(ctx.message) + 'trigger add zu nutzen.', id=ctx.guild.id)
        if isinstance(error, MissingRequiredArgument):
            embed = discord.Embed(title='**Fehler**', colour=get_colour(ctx.message))
            embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' + get_prefix_string(
                message=ctx.message), icon_url='https://media.discordapp.net/attachments/645276319311200286'
                                               '/803322491480178739/winging-easy.png?width=676&height=676')
            embed.add_field(name='‎',
                            value='Du hast nicht alle erforderlichen Argumente angegeben, Nutzung: ```' +
                                  get_prefix_string(ctx.message) + 'trigger add <Trigger Name : Antwort Nachricht>```',
                            inline=False)
            await ctx.send(embed=embed)
            log(input=str(time) + ': Der Spieler ' + str(
                user) + ' hat nicht alle erforderlichen Argumente beim Befehl ' +
                      get_prefix_string(ctx.message) + 'trigger add eingegeben.', id=ctx.guild.id)

    @trigger.command()
    @commands.has_permissions(administrator=True)
    async def remove(self, ctx):
        time = datetime.datetime.now()
        user = ctx.author.name
        name = ctx.channel.name
        msg2 = ctx.message
        mention = ctx.author.mention
        botchannel = get_botc(message=ctx.message)
        if name == botchannel or botchannel == 'None':
            cmsg = ctx.message.content[15:]
            word = cmsg.split(" : ")[0]
            msg = cmsg.split(" : ")[1]
            if trigger in get_trigger_list(guildid=ctx.guild.id):
                embed = discord.Embed(title=f"**Fehler**", description=f"Der Trigger {word} existiert bereits!"
                                                                       f"Wenn du ihn verändern möchtest, nutze "
                                                                       f"```trigger edit {word}``` oder klicke auf "
                                                                       f"den unteren Knopf. Wenn du ihn komplett "
                                                                       f"entfernen möchtest, "
                                                                       f"nutze ```trigger remove {word}```",
                                      colour=get_colour(ctx.message))
                embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' +
                                      get_prefix_string(message=ctx.message),
                                 icon_url='https://media.discordapp.net/attachments/645276319311200286'
                                          '/803322491480178739/winging-easy.png?width=676&height=676')
                await ctx.send(embed=embed)  # todo add components
                log(f'{time}: Der Spieler {user} hat versucht den Befehl {get_prefix_string(ctx.message)}'
                    f'trigger add zu benutzen und damit den Trigger {word} hinzuzufügen, konnte'
                    f' es aber nicht da dieser bereits existiert hat!', id=ctx.guild.id)
                return
            add_trigger(guildid=ctx.guild.id, trigger=word, msg=msg)
            embed = discord.Embed(title=f"**Trigger Add**",
                                  description=f"Der Bot reagiert nun auf ```{word}``` mit der Nachricht:"
                                              f"```{msg}```",
                                  colour=get_colour(ctx.message))
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/645276319311200286/803322491480178739/winging-easy'
                    '.png?width=676&height=676')
            embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' +
                                  get_prefix_string(message=ctx.message),
                             icon_url='https://media.discordapp.net/attachments/645276319311200286'
                                      '/803322491480178739/winging-easy.png?width=676&height=676')
            await ctx.send(embed=embed)
            log(f'{time}: Der Spieler {user} hat den Befehl {get_prefix_string(ctx.message)}'
                f'trigger add benutzt und damit den Trigger {word} hinzugefügt.!', id=ctx.guild.id)

        else:
            log(input=f'{time}: Der Spieler {user} hat probiert den Befehl {get_prefix_string(ctx.message)}'
                      f'trigger add im Channel #{name} zu benutzen!', id=ctx.guild.id)
            await ctx.send(f'{mention}, dieser Befehl kann nur im Kanal #{botchannel} genutzt werden.',
                           delete_after=3)
            await msg2.delete()

    @add.error
    async def handle_error(self, ctx, error):
        time = datetime.datetime.now()
        user = ctx.author.name
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title='**Fehler**', colour=get_colour(ctx.message))
            embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' + get_prefix_string(
                message=ctx.message),
                             icon_url='https://media.discordapp.net/attachments/645276319311200286/803322491480178739'
                                      '/winging-easy.png?width=676&height=676')
            embed.add_field(name='‎',
                            value='Dir fehlt folgende Berrechtigung um den Befehl auszuführen: '
                                  '```administrator```',
                            inline=False)
            await ctx.send(embed=embed)
            log(input=str(time) + ': Der Spieler ' + str(
                user) + ' hatte nicht die nötigen Berrechtigungen um ' +
                      get_prefix_string(ctx.message) + 'trigger add zu nutzen.', id=ctx.guild.id)
        if isinstance(error, MissingRequiredArgument):
            embed = discord.Embed(title='**Fehler**', colour=get_colour(ctx.message))
            embed.set_footer(text='for ' + str(user) + ' | by ' + str(get_author()) + ' | Prefix ' + get_prefix_string(
                message=ctx.message), icon_url='https://media.discordapp.net/attachments/645276319311200286'
                                               '/803322491480178739/winging-easy.png?width=676&height=676')
            embed.add_field(name='‎',
                            value='Du hast nicht alle erforderlichen Argumente angegeben, Nutzung: ```' +
                                  get_prefix_string(ctx.message) + 'trigger add <Trigger Name : Antwort Nachricht>```',
                            inline=False)
            await ctx.send(embed=embed)
            log(input=str(time) + ': Der Spieler ' + str(
                user) + ' hat nicht alle erforderlichen Argumente beim Befehl ' +
                      get_prefix_string(ctx.message) + 'trigger add eingegeben.', id=ctx.guild.id)


########################################################################################################################


def setup(bot):
    bot.add_cog(trigger(bot))
