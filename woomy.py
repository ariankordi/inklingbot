import discord
import asyncio
import OpenSSL
import base64
import binascii
from random import choice
import hashlib
import struct
import time
import subprocess
import sys
import random
import json
import urllib.request
import html
from discord.ext.commands import Bot
#config?
settings = json.load(open("settings.json"))
secret = settings["secret"]; normie = settings["n"]; fuckeric = settings["fe"];
#/config
main = Bot(command_prefix="woomy ")

if normie:
	@main.async_event
	async def on_ready():
		await main.change_presence(game=discord.Game(name="'woomy how2use' for help"))
	@main.command()
	async def how2use(*args):
		return await main.say("""
okay the command prefix is `woomy` so type that before everything and it'll work
`woomy help` will list all commands however none of them are commented so you'll have to try them if you want to see if they work
if a command requires args then it'll tell you
that's about it""")

async def name_from_at(a):
	print("todo get name from user id at")

#first command made
@main.command()
async def hot(*args):
	return await main.say("damn right")
@main.command()
async def canada(*args):
	return await main.say("O CANADA```\n  _\n (_)\n  |_____________________________________\n  |&&&&&&                         &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&          .\\^/.          &&&&&&|\n  |&&&&&&        . |   | .        &&&&&&|\n  |&&&&&&        |\\|   |/|        &&&&&&|\n  |&&&&&&     .--'       '--.     &&&&&&|\n  |&&&&&&      \\           /      &&&&&&|\n  |&&&&&&       >         <       &&&&&&|\n  |&&&&&&      '~|/~~|~~\\|~'      &&&&&&|\n  |&&&&&&            |            &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&                         &&&&&&|\n  |&&&&&&_________________________&&&&&&|\n  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n```")
@main.command()
async def ass(*args):
	return await main.say("todo put ass here\nhttps://s18.postimg.org/4np6ebpcp/Wii_U_screenshot_TV_01769.jpg\nhttps://s1.postimg.org/p5vtn7xu7/Wii_U_screenshot_TV_01769.jpg")
@main.command()
async def hi(*args):
	return await main.say("heyyy")
@main.command()
async def rijndael(*args):
	return await main.say(binascii.hexlify(OpenSSL.rand.bytes(150)).decode())
@main.command()
async def speak(*args):
	return await main.say("".join([choice("abcdefghijklmnopqrstuvwxyz") for i in range(12)]))
@main.command()
async def python(*args):
	return await main.say("KeyboardInterrupt")
@main.command()
async def mysql(*args):
	return await main.say("greedy fuck")
@main.command()
async def ok(*args):
	return await main.say("don't you fucking ok me cunt")
@main.command()
async def pikamasterjesi(*args):
	return await main.say("<@295395343137505282>\nhttps://yt3.ggpht.com/-jl5w8T6GckA/AAAAAAAAAAI/AAAAAAAAAAA/foES_M_6PQ8/s500-c-k-no-mo-rj-c0xffffff/photo.jpg")
@main.command()
async def nnpasswordhash(*a):
	if not a:
		return await main.say("```\nnnpasswordhash [pid] [passwd]```")
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
		if len(str) > 50:
			return await main.say("2 long asshole")
		try:
			out = subprocess.getoutput("php open-logo-pyc.php \"" + str + "\"")
		except Exception as e:
			return await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```")
		return await main.send_file(ctx.message.channel, "open-py.png")
@main.command()
async def invite(*args):
	app = await main.application_info()
	return await main.say("invite deez nuts hah goteem\n" + discord.utils.oauth_url(app.id))
@main.command()
async def ponder(*q):
	if not q:
		return await main.say("```\nponder [question]\n```")
	if bool(random.getrandbits(1)):
		return await main.say("yes")
	else:
		return await main.say("nah")
@main.command()
async def compiler(*args):
	return await main.say(sys.version)
@main.command()
async def uname(*args):
	return await main.say(subprocess.getoutput("uname -a"))
@main.command()
async def length(*lol):
	if not lol:
		return await main.say("```\nlength [object]\n```")
	if lol[0] == 'arian':
		return await main.say("actually arian is `5'11 ft` tall as of now")
	else:
		if lol[0] == 'eric\'s':
			thing = 0
		else:
			thing = int(random.getrandbits(5))
		return await main.say(str(thing) + " cm")
if fuckeric:
	@main.command(pass_context=True)
	async def fuckofferic(ctx):
		faggot = 151466174683545600
		await main.say("goodbye eric d faggot :wave: <@"+str(faggot)+">")
		try:
			await main.kick(ctx.message.server.get_member(str(faggot)))
		except Exception as e:
			await main.say("i couldn't do it :thinking: ```\n" + str(e) + "\n```did Eric leave? do I not have permissions? IDK you decide")
		return 0;
@main.command()
async def sethfuck(*a):
	if not a:
		with open("seth.json") as cumd:
			cummies = random.choice(json.load(cumd))
	else:
		cummies = " ".join(a)
	return await main.say("```\nseth 10 year old sperm ---) " + cummies + "\n```")
if fuckeric:
	@main.command()
	async def eric(*args):
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
		japanese = "".join([choice("".join(katakana)) for i in range(6)])
	return await main.say(japanese)
@main.command()
async def arian(*args):
	app = await main.application_info()
	return await main.say("that's me <@"+app.owner.id+"> https://ariankordi.net/")
@main.command(pass_context=True)
async def sex(ctx, *u):
	app = await main.application_info()
	if bool(random.getrandbits(1)):
		only2genders = "♀"
	else:
		only2genders = "♂"
	if not u:
		return await main.say("you are " + only2genders)
	if u[0].startswith("<@"):
		try:
			if u[0].startswith("<@!"):
				user = ctx.message.server.get_member(u[0][3:-1])
			else:
				user = ctx.message.server.get_member(u[0][2:-1])
			if user == app.name:
				only2genders = "an inkling"
			return await main.say(user.name + " is " + only2genders)
		except Exception as e:
			return await main.say("they don't exist for some reason")
	else:
		return await main.say(u[0] + " is " + only2genders)
@main.command(pass_context=True)
async def php(ctx, *txt):
	#return await main.say("it sucks")
	if not txt:
		return await main.say("```\nphp [text]\n```")
	tex = " ".join(txt)
	if len(tex) > 50:
		return await main.say("2 long asshole")
	try:
		out = subprocess.getoutput("php php-logo-pyc.php \"" + tex + "\"")
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
	msg = await main.send_message(ctx.message.channel, "doing it")
	try:
		out = subprocess.getoutput("php nnmii.php \"" + n[0] + "\"")
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
	if nam.startswith("<@"):
		try:
			if nam.startswith("<@!"):
				user = ctx.message.server.get_member(nam[3:-1])
			else:
				user = ctx.message.server.get_member(nam[2:-1])
		except Exception as e:
			return await main.say("i couldn't do it, sorry, happy birthday anyway :tada: unless you're a cunt then fuck you suck a dick")
		nam = user.name + " <@"+user.id+">"
	return await main.say(":tada::tada::tada::tada::tada: HAPPY BIRTHDAY " + nam.upper() + " :tada::tada::tada::tada::tada:")
@main.command(pass_context=True)
async def blacklist(ctx, *nig):
	if not nig:
		user = ctx.message.author.id
	else:
		if nig[0].startswith("<@"):
				if nig[0].startswith("<@!"):
					user = nig[0][3:-1]
				else:
					user = nig[0][2:-1]
	return await main.say("<@"+ user +">: :hammer: ***BLACKLISTED*** :hammer: for **24:00:00**")
@main.command()
async def splatoonrotation(*args):
	msg1 = await main.say("getting stats for a dead game (Splatoon), give me a moment")
	try:
		srv = urllib.request.urlopen("https://s3-ap-northeast-1.amazonaws.com/splatoon-data.nintendo.net/stages_info.json")
		stages = json.loads(srv.read().decode())
		message = "Rotation 1: begins {}, ends {}\nTurf War stage 1: {}\nTurf War stage 2: {}\nRotation 2: begins {}, ends {}\nTurf War stage 1: {}\nTurf War stage 2: {}\nRotation 3: begins {}, ends {}\nTurf War stage 1: {}\nTurf War stage 2: {}".format(stages[0]['datetime_term_begin'], stages[0]['datetime_term_end'], stages[0]['stages'][0]['name'], stages[0]['stages'][1]['name'], stages[1]['datetime_term_begin'], stages[1]['datetime_term_end'], stages[1]['stages'][0]['name'], stages[1]['stages'][1]['name'], stages[2]['datetime_term_begin'], stages[2]['datetime_term_end'], stages[2]['stages'][0]['name'], stages[2]['stages'][1]['name'])
		await main.edit_message(msg1, message)
	except Exception as e:
		await main.say("didn't work :frowning2: \n```" + str(e) + "\n```")
@main.command(pass_context=True)
async def suck(ctx, *per):
	app = await main.application_info()
	if not per:
		return await main.say("```\nsuck [@ person]\n```")
	if per[0].startswith("<@"):
		if per[0].startswith("<@!"):
			user = per[0][3:-1]
		else:
			user = per[0][2:-1]
		if user == app.id:
			return await main.say("um")
		return await main.say(ctx.message.author.name + " has sucked your dick <@"+user+">")
	elif "@everyone" in per[0] or "@here" in per[0]:
		return await main.say("fuck off")
	else:
		return await main.say("you're supposed to @ someone idiot")
# At end of location actually
@main.command(pass_context=True)
async def tittyfuck(ctx, *unlucky):
	app = await main.application_info()
	if not unlucky:
		return await main.say("because 9 people wanted this command\n```\ntittyfuck [victim]\n```")
	if unlucky[0].startswith("<@"):
		if unlucky[0].startswith("<@!"):
			user = unlucky[0][3:-1]
		else:
			user = unlucky[0][2:-1]
		if user == app.id:
			return await main.say("um")
		return await main.say(ctx.message.author.name + " has fucked your tits <@"+user+">")
	elif "@everyone" in unlucky[0] or "@here" in unlucky[0]:
		return await main.say("fuck off")
	else:
		return await main.say("how are you supposed to tittyfuck if you don't @ who you want to fucktitty")
@main.command(pass_context=True)
async def cat(ctx, *args):
	msg = await main.say("nya")
	try:
		img = urllib.request.urlopen("http://thecatapi.com/api/images/get?&format=src&type=png").geturl()
	except:
		return await main.say("aw man")
	return await main.edit_message(msg, "nya\n" + img)
@main.command()
async def location(*args):
	loc = urllib.request.urlopen("https://ipinfo.io/region").read().decode()[:-1]
	return await main.say("I am in " + loc + " right now.")
@main.command()
async def fuckingyourniece(*args):
	return await main.say("is totally okay, woomy approved :thumbsup: ")
@main.command()
async def anime(*args):
	msg = await main.say("loading anime wallpapers from /r/animewallpapers x333")
	try:
		all = json.loads(urllib.request.urlopen(urllib.request.Request(url="https://api.reddit.com/r/Animewallpaper/search?q=flair%3ADesktop+self%3Ano&restrict_sr=on&sort=new&t=all", data=None, headers={"User-Agent": "Python3 urllib.request.urlopen",})).read().decode())
	except:
		return await main.say("oops didn't work, maybe Reddit is limiting us")
	images = []
	for things in all["data"]["children"]:
		if things["kind"] == "t3":
			images.append(html.unescape(things["data"]["preview"]["images"][0]["resolutions"][5]["url"]))
	return await main.edit_message(msg, random.choice(images))
@main.command(pass_context=True)
async def boobsize(ctx, *fem):
	app = await main.application_info()
	if not fem:
		return await main.say("sorry```\nboobsize [female]\n```")
	cup = random.choice(["A", "A", "B", "B", "B", "C", "C", "D"]) + " " + str(random.randint(10,50))
	if fem[0].startswith("<@"):
		try:
			if fem[0].startswith("<@!"):
				user = ctx.message.server.get_member(fem[0][3:-1])
			else:
				user = ctx.message.server.get_member(fem[0][2:-1])
			if fem[0][2:-1] == app.id:
				return await main.say("um")
			person = user.name
			return await main.say(user.name + "'s boob size is **" + cup + "**")
		except Exception as e:
			return await main.say("they don't exist for some reason")
	elif "@everyone" in fem[0] or "@here" in fem[0]:
		return await main.say("fuck off")
	else:
		person = " ".join(fem)
	return await main.say(person + "'s boob size is **" + cup + "**")
@main.command(pass_context=True)
async def nut(ctx, *target):
	app = await main.application_info()
	if not target:
		return await main.say("```\nnut [target]\n```")
	if target[0].startswith("<@"):
		try:
			if target[0].startswith("<@!"):
				user = ctx.message.server.get_member(target[0][3:-1])
			else:
				user = ctx.message.server.get_member(target[0][2:-1])
			if target[0][2:-1] == app.id:
				return await main.say("um")
			person = user.name
		except Exception as e:
			return await main.say("they don't exist for some reason")
	elif "@everyone" in target[0] or "@here" in target[0]:
		return await main.say("fuck off")
	else:
		person = target[0]
	you = ctx.message.author.name
	return await main.say(
	"{0}: AAAAAAA FINNA BUST\n{1}: what why are you yelling what's this\n{0}: AAFDJFKDSHF AHUAHUAHAHUAHAUA **nuts on {1}**\n{1}: ew what is this hot white substance\n{0}: it's, it's-\n{1}: and it's STICKY GROSS EW\n{0}: it's my nut\n{1}: i don't see any nuts\n{0}: sperm\n{1}: what's that\n{0}: it's how babies are made\n{1}: so i'm pregnant? i hate you {0}!\n{0}: no it's supposed to go into the vagina\n{1}: then why did you shoot your sperm on my head ew\n{0}: bc ur hot\n{1}: what\n{0}: yes\n{1}: brb calling police\nand then {1} called police and now {0} is an officially registered sex offender"
	.format(you, person))

# Run
try:
	#todo put the secret into a config json and load that
	main.loop.run_until_complete(main.start(secret))
except KeyboardInterrupt:
	print("KeyboardInterrupt")
	main.send_message("I was KeyboardInterrupted :wave: ")
	main.loop.run_until_complete(main.logout())
finally:
    main.loop.close()
    exit()