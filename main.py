import discord


client = discord.Client()
open_mc = ["will server open", "will the server open", "going to open", "open date", "opening date",
           "have a opening date", "ur server open"]
bellaid = ["<@!731653018629439579"]
frostid = ["<@!543603797956755456>"]
myid = ["<@!367015321380454402>"]
berryid = ["<@!781180195670720543"]
disid = ["<@!395837742715502604"]
wild_help = ["wild help", "wild i broke it"]
youtube = ["is the youtube", "is the yt", "find the youtube", "find the yt", "there a youtube", "there a yt",
           "have a youtube", "have a yt", "have a YT", "ur youtube", "ur yt", "ur YT", "whats the yt", "whats the YT",
           "whats the youtube", "what's the YT", "what's the yt", "what's the youtube"]
instagram = ["is the insta", "find the insta", "there a insta", "have a insta", "ur insta"]
twitch = ["is the twitch", "find the twitch", "there a twitch", "have a twitch", "ur twitch"]
patreon = ["is the patreon", "find the patreon", "there a patreon", "have a patreon", "i donate", "I donate",
           "wants to donate", "want's to donate", "ur patreon"]
staff_app = ["join staff", "the staff app", "there a staff app", "have a staff app", "ur staff app"]
beta_app = ["join beta", "the beta app", "the beta testing app", "there a beta app", "there a beta testing app",
            "have a beta app", "have a beta testing app", "be a mod", "apply for staff", "be a staff", "be staff",
            "ur staff"]
beta_open = ["does beta testing open", "is beta testing", "is beta", "going to be beta", "have a beta date", "your beta"]
eqpd_help = ["help", "helps"]
rules = ["rule", "rules"]

@client.event
async def on_ready():
    print('Bot {0.user} has started up!'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('~'):
        if any(word.capitalize() in msg for word in eqpd_help):
#help command
            embed = discord.Embed(title="Commands", description="*all discord bot commands*", color=0x00e1ff)
            embed.add_field(name="~Rules", value="Displays all server rules", inline=False)
            embed.add_field(name="~Help", value="Displays this ", inline=False)
            await message.channel.send(embed=embed)
        if any(word.lower() in msg for word in eqpd_help):
            embed = discord.Embed(title="Commands", description="*all discord bot commands*", color=0x00e1ff)
            embed.add_field(name="~Rules", value="Displays all server rules", inline=False)
            embed.add_field(name="~Help", value="Displays this ", inline=False)
            await message.channel.send(embed=embed)
        if any(word.upper() in msg for word in eqpd_help):
            embed = discord.Embed(title="Commands", description="*all discord bot commands*", color=0x00e1ff)
            embed.add_field(name="~Rules", value="Displays all server rules", inline=False)
            embed.add_field(name="~Help", value="Displays this ", inline=False)
            await message.channel.send(embed=embed)
#Rules Command
        if any(word.capitalize() in msg for word in rules):
            embed = discord.Embed(title="Discord Rules", description="*This servers rules*", color=0x00e1ff)
            embed.add_field(name="1) Keep all chat, media and videos in their correct channels.", value="🌸", inline=False)
            embed.add_field(name="2) Do not discuss sensitive topics that could be triggering to others.", value="🌸", inline=False)
            embed.add_field(name="3) Do not talk about other servers or post links to other servers.", value="🌸", inline=False)
            embed.add_field(name="4) Please be respectful of all staff and players.", value="🌸", inline=False)
            embed.add_field(name="5) We don’t not allow any unapproved alternate accounts onto our discord. If we find you have an alt, it will be banned from our discord.", value="*Please talk to an owner for certain situations!*", inline=False)
            embed.add_field(name="6) Cussing is allowed try to keep it to a minimum.", value="🌸", inline=False)
            embed.add_field(name="7) Harassment of any kind will not be tolerated.", value="🌸", inline=False)
            embed.add_field(name="8) Only post Eqpd related content in our advertisement channels.", value="🌸", inline=False)
            embed.add_field(name="9) Staff can mute, kick or ban you at anytime if they feel you have violated our rules.", value="🌸", inline=False)
            embed.add_field(name="10) We have the right to deny you access to the discord server if we feel that you are suspicious or here to cause problems.", value=":🌸", inline=False)
            embed.add_field(name="11) All nicknames must be appropriate and not contain offensive terms, slang, etc.", value="🌸", inline=False)
            embed.add_field(name="12) Everyone in our discord, MUST follow discord TOS.", value="🌸", inline=False)
            embed.add_field(name="13) All accounts must be at least a month old in order to gain full access to our server.", value="🌸", inline=False)
            await message.channel.send(embed=embed)
        if any(word.lower() in msg for word in rules):
            embed = discord.Embed(title="Discord Rules", description="*This servers rules*", color=0x00e1ff)
            embed.add_field(name="1) Keep all chat, media and videos in their correct channels.", value="🌸", inline=False)
            embed.add_field(name="2) Do not discuss sensitive topics that could be triggering to others.", value="🌸", inline=False)
            embed.add_field(name="3) Do not talk about other servers or post links to other servers.", value="🌸", inline=False)
            embed.add_field(name="4) Please be respectful of all staff and players.", value="🌸", inline=False)
            embed.add_field(name="5) We don’t not allow any unapproved alternate accounts onto our discord. If we find you have an alt, it will be banned from our discord.", value="*Please talk to an owner for certain situations!*", inline=False)
            embed.add_field(name="6) Cussing is allowed try to keep it to a minimum.", value="🌸", inline=False)
            embed.add_field(name="7) Harassment of any kind will not be tolerated.", value="🌸", inline=False)
            embed.add_field(name="8) Only post Eqpd related content in our advertisement channels.", value="🌸", inline=False)
            embed.add_field(name="9) Staff can mute, kick or ban you at anytime if they feel you have violated our rules.", value="🌸", inline=False)
            embed.add_field(name="10) We have the right to deny you access to the discord server if we feel that you are suspicious or here to cause problems.", value="🌸", inline=False)
            embed.add_field(name="11) All nicknames must be appropriate and not contain offensive terms, slang, etc.", value="🌸", inline=False)
            embed.add_field(name="12) Everyone in our discord, MUST follow discord TOS.", value="🌸", inline=False)
            embed.add_field(name="13) All accounts must be at least a month old in order to gain full access to our server.", value="🌸", inline=False)
            await message.channel.send(embed=embed)
        if any(word.upper() in msg for word in rules):
            embed = discord.Embed(title="Discord Rules", description="*This servers rules*", color=0x00e1ff)
            embed.add_field(name="1) Keep all chat, media and videos in their correct channels.", value="🌸", inline=False)
            embed.add_field(name="2) Do not discuss sensitive topics that could be triggering to others.", value="🌸", inline=False)
            embed.add_field(name="3) Do not talk about other servers or post links to other servers.", value="🌸", inline=False)
            embed.add_field(name="4) Please be respectful of all staff and players.", value="🌸", inline=False)
            embed.add_field(name="5) We don’t not allow any unapproved alternate accounts onto our discord. If we find you have an alt, it will be banned from our discord.", value="*Please talk to an owner for certain situations!*", inline=False)
            embed.add_field(name="6) Cussing is allowed try to keep it to a minimum.", value="🌸", inline=False)
            embed.add_field(name="7) Harassment of any kind will not be tolerated.", value="🌸", inline=False)
            embed.add_field(name="8) Only post Eqpd related content in our advertisement channels.", value="🌸", inline=False)
            embed.add_field(name="9) Staff can mute, kick or ban you at anytime if they feel you have violated our rules.", value="🌸", inline=False)
            embed.add_field(name="10) We have the right to deny you access to the discord server if we feel that you are suspicious or here to cause problems.", value="🌸", inline=False)
            embed.add_field(name="11) All nicknames must be appropriate and not contain offensive terms, slang, etc.", value="🌸", inline=False)
            embed.add_field(name="12) Everyone in our discord, MUST follow discord TOS.", value="🌸", inline=False)
            embed.add_field(name="13) All accounts must be at least a month old in order to gain full access to our server.", value="🌸", inline=False)
            await message.channel.send(embed=embed)
# auto question reply
    if any(word in msg for word in myid):
        await message.channel.send('NO GO AWAY!')
    if any(word in msg for word in frostid):
        await message.channel.send('Yes love?')
    if any(word in msg for word in disid):
        await message.channel.send('Please leave all business inquiries in D1ssrupts DMs. Thanks.')
    if any(word in msg for word in berryid):
        await message.channel.send('I’m either napping or crying, leaf me alone!')
    if any(word in msg for word in bellaid):
        await message.channel.send('I’m busy simping over Josh!')
    if any(word.capitalize() in msg for word in open_mc):
        await message.channel.send('We currently do not have a opening date, but hope to be opening for beta very soon!')
    if any(word.upper() in msg for word in open_mc):
        await message.channel.send('We currently do not have a opening date, but hope to be opening for beta very soon!')
    if any(word.lower() in msg for word in open_mc):
        await message.channel.send('We currently do not have a opening date, but hope to be opening for beta very soon!')
    if any(word.capitalize() in msg for word in wild_help):
        await message.channel.send('No go away!')
    if any(word.upper() in msg for word in wild_help):
        await message.channel.send('No go away!')
    if any(word.lower() in msg for word in wild_help):
        await message.channel.send('No go away!')
    if any(word.capitalize() in msg for word in youtube):
        await message.channel.send('Our youtube is: https://www.youtube.com/channel/UCz_cNsLl1b6nXNF5f46EH9A')
    if any(word.upper() in msg for word in youtube):
        await message.channel.send('Our youtube is: https://www.youtube.com/channel/UCz_cNsLl1b6nXNF5f46EH9A')
    if any(word.lower() in msg for word in youtube):
        await message.channel.send('Our youtube is: https://www.youtube.com/channel/UCz_cNsLl1b6nXNF5f46EH9A')
    if any(word.capitalize() in msg for word in instagram):
        await message.channel.send('Our instagram is: https://instagram.com/eqpd.official?igshid=1adhbou9kh90n')
    if any(word.upper() in msg for word in instagram):
        await message.channel.send('Our instagram is: https://instagram.com/eqpd.official?igshid=1adhbou9kh90n')
    if any(word.lower() in msg for word in instagram):
        await message.channel.send('Our instagram is: https://instagram.com/eqpd.official?igshid=1adhbou9kh90n')
    if any(word.capitalize() in msg for word in patreon):
        await message.channel.send('Our patreon is: https://www.patreon.com/EquestrianParadise')
    if any(word.upper() in msg for word in patreon):
        await message.channel.send('Our patreon is: https://www.patreon.com/EquestrianParadise')
    if any(word.lower() in msg for word in patreon):
        await message.channel.send('Our patreon is: https://www.patreon.com/EquestrianParadise')
    if any(word.capitalize() in msg for word in twitch):
        await message.channel.send('Our twitch is: https://www.twitch.tv/eqpdmc')
    if any(word.upper() in msg for word in twitch):
        await message.channel.send('Our twitch is: https://www.twitch.tv/eqpdmc')
    if any(word.lower() in msg for word in twitch):
        await message.channel.send('Our twitch is: https://www.twitch.tv/eqpdmc')
    if any(word.capitalize() in msg for word in staff_app):
        await message.channel.send('Our staff app is: https://docs.google.com/forms/d/1eUrhEJF6_IZdht3McWrwcHcguLZJrILl-aVIj4lnH1o/edit')
    if any(word.upper() in msg for word in staff_app):
        await message.channel.send('Our staff app is: https://docs.google.com/forms/d/1eUrhEJF6_IZdht3McWrwcHcguLZJrILl-aVIj4lnH1o/edit')
    if any(word.lower() in msg for word in staff_app):
        await message.channel.send('Our staff app is: https://docs.google.com/forms/d/1eUrhEJF6_IZdht3McWrwcHcguLZJrILl-aVIj4lnH1o/edit')
    if any(word.capitalize() in msg for word in beta_app):
        await message.channel.send('Our beta testing app is: https://docs.google.com/forms/d/e/1FAIpQLSfut0ZggRzaPLBTXaDDzc9s9Kr5oxQ1f9VajUuM4XSKezPUcA/viewform')
    if any(word.upper() in msg for word in beta_app):
        await message.channel.send('Our beta testing app is: https://docs.google.com/forms/d/e/1FAIpQLSfut0ZggRzaPLBTXaDDzc9s9Kr5oxQ1f9VajUuM4XSKezPUcA/viewform')
    if any(word.lower() in msg for word in beta_app):
        await message.channel.send('Our beta testing app is: https://docs.google.com/forms/d/e/1FAIpQLSfut0ZggRzaPLBTXaDDzc9s9Kr5oxQ1f9VajUuM4XSKezPUcA/viewform')
    if any(word.capitalize() in msg for word in beta_open):
        await message.channel.send('We currently do not have a opening date for beta, but if you want to apply for beta please apply here: https://docs.google.com/forms/d/e/1FAIpQLSfut0ZggRzaPLBTXaDDzc9s9Kr5oxQ1f9VajUuM4XSKezPUcA/viewform')
    if any(word.upper() in msg for word in beta_open):
        await message.channel.send('We currently do not have a opening date for beta, but if you want to apply for beta please apply here: https://docs.google.com/forms/d/e/1FAIpQLSfut0ZggRzaPLBTXaDDzc9s9Kr5oxQ1f9VajUuM4XSKezPUcA/viewform')
    if any(word.lower() in msg for word in beta_open):
        await message.channel.send('We currently do not have a opening date for beta, but if you want to apply for beta please apply here: https://docs.google.com/forms/d/e/1FAIpQLSfut0ZggRzaPLBTXaDDzc9s9Kr5oxQ1f9VajUuM4XSKezPUcA/viewform')
client.run('ODA5NDU5NTcyODMyOTkzMzcw.YCVZ-Q.MMdMER_qRqC-u0abvTxiLufAZfs')
