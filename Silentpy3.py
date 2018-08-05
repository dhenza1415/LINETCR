# -*- coding: utf-8 -*-
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
from multiprocessing import Pool, Process
from googletrans import Translator

#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE("Ev1G3uywh9IGw0Sv6eI0.9WYN3zwDz6SB8repaA9mCa.EOg0Y7CdooSc0LQ2+OWP/4MjPtjip2mQZ0s5vLsK2lk=")
line.log("Auth Token : " + str(line.authToken))

ki = LINE("EvjUlscCS1qE3Q2z9WB4.Wtcko8WDgnzsmCJwcY4pra.OADeBm0MtyI/8TciTA5nJMFz1DP+14WdXYC7yRVTKGo=")
ki.log("Auth Token : " + str(ki.authToken))

kk = LINE("EvH1CMn6jB1BESCQybVb.02AXc0wyImk1MchKZcijIW.m/iQMziOUQlaE2jaWhoNpCD7gUbi9dTVf1CVW1S8we8=")
kk.log("Auth Token : " + str(kk.authToken))

kc = LINE("Evs01WLwiOtFPz0NSuGf.h7/+DhAi/9tcWOXbk9TC7W.xYXzwloO23qHfhT6WB1TLg2i/+B0WQ+1yEZNOUX22vU=")
kc.log("Auth Token : " + str(kc.authToken))

ke = LINE("EvSIQpNSVZDsZNrE60l5.lBxVjRgHNkE/jLB/U0/Vnq.nc2hm8h2xNTnAIvl3wORxKR+jXFSy1o9AU5yuNVCm9A=")
ke.log("Auth Token : " + str(ke.authToken))

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

kiMID = ki.profile.mid
kiProfile = ki.getProfile()
kiSettings = ki.getSettings()

kkMID = kk.profile.mid
kkProfile = kk.getProfile()
kkSettings = kk.getSettings()

kcMID = kc.profile.mid
kcProfile = kc.getProfile()
kcSettings = kc.getSettings()

keMID = ke.profile.mid
keProfile = ke.getProfile()
keSettings = ke.getSettings()

oepoll = OEPoll(ke)
oepoll = OEPoll(kc)
oepoll = OEPoll(kk)
oepoll = OEPoll(ki)
oepoll = OEPoll(line)
KAC = [line,ki,kk,kc,ke]
lineMID = line.getProfile().mid
kiMID = ki.getProfile().mid
kkMID = kk.getProfile().mid
kcMID = kc.getProfile().mid
keMID = ke.getProfile().mid

Bots=[lineMID,kiMID,kkMID,kcMID,keMID]
creator = ["u58714149295f212f741f18624cbba58d","u0f6df437fe3e32f07c4562308ac430a9"]
owner=['u58714149295f212f741f18624cbba58d']
admin=['u58714149295f212f741f18624cbba58d']
staff=['u58714149295f212f741f18624cbba58d']
Bots = Bots 

lineMIDProfile = line.getProfile()
kiMIDProfile = ki.getProfile()
kkMIDProfile = kk.getProfile()
kcMIDProfile = kc.getProfile()
keMIDProfile = ke.getProfile()

lineMIDSettings = line.getSettings()
kiMIDSettings = ki.getSettings()
kkMIDSettings = kk.getSettings()
kcMIDSettings = kc.getSettings()
keMIDSettings = ke.getSettings()

responsename = line.getProfile().displayName
responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = ke.getProfile().displayName

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectcancl = []
protection = []
autocancel = []
autoinvite = []
autoleaveroom = []
targets = []
welcome = []
msg_dict = []
msg_dict1 = []
#==============================================================================#
settings = {
    "autoJoin": True,
    'autoCancel':{"on":True,"members":1},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "potoMention": False,
    "autoJoinTicket": False,
    "atjointicket": False,
    "checkContact": False,
    "lang":"JP",
    "tag2": True,
    "Wc": False,
    "Lv": False,
    "limit": 1,
    "whitelist": {},
    "blacklist":{},
    "commentBlack":{},
    "owner":{},
    "staff":{},
    "admin":{},
    "Bots":{},
    "winvite": {},
    "wblacklist": False,
    "dblacklist": False,
    "wblack": False,
    "dblack": False,
    "clock": False,
    "contact": False,
    "cName":"",
    "cNames":"",
    "invite": {},
    "foto": {},
    "Picture":False,
    "groupPicture":False,
    "changePicture":False,
    "Bots": {},
    "group": {},
    "sider": {},
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "message":"Thanks for add me",
    "comment":"Like like & like by ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬",
    "Respontag":"",
    "mention":"",
    "welcome":"",
    "bye":"",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

Protect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
}

#Setmain = {
    #"foto": {},
#}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

Set = {
    'setTime':{},
    'ricoinvite':{},
    }

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
mulai = time.time()

setTime = {}
setTime = Set['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile() 
backup = ki.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile() 
backup = kk.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile() 
backup = kc.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ke.getProfile() 
backup = ke.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def templatemusic(line,img,text,stext):
        a = line.getProfile().userid
        contentMetadata={
        'subText': stext,
        'countryCode': 'ID',
        'a-packageName': 'com.spotify.music',
        'previewUrl': img, 'text': text,
        'linkUri': 'line://ti/p/~{}'.format(a), 'id': 'mt000000000a6b79f9', 'i-installUrl': 'line://ti/p/~{}'.format(a)
        , 'type': 'mt', 'a-installUrl': 'line://ti/p/~{}'.format(a), 'i-linkUri': 'line://ti/p/~{}'.format(a), 'a-linkUri': 'line://ti/p/~{}'.format(a)}
        return contentMetadata
      
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
      
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
  
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
  
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]     
            
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = line.getAllContactIds()
        gid = line.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"™↔ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n™↔ Group : "+str(len(gid))+"\n™↔ Teman : "+str(len(teman))+"\n™↔ Expired : In "+hari+"\n™↔ Version : ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬\n™↔ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n™↔ Runtime : \n • "+bot
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for lineMID in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」 ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
  
def myhelp():
    myHelp = "🦆 🔥sᴇᴛᴛɪɴɢs ʜᴇʟᴘ🔥 " + "\n" + \
                  "🦆「Info」"+ "\n" + \
                  "🦆「Help」"+ "\n" + \
                  "🦆「Hk」"+ "\n" + \
                  "🦆「Me」"+ "\n" + \
                  "🦆「Sp,Speed」"+ "\n" + \
                  "🦆「Waktu」"+ "\n" + \
                  "🦆「Restart」"+ "\n" + \
                  "🦆「Mid @」"+ "\n" + \
                  "🦆「Set」"+ "\n" + \
                  "🦆「Gcel」"+ "\n" + \
                  "🦆「Devil「On/Off」"+ "\n" + \
                  "🦆「Creator」"+ "\n" + \
                  "🦆「Autojoin「On/Off」"+ "\n" + \
                  "🦆「Autoleave「On/Off」"+ "\n" + \
                  "🦆「Autojointicket「On/Off」"+ "\n" + \
                  "🦆「K「On/Off」"+ "\n" + \
                  "🦆「MimicList」"+ "\n" + \
                  "🦆「MimicAdd」"+ "\n" + \
                  "🦆「MimicDel」"+ "\n" + \
                  "🦆「Sayang」"+ "\n" + \
                  "🦆「Copy @」"+ "\n" + \
                  "🦆「Backup」"+ "\n" + \
                  "🦆「Mid」"+ "\n" + \
                  "🦆「Fotoku」"+ "\n" + \
                  "🦆「Mid @」"+ "\n" + \
                  "🦆「Creator」"+ "\n" + \
                  "🦆「Nama」"+ "\n" + \
                  "🦆「Statusku」"+ "\n" + \
                  "🦆「Coverku」"+ "\n" + \
                  "🦆「Videoku」"+ "\n" + \
                  "🦆「Status @」"+ "\n" + \
                  "🦆「Foto @」"+ "\n" + \
                  "🦆「Cover @」"+ "\n" + \
                  "🦆「Video @」"+ "\n" + \
                  "🦆「Gcreator」"+ "\n" + \
                  "🦆「Gfoto」"+ "\n" + \
                  "🦆「Spam jumlah」"+ "\n" + \
                  "🦆「Reject」"+ "\n" + \
                  "🦆「Gticket」"+ "\n" + \
                  "🦆「Gticket on」"+ "\n" + \
                  "🦆「Gticket off」"+ "\n" + \
                  "🦆「Bc:」"+ "\n" + \
                  "🦆「Ginfo」"+ "\n" + \
                  "🦆「Invite」"+ "\n" + \
                  "🦆「Gmlist」"+ "\n" + \
                  "🦆「Glist」"+ "\n" + \
                  "🦆「Instagram」"+ "\n" + \
                  "🦆「Image」"+ "\n" + \
                  "🦆「Yt」"+ "\n" + \
                  "🦆「Music」"+ "\n" + \
                  "🦆「Id nama」"+ "\n" + \
                  "🦆「Smule nama」"+ "\n" + \
                  "🦆「Bokep」"+ "\n" + \
                  "🦆「Kalender」"+ "\n" + \
                  "🦆「B1list」"+ "\n" + \
                  "🦆「B2list」"+ "\n" + \
                  "🦆「Wikipedia」"+ "\n" + \
                  "🦆「Ban @」"+ "\n" + \
                  "🦆「Banlist」"+ "\n" + \
                  "🦆「Clearban」"+ "\n" + \
                  "🦆「Jitak @」"+ "\n" + \
                  "🦆「Tampol @」"+ "\n" + \
                  "🦆「B1 @」"+ "\n" + \
                  "🦆「B2 @」"+ "\n" + \
                  "🦆「1invite」"+ "\n" + \
                  "🦆「Gantipp」"+ "\n" + \
                  "🦆「Ancur」"+ "\n" + \
                  "🦆「Kumpul」"+ "\n" + \
                  "🦆「Byeall」"+ "\n" + \
                  "🦆「Myname:」"+ "\n" + \
                  "🦆「Absen」"+ "\n" + \
                  "🦆「Ciduk」"+ "\n" + \
                  "🦆「Cek」"+ "\n" + \
                  "🦆「Bcvc 」"+ "\n" + \
                  "🦆「Cbcv 」"+ "\n" + \
                  "🦆「Tlist」"+ "\n" + \
                  "🦆「1name:」"+ "\n" + \
                  "🦆「Join on\off」"+ "\n" + \
                  "🦆「Wc on\off 」"+ "\n" + \
                  "🦆「Left on\off 」"+ "\n" + \
                  "🦆「Sider on\off」"+ "\n" + \
                  "🦆「kuy」"+ "\n" + \
                  "🦆「keluar」"+ "\n" + \
                  "🦆「Buka qr」"+ "\n" + \
                  "🦆「Tutup qr」"+ "\n" + \
                  "🦆「Bye」"+ "\n" + \
                  "🦆「Link」"+ "\n" + \
                  "🦆「Masuk invbot」"+ "\n" + \
                  "🦆「1foto」"+ "\n" + \
                  "🦆「Angus kicksiri」"+ "\n" + \
                  "🦆 ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ "
    return myHelp

def helpkicker():
    helpKicker = "🦆 🔥ʜᴇʟᴘ ᴋɪᴄᴋᴇʀ🔥 " + "\n" + \
    "🦆 Ancur" + "\n" + \
    "🦆 kiss @" + "\n" + \
    "🦆 c2 @" + "\n" + \
    "🦆 desah @" + "\n" + \
    "🦆 c1 @" + "\n" + \
    "🦆 Bsiri @"+ "\n" + \
    "🦆 ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ "
    return helpKicker
    
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)		
        if op.type == 13:
            if kiMID in op.param3:
                G = ki.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)	
        if op.type == 13:
            if kkMID in op.param3:
                G = kk.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)		
        if op.type == 13:
            if kcMID in op.param3:
                G = kc.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    kc.cancelGroupInvitation(op.param1, matched_list)	
        if op.type == 13:
            if keMID in op.param3:
                G = ke.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ke.rejectGroupInvitation(op.param1)
                        else:
                            ke.acceptGroupInvitation(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ke.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ke.cancelGroupInvitation(op.param1, matched_list)		
#======================================================================================================#
#======================================================================================================#  
        if op.type == 13:
            if op.param3 in lineMID:
                if op.param2 in Bots:
                    line.acceptGroupInvitation(op.param1)
            if op.param3 in kiMID:
                if op.param2 in Bots:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in kkMID:
                if op.param2 in Bots:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in kcMID:
                if op.param2 in Bots:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in keMID:
                if op.param2 in Bots:
                    ke.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in lineMID:
		            if op.param2 in kiMID:
		                line.acceptGroupInvitation(op.param1)
            if op.param3 in lineMID:
		            if op.param2 in kkMID:
		                line.acceptGroupInvitation(op.param1)
            if op.param3 in lineMID:
		            if op.param2 in kcMID:
		                line.acceptGroupInvitation(op.param1)
            if op.param3 in lineMID:
		            if op.param2 in keMID:
		                line.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in kiMID:
		            if op.param2 in lineMID:
		                ki.acceptGroupInvitation(op.param1)
            if op.param3 in kiMID:
		            if op.param2 in kkMID:
		                ki.acceptGroupInvitation(op.param1)
            if op.param3 in kiMID:
		            if op.param2 in kcMID:
		                ki.acceptGroupInvitation(op.param1)
            if op.param3 in kiMID:
		            if op.param2 in keMID:
		                ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in kkMID:
		            if op.param2 in lineMID:
		                kk.acceptGroupInvitation(op.param1)
            if op.param3 in kkMID:
		            if op.param2 in kiMID:
		                kk.acceptGroupInvitation(op.param1)
            if op.param3 in kkMID:
		            if op.param2 in kcMID:
		                kk.acceptGroupInvitation(op.param1)
            if op.param3 in kkMID:
		            if op.param2 in keMID:
		                kk.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in kcMID:
            		if op.param2 in lineMID:
		                kc.acceptGroupInvitation(op.param1)
            if op.param3 in kcMID:
		            if op.param2 in kiMID:
		                kc.acceptGroupInvitation(op.param1)
            if op.param3 in kcMID:
		            if op.param2 in kkMID:
		                kc.acceptGroupInvitation(op.param1)
            if op.param3 in kcMID:
		            if op.param2 in keMID:
		                kc.acceptGroupInvitation(op.param1)
#--------------------------------------------------------  
            if op.param3 in keMID:
		            if op.param2 in lineMID:
		                ke.acceptGroupInvitation(op.param1)
            if op.param3 in keMID:
		            if op.param2 in kiMID:
		                ke.acceptGroupInvitation(op.param1)
            if op.param3 in keMID:
		            if op.param2 in kkMID:
		                ke.acceptGroupInvitation(op.param1)
            if op.param3 in keMID:
		            if op.param2 in kcMID:
		                ke.acceptGroupInvitation(op.param1)
#=============================================================================#
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if line.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            line.reissueGroupTicket(op.param1)
                            X = line.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(X)
                            line.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            line.sendText(op.param1,line.getContact(op.param2).displayName + "Jangan Buka QR kk")
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = random.choice(KAC).getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(KAC).updateGroup(X)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = random.choice(KAC).getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(KAC).updateGroup(X)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = random.choice(KAC).getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).updateGroup(X)
                            except:
                                try:
                                    if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ke.reissueGroupTicket(op.param1)
                                            X = random.choice(KAC).getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(KAC).updateGroup(X)
                                except:
                                    pass
#======================================================================================================#
#======================================================================================================#  
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in settings['pname']:
                    try:
                        G = line.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ke.getGroup(op.param1)
                                    except:
                                        pass
                    G.name = settings['pro_name'][op.param1]
                    try:
                        line.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ke.updateGroup(G)
                                    except:
                                        pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            line.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
#======================================================================================================#
#======================================================================================================#                                            
        if op.type == 13:
            if op.param3 in lineMID:
                if op.param2 in kiMID:
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)

            if op.param3 in kiMID:
                if op.param2 in lineMID:
                    X = line.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    line.updateGroup(X)
                    Ti = line.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X.preventedJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in kkMID:
                if op.param2 in kiMID:
                    X = ki.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X.preventedJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in kcMID:
                if op.param2 in kkMID:
                    X = kk.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X.preventedJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in keMID:
                if op.param2 in kcMID:
                    X = kc.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X.preventedJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                
            if op.param3 in lineMID:
                if op.param2 in keMID:
                    X = ke.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X.preventedJoinByTicket = True
                    line.updateGroup(X)
                    Ti = line.reissueGroupTicket(op.param1)
                    
        if op.type == 13:
            if lineMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        line.acceptGroupInvitation(op.param1)
                        ginfo = line.getGroup(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                        
            if kiMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        
            if kkMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        
            if kcMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                       
            if keMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
#======================================================================================================#
#======================================================================================================#
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = line.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = random.choice(KAC).getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = random.choice(KAC).getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = random.choice(KAC).getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
#======================================================================================================#
#======================================================================================================#
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass 
                                  
        if op.type == 13:
            if op.param1 in protectcancl:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
#======================================================================================================#
#======================================================================================================#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                  
        if op.type == 19:
            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                if op.param3 in admin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      
        if op.type == 19:
            if op.param2 in Bots and admin:
                random.choice(KAC).inviteIntoGroup(op.param1,admin)
#======================================================================================================#
#======================================================================================================#    
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in settings["blacklist"]:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
        
        if op.type == 19:
            if lineMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        line.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            line.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if kiMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if kkMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                line.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if kcMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if keMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = line.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    line.kickoutFromGroup(op.param1,[op.param2])
                                    line.updateGroup(G)
                                    Ticket = line.reissueGroupTicket(op.param1)
                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = line.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    line.updateGroup(G)
                                    Ticket = line.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
                  
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        line.findAndAddContactsByMid(op.param1,admin)
                        kc.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,admin)
                                ke.inviteIntoGroup(op.param1,admin)
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                pass
        
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = line.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            line.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                line.findAndAddContactsByMid(target)
                                line.inviteIntoGroup(msg.to,[target])
                                line.sendText(msg.to,"Invite " + _name)
                                settings["invite"] = False
                                break                              
                            except:             
                                    line.sendText(msg.to,"ᴇʀʀᴏʀ")
                                    settings["invite"] = False
                                    break
            else:
                if settings["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = line.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            line.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                line.findAndAddContactsByMid(target)
                                line.inviteIntoGroup(msg.to,[target])
                                line.sendText(msg.to,"Invite " + _name)
                                settings["invite"] = False
                                break                              
                            except:             
                                    line.sendText(msg.to,"ᴇʀʀᴏʀ")
                                    settings["invite"] = False
                                    break
                                    
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"already")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"Deleted")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"It is not in the black list")
               elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Already")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"Aded")

               elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"Deleted")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"It is not in the black list")

               elif settings["contact"] == True:
                    msg.contentType = 0
                    line.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = line.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        line.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = line.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        line.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#UPDATE FOTO
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                      path = line.downloadObjectMsg(msg_id)
                      settings["groupPicture"] = False
                      line.updateGroupPicture(msg.to, path)
                      line.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                 if sender in settings["foto"]:
                    path = line.downloadObjectMsg(msg_id)
                    del settings["foto"][sender]
                    line.updateProfilePicture(path)
                    line.sendMessage(to,"Foto berhasil dirubah")  
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return   
#==============================================================================#
                if text.lower() == 'help':
                  if msg._from in admin + staff:
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'hk':
                  if msg._from in admin + staff:
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
#==============================================================================#
                elif text.lower() == 'speed':
                  if msg._from in admin + staff:
                    start = time.time()
                    line.sendMessage(msg.to, "...")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                elif text.lower() == 'sp':
                  if msg._from in admin + staff:
                    start = time.time()
                    line.sendMessage(msg.to, "...")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))						
                elif text.lower() == 'restart':
                  if msg._from in admin + staff:
                    line.sendMessage(to, "Tunggu ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == 'waktu':
                  if msg._from in admin + staff:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "Bot berjalan .. {}".format(str(runtime)))
                elif text.lower() == 'info':
                  if msg._from in admin + staff:
                    try:
                        arr = []
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        ret_ = "╔══[ INFO BOTS ]"
                        ret_ += "\n╠✪ NAMA : {}".format(contact.displayName)
                        ret_ += "\n╠✪ GROUP : {}".format(str(len(grouplist)))
                        ret_ += "\n╠✪ TEMAN : {}".format(str(len(contactlist)))
                        ret_ += "\n╠✪ VERSION : SELFBOTS"
                        ret_ += "\n╠══[☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬]"
                        line.sendMessage(msg.to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                  if msg._from in admin + staff:
                    try:
                        ret_ = "Protect ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬"
                        if settings["checkSticker"] == True: ret_ +="🦆 Check Sticker「on」\n"
                        else: ret_ +="🦆 Check Sticker「off」\n"
                        if settings["autoJoinTicket"] == True: ret_ += "🦆 Auto Join Ticket「on」\n"
                        else: ret_ += "🦆 Auto Join Ticket「off」\n"
                        if settings["autoRead"] == True: ret_ += "🦆 Auto Read 「on」\n"
                        else: ret_ += "🦆 Auto Read 「off」\n"
                        if settings["contact"] == True: ret_ +="🦆 Contact「on」\n"
                        else: ret_ +="🦆 Contact「off」\n"
                        if settings["autoJoin"] == True: ret_ +="🦆 Autojoin「on」\n"
                        else: ret_ +="🦆 Autojoin「off」\n"
                        if msg.to in welcome: ret_ +="🦆 Welcome「on」\n"
                        else: ret_ +="🦆 Welcome「off」\n"
                        if settings["autoLeave"] == True: ret_ +="🦆 Autoleave「on」\n"
                        else: ret_ +="🦆 Autoleave「off」\n"
                        if msg.to in protectqr: ret_ +="🦆 Protecturl「on」\n"
                        else: ret_ +="🦆 Protecturl「off」\n"
                        if msg.to in protectjoin: ret_ +="🦆 Protectjoin「on」\n"
                        else: ret_ +="🦆 Protectjoin「off」\n"
                        if msg.to in protectkick: ret_ +="🦆 Protectkick「on」\n"
                        else: ret_ +="🦆 Protectkick「off」\n"
                        if msg.to in protectcancel: ret_ +="🦆 Protectcancel「on」\n"
                        else: ret_ +="🦆 Protectcancel「off」\n"
                        if msg.to in protectinvite: ret_ +="🦆 Protectinvite「on」\n"
                        else: ret_ +="🦆 Protectinvite「off」\n"
                        ret_ += "\n☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif "Gcel:" in msg.text:
                  if msg._from in admin + staff:
                    try:
                        strnum = msg.text.replace("Gcel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    line.sendText(msg.to,"Undangan yang ditutup ditolak")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,strnum + " Anggota grup secara otomatis menolak undangan.")
                                else:
                                    line.sendText(msg.to,strnum + "Kelompok-kelompok berikut ditolak otomatis")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,"Value is wrong")
                        else:
                                line.sendText(msg.to,"Bizarre ratings")
                elif text.lower() == "autojoin on":
                  if msg._from in admin + staff:
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto join")
                elif text.lower() == "autojoin off":
                  if msg._from in admin + staff:
                    settings["autoJoin"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto join")
                elif text.lower() == "autoleave on":
                  if msg._from in admin + staff:
                    settings["autoLeave"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto leave")
                elif text.lower() == "autoleave off":
                  if msg._from in admin + staff:
                    settings["autoLeave"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto leave")
                elif text.lower() == "autojointicket on":
                  if msg._from in admin + staff:
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                elif text.lower() == "autoJoinTicket off":
                  if msg._from in admin + staff:
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                elif text.lower() == "k on":
                  if msg._from in admin + staff:
                    settings["checkContact"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan check details contact")
                elif text.lower() == "k off":
                  if msg._from in admin + staff:
                    settings["checkContact"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan check details contact")
                elif text.lower() == "sticker on":
                  if msg._from in admin + staff:
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan check details sticker")
                elif text.lower() == "sticker off":
                  if msg._from in admin + staff:
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan check details sticker")
                elif text.lower() == "crash":
                  if msg._from in admin + staff:
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                elif msg.text.lower() == "gift":
                  if msg._from in admin + staff:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)                  
#==============================================================================#
                elif text.lower() == 'creator':
                  if msg._from in admin + staff:
                    line.sendText(msg.to,"Creator kami ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬") 
                    ma = ""
                    for i in creator:
                        ma = line.getContact(i)
                        line.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                elif text.lower() == 'me':
                  if msg._from in admin + staff:
                    sendMessageWithMention(to, msg._from)
                elif msg.text.lower().startswith("mid "):
                  if msg._from in admin + staff:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}".format(str(ls))
                        line.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("status "):
                  if msg._from in admin + staff:
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ status ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("foto "):
                  if msg._from in admin + staff:
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("video "):
                  if msg._from in admin + staff:
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                  if msg._from in admin + staff:
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
#==============================================================================#              
                elif msg.text.lower().startswith("mimicadd "):
                  if msg._from in admin + staff:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                  if msg._from in admin + staff:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                  if msg._from in admin + staff:
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                  if msg._from in admin + staff:
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == 'gcreator':
                  if msg._from in admin + staff:
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "")
                elif text.lower() == 'gcid':
                  if msg._from in admin + staff:
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ID GROUP \n" + gid.id)
                elif text.lower() == 'gfoto':
                  if msg._from in admin + staff:
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'gticket':
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'gticket on':
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'gticket off':
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Berhasil menutup grup qr")
                elif "bc:" in msg.text:
                  if msg._from in admin + staff:
                    bctxt = text.replace("bc:","")
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendMessage(manusia,(bctxt))
                
                elif text.lower() == 'ginfo':
                  if msg._from in admin + staff:
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Done ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'gmlist':
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'glist':
                  if msg._from in admin + staff:
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))

                elif text.lower() == 'b1glist':
                  if msg._from in admin + staff:
                        groups = ki.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        ki.sendMessage(to, str(ret_))

                elif text.lower() == 'b2glist':
                  if msg._from in admin + staff:
                        groups = kk.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kk.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        kk.sendMessage(to, str(ret_))

                elif text.lower() == 'b3glist':
                  if msg._from in admin + staff:
                        groups = kc.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kc.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        kc.sendMessage(to, str(ret_))

                elif text.lower() == 'b4glist':
                  if msg._from in admin + staff:
                        groups = ke.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ke.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        ke.sendMessage(to, str(ret_))						
#==============================================================================#
                elif text.lower() == 'kumpul':
                  if msg._from in admin + staff:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members if contact.mid != lineMID]
                    k = len(nama)//500
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*500 : (a+1)*500]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "Total {} members".format(str(len(nama))))          

                elif text.lower() == 'cek':
                  if msg._from in admin + staff:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"cctv telah diaktifkan")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "ngintip pelaku cctv:\n" + readTime)
                            
                elif text.lower() == 'ciduk':
                  if msg._from in admin + staff:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ pelaku ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ pelaku ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ pelaku ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"cctv has not been set.")
#==============================================================================#   
                elif "Bcvc " in msg.text:
                  if msg._from in admin + staff:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam satu jiwa.. by. BEBEK TEAM BOTS")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbcv " in msg.text:
                  if msg._from in admin + staff:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam satu jiwa.. by. BEBEK TEAM BOTS")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Wikipedia " in msg.text:
                  if msg._from in admin + staff:
                      try:
                          wiki = msg.text.lower().replace("Wikipedia ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))

                elif text.lower() == 'kalender':
                  if msg._from in admin + staff:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                
                elif "image " in msg.text.lower():
                  if msg._from in admin + staff:
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
               
                elif "music " in msg.text.lower():
                  if msg._from in admin + staff:
                    try:
                        dan = text.replace("music ","")
                        r = requests.get("http://leert.corrykalam.gq/joox.php?song={}"+urllib.parse.quote(dan))
                        data = r.json()
                        l = data["lyric"].replace("ti:","Judul: ")
                        i = l.replace("ar:","Penyanyi: ")
                        r = i.replace("al:","Album: ")
                        ii = r.replace("[by:]","")
                        k = ii.replace("[offset:0]","")
                        lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                        line.sendImageWithURL(msg.to, data["image"])
                        t = "[ Music ]"
                        t += "\n\nJudul: "+str(data["title"])
                        t+="\nPenyanyi: "+str(data["singer"])
                        t+="\n\n[ Finish ]\n\n"+str(lirik)
                        line.sendMessage(msg.to, str(t))
                        line.sendAudioWithURL(msg.to, data["url"])
                        line.sendText(msg.to,"Tuh Lagunya Kak (^_^)")
                    except Exception as error:
                        pass
                
                elif "musik " in msg.text.lower():
                    try:                    
                        search = text.replace("musik ","")
                        r = requests.get("http://leert.corrykalam.gq/joox.php?song={}"+urllib.parse.quote(search))
                        data = r.text
                        data = json.loads(data)
                        info = data["info"]
                        audio = data["audio"]
                        hasil = "「 Hasil Musik 」\n"
                        hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                        hasil += "\nJudul : {}".format(str(info["judul"]))
                        hasil += "\nAlbum : {}".format(str(info["album"]))
                        hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                        hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                        hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                        line.sendImageWithURL(to, str(data["gambar"]))
                        line.sendMessage(to, str(hasil))
                        line.sendMessage(to, "Downloading...")
                        line.sendMessage(to, "「 Result MP3 」")
                        line.sendAudioWithURL(to, str(audio["mp3"]))
                        line.sendMessage(to, "「 Result M4A 」")
                        line.sendVideoWithURL(to, str(audio["m4a"]))
                        line.sendMessage(to, "Success Download...")
                    except Exception as error:
                        pass
                        
                elif "yt " in msg.text.lower():
                  if msg._from in admin + staff:
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif 'ID ' in msg.text:
                  if msg._from in admin + staff:
                    msgs = msg.text.replace('ID ','')
                    con = line.findContactsByUserid(msgs)
                    if True:
                        line.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                        line.sendMessage(msg.to, None, contentMetadata={'mid': con.mid}, contentType=13)

                elif "smule " in msg.text.lower():
                  if msg._from in admin + staff:
                    tob = msg.text.lower().replace("smule ","")
                    line.sendText(msg.to,"Title : "+tob+"\nSource : Smule\nLink : https://www.smule.com/search?q=" + tob)
                    line.sendText(msg.to,"Tuh Linknya Kak (^_^)")
#============================================================================================#                                
                elif text.lower() == 'tlist':
                  if msg._from in admin + staff:
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎List Friend🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎List Friend🎎\n\nTotal Teman : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["Cekban"]: 
                  if msg._from in admin + staff:
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════Daftar Akun Yang di Blocked═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════List Blocked════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == "bokep":
                  if msg._from in admin + staff:
                	  line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")

                elif msg.text in ["keluar"]:
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            ki.leaveGroup(receiver)
                            kk.leaveGroup(receiver)
                            kc.leaveGroup(receiver)
                            ke.leaveGroup(receiver)
                            line.leaveGroup(receiver)		
                        except:
                            pass
                          
                elif msg.text in ["LG"]: #Melihat List Group
                  if msg._from in admin:
                    gids = line.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      h += "[•]%s Member\n" % (line.getGroup(i).name   +"👉"+str(len(line.getGroup(i).members)))
                      line.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
                elif msg.text in ["LG2"]:
                  if msg._from in admin:
                    gid = line.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (line.getGroup(i).name,i)
                    line.sendText(msg.to,h)
#===========================================================================#
                elif msg.text in ["bsiri"]:
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = line.getGroup(msg.to)
                        if kiMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                line.sendText(msg.to,"error")
                            for target in sirilist:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                except:
                                    pass

                elif msg.text in ["b1siri"]:
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki.getGroup(msg.to)
                        if kkMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki.sendText(msg.to,"error")
                            for target in sirilist:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                
                elif "/invite: " in msg.text:
                  if msg._from in owner:
                    gid = msg.text.replace("/invite: ","")
                    if gid == "":
                      line.sendText(msg.to,"Invalid group id")
                    else:
                      try:
                        line.findAndAddContactsByMid(msg._from)
                        line.inviteIntoGroup(gid,[msg._from])
                      except:
                        line.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

                elif "Spam " in msg.text:
                  if msg._from in admin + staff:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
#=============COMMAND KICKER===========================#
                elif text.lower() == 'cin':
                  if msg._from in admin + staff:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)   
                        group.preventedJoinByTicket = True
                        random.choice(KAC).updateGroup(group)
                        print ("Kicker Join")

                elif 'kiss ' in text.lower():
                  if msg._from in admin + staff:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])      
                              print ("Bots kick User")
                          except:
                              random.choice(KAC).sendMessage(msg.to,"Limit kaka 😫")

                elif 'desah ' in text.lower():
                  if msg._from in admin + staff:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              line.kickoutFromGroup(msg.to,[target])             
                              print ("sb Kick User")
                          except:
                              line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'c1 ' in text.lower():
                  if msg._from in admin + staff:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              ki.kickoutFromGroup(msg.to,[target])             
                              print ("b1 Kick User")
                          except:
                              ki.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'c2 ' in text.lower():
                  if msg._from in admin + staff:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              kk.kickoutFromGroup(msg.to,[target])           
                              print ("b2 Kick User")
                          except:
                              kk.sendMessage(msg.to,"Limit kaka 😫")                                                      
                               
                elif "ancur" in msg.text:
                  if msg._from in admin + staff:
                	  if msg.toType == 2:
                           _name = msg.text.replace("ancur","")
                           gs = line.getGroup(receiver)
                           line.sendMessage(receiver,"papay kk..")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                   targets.append(g.mid)
                           if targets == []:
                               line.sendMessage(receiver,"Not found.")
                           else:
                               for target in targets:
                             	  if not target in Bots:
                                       try:
                                           klist=[ki,kk,kc,ke,line]
                                           kicker=random.choice(klist)
                                           kicker.kickoutFromGroup(receiver,[target])
                                           print((receiver,[g.mid]))
                                       except:
                                           line.sendMessage(receiver,"Group bersih")
                                           print ("Bersih Group")

                elif text.lower() == "hapuschat":
                        if msg._from in admin + staff:
                            try:
                                ki.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2)  
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"Done")
                            except:
                                pass
                                print ("done")

                elif text.lower() == "balik":
                    if msg._from in admin + staff:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)  
                        line.leaveGroup(msg.to)
                        print ("Kicker Leave")

                elif text.lower() == "balikall":
                    if msg._from in owner:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki.leaveGroup(i)
                            kk.leaveGroup(i)
                            kc.leaveGroup(i)
                            ke.leaveGroup(i)   
                            line.leaveGroup(i)
                            print ("Kicker Leave All group")

                elif "myname: " in text.lower():
                    if msg._from in owner:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"succes.. " + string)
                        print ("Update Name")

                elif "bio: " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"succes.. " + string)
                        print ("Update Bio Succes")

                elif text.startswith("1name: "):
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                elif text.startswith("2name: "):
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                elif text.startswith("3name: "):
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                elif text.startswith("4name: "):
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = ke.getProfile()
                        profile.displayName = string
                        ke.updateProfile(profile)
                        ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#===========BOT UPDATE============#
                elif text.lower() == 'absen':
                  if msg._from in admin + staff:
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                    if jml <= 40:
                        mentionMembers(msg.to, nama)
                    if jml > 20 and jml < 40:
                        for i in range (20, 40):
                            nm1 += [nama[i]]
                        mentionMembers(msg.to, nm1)
                        for j in range (20, len(nama)-1):
                            nm2 += [nama[j]]
                        mentionMembers(msg.to, nm2)
                    if jml > 20 and jml < 40:
                        for i in range (0, 20):
                            nm1 += [nama[i]]
                        mentionMembers(msg.to, nm1)
                        for j in range (0, 20):
                            nm2 += [nama[j]]
                        mentionMembers(msg.to, nm2)
                        for k in range (20, len(nama)-1):
                            nm3 += [nama[k]]
                        mentionMembers(msg.to, nm3)
                    if jml > 20 and jml < 40:
                        for i in range (0, 20):
                            nm1 += [nama[i]]
                        mentionMembers(msg.to, nm1)
                        for j in range (0, 20):
                            nm2 += [nama[j]]
                        mentionMembers(msg.to, nm2)
                        for k in range (0, 20):
                            nm3 += [nama[k]]
                        mentionMembers(msg.to, nm3)
                        for l in range (20, len(nama)-1):
                            nm4 += [nama[l]]
                        mentionMembers(msg.to, nm4)
                    if jml > 20 and jml < 40:
                        for i in range (0, 20):
                            nm1 += [nama[i]]
                        mentionMembers(msg.to, nm1)
                        for j in range (0, 20):
                            nm2 += [nama[j]]
                        mentionMembers(msg.to, nm2)
                        for k in range (0, 20):
                            nm3 += [nama[k]]
                        mentionMembers(msg.to, nm3)
                        for l in range (0, 20):
                            nm4 += [nama[l]]
                        mentionMembers(msg.to, nm4)
                        for m in range (20, len(nama)-1):
                            nm5 += [nama[m]]
                        mentionMembers(msg.to, nm5)
                        
                elif text.lower() == "botlist":
                  if msg._from in admin + staff:
                      ma = ""
                      a = 0
                      for m_id in Bots:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬\n\n"+ma+"\nTotal「%s」" %(str(len(Bots))))

                elif text.lower() == "adminlist":
                  if msg._from in admin + staff:
                      ma = ""
                      mb = ""
                      mc = ""
                      a = 0
                      b = 0
                      c = 0
                      for m_id in owner:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      for m_id in admin:
                          b = b + 1
                          end = '\n'
                          mb += str(b) + ". " +line.getContact(m_id).displayName + "\n"
                      for m_id in staff:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬\n\nOwner:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬" %(str(len(owner)+len(admin)+len(staff))))

                elif text.lower() ==  "protectlist":
                  if msg._from in admin + staff:
                      ma = ""
                      mb = ""
                      mc = ""
                      md = ""
                      a = 0
                      b = 0
                      c = 0
                      d = 0
                      gid = protectqr
                      for group in gid:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getGroup(group).name + "\n"
                      gid = protectkick
                      for group in gid:
                          a = a + 1
                          end = '\n'
                          mb += str(a) + ". " +line.getGroup(group).name + "\n"
                      gid = protectjoin
                      for group in gid:
                          b = b + 1
                          end = '\n'
                          md += str(b) + ". " +line.getGroup(group).name + "\n"
                      gid = protectcancel
                      for group in gid:
                          b = b + 1
                          end = '\n'
                          md += str(b) + ". " +line.getGroup(group).name + "\n"
                      gid = protectcancl
                      for group in gid:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getGroup(group).name + "\n"
                          gid = protectinvite
                      for group in gid:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getGroup(group).name + "\n"
                      line.sendMessage(msg.to,"Protection\n\nProtect Url :\n"+ma+"\nProtect Kick:\n"+mb+"\nprotect Join:\n"+md+"\nProtect Cancel:\n"+md+"\nProtect Cancl:\n"+md+"\nProtect Invite:\n"+mc+"\nTotal「%s」Grup protect" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                elif text.lower() ==  "respon":
                  if msg._from in admin + staff:
                      line.sendText(msg.to,"A")
                      ki.sendText(msg.to,"B")
                      kk.sendText(msg.to,"C")
                      kc.sendText(msg.to,"D")
                      ke.sendText(msg.to,"E")    
                      random.choice(KAC).sendText(msg.to,"Semua Udah Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu")
                      
                elif text.lower() == "salam":
                  if msg._from in admin + staff:
                      line.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                      line.sendText(msg.to,"Assalamu'alaikum.Wr,Wb")
                      
                elif text.lower() == "salam2":
                  if msg._from in admin + staff:
                      line.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                      line.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                      
                elif text.lower() == "sayang":
                  if msg._from in admin + staff:
                      ki.sendText(msg.to,"Yaa\nSayang")
                      kk.sendText(msg.to,"Kangen\nSayang")
                      kc.sendText(msg.to,"Kojom\nSayang")
                      ke.sendText(msg.to,"Ehhhh\nSayang")
                      line.sendText(msg.to,"Callme\nSayang")

                elif text.lower() == "cinta":
                  if msg._from in admin + staff:
                      ki.sendMessage(msg.to,responsename1)
                      kk.sendMessage(msg.to,responsename2)
                      kc.sendMessage(msg.to,responsename3)
                      ke.sendMessage(msg.to,responsename4)
                      line.sendMessage(msg.to,responsename)
                      ks.sendMessage(msg.to,responsename5)
                      kt.sendMessage(msg.to,responsename6)
                      ka.sendMessage(msg.to,responsename7)
                      kb.sendMessage(msg.to,responsename8)
                      ko.sendMessage(msg.to,responsename9)
                      
                elif text.lower() == "papay":
                  if msg._from in admin:
                      G = line.getGroup(msg.to)
                      line.sendText(msg.to, "Bye bye fams "+str(G.name))
                      line.leaveGroup(msg.to)
                      
                elif text.lower() == "buka qr":
                  if msg._from in admin:
                      if msg.toType == 2:
                         X = line.getGroup(msg.to)
                         X.preventedJoinByTicket = False
                         line.updateGroup(X)
                                  
                elif text.lower() == "tutup qr":
                  if msg._from in admin:
                      if msg.toType == 2:
                         X = line.getGroup(msg.to)
                         X.preventedJoinByTicket = True
                         line.updateGroup(X)

                elif text.lower() == "link":
                  if msg._from in admin:
                      if msg.toType == 2:
                         x = line.getGroup(msg.to)
                         if x.preventedJoinByTicket == True:
                            x.preventedJoinByTicket = False
                            line.updateGroup(x)
                         gurl = line.reissueGroupTicket(msg.to)
                         line.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                
                elif text.lower() == "invite":
                  if msg._from in admin + staff:
                      settings["invite"] = True
                      line.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                      
                elif text.lower() == "1invite":
                  if msg._from in admin + staff:
                      settings["invite"] = True
                      ki.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                        
                elif text.lower() == "gantipp":
                  if msg._from in admin + staff:
                      settings["foto"] = True
                      line.sendMessage(to, "Silahkan kirim gambarnya")
                        
                elif text.lower() == "out: ":
                  if msg._from in owner:
                        proses = text.split(" ")
                        ng = text.replace(proses[0] + " ","")
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            h = line.getGroup(i).name
                            if h == ng:
                                ki.leaveGroup(i)
                                kk.leaveGroup(i)
                                kc.leaveGroup(i)
                                ke.leaveGroup(i)
                                line.leaveGroup(i)
                                line.sendMessage(to,"Berhasil keluar dari grup " +h)
                                
                elif text.lower() == "masuk":
                  if msg._from in admin:
                      try:
                          anggota = [kiMID,kkMID,kcMID,keMID]
                          line.inviteIntoGroup(msg.to, anggota)
                          ki.acceptGroupInvitation(msg.to)
                          kk.acceptGroupInvitation(msg.to)
                          kc.acceptGroupInvitation(msg.to)
                          ke.acceptGroupInvitation(msg.to)
                      except:
                          pass
                        
                elif msg.text.lower() == "1foto":
                  if msg._from in admin:
                      settings["foto"][kiMID] = True
                      ki.sendText(msg.to,"Kirim fotonya.....")

                elif msg.text.lower() == "2foto":
                  if msg._from in admin:
                      settings["foto"][kkMID] = True
                      kk.sendText(msg.to,"Kirim fotonya.....")
                      
                elif msg.text.lower() == "3foto":
                  if msg._from in admin:
                      settings["foto"][kcMID] = True
                      kc.sendText(msg.to,"Kirim fotonya.....")

                elif msg.text.lower() == "4foto":
                  if msg._from in admin:
                      settings["foto"][keMID] = True
                      ke.sendText(msg.to,"Kirim fotonya.....")
#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'wc on':
                  if msg._from in admin + staff:
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready on")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready on")
                elif msg.text.lower() == 'wc off':
                  if msg._from in admin + staff:
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready off")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready off")

                elif msg.text.lower() == 'left on':
                  if msg._from in admin + staff:
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready on")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready on")
                elif msg.text.lower() == 'left off':
                  if msg._from in admin + staff:
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready off")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"Ready on")
                                
                elif text.lower() == "sider on":
                  if msg._from in admin + staff:
                      try:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          line.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                          del cctv['point'][msg.to]
                          del cctv['sidermem'][msg.to]
                          del cctv['cyduk'][msg.to]
                      except:
                          pass
                      cctv['point'][msg.to] = msg.id
                      cctv['sidermem'][msg.to] = ""
                      cctv['cyduk'][msg.to]=True

                elif text.lower() == "sider off":
                  if msg._from in admin + staff:
                    if msg.to in cctv['point']:
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        cctv['cyduk'][msg.to]=False
                        line.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                    else:
                        line.sendMessage(msg.to, "Sudak tidak aktif")
#===========Protection============#
                elif 'Protecturl ' in msg.text:
                      spl = msg.text.replace('Protecturl ','')
                      if spl == 'on':
                          if msg.to in protectqr:
                               msgs = "Protect url sudah aktif"
                          else:
                               protectqr.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectqr:
                                 protectqr.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect url sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectkick ' in msg.text:
                      spl = msg.text.replace('Protectkick ','')
                      if spl == 'on':
                          if msg.to in protectkick:
                               msgs = "Protect kick sudah aktif"
                          else:
                               protectkick.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectkick:
                                 protectkick.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect kick sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectjoin ' in msg.text:
                                  spl = msg.text.replace('Protectjoin ','')
                                  if spl == 'on':
                                      if msg.to in protectjoin:
                                           msgs = "Protect join sudah aktif"
                                      else:
                                           protectjoin.append(msg.to)
                                           ginfo = line.getGroup(msg.to)
                                           msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                      line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                                  elif spl == 'off':
                                        if msg.to in protectjoin:
                                             protectjoin.remove(msg.to)
                                             ginfo = line.getGroup(msg.to)
                                             msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                        else:
                                             msgs = "Protect join sudah tidak aktif"
                                        line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Protectcancel ' in msg.text:
                      spl = msg.text.replace('Protectcancel ','')
                      if spl == 'on':
                          if msg.to in protectcancel:
                               msgs = "Protect cancel sudah aktif"
                          else:
                               protectcancel.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectcancel:
                                 protectcancel.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect cancel sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Protectcancl ' in msg.text:
                      spl = msg.text.replace('Protectcancl ','')
                      if spl == 'on':
                          if msg.to in protectcancel:
                               msgs = "Protect cancl sudah aktif"
                          else:
                               protectcancl.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect cancl diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectcancl:
                                 protectcancl.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect cancl dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect cancel sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectinvite ' in msg.text:
                      spl = msg.text.replace('Protectinvite ','')
                      if spl == 'on':
                          if msg.to in protectinvite:
                               msgs = "Protect invite sudah aktif"
                          else:
                               protectinvite.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectinvite:
                                 protectinvite.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect invite sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Cinta ' in msg.text:
                  if msg._from in admin + staff:
                      spl = msg.text.replace('Cinta ','')
                      if spl == 'on':
                          if msg.to in protectqr:
                               msgs = ""
                          else:
                              protectqr.append(msg.to)
                          if msg.to in protectkick:
                              msgs = ""
                          else:
                              protectkick.append(msg.to)
                          if msg.to in protectjoin:
                              msgs = ""
                          else:
                              protectjoin.append(msg.to)
                          if msg.to in protectcancel:
                              msgs = ""
                          else:
                              protectcancel.append(msg.to)
                          if msg.to in protectcancl:
                              msgs = ""
                          else:
                              protectcancl.append(msg.to)
                          if msg.to in protectinvite:
                              ginfo = line.getGroup(msg.to)
                              msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                          else:
                              protectinvite.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectqr:
                                 protectqr.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectkick:
                                protectkick.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectjoin:
                                protectjoin.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectcancel:
                                protectcancel.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectcancl:
                                protectcancl.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectinvite:
                                protectinvite.remove(msg.to)
                                ginfo = line.getGroup(msg.to)
                                msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                            else:
                                ginfo = line.getGroup(msg.to)
                                msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#===========ADMIN ADD============#
                elif ("Adminon " in msg.text):
                  if msg._from in owner:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                      for target in targets:
                              try:
                                  admin.append(target)
                                  line.sendMessage(msg.to,"Berhasil menambahkan admin")
                              except:
                                  pass

                elif ("Staffon " in msg.text):
                  if msg._from in admin:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                      for target in targets:
                              try:
                                  staff.append(target)
                                  line.sendMessage(msg.to,"Berhasil menambahkan staff")
                              except:
                                  pass

                elif ("Adminoff " in msg.text):
                  if msg._from in owner:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                      for target in targets:
                          if target not in Bots:
                              try:
                                  admin.remove(target)
                                  line.sendMessage(msg.to,"Berhasil menghapus admin")
                              except:
                                  pass

                elif ("Staffoff " in msg.text):
                  if msg._from in admin:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                      for target in targets:
                          if target not in Bots:
                              try:
                                  staff.remove(target)
                                  line.sendMessage(msg.to,"Berhasil menghapus admin")
                              except:
                                  pass
#===========COMMAND BLACKLIST============#
                elif ("Ban " in msg.text):
                  if msg._from in admin + staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                   for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               line.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                           except:
                               pass
   
                elif text.lower() == 'banlist':
                  if msg._from in admin + staff:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"Tidak ada blacklist")
                        ki.sendMessage(msg.to,"Tidak ada blacklist")
                        kk.sendMessage(msg.to,"Tidak ada blacklist")
                        kc.sendMessage(msg.to,"Tidak ada blacklist")
                        ke.sendMessage(msg.to,"Tidak ada blacklist")
                    else:
                      ma = ""
                      a = 0
                      for m_id in settings["blacklist"]:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ki.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kk.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kc.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ke.sendMessage(msg.to,"☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))

                elif text.lower() == 'clearban':
                  if msg._from in admin + staff:
                    settings["blacklist"] = {}
                    ragets = line.getContacts(settings["blacklist"])
                    mc = "「%i」User Blacklist" % len(ragets)
                    line.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ki.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kk.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kc.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ke.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              
                elif text.lower() == 'reject':
                  if msg._from in admin + staff:
                    gid = line.getGroupIdsInvited()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    if settings["lang"] == "JP":
                        line.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                    else:
                        line.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
#===========================================================================================#
            elif msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "╔══[ Details Contact ]"
                        ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                        ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                        ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                        ret_ += "\n╚══[ Finish ]"
                        line.sendMessage(to, str(ret_))
                    except:
                        line.sendMessage(to, "Kontak tidak valid")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
#======================================================================================================#
#======================================================================================================#                  
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)  
                ks.leaveRoom(op.param1)
                kt.leaveRoom(op.param1)
                ka.leaveRoom(op.param1)
                kb.leaveRoom(op.param1)
                ko.leaveRoom(op.param1)   
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)  
                ks.leaveRoom(op.param1)
                kt.leaveRoom(op.param1)
                ka.leaveRoom(op.param1)
                kb.leaveRoom(op.param1)
                ko.leaveRoom(op.param1)
#==============================================================================#
#==============================================================================#                             
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                    ki.sendChatChecked(to, msg_id)
                    kk.sendChatChecked(to, msg_id)
                    kc.sendChatChecked(to, msg_id)
                    ke.sendChatChecked(to, msg_id)					
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = line.findGroupByTicket(ticket_id)
                            line.acceptGroupInvitationByTicket(group.id,ticket_id)
                            group = ki.findGroupByTicket(ticket_id)
                            ki.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = kk.findGroupByTicket(ticket_id)
                            kk.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = kc.findGroupByTicket(ticket_id)
                            kc.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = ke.findGroupByTicket(ticket_id)
                            ke.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = ks.findGroupByTicket(ticket_id)
                            ks.acceptGroupInvitationByTicket(group.id,ticket_id)
                            group = kt.findGroupByTicket(ticket_id)
                            kt.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = ka.findGroupByTicket(ticket_id)
                            ka.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = kb.findGroupByTicket(ticket_id)
                            kb.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            group = ko.findGroupByTicket(ticket_id)
                            ko.acceptGroupInvitationByTicket(ra.id,ticket_id)
                            line.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                      
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = "" + random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["Don't Tag Me! iam Bussy!, ",cName + "Ada perlu apa, ?",cName + " pc aja klo urgent! sedang sibuk,", "berisik peakk lu, ", cName + " kangen?pm aj lngsung..ga ush ngetag","kangen bilang gak usah tag tag, " + cName, "maaf sedang meeting jangan di ganggu?, " + cName, "apa sih,lgi tanggung nie?, " + cName + "kampret ganggu mulu", "pulang gih sana ngtag mulu dasar vekok, " + cName + "?","aya naon, ?" + cName + "lagi syuting nih -_-","dasar jones kerjaan nya cuma tag mele😒"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          #sendMessageWithMention(to, contact.mid)
                                          line.sendMessage(msg.to, None, contentMetadata={"STKID":"17165590","STKPKGID":"1454876","STKVER":"1"}, contentType=7)
                                          break
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
           #print ("MEMBER JOIN TO GROUP")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendMessage(op.param1,line.getContact(op.param2).displayName + str(ginfo.name))
             line.sendMessage(to,str(settings["welcome jngn lupa cek note biar pinter.."]))
             line.sendImageWithURL(op.param1,image)
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if settings['Lv'] == True:
            if op.param2 in bot1:
                return
            line.sendMessage(op.param1,line.getContact(op.param2).displayName)
            line.sendMessage(op.param1,str(settings["selamat jalan moga tenang di alam sana.."]))
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        path = "http://dl.profile.line-cdn.net/" + line.getContact(op.param2).pictureStatus
                        Name = line.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n~ " + Name
                            siderMembers(op.param1, [op.param2])
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    line.sendImageWithURL(op.param1, path)
                                    line.sendText(op.param1, nick[0] + "Ngintip Aja Niih. . .\nChat Kek Idiih (-__-) ")
                                else:
                                    line.sendImageWithURL(op.param1, path)
                                    line.sendText(op.param1, nick[1] + "Betah Banget Jadi Penonton. . .\nChat Napa (-__-) ")
                            else:
                                line.sendImageWithURL(op.param1, path)
                                line.sendText(op.param1, Name[0] + "Ngapain Kak Ngintip Aja???\nSini Gabung Chat...")
                    else:
                        line.sendImageWithURL(op.param1, path)
                        line.sendText(op.param1, Name[1] + "Tukang ngintip ol noh...")
                else:
                    pass
            except:
                pass
        else:
            pass

        #if op.type == 55:
         #   try:
          #      if cctv['cyduk'][op.param1]==True:
           #         if op.param1 in cctv['point']:
            #            Name = line.getContact(op.param2).displayName
             #           if Name in cctv['sidermem'][op.param1]:
              #              pass
               #         else:
                #            cctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                 #           if " " in Name:
                  #          	nick = Name.split(' ')
                   #         if len(nick) == 2:
                    #        	line.sendMessage(op.param1, "Nah " +nick[0])
                     #       summon(op.param1, [op.param2])
                    #else:
                     #   pass
                #else:
                 #   pass
            #except:
             #   pass
        if op.type == 55:
            print ("[ 55 ] succes")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
