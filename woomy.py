#!/usr/bin/python3
import discord
import asyncio
import OpenSSL
import base64
import binascii
import hashlib
import struct
import time
import subprocess
import sys
import random
import json
import urllib.request, urllib.parse
import html
import platform
import time
import requests
from lxml import html
from discord.ext.commands import Bot
#config?
settings = json.load(open("settings.json"))
secret = settings["secret"]; normie = settings["n"]; fuckeric = settings["fe"];
#/config
main = Bot(command_prefix=("woomy ", "Woomy ", "WOOMY ", "\U0001f991 "))

if normie:
	@main.async_event
	async def on_ready():
		return await main.change_presence(game=discord.Game(name="'woomy how2use', or for music: ';;woomy help'"))
	@main.command()
	async def how2use(*args):
		return await main.say("""
the command prefix is `woomy` so use that before everything
`woomy help` will list all commands however none of them are commented so you'll have to try them if you want to know what they do
if a command requires args then it'll tell you
(also `:squid:` will work in place of `woomy` shhh)""")
	main.remove_command("help")
	@main.command()
	async def help(*args):
		return await main.say("""
```
"Util":
ping, rijndael, speak, SystemExit, nnpasswordhash, python3, uname, os, lsblk, invite, ponder, mii, splatoon1rotation, splatoon2rotation, location, miiverse
SFW:
hot, canada, hi, openverse, length, japanese, arian, sex, php, birthday, blacklist, cat, anime, girl, secure, getjob, bully, linux, phpsponsor, hitler
Not so SFW:
ass, fuckofferic, rant, sethfuck, eric, suck, tittyfuck, boobsize, nut, fuckseth, kai, respect, eek, loli, 69, succme, neko
```
**Side-note**: `openverse, arian, sex, fuckofferic, rant, sethfuck, eric, fuckseth, kai, eek` and `respect` are only meant to be used in one guild, or rather they're only meant for one, you sure can run them if you want, but they probably won't be nice.
""")

# gets a username from either if someone says it plainly or @s someone
@main.async_event
async def user_from_at(ctx, a, all=True, plain=True):
	app = await main.application_info()
	if a.startswith("<@"):
		try:
			if a.startswith("<@!"):
				user = ctx.message.server.get_member(a[3:-1])
			else:
				user = ctx.message.server.get_member(a[2:-1])
			if user.id == app.id:
				await main.send_message(ctx.message.channel, "um")
				return 69
			if all:
				return user
			else:
				return user.name
		except Exception as e:
			return False
	elif "@everyone" in a or "@here" in a:
		await main.send_message(ctx.message.channel, "fuck off")
		return 69
	else:
		if plain:
			return a
		else:
			return False
@main.async_event
async def erickek(ctx):
	hr = int(time.strftime("%H"))
	app = await main.application_info()
	if not fuckeric and not (hr in range(1,5)) and not ctx.message.author.id == app.owner.id:
		await main.say("sorry")
		return 69
	else:
		return None

#first command made
@main.command()
async def hot(*args):
	return await main.say("damn right")
@main.command()
async def canada(*args):
	return await main.say("O CANADA```\n  _\n (_)\n  |_____________________________________\n  |&&&&&&                         &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&          .\\^/.          &&&&&&|\n  |&&&&&&        . |   | .        &&&&&&|\n  |&&&&&&        |\\|   |/|        &&&&&&|\n  |&&&&&&     .--'       '--.     &&&&&&|\n  |&&&&&&      \\           /      &&&&&&|\n  |&&&&&&       >         <       &&&&&&|\n  |&&&&&&      '~|/~~|~~\\|~'      &&&&&&|\n  |&&&&&&            |            &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&_________________________&&&&&&|\n  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n```")
@main.command()
async def ass(*args):
	return await main.say("todo put ass here\nhttps://s18.postimg.org/4np6ebpcp/Wii_U_screenshot_TV_01769.jpg\nhttps://s1.postimg.org/p5vtn7xu7/Wii_U_screenshot_TV_01769.jpg\nalso hot squid vag\nhttps://s2.postimg.org/bmyqgly5l/Wii_U_screenshot_TV_01769.jpg\nhttps://s12.postimg.org/4rb9o7nyl/Wii_U_screenshot_TV_01769.jpg")
@main.command()
async def hi(*args):
	return await main.say("heyyy")
# at the end of nut, after SystemExit
@main.command(pass_context=True)
async def ping(ctx, *args):
	if args:
		return await main.say("that's not how it works")
	now = time.time()
	msg = await main.say("pingas")
	return await main.edit_message(msg, "it took `" + str(time.time() - now) + "` seconds to (asynchronously) send a message to `" + ctx.message.server.name + "`")
@main.command()
async def rijndael(*args):
	return await main.say(binascii.hexlify(OpenSSL.rand.bytes(150)).decode())
@main.command()
async def speak(*args):
	return await main.say("".join([random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(12)]))
# at the end of nut, replaces mysql and python, rest in peace
@main.command(pass_context=True)
async def SystemExit(ctx, *args):
	app = await main.application_info()
	if ctx.message.author.id != app.owner.id:
		return await main.say("you're not the boss of me :angry: <@"+ctx.message.author.id+">")
	else:
		await main.say("bye :wave: ")
		main.loop.run_until_complete(main.logout())
		main.loop.close()
		sys.exit(0)
@main.command()
async def nnpasswordhash(*a):
	if not a:
		return await main.say("but only for the _realest of real_ haxx0rz ```\nnnpasswordhash [pid] [passwd]```")
	else:
		if not a[1]:
			return await main.say("you forgot the password idiot are you sure you know what this is even for")
		else:
			a1 = int(round(time.time() * 1000))
			try:
				h = hashlib.sha256(struct.pack("<I", int(a[0])) + b"\x02\x65\x43\x46" + a[1].encode("ascii")).hexdigest()
			except Exception as e:
				return await main.say("it didn't work :(")
			t = str(int(round(time.time() * 1000)) - a1)
			if t == "0":
					t += " :sunglasses: "
			return await main.say("Did it in " + t + " ms\n```\n" + h + "\n```")
@main.command(pass_context=True)
async def openverse(ctx, *all):
	if not all:
		return await main.say("```\nopenverse [text]\n```")
	else:
		str = " ".join(all);
		if len(str) > 250:
			return await main.say("2 long asshole")
		await main.send_typing(ctx.message.channel)
		try:
			out = subprocess.Popen(["php", "open-logo-pyc.php", str], stdout=subprocess.PIPE).stdout.read()
		except Exception as e:
			return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
		return await main.send_file(ctx.message.channel, "open-py.png")
@main.command()
async def invite(*args):
	app = await main.application_info()
	if not normie:
		return await main.say("invite deez nuts hah goteem")
	else:
		return await main.say("put it on your christmas tree\n" + discord.utils.oauth_url(app.id))
@main.command()
async def ponder(*q):
	if not q:
		return await main.say("```\nponder [question]\n```")
	# prevent people from doing bad things :(
	bad = [
	'die',
	'death',
	'kms',
	'kill',
	]
	for badbad in bad:
		if badbad in q:
			return await main.say("no don't please\ni care :sparkling_heart:")
	if bool(random.getrandbits(1)):
		return await main.say("yes")
	else:
		return await main.say("nah")
@main.command()
async def python3(*args):
	return await main.say(sys.version)
@main.command()
async def uname(*args):
	return await main.say(subprocess.getoutput("uname -a"))
# at the end of getjob
@main.command()
async def os(*args):	
	return await main.say("```\n" + platform.platform() + "\n```")
@main.command()
async def lsblk(*args):
	command = subprocess.getoutput("lsblk")
	return await main.say("```\n" + command + "```")
@main.command()
async def length(*lol):
	if not lol:
		return await main.say("```\nlength [object]\n```")
	if lol[0] == 'arian':
		return await main.say("actually arian is `6 ft` tall as of now")
	else:
		if 'eric' in lol[0]:
			thing = 0
		else:
			thing = int(random.getrandbits(5))
		return await main.say(str(thing) + " cm")
@main.command(pass_context=True)
async def fuckofferic(ctx, *args):
	#return await main.say("Not today.")
	suckass = await erickek(ctx)
	if not suckass == 69:
		faggot = "151466174683545600"
		await main.say("goodbye eric d faggot :wave: <@"+faggot+">")
		try:
			await main.kick(ctx.message.server.get_member(faggot))
		except Exception as e:
			await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```did Eric leave? do I not have permissions? IDK you decide")
		return 0
@main.command()
async def rant(*args):
	with open("mostrants.json") as rants:
		rant = random.choice(json.load(rants))
	return await main.say(rant)
@main.command(pass_context=True)
async def sethfuck(ctx, *a):
	if not a:
		with open("seth.json") as cumd:
			person = random.choice(json.load(cumd))
	else:
		person = await user_from_at(ctx, " ".join(a), False)
		if not person:
			return await main.say("fuck")
		elif person == 69:
			return 0
	return await main.say("```\nseth 10 year old sperm ---) " + person + "\n```")
@main.command(pass_context=True)
async def eric(ctx, *args):
	suckass = await erickek(ctx)
	if not suckass == 69:
		with open("eric.json") as mistaked:
			mistakes = json.load(mistaked)
		return await main.say(random.choice(mistakes))
@main.command()
async def japanese(*a):
	katakana = ["ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","ガ","ギ","グ","ゲ","ゴ","サ","シ","ス","セ","ソ","ザ","ジ","ズ","ゼ","ゾ","タ","チ","ツ","テ","ト","ダ","ヂ","ヅ","デ","ド","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","バ","ビ","ブ","ベ","ボ","パ","ピ","プ","ペ","ポ","マ","ミ","ム","メ","モ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン"]
	if a:
		nval = [str(ord(char) - 96) for char in " ".join(a).lower()]
		japanese = ""
		for num in nval:
			if int(num) == -64:
				japanese += " "
			else:
				japanese += katakana[int(num)]
	else:
		japanese = "".join([random.choice("".join(katakana)) for i in range(6)])
	return await main.say(japanese)
@main.command()
async def arian(*args):
	app = await main.application_info()
	return await main.say("that's me <@"+app.owner.id+"> https://ariankordi.net/\nhttps://github.com/ariankordi/inklingbot")
@main.command()
async def gender(*args):
	return await main.say("no, it's `sex`, not \"gender\"")
@main.command(pass_context=True)
async def sex(ctx, *u):
	app = await main.application_info()
	if bool(random.getrandbits(1)):
		only2genders = "♀"
	else:
		only2genders = "♂"
	if not u:
		return await main.say("you are " + only2genders)
	person = await user_from_at(ctx, u[0], False, True)
	if not person:
		return await main.say("who")
	elif person == 69:
			return 0
	else:
		return await main.say(person + " is " + only2genders)
@main.command(pass_context=True)
async def php(ctx, *txt):
	#return await main.say("it sucks")
	if not txt:
		return await main.say("```\nphp [text]\n```")
	tex = " ".join(txt)
	if len(tex) > 250:
		return await main.say("2 long asshole")
	await main.send_typing(ctx.message.channel)
	try:
		out = subprocess.Popen(["php", "php-logo-pyc.php", tex], stdout=subprocess.PIPE).stdout.read()
	except Exception as e:
		return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
	return await main.send_file(ctx.message.channel, "php-py.png")
@main.command(pass_context=True)
async def mii(ctx, *n):
	if not n:
		return await main.say("```\nmii [nnid]\n```")
	if len(n[0]) < 6:
		return await main.say("too short like your dick <@" + ctx.message.author.id + ">")
	if len(n[0]) > 16:
		return await main.say("what how do you have an nnid that's more than 16 characters")
	if n[0].lower() == 'reaidonaldtrump':
		return await main.say("go fuck yourself tutikaz")
	msg = await main.send_message(ctx.message.channel, "doing it")
	try:
		out = subprocess.Popen(["php", "nnmii.php", n[0]], stdout=subprocess.PIPE).stdout.read().decode()
	except Exception as e:
		return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
	if out == 'n':
		return await main.say("there was nothing there")
	await main.edit_message(msg, out)
@main.command(pass_context=True)
async def birthday(ctx, *nam):
	if not nam:
		return await main.say("```\nbirthday [name] but only if it's their birthday```\n")
	nam = " ".join(nam)
	person = await user_from_at(ctx, nam, True, False)
	if not person:
		person = nam
	elif person == 69:
			return 0
	else:
		person = person.name + " <@"+person.id+">"
	return await main.say(":tada::tada::tada::tada::tada: HAPPY BIRTHDAY " + person.upper() + " :tada::tada::tada::tada::tada:")
@main.command(pass_context=True)
async def blacklist(ctx, *nig):
	if not nig:
		person = ctx.message.author
	else:
		person = await user_from_at(ctx, nig[0])
		if not person:
			person = ctx.message.author
		elif person == 69:
			return 0
	return await main.say("<@"+ person.id +">: :hammer: ***BLACKLISTED*** :hammer: for **24:00:00**")
@main.command(pass_context=True)
async def splatoon1rotation(ctx, *args):
	msg1 = await main.say("getting stats for a dead game (Splatoon), give me a moment")
	try:
		srv = urllib.request.urlopen("https://splatoon.ink/schedule")
		stages = json.loads(srv.read().decode())
		message = "Current Turf War stages:\n```\n{0}\n{1}\n```\nCurrent {2} stages:\n```\n{3}\n{4}\n```".format(
stages['schedule'][0]['modes'][0]['maps'][0]['nameEN'], stages['schedule'][0]['modes'][0]['maps'][1]['nameEN'],
stages['schedule'][0]['modes'][1]['rulesEN'],
stages['schedule'][0]['modes'][1]['maps'][0]['nameEN'], stages['schedule'][0]['modes'][1]['maps'][1]['nameEN'],
)
		await main.edit_message(msg1, message)
	except Exception as e:
		await main.say("didn't work :frowning2: \n```" + str(e) + "\n```")
@main.command(pass_context=True)
async def splatoon2rotation(ctx, *args):
	msg1 = await main.say("hacking nintendo switch :(, please wait")
	try:
		srv = urllib.request.urlopen("https://splatoon.ink/schedule2")
		stages = json.loads(srv.read().decode())
		message = "Current {0} stages:\n```\n{1}\n{2}\n```\nCurrent {3} stages:\n```\n{4}\n{5}\n```".format(stages['modes']['regular'][0]['rule']['name'],
		stages['modes']['regular'][0]['maps'][0],
		stages['modes']['regular'][0]['maps'][1],
		stages['modes']['gachi'][0]['rule']['name'],
		stages['modes']['gachi'][0]['maps'][0],
		stages['modes']['gachi'][0]['maps'][1],
		)
		await main.edit_message(msg1, message)
	except Exception as e:
		await main.say("didn't work :frowning2: \n```" + str(e) + "\n```")
@main.command(pass_context=True)
async def suck(ctx, *per):
	if not per:
		return await main.say("```\nsuck [@ person]\n```")
	person = await user_from_at(ctx, per[0], True, False)
	if not person:
		return await main.say("you're supposed to @ someone idiot")
	elif person == 69:
			return 0
	return await main.say(ctx.message.author.name + " has sucked your dick <@"+person.id+">")
# At end of location actually
@main.command(pass_context=True)
async def tittyfuck(ctx, *unlucky):
	app = await main.application_info()
	if not unlucky:
		return await main.say("because 9 people wanted this command\n```\ntittyfuck [victim]\n```")
	person = await user_from_at(ctx, unlucky[0], True, False)
	if not person:
		return await main.say("how are you supposed to tittyfuck if you don't @ who you want to fucktitty")
	elif person == 69:
			return 0
	return await main.say(ctx.message.author.name + " has fucked your tits <@"+person.id+">")
@main.command(pass_context=True)
async def cat(ctx, *args):
	msg = await main.say("nya")
	try:
		srv = urllib.request.urlopen("http://random.cat/meow").read().decode()
		img = json.loads(srv)["file"]
	except Exception as e:
		return await main.say("aw man\n```"+ str(e) +"```")
	return await main.edit_message(msg, "nya\n" + img)
@main.command()
async def location(*args):
	loc = urllib.request.urlopen("https://ipinfo.io/region").read().decode()[:-1]
	return await main.say("I am in " + loc + " right now.")
@main.command()
async def anime(*args):
	msg = await main.say("loading anime wallpapers from /r/animewallpapers x333")
	try:
		all = json.loads(urllib.request.urlopen(urllib.request.Request(url="https://api.reddit.com/r/Animewallpaper/search?q=flair%3ADesktop+self%3Ano&restrict_sr=on&sort=new&t=all", data=None, headers={"User-Agent": "Python3 urllib.request.urlopen",})).read().decode())
	except:
		return await main.say("oops didn't work, maybe Reddit is limiting us")
	images = []
	try:
		for things in all["data"]["children"]:
			if things["kind"] == "t3":
				images.append(things["data"]["preview"]["images"][0]["source"]["url"].replace('&amp;', '&'))
	except Exception as e:
		return await main.say("FUCK\n```" + str(e) + "\n```")
	return await main.edit_message(msg, random.choice(images))
@main.command(pass_context=True)
async def boobsize(ctx, *fem):
	app = await main.application_info()
	if not fem:
		return await main.say("sorry```\nboobsize [female]\n```")
	cup = random.choice(["A", "A", "B", "B", "B", "C", "C", "D"]) + " " + str(random.randint(10,50))
	person = await user_from_at(ctx, " ".join(fem), False)
	if not person:
		return await main.say("they don't exist for some reason")
	elif person == 69:
			return 0
	return await main.say(person + "'s boob size is **" + cup + "**")
@main.command(pass_context=True)
async def nut(ctx, *target):
	app = await main.application_info()
	if not target:
		return await main.say("```\nnut [target]\n```")
	person = await user_from_at(ctx, " ".join(target), False)
	if not person:
		return await main.say("they don't exist for some reason")
	elif person == 69:
			return 0
	you = ctx.message.author.name
	return await main.say(
	"{0}: AAAAAAA FINNA BUST\n{1}: what why are you yelling what's this\n{0}: AAFDJFKDSHF AHUAHUAHAHUAHAUA **nuts on {1}**\n{1}: ew what is this hot white substance\n{0}: it's, it's-\n{1}: and it's STICKY GROSS EW\n{0}: it's my nut\n{1}: i don't see any nuts\n{0}: sperm\n{1}: what's that\n{0}: it's how babies are made\n{1}: so i'm pregnant? i hate you {0}!\n{0}: no it's supposed to go into the vagina\n{1}: then why did you shoot your sperm on my head ew\n{0}: bc ur hot\n{1}: what\n{0}: yes\n{1}: brb calling police\nand then {1} called police and now {0} is an officially registered sex offender"
	.format(you, person))
@main.command()
async def girl(*args):
	girls = json.load(open("girls.json"))
	rg = random.choice(girls)
	return await main.say(rg)
@main.command(pass_context=True)
async def secure(ctx, *all):
	if not all:
		return await main.say("```\nsecure [thing that isn't secure that needs to be secured]\n```")
	else:
		str = " ".join(all);
		if len(str) > 500:
			return await main.say("2 long asshole")
		await main.send_typing(ctx.message.channel)
		try:
			out = subprocess.Popen(["php", "secure-text-pyc.php", str], stdout=subprocess.PIPE).stdout.read()
		except Exception as e:
			return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
		return await main.send_file(ctx.message.channel, "secure-py.png")
@main.command(pass_context=True)
async def getjob(ctx, *argh):
	titles = ["CEO", "Manager", "Founder", "Co-Founder", "Director", "Lead Programmer", "Designer", ]
	types = ["Co, Ltd.", "Inc.", "Ltd.", "LLC", "Industries", "Corporation", ]
	companies = ["Google", "Microsoft", "Amazon", "Openverse", "Cedar", "PF2MCorp", "Discord", "Ruby on Rails", "Python", "PHP: Hypertext Preprocessor", "Mac OS X", "Red Hat", "Nintendo", "Log into most any Linux system by hitting backspace 28 times", ]
	lastnames = ["Johnson", "Smith", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Moore", "Jackson", "Thompson", "Torvalds", "Humphries", ]
	if argh:
		p1 = await user_from_at(ctx, " ".join(argh), True, False)
		if not p1:
			return await main.say("you have to @ someone, there are lotso f people in this world!!!!")
		person = p1.name.title() + " " + random.choice(lastnames)
		personid = p1.id
	else:
		person = ctx.message.author.name.title() + " " + random.choice(lastnames)
		personid = ctx.message.author.id
	
	final = "{0}, {1} of {2} {3}".format(person, random.choice(titles), random.choice(companies), random.choice(types))
	return await main.say("<@"+personid+"> is now " + final)
#at the end of secure
@main.command(pass_context=True)
async def bully(ctx, *victim):
	if not victim:
		return await main.say("warning: Bullying is Not OK,. Please do not Bully in Real Life or on Line thank you "+ctx.message.author.name.title()+".```\nbully [victim]\n```")
	person = await user_from_at(ctx, " ".join(victim), False)
	if not person == 69:
		return await main.say("todo put \"roasts\" in `roasts.json` and format them with a mentioned user/string ({0})\n\noh who am I kidding I'll never get to doing this one\nsorry folks".format(person))
@main.command(pass_context=True)
async def fuckseth(ctx, *ann):
	recipient = ctx.message.server.get_member("286909633187151873")
	death = """
Dear Seth,

I legitimately hope you die.

Love, {0}.""".format(ctx.message.author.name.title())
	try:
		await main.send_message(recipient, "```\n{}\n```".format(death))
	except Exception as e:
		return await main.say("uh-oh \n```" + e + "```")
	return await main.say("it was sent ;) <@"+ recipient.id +">")
@main.command(pass_context=True)
async def phpsponsor(ctx, *arghss):
	if not arghss:
		return await main.say("```\nphpsponsor [image url]\n```")
	else:
		str = " ".join(arghss)
		if str.startswith("<@"):
			if str.startswith("<@!"):
				uav = ctx.message.server.get_member(str[3:-1]).avatar_url
			else:
				uav = ctx.message.server.get_member(str[2:-1]).avatar_url
			str = uav
		if len(str) > 250:
			return await main.say("2 long asshole")
		await main.send_typing(ctx.message.channel)
		try:
			out = subprocess.Popen(["php", "php-sponsor-pyc.php", str], stdout=subprocess.PIPE).stdout.read()
			if not out == b'1':
				return await main.say("either that isn't an image url or it's not at least `500x500`")
		except Exception as e:
			return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
		return await main.send_file(ctx.message.channel, "php-sp-py.png")
@main.command()
async def linux(*stallman):
	if stallman:
		linux = " ".join(stallman)
	else:
		linux = 'Linux'
	return await main.say("""
I'd just like to interject for a moment.  What you're referring to as {0}, is in fact, GNU/{0}, or as I've recently taken to calling it, GNU plus {0}. {0} is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it.  Through a peculiar turn of events, the version of GNU which is widely used today is often called "{0}", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a {0}, and these people are using it, but it is just a part of the system they use. {0} is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system.  {0} is normally used in combination with the GNU operating system: the whole system is basically GNU with {0} added, or GNU/{0}. All the so-called "{0}" distributions are really distributions of GNU/{0}.
	""".format(linux))
@main.command(pass_context=True)
async def kai(ctx, *thirteenyoboys):
	if ctx.message.server.id != '298564047991996416':
		return await main.say("this command is --EXPLICIT-- and can only be used on a very specific server\nsorry, kids")
	if thirteenyoboys:
		boyz = ' '.join(thirteenyoboys)
	else:
		boyz = random.choice([
		'shit', 'suck',
		'lick', 'puke',
		'nuke', 'sit',
		])
	return await main.say("<@303983560740569089> {0} on my dick".format(boyz))
@main.command(pass_context=True)
async def respect(ctx, *ericsucks):
	if ericsucks:
		person = await user_from_at(ctx, ' '.join(ericsucks), False)
	else:
		person = ctx.message.author.name
	if not person == 69:
		return await main.say("{0} shut the fuck up you waste of life".format(person.lower()))
@main.command(pass_context=True)
async def miiverse(ctx, *url):
	if not url:
		return await main.say("```\nmiiverse [post URL, e.g. AYEBAAAEAAB2UZ8mAzTspw]```")
	if url[0] == 'AYEBAAAEAAB2UZ8mAzTspw':
		return await main.say("haha that isn't actually a post")
	await main.send_typing(ctx.message.channel)
	try:
		srv = urllib.request.urlopen("https://miiverse.nintendo.net/posts/{0}/embed".format(url[0]))
	except Exception as e:
		return await main.say("```\n" + str(e) + "```")
	ftree = html.fromstring(srv.read().decode())
	drawing = ftree.xpath('//*[@id="post-content"]/div/p/img/@src')
	post = ftree.xpath('//*[@id="post-content"]/div/p/text()')
	screenshot = ftree.xpath('//*[@id="post-content"]/div/div[1]/img/@src')
	thing = ""
	if drawing:
		thing += "c'est une belle peinture\n\n" + drawing[0]
	else:
		thing += post[0]
	if screenshot:
		thing += "\n" + screenshot[0]
	return await main.say(thing)
@main.command(pass_context=True)
async def eek(ctx, *args):
	if not ctx.message.server.id == "298564047991996416":
		return await main.say("this command is only meant to be used in one server :frowning2: ")
	# Please do not harass this person or in fact anyone else in here
	die = "148564483122528265"
	if not ctx.message.server.default_channel.permissions_for(ctx.message.server.me).kick_members:
		return await main.say("aw man I do not have the necessary (s)perms")
	niggersearch = ctx.message.server.get_member(die)
	if not niggersearch:
		return await main.say("the coast is clear :eyes: ")
	await main.say("ban or kick? :thinking: ")
	await main.send_typing(ctx.message.channel)
	time.sleep(1)
	hh = "got any last words? :gun: "
	if random.choice([True, True, False]):
		await main.say("ban it is! goodbye faggot, next time learn how to fucking respect other humans :wave: <@"+die+">")
		thingy = await main.say(hh + "(5)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(4)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(3)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(2)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(1)")
		time.sleep(1)
		await main.edit_message(thingy, hh)
		try:
			await main.ban(niggersearch)
			await main.kick(niggersearch)
		except Exception as e:
			await main.say("aw man, never mind\n```\n"+e+"```")
		await main.say("okay he's gone, now get back to work")
	else:
		await main.say("time for a kick! see ya dude, I'll let you off for now, next time learn how to fucking respect other humans :wave: <@"+die+">")
		thingy = await main.say(hh + "(5)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(4)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(3)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(2)")
		time.sleep(1)
		await main.edit_message(thingy, hh + "(1)")
		time.sleep(1)
		await main.edit_message(thingy, hh)
		try:
			await main.kick(niggersearch)
		except Exception as e:
			await main.say("aw man, never mind\n```\n"+e+"```")
		await main.say("okay he's gone, now get back to work")
@main.command(pass_context=True)
async def loli(ctx, *ericdick):
	if not ("nsfw" in ctx.message.channel.name or "loli" in ctx.message.channel.name) and not ctx.message.server.id == "298564047991996416":
		return await main.say("this isn't an NSFW channel\nor maybe it is and I can't tell because fucking DISCORDPY doesn't have that implemented\n\nyet")
	mess = await main.say(":thinking: ")
	try:
		pag = random.choice([0, 1, 2, ])
		
		arg = "splatoon"
		if ericdick:
			pag = 0
			arg += " " + urllib.parse.quote_plus(" ".join(ericdick))
		srv = urllib.request.urlopen("https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&pid="+ str(pag) + "&tags=" + arg)
		lolis = json.loads(srv.read().decode())
		imagags = []
		for thing in lolis:
			imagags.append([thing["file_url"], thing["score"]])
	except ValueError:
		return await main.say("nothing found")
	except Exception as e:
		return await main.say("fuck\n```" + str(e) + "```")
	scramble = random.choice(imagags)
	rate = str(scramble[1])
	if not scramble[1]:
		rate += " ewww"
	elif scramble[1] >= 100:
		rate += " holy shit"
	elif scramble[1] >= 50:
		rate += " yes"
	elif scramble[1] >= 30:
		rate += " :ok_hand: "
	return await main.edit_message(mess, "score: {0}\n".format(rate) + scramble[0])
@main.command(pass_context=True)
async def hitler(ctx, *arghss):
	str = " ".join(arghss)
	if str.startswith("<@"):
		if str.startswith("<@!"):
			uav = ctx.message.server.get_member(str[3:-1]).avatar_url
		else:
			uav = ctx.message.server.get_member(str[2:-1]).avatar_url
	else:
		uav = ctx.message.author.avatar_url
	await main.send_typing(ctx.message.channel)
	try:
		out = subprocess.Popen(["php", "hitler.php", uav], stdout=subprocess.PIPE).stdout.read()
	except Exception as e:
		return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
	return await main.send_file(ctx.message.channel, "hitler-py.png")
@main.command(pass_context=True, aliases=["69"])
async def sixty_nine(ctx, *arghss):
	if not ("nsfw" in ctx.message.channel.name or "loli" in ctx.message.channel.name):
		return await main.say("this isn't an NSFW channel, and while this command isn't directly explicit, the theme is explicit\nsorry kids")
	str = " ".join(arghss)
	if str.startswith("<@"):
		if str.startswith("<@!"):
			uav = ctx.message.server.get_member(str[3:-1]).avatar_url
		else:
			uav = ctx.message.server.get_member(str[2:-1]).avatar_url
	else:
		uav = ctx.message.author.avatar_url
	await main.send_typing(ctx.message.channel)
	try:
		out = subprocess.Popen(["php", "69.php", uav], stdout=subprocess.PIPE).stdout.read()
	except Exception as e:
		return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
	return await main.send_file(ctx.message.channel, "69-py.png")
@main.command()
async def succme(*args):
	rando = random.choice(range(1, 10))
	#vrando = random.choice(range(1, 50))
	#if vrando == 35:
	#	return await main.say("WARNING: <@"+  +"> has been newly placed on to the _[] Sex Offender Directory_")
	if not rando == 7:
		return await main.say("no")
	if bool(random.getrandbits(1)):
		return await main.say("""
\*succ\*
wait a sec what am i sucking
\*pulls off blindfold\*
EW WHAT THAT IS NOT A PENIS THAT IS VAG
\*pukes\*
\***on _vag_**\*
\*runs\*
""")
	return await main.say("""
todo put hot scene here :wink: 
""")
@main.command(pass_context=True)
async def neko(ctx, *args):
	await main.send_typing(ctx.message.channel)
	try:
		srv = requests.get("https://nekos.life/api/lewd/neko")
	except Exception as e:
		return await main.say("aw\n```" + str(e) + "```")
	nya = json.loads(srv.text)['neko']
	return await main.say(nya)

# Run
try:
	main.loop.run_until_complete(main.start(secret))
except Exception as e:
	print(str(e))
	main.loop.run_until_complete(main.logout())
finally:
    main.loop.close()
    sys.exit(0)