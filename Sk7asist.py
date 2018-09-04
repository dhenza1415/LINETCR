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
line = LINE("EwLKRjb2gIc2fwLuaK3d.jB/U5D2EIoY5xGkQ7FOTtq.1kJkN87TzvnXMGxBEVDqEgCfp1S/8891MLVWIJu6S9g=")
line.log("Auth Token : " + str(line.authToken))

ki = LINE("EwSWhgJ3rpm9UJapNxPa.y5VxpNSHKkly4g+m7/UdgG.0vC9JMFGAp7LHn/bT141oGO+SkG6mYpxl8RBhwAM3hI=")
ki.log("Auth Token : " + str(ki.authToken))

kk = LINE("Ew6ffhWhAJHX9Zd1Elw1.tymKwInKTygiyMM1IX4vuq.Z/pXh+y9aSIsgc+jWj1dNiZ63f2Oz3IwVu4kTRAlvmU=")
kk.log("Auth Token : " + str(kk.authToken))

kc = LINE("EwPL9GuJT7Yg3LI1TeM0.6J6qgHD0ZdGzCmnm366bia.gbwIhg/zNNWIHX63fnfc5mwmvt2uD1VPoM+6A+3+rLU=")
kc.log("Auth Token : " + str(kc.authToken))

ke = LINE("EwuR5GWpcVQ6eGtw7AU4.XuQrezi1qIyJlRlvV0wxra.adC3tl3rOuS2rLo0udQcWrlht3qnQCe0G3R3+t1/lRk=")
ke.log("Auth Token : " + str(ke.authToken))

kt = LINE("EwU9VtpfZhjoswvQYCz2.UgaA6PtgDwrhl20KYKxh8G.28eSP4e5KSlunEqMviYPucDcLqaCuAihxzdyes+/w+c=")
kt.log("Auth Token : " + str(kt.authToken))

ks = LINE ("Ew2fWhvUOtg1yCBHfqZ0.+CiloGc16pmEt5ebFRnHSa.ky9+kaiQSVX2p2Uc/d4+PCCJoEOCnfhSGCNwaY/N2FQ=")
ks.log("Auth Token : " + str(ks.authToken))

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

ktMID = kt.profile.mid
ktProfile = kt.getProfile()
ktSettings = kt.getSettings()

ksMID = ks.profile.mid
ksProfile = ks.getProfile()
ksSettings = ks.getSettings()

oepoll = OEPoll(ks)
oepoll = OEPoll(kt)
oepoll = OEPoll(ke)
oepoll = OEPoll(kc)
oepoll = OEPoll(kk)
oepoll = OEPoll(ki)
oepoll = OEPoll(line)

Bots=[lineMID,kiMID,kkMID,kcMID,keMID,ktMID,ksMID]
KAC = [line,ki,kk,kc,ke,kt]
ABC = [ki,kk,kc,ke,ke,kt]
creator = ["ufdc20b3a00b5e8f31e4f91017eb361b0","ufa6ba7212303e85f5460d9600264471c","ub1c5a71f27b863896e9d44bea857d35b","u0f6df437fe3e32f07c4562308ac430a9"]
admin=['ufdc20b3a00b5e8f31e4f91017eb361b0','ub1c5a71f27b863896e9d44bea857d35b','ufa6ba7212303e85f5460d9600264471c']
Bots = Bots

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = ke.getProfile().displayName
responsename5 = kt.getProfile().displayName

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectguest = []
protectantijs = []
autocancel = []
autoinvite = []
autoleaveroom = []
welcome = []
targets = []
ghost = []
#==============================================================================#
settings = {
    "picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoin": True,
    'autoCancel':{"on":True,"members":1},
    "autoLeave": False,
    "leaveRoom": False,
    "autoJoinTicket": False,
    "atjointicket": False,
    "checkContact": False,
    "contact":False,
    "Wc": False,
    "Lv": False,
    "limit": 100,
    "whitelist":{},
    "commentBlack":{},
    "winvite":{},
    "wblacklist": False,
    "dblacklist": False,
    "stk":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "invite":{},
    "group":{},
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
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

wait = {
    "addbots":False,
    "dellbots":False,
    "contact":False,
    "addadmin":False,
    "delladmin":False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "blacklist": True,
    "addbots":False,
    "dellbots":False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "mention":"Masuk kuy tmnin Cuby",
    "Respontag":"Tag gw buntingin",
    "welcome":"Selamat datang & betah",
    "message":"Terimakasih sudah add saya 😃",
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
}

Protect = {
    "protect": False,
    "cancelprotect5": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "Protectantijs": False,
    "Ghost": False,
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": "",
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
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)

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

contact = kt.getProfile()
backup = kt.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
ackup = ks.getProfile()
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
def sticker():
    if msg.contentType == 7:
       if wait["sticker"] == True:
          msg.contentType = 0
          line.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
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

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
      
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
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
        teman = cl.getAllContactIdsx()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"⏩Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n⏩Group : "+str(len(gid))+"\n⏩Teman : "+str(len(teman))+"\n⏩Expired : In "+hari+"\n⏩Version : SILENBOT\n⏩Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n⏩Runtime : \n • "+bot
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))


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
    myHelp = "╔═[·✪·Help Menu™·✪·]═╗\n" + \
                  "╠❂➣ 「Help」"+ "\n" + \
                  "╠❂➣ 「Hk」"+ "\n" + \
                  "╠❂➣ 「Sp」"+ "\n" + \
                  "╠❂➣ 「Waktu」"+ "\n" + \
                  "╠❂➣ 「Mid @」"+ "\n" + \
                  "╠❂➣ 「LG2」"+ "\n" + \
                  "╠❂➣ 「invite: 」"+ "\n" + \
                  "╠❂➣ 「Set」"+ "\n" + \
                  "╠❂➣ 「Botlist」"+ "\n" + \
                  "╠❂➣ 「Protectlist」"+ "\n" + \
                  "╠❂➣ 「Skpro「On/Off」"+ "\n" + \
                  "╠❂➣ 「Creator」"+ "\n" + \
                  "╠❂➣ 「Autojoin「On/Off」"+ "\n" + \
                  "╠❂➣ 「Autoleave「On/Off」"+ "\n" + \
                  "╠❂➣ 「Autojointicket「On/Off」"+ "\n" + \
                  "╠❂➣ 「K「On/Off」"+ "\n" + \
                  "╠❂➣ 「Sk」"+ "\n" + \
                  "╠❂➣ 「Reject」"+ "\n" + \
                  "╠❂➣ 「Bc:」"+ "\n" + \
                  "╠❂➣ 「Skinvite」"+ "\n" + \
                  "╠❂➣ 「Ban @」"+ "\n" + \
                  "╠❂➣ 「Sklist」"+ "\n" + \
                  "╠❂➣ 「Skcban」"+ "\n" + \
                  "╠❂➣ 「Kabur」"+ "\n" + \
                  "╠❂➣ 「Autojoin on\off」"+ "\n" + \
                  "╠❂➣ 「Cuby masuk」"+ "\n" + \
                  "╠❂➣ 「botmid " + "\n" + \
                  "╠❂➣ 「Skrespon」"+ "\n" + \
                  "╠❂➣ 「Skbuka qr」"+ "\n" + \
                  "╠❂➣ 「Sktutup qr」"+ "\n" + \
                  "╠❂➣ 「Botadd「@」" + "\n" + \
                  "╠❂➣ 「Botdell「@」" + "\n" + \
                  "╠❂➣ 「Sider「on/off」" + "\n" + \
                  "╠❂➣ 「Ytmp3:「Judul lagu」" + "\n" + \
                  "╠❂➣ 「Ytmp4:「Judul video」" + "\n" + \
                  "╠❂➣ 「Music「Judul lagu」" + "\n" + \
                  "╠❂➣ 「Antjs「on/off」" + "\n" + \
                  "╠❂➣ 「Antijs stay" + "\n" + \
                  "╠❂➣ 「Pulang」"+ "\n" + \
                  "╠❂➣ 「Sk qr」"+ "\n" + \
                  "╚═[°✪° ™Silent Bot Pro °✪°]═╝"
    return myHelp

def helpkicker():
    helpKicker = "╔═[·✪Help Kicker™✪·]╗\n" + \
                 "╠❂➣  Sk3 @" + "\n" + \
                 "╠❂➣  Sk2 @" + "\n" + \
                 "╠❂➣  Sk4 @" + "\n" + \
                 "╠❂➣  Sk1 @" + "\n" + \
                 "╠❂➣  Sksiri @"+ "\n" + \
                 "╚[✪™Silent Bot°✪°]╝"
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
        if op.type == 13:
           if ktMID in op.param3:
               G = kt.getGroup(op.param1)
               if settings["autoJoin"] == True:
                   if settings["autoCancel"]["on"] == True:
                       if len(G.members) <= settings["autoCancel"]["members"]:
                           kt.rejectGroupInvitation(op.param1)
                       else:
                           kt.acceptGroupInvitation(op.param1)
                   else:
                       kt.acceptGroupInvitation(op.param1)
               elif settings["autoCancel"]["on"] == True:
                   if len(G.members) <= settings["autoCancel"]["members"]:
                       kt.rejectGroupInvitation(op.param1)
           else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    kt.cancelGroupInvitation(op.param1, matched_list)


        if op.type == 13:
            if ksMID in op.param3:
                G = ks.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ks.rejectGroupInvitation(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ks.rejectGroupInvitation(op.param1)
            else:

                Inviter = op.param3.replace("^^",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ks.cancelGroupInvitation(op.param1, matched_list)

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
            if op.param3 in ktMID:
                if op.param2 in Bots:
                    kt.acceptGroupInvitation(op.param1)
            if op.param3 in ksMID:
                if op.param2 in Bots:
                    ks.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in lineMID:
                            if op.param2 in ksMID:
                                line.acceptGroupInvitation(op.param1)
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
            if op.param3 in lineMID:
		            if op.param2 in ktMID:
		                line.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in kiMID:
                            if op.param2 in ksMID:
                                line.acceptGroupInvitation(op.param1)
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
            if op.param3 in kiMID:
		            if op.param2 in ktMID:
		                ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in kkMID:
                            if op.param2 in ksMID:
                                kk.acceptGroupInvitation(op.param1)
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
            if op.param3 in kkMID:
		            if op.param2 in ktMID:
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
            if op.param3 in kcMID:
		            if op.param2 in ktMID:
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
            if op.param3 in keMID:
		            if op.param2 in ktMID:
		                ke.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in ktMID:
		            if op.param2 in lineMID:
		                kt.acceptGroupInvitation(op.param1)
            if op.param3 in ktMID:
		            if op.param2 in kiMID:
		                kt.acceptGroupInvitation(op.param1)
            if op.param3 in ktMID:
		            if op.param2 in kkMID:
		                kt.acceptGroupInvitation(op.param1)
            if op.param3 in ktMID:
		            if op.param2 in kcMID:
		                kt.acceptGroupInvitation(op.param1)
            if op.param3 in ktMID:
		            if op.param2 in keMID:
		                kt.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in ksMID:
                            if op.param2 in lineMID:
                                ks.acceptGroupInvitation(op.param1)
            if op.param3 in ksMID:
                            if op.param2 in kiMID:
                                ks.acceptGroupInvitation(op.param1)
            if op.param3 in ksMID:
                            if op.param2 in kkMID:
                                ks.acceptGroupInvitation(op.param1)
            if op.param3 in ksMID:
                            if op.param2 in kcMID:
                                ks.acceptGroupInvitation(op.param1)
            if op.param3 in ksMID:
                            if op.param2 in keMID:
                                ks.acceptGroupInvitation(op.param1)

#=============================================================================#
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 in settings["blacklist"]:
                    try:
                        if line.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots:
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
                                if op.param2 not in Bots:
                                    ki.reissueGroupTicket(op.param1)
                                    X = random.choice(KAC).getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(KAC).updateGroup(X)
                        except:
                            try:
                                if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots:
                                        kk.reissueGroupTicket(op.param1)
                                        X = random.choice(KAC).getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).updateGroup(X)
                            except:
                                try:
                                    if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots:
                                            kc.reissueGroupTicket(op.param1)
                                            X = random.choice(KAC).getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(KAC).updateGroup(X)
                                except:
                                    try:
                                        if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots:
                                                ke.reissueGroupTicket(op.param1)
                                                X = random.choice(KAC).getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).updateGroup(X)
                                    except:
                                        try:
                                            if ks.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots:
                                                    ks.reissueGroupTicket(op.param1)
                                                    X = random.choice(KAC).getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ks.kickoutFromGroup(op.param1,[op.param2])
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
                                        try:
                                            G = ks.getGroup(op.param1)
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
                                        try:
                                            ks.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        settings["blacklist"][op.param2] = True
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
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ks.kickoutFromGrup(op.parm1,[op.parm2])
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
                    
            if op.param3 in ktMID:
                if op.param2 in keMID:
                    X = ke.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    X.preventedJoinByTicket = True
                    kt.updateGroup(X)
                    Ti = kt.reissueGroupTicket(op.param1)
                    
            if op.param3 in lineMID:
                if op.param2 in ktMID:
                    X = kt.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    kt.updateGroup(X)
                    Ti = kt.reissueGroupTicket(op.param1)
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
                        
            if ktMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        kt.acceptGroupInvitation(op.param1)
                        ginfo = kt.getGroup(op.param1)
                    else:
                        kt.acceptGroupInvitation(op.param1)
            if ksMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in Bots and admin:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
                    else:
                        kt.acceptGroupInvitation(op.param1)
#======================================================================================================#
#======================================================================================================#
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots:
                    settings["blacklist"][op.param2] = True
                    try:
                        group = line.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            kk.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = random.choice(KAC).getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                kc.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = random.choice(KAC).getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    ke.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = random.choice(KAC).getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
                                  
                return         
              
        if op.type == 13:
            if op.param1 in protectguest:
                if op.param2 not in Bots:
                    settings["blacklist"][op.param2] = True
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
                                        ks.kickoutFromGroup(op.parm1,[op.parm2])
                                    except:
                                        try:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
#======================================================================================================#
#======================================================================================================#
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass 
                                      
                return
              
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                if op.param2 not in Bots:
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
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
#======================================================================================================#
#======================================================================================================#
        if op.type == 13:
            if op.param1 in protectguest:
                if op.param2 not in Bots:
                    if op.param3 not in Bots:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    else:
                        pass
                      
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                  
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                  
        if op.type == 19:
            if op.param3 in admin and Bots:
                if op.param2 not in Bots:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#======================================================================================================#
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in lineMID:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ks.acceptGroupInvitation(op.param1)
                        G = ks.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        ks.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        ks.leaveGroup(op.param1)
                        line.inviteIntoGroup(op.param1,[ksMID])
                        line.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in ksMID:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.findAndAddContactsByMid(op.param3)
                        line.inviteIntoGroup(op.param1,[ksMID])
                        line.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.findAndAddContactsByMid(op.param3)
                        line.inviteIntoGroup(op.param1,[ksMID])
                        line.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            line.kickoutFromGroup(op.param1,[op.param2])
                            line.findAndAddContactsByMid(op.param3)
                            line.inviteIntoGroup(op.param1,[op.param3])
                            line.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

#======================================================================================================#
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 32:
            if op.param3 in ksMID:
                if op.param2 not in Bots  and op.param2 not in admin:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            lineinviteIntoGroup(op.param1,[ksMID])
                            line.sendMessage(op.param1, "Songong jirr main cancel aja kapok w tabok")
                    except:
                        pass
                return
        if op.type == 19:
            if lineMID in op.param3:
                if op.param2 not in Bots:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param3)
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.findAndAddContactsByMid(op.param3)
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    line.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kt.kickoutFromGroup(op.param1,[op.param2])
                                        kt.findAndAddContactsByMid(op.param3)
                                        kt.inviteIntoGroup(op.param1,[op.param3])
                                        line.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
                                    except:
                                        pass
                                      
                return         
              
        if op.type == 19:
            if kiMID in op.param3:
                if op.param2 not in Bots:
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.findAndAddContactsByMid(op.param3)
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.findAndAddContactsByMid(op.param3)
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.findAndAddContactsByMid(op.param3)
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    kt.kickoutFromGroup(op.param1,[op.param2])
                                    kt.findAndAddContactsByMid(op.param3)
                                    kt.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        line.kickoutFromGroup(op.param1,[op.param2])
                                        line.findAndAddContactsByMid(op.param3)
                                        line.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
                                    except:
                                        pass
                                      
                return         
              
        if op.type == 19:
            if kkMID in op.param3:
                if op.param2 not in Bots:
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.findAndAddContactsByMid(op.param3)
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.findAndAddContactsByMid(op.param3)
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                kt.kickoutFromGroup(op.param1,[op.param2])
                                kt.findAndAddContactsByMid(op.param3)
                                kt.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    line.kickoutFromGroup(op.param1,[op.param2])
                                    line.findAndAddContactsByMid(op.param3)
                                    line.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.findAndAddContactsByMid(op.param3)
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True  
                                    except:
                                        pass
                                      
                return         
              
        if op.type == 19:
            if kcMID in op.param3:
                if op.param2 not in Bots:
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.findAndAddContactsByMid(op.param3)
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            kt.kickoutFromGroup(op.param1,[op.param2])
                            kt.findAndAddContactsByMid(op.param3)
                            kt.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                line.findAndAddContactsByMid(op.param3)
                                line.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.findAndAddContactsByMid(op.param3)
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.findAndAddContactsByMid(op.param3)
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True  
                                    except:
                                        pass
                                      
                return         
              
        if op.type == 19:
            if keMID in op.param3:
                if op.param2 not in Bots:
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                        kt.findAndAddContactsByMid(op.param3)
                        kt.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            line.findAndAddContactsByMid(op.param3)
                            line.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupkInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.findAndAddContactsByMid(op.param3)
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.findAndAddContactsByMid(op.param3)
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
                                    except:
                                        pass
                                      
                return         
              
        if op.type == 19:
            if ktMID in op.param3:
                if op.param2 not in Bots:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.findAndAddContactsByMid(op.param3)
                        line.inviteIntoGroup(op.param1,[op.param3])
                        kt.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param3)
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kt.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param3)
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kt.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kt.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        kt.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
                                    except:
                                        pass
                                      
                return
        
        if op.type == 19:
            if lineMID in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    line.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kt.kickoutFromGroup(op.param1,[op.param2])
                                        kt.inviteIntoGroup(op.param1,[op.param3])
                                        line.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
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
                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = line.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            line.updateGroup(G)
                                            Ticket = line.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                line.acceptGroupInvitation(op.param1)
                                                settings["blacklist"][op.param2] = True
                                            except:
                                                pass
                                          
                return
        
        if op.type == 19:
            if kiMID in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                kt.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    kt.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        line.kickoutFromGroup(op.param1,[op.param2])
                                        line.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
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
                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                settings["blacklist"][op.param2] = True
                                            except:
                                                pass
                                                  
                return
        
        if op.type == 19:
            if kkMID in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                kt.kickoutFromGroup(op.param1,[op.param2])
                                line.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    line.kickoutFromGroup(op.param1,[op.param2])
                                    kt.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
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
                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                                settings["blacklist"][op.param2] = True
                                            except:
                                                pass
                                          
                return
        
        if op.type == 19:
            if kcMID in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        kt.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            kt.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    line.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
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
                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                                settings["blacklist"][op.param2] = True
                                            except:
                                                pass
                                              
                return
        
        if op.type == 19:
            if keMID in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            kt.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
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
                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                                settings["blacklist"][op.param2] = True
                                            except:
                                                pass
                 
                return
        
        if op.type == 19:
            if ktMID in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                        kt.acceptGroupInvitation(op.param1)
                        settings["blacklist"][op.param2] = True
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kt.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kt.acceptGroupInvitation(op.param1)
                                settings["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kt.acceptGroupInvitation(op.param1)
                                    settings["blacklist"][op.param2] = True
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        kt.acceptGroupInvitation(op.param1)
                                        settings["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            G = kt.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                            kt.updateGroup(G)
                                            Ticket = kt.reissueGroupTicket(op.param1)
                                            line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kt.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kt.updateGroup(G)
                                            Ticket = kt.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                kt.acceptGroupInvitation(op.param1)
                                                settings["blacklist"][op.param2] = True
                                            except:
                                                pass
                                              
                return
        
        if op.type == 19:
            if op.param3 in lineMID:
                if op.param2 in kiMID:
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                else:
                    G = ki.getGroup(op.param1)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    settings["blacklist"][op.param2] = True  

            if op.param3 in kiMID:
                if op.param2 in kkMID:
                    G = kk.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kk.updateGroup(G)
                else:
                    G = kk.getGroup(op.param1)
                    kk.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kk.updateGroup(G) 
                    settings["blacklist"][op.param2] = True
            if op.param3 in kkMID:
                if op.param2 in kcMID:
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kc.updateGroup(G)
                else:
                    G = kc.getGroup(op.param1)
                    kc.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kc.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            if op.param3 in kcMID:
                if op.param2 in keMID:
                    G = ke.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ke.updateGroup(G)
                else:
                    G = ke.getGroup(op.param1)
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ke.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            if op.param3 in keMID:
                if op.param2 in ktMID:
                    G = kt.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kt.updateGroup(G)
                    Ticket = kt.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kt.updateGroup(G)
                else:
                    G = kt.getGroup(op.param1)
                    kt.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    kt.updateGroup(G)
                    Ticket = kt.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kt.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            if op.param3 in ktMID:
                if op.param2 in lineMID:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                else:
                    G = line.getGroup(op.param1)
                    line.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            if op.param3 in ksMID:
                if op.param2 in lineMID:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                else:
                    G = line.getGroup(op.param1)
                    line.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    settings["blacklist"][op.param2] = True

            else:
                pass
#======================================================================================================#
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

            if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        line.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        line.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        line.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        line.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        line.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        line.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        line.sendMessage(msg.to,"Contact itu bukan staff")
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        line.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        line.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        line.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        line.sendMessage(msg.to,"Contact itu bukan admin")
#Update foto
            if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = line.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            line.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

            if msg.toType == 2:
                 if msg._from in admin:
                    if settings["groupPicture"] == True:
                     path = line.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     line.updateGroupPicture(msg.to, path)
                     line.sendMessage(msg.to, "Berhasil mengubah foto group")

            if msg.contentType == 1:
                if msg._from in admin:
                       if lineMID in Setmain["Skfoto"]:
                            path = line.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][mid]
                            line.updateProfilePicture(path)
                            line.sendMessage(msg.to,"Foto berhasil dirubah")

            if msg.contentType == 1:
                if msg._from in admin:
                       if kiMID in Setmain["Skfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][kiMID]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                       elif kkMID in Setmain["Skfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][kkMID]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                       elif kcMID in Setmain["Skfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][kcMID]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                       elif keMID in Setmain["Skfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][keMID]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")
                       elif ktMID in Setmain["Skfoto"]:
                            path = kt.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][ktMID]
                            kt.updateProfilePicture(path)
                            kt.sendMessage(msg.to,"Foto berhasil dirubah")
                       elif ksMID in Setmain["Skfoto"]:
                            path = ks.downloadObjectMsg(msg_id)
                            del Setmain["Skfoto"][ksMID]
                            ks.updateProfilePicture(path)
                            ks.sendMessage(msg.to,"Foto berhasil dirubah")



            else:
                pass
#======================================================================================================#
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
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg._from in admin:
                  if settings["invite"] == True:
                    msg.contentType = 0
                    contact = line.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = line.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in settings["blacklist"]:
                            line.sendMessage(msg.to, "「Awas kikil boss... hpus daftar bl dulu baru invite lagi boss」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                            try:
                                line.findAndAddContactsByMid(target)
                                line.inviteIntoGroup(msg.to,[target])
                                ryan = line.getContact(target)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sukses Invite 」\nNama "
                                ret_ = "「Ketik Invite off jika sudah done」"
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                line.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                settings["invite"] = False
                                break
                            except:
                                line.sendText(msg.to,"Limit boss")
                                settings["invite"] = False
                                break
                                
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            msg.from_ = msg._from
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 13:
                    if settings["contact"] == True:
                      msg.contentType = 0
                      line.sendMessage(msg.to,msg.contentMetadata["mid"])
                      if 'displayName' in msg.contentMetadata:
                          contact = line.getContact(msg.contentMetadata["mid"])
                          path = line.getContact(msg.contentMetadata["mid"]).picturePath
                          image = 'http://dl.profile.line.naver.jp'+path
                          line.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                          line.sendImageWithURL(msg.to, image)
             
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
                  if msg._from in admin:
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'hk':
                  if msg._from in admin:
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
#==============================================================================#
                elif text.lower() == "gue":
                  if msg._from in admin:
                    line.sendContact(to, str(msg._from))
                    line.sendMessage(to, "My creator : https:/line.me/ti/p/~dhenz415")
                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626509","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                elif text.lower() == "sider on":
                  if msg._from in admin:
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

                elif text.lower()  == "sider off":
                  if msg._from in admin:
                   if msg.to in cctv['point']:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      cctv['cyduk'][msg.to]=False
                      line.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                   else:
                      line.sendMessage(msg.to, "Sudak tidak aktif")

                elif text.lower() == 'sp':
                  if msg._from in admin:
                    start = time.time()
                    line.sendMessage(msg.to, "Waiting..")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                elif text.lower() == 'restart':
                  if msg._from in admin:
                    line.sendMessage(to, "Tunggu ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == 'waktu':
                  if msg._from in admin:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "Bot berjalan .. {}".format(str(runtime)))
                elif text.lower() == 'info':
                  if msg._from in admin:
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
                        ret_ += "\n╠══[🛠●☆Silent bot☆●🛠]"
                        line.sendMessage(msg.to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                  if msg._from in admin:
                    try:
                        ret_ = "  ╔═[°✪°SETING BOT°✪°]╗  \n"
                        if settings["autoJoinTicket"] == True: ret_ +="  ╠❂➣ Auto Join Ticket「on」\n"
                        else: ret_ +="  ╠❂➣ Auto Join Ticket「 off」 \n"
                        if settings["contact"] == True: ret_ +="  ╠❂➣ Contact「 on」 \n"
                        else: ret_ +="  ╠❂➣ Contact「 off」 \n"
                        if settings["autoJoin"] == True: ret_ +="  ╠❂➣ Autojoin「 on」 \n"
                        else: ret_ +="  ╠❂➣ Autojoin「 off」 \n"
                        if msg.to in protectqr: ret_ +="  ╠❂➣ Protecturl「 on」 \n"
                        else: ret_ +="  ╠❂➣ Protecturl「 off」 \n"
                        if msg.to in protectjoin: ret_ +="  ╠❂➣ Protectjoin「 on」 \n"
                        else: ret_ +="  ╠❂➣ Protectjoin「 off」 \n"
                        if msg.to in protectkick: ret_ +="  ╠❂➣ Protectkick「 on」 \n"
                        else: ret_ +="  ╠❂➣ Protectkick「 off」 \n"
                        if msg.to in protectcancel: ret_ +="  ╠❂➣ Protectcancel「 on」 \n"
                        else: ret_ +="  ╠❂➣ Protectcancel「 off」 \n"
                        if msg.to in protectguest: ret_ +="  ╠❂➣ Protectguest「 on」 \n"
                        else: ret_ +="  ╠❂➣ Protectguest「 off」 \n"
                        if msg.to in protectinvite: ret_ +="  ╠❂➣ Protectinvite「 on」 \n"
                        else: ret_ +="  ╠❂➣ Protectinvite「 off」 \n"
                        if msg.to in protectantijs: ret_ +="  ╠❂➣ Protectantijs 「 on」\n"
                        else: ret_ +="  ╠❂➣ Protectantijs「off」\n"
                        if msg.to in ghost: ret_ +="  ╠❂➣ Ghost「 on」\n"
                        else: ret_ +="  ╠❂➣ Ghost 「 off」 \n"
                        ret_ += "  ╚═[°✪°SILENT BOT Pro°✪°]╝"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == "autojoin on":
                  if msg._from in admin:
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto join")
                elif text.lower() == "autojoin off":
                  if msg._from in admin:
                    settings["autoJoin"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto join")
                elif text.lower() == "autojointicket on":
                  if msg._from in admin:
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                elif text.lower() == "autoJoinTicket off":
                  if msg._from in admin:
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                elif text.lower() == "k on":
                  if msg._from in admin:
                    settings["checkContact"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan check details contact")
                elif text.lower() == "k off":
                  if msg._from in admin:
                    settings["checkContact"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan check details contact")
                
                elif text.lower() == "crash":
                  if msg._from in admin:
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")          
#==============================================================================#
                elif text.lower() == 'creator':
                  if msg._from in admin:
                    line.sendText(msg.to,"Creator kami ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬\n\n☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠")
                    ma = ""
                    for i in creator:
                        ma = line.getContact(i)
                        line.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626509","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                     
                elif text.lower() == "mid ":
                  if msg._from in admin:
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
#==============================================================================#              
#==============================================================================#
                elif "bc:" in msg.text:
                  if msg._from in admin:
                    bctxt = text.replace("bc:","")
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendMessage(manusia,(bctxt))
#==============================================================================#                      
                elif msg.text in ["LG2"]:
                  if msg._from in admin:
                    gid = line.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (line.getGroup(i).name,i)
                    line.sendText(msg.to,h)
#===========================================================================#
                elif msg.text in ["sksiri"]:
                  if msg._from in admin:
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
                
                elif "invite: " in msg.text:
                  if msg._from in admin:
                    gid = msg.text.replace("invite: ","")
                    if gid == "":
                      line.sendText(msg.to,"Invalid group id")
                    else:
                      try:
                        line.findAndAddContactsByMid(msg._from)
                        line.inviteIntoGroup(gid,[msg._from])
                      except:
                        line.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#=============COMMAND KICKER===========================#
                elif text.lower() == 'cuby masuk':
                  if msg._from in admin:
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
                        kt.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        group.preventedJoinByTicket = True
                        random.choice(KAC).updateGroup(group)
                        print ("Kicker Join")
                elif text.lower() == 'cin':
                  if msg._from in admin:
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
                        kt.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        group.preventedJoinByTicket = True
                        random.choice(KAC).updateGroup(group)
                        print ("Kicker Join")

                elif 'sk3 ' in msg.text.lower():
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              ke.kickoutFromGroup(msg.to,[target])      
                              print ("Bots kick User")
                          except:
                              ke.sendMessage(msg.to,"Limit kaka 😫")

                elif 'sk4 ' in msg.text.lower():
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              kc.kickoutFromGroup(msg.to,[target])             
                              print ("sb Kick User")
                          except:
                              kc.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'sk1 ' in msg.text.lower():
                  if msg._from in admin:
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

                elif 'sk2 ' in msg.text.lower():
                  if msg._from in admin:
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
                   
                elif text.lower() == "hapuschat":
                        if msg._from in admin:
                            try:
                                ki.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2)
                                kt.removeAllMessages(op.param2)
                                ks.removeAllMessages(op.param2)
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"Done")
                                line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626509","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                            except:
                                pass
                                print ("done")

                elif text.lower() == "kabur":
                  if msg._from in admin:
                        ks.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kt.leaveGroup(msg.to)
                        line.leaveGroup(msg.to)
                        print ("Kicker Leave")

                elif text.lower() == "js on":
                  if msg._from in admin:
                      try:
                          ginfo = line.getGroup(msg.to)
                          line.inviteIntoGroup(msg.to, [ksMID])
                          line.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                      except:
                          pass


                elif text.lower() == "js off":
                  if msg._from in admin:
                          gid = line.getGroup(msg.to)
                          ks.leaveGroup(msg.to)

                elif text.lower() == "leaveall":
                    if msg._from in admin:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ks.liveGroup(i)
                            ki.leaveGroup(i)
                            kk.leaveGroup(i)
                            kc.leaveGroup(i)
                            ke.leaveGroup(i)
                            kt.leaveGroup(i)
                            line.leaveGroup(i)
                            print ("Kicker Leave All group")
#===========BOT UPDATE============# 
                elif text.lower() == "botlist":
                  if msg._from in admin:
                      ma = ""
                      a = 0
                      for m_id in Bots:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠\n\n"+ma+"\nTotal「%s」" %(str(len(Bots))))

                elif text.lower() == "protectlist":
                  if msg._from in admin:
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
                      gid = protectguest
                      for group in gid:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getGroup(group).name + "\n"
                          gid = protectinvite
                      for group in gid:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getGroup(group).name + "\n"
                      line.sendMessage(msg.to,"Protection\n\nProtect Url :\n"+ma+"\nProtect Kick:\n"+mb+"\nprotect Join:\n"+md+"\nProtect Cancel:\n"+md+"\nProtect Guest:\n"+md+"\nProtect Invite:\n"+mc+"\nTotal「%s」Grup protect" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))
                     
                elif text.lower() == "cuby":
                  if msg._from in admin:
                      ki.sendText(msg.to,"Cuby Hadir kk")
                      kk.sendText(msg.to,"Imut hadir kk")
                      kc.sendText(msg.to,"Manis hadir kk")
                      ke.sendText(msg.to,"Lucu hadir kk")
                      line.sendText(msg.to,"Gemes hadir kk")
                      kt.sendText(msg.to,"Unyu juga hadir kk")
                      line.sendText(msg.to,"😍😍😍😍\nSmua hadir kk\n😆😆\n\ncreator\nBy https://line://ti/p/~dhenz415")
                      line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626509","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                     
                elif text.lower() ==  "skname":
                  if msg._from in admin:
                      line.sendText(msg.to,"⚝ཧ̌̌̌̌ł̌̌̌̌Ꮮ̌̌̌̌ཛ̌̌̌̌སོ̌̌̌ਓ̌̌̌̌བཽ̐̌̌ㄒ™⚝")
                      ki.sendText(msg.to,"⚝ཧ̌̌̌̌ł̌̌̌̌Ꮮ̌̌̌̌ཛ̌̌̌̌སོ̌̌̌ਓ̌̌̌̌བཽ̐̌̌ㄒ™⚝")
                      kk.sendText(msg.to,"⚝ཧ̌̌̌̌ł̌̌̌̌Ꮮ̌̌̌̌ཛ̌̌̌̌སོ̌̌̌ਓ̌̌̌̌བཽ̐̌̌ㄒ™⚝")
                      kc.sendText(msg.to,"⚝ཧ̌̌̌̌ł̌̌̌̌Ꮮ̌̌̌̌ཛ̌̌̌̌སོ̌̌̌ਓ̌̌̌̌བཽ̐̌̌ㄒ™⚝")
                      ke.sendText(msg.to,"⚝ཧ̌̌̌̌ł̌̌̌̌Ꮮ̌̌̌̌ཛ̌̌̌̌སོ̌̌̌ਓ̌̌̌̌བཽ̐̌̌ㄒ™⚝")
                      kt.sendText(msg.to,"SilentBotpro Ready")
                      random.choice(KAC).sendText(msg.to,"⚝ཧ̌̌̌̌ł̌̌̌̌Ꮮ̌̌̌̌ཛ̌̌̌̌སོ̌̌̌ਓ̌̌̌̌བཽ̐̌̌ㄒ™⚝ Allready")
                elif text.lower() == "botmid":
                  if msg._from in admin:
                      line.sendText(msg.to,lineMID)
                      ki.sendText(msg.to,kiMID)
                      kk.sendText(msg.to,kkMID)
                      kc.sendText(msg.to,kcMID)
                      ke.sendText(msg.to,keMID)
                      kt.sendText(msg.to,ktMID)
                   
                elif text.lower() == "sayang":
                  if msg._from in admin:
                      ki.sendText(msg.to,"Yaa\nSayang")
                      kk.sendText(msg.to,"Kangen\nSayang")
                      kc.sendText(msg.to,"Kojom\nSayang")
                      ke.sendText(msg.to,"Ehhhh\nSayang")
                      kt.sendText(msg.to,"Beb\nSayang")
                      line.sendText(msg.to,"Callme\nSayang")



                elif text.lower() == "mybot":
                  if msg._from in admin:
                      line.sendContact(to, lineMID)
                      line.sendContact(to, kiMID)
                      line.sendContact(to, kkMID)
                      line.sendContact(to, kcMID)
                      line.sendContact(to, keMID)
                      line.sendContact(to, ktMID)
                      line.sendContact(to, ksMID)
                      line.sendText(msg.to,"Hadir smua bos")
                     
                elif text.lower()  == "antijs stay":
                            if msg._from in admin:
                                try:
                                    ginfo = line.getGroup(msg.to)
                                    line.inviteIntoGroup(msg.to, [ksMID])
                                    line.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass

                elif text.lower() == "qr on":
                  if msg._from in admin:
                      if msg.toType == 2:
                         X = line.getGroup(msg.to)
                         X.preventedJoinByTicket = False
                         line.updateGroup(X)
                     
                elif text.lower() == "qr off":
                  if msg._from in admin:
                      if msg.toType == 2:
                         X = line.getGroup(msg.to)
                         X.preventedJoinByTicket = True
                         line.updateGroup(X)

                elif text.lower() == "sk qr":
                  if msg._from in admin:
                      if msg.toType == 2:
                         x = line.getGroup(msg.to)
                         if x.preventedJoinByTicket == True:
                            x.preventedJoinByTicket = False
                            line.updateGroup(x)
                         gurl = line.reissueGroupTicket(msg.to)
                         line.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                     
                elif text.lower() == "skinvite":
                  if msg._from in admin:
                      settings["invite"] = True
                      line.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                     
                elif text.lower() == "gantipp":
                  if msg._from in admin + staff: 
                      settings["foto"] = True
                      line.sendMessage(to, "Silahkan kirim gambarnya")
                    
                elif text.lower() == "masuk":
                  if msg._from in admin:
                     try:
                          anggota = [kiMID,kkMID,kcMID,keMID,ktMID,ksMID]
                          line.inviteIntoGroup(msg.to, anggota)
                          ki.acceptGroupInvitation(msg.to)
                          kk.acceptGroupInvitation(msg.to)
                          kc.acceptGroupInvitation(msg.to)
                          ke.acceptGroupInvitation(msg.to)
                          kt.acceptGroupInvitation(msg.to)
                          ks.acceptGroupInvitation(msg.to)
                     except:
                          pass

#=============COMMAND PROTECT=========================#
#===========Protection============#
                elif 'Protecturl ' in msg.text:
                   if msg._from in admin:
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
                  if msg._from in admin:
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
                  if msg._from in admin:
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

                elif 'Protectguest ' in msg.text:
                  if msg._from in admin:
                      spl = msg.text.replace('Protectguest ','')
                      if spl == 'on':
                          if msg.to in protectguest:
                               msgs = "Protect guest sudah aktif"
                          else:
                               protectguest.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect guest diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectguest:
                                 protectguest.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect guest dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect guest sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectinvite ' in msg.text:
                  if msg._from in admin:
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

                elif 'Protectantijs ' in msg.text:
                  if msg._from in admin:
                      spl = msg.text.replace('Protectantijs ','')
                      if spl == 'on':
                          if msg.to in protectantijs:
                               msgs = "Protect antiJS sudah aktif"
                          else:
                               protectantijs.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect antiJS diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectantijs:
                                 protectantijs.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect antiJS dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect antiJS sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Ghost ' in msg.text:
                  if msg._from in admin:
                      spl = msg.text.replace('Ghost ','')
                      if spl == 'on':
                          if msg.to in ghost:
                               msgs = "Ghost sudah aktif"
                          else:
                               ghost.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                               line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in ghost:
                                 ghost.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Ghost Sudah Tidak Aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    


                elif 'skpro ' in msg.text:
                  if msg._from in admin:
                      spl = msg.text.replace('skpro ','')
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
                          if msg.to in protectguest:
                              msgs = ""
                          else:
                              protectguest.append(msg.to)
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
                            if msg.to in protectguest:
                                protectguest.remove(msg.to)
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
#===========COMMAND BLACKLIST============#
                elif "ban " in msg.text:
                  if msg._from in admin:
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
   
                elif text.lower() == 'skklist':
                  if msg._from in admin:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"Tidak ada blacklist")
                        ki.sendMessage(msg.to,"Tidak ada blacklist")
                        kk.sendMessage(msg.to,"Tidak ada blacklist")
                        kc.sendMessage(msg.to,"Tidak ada blacklist")
                        ke.sendMessage(msg.to,"Tidak ada blacklist")
                        kt.sendMessage(msg.to,"Tidak ada blacklist")
                    else:
                      ma = ""
                      a = 0
                      for m_id in settings["blacklist"]:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ki.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kk.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kc.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ke.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kt.sendMessage(msg.to,"☠⚝ཧ̌̌̌̌̌ł̌̌̌̌̌̌Ꮮ̌̌̌̌̌̌̌̌̌̌̌ཛ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌སོ̌̌̌̌̌̌̌̌̌̌̌ਓ̌̌̌̌̌̌̌བཽ̐̌̌̌̌ㄒ̌̌™⚝☠ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      
                elif text.lower() == 'skcban':
                  if msg._from in admin:
                    settings["blacklist"] = {}
                    ragets = line.getContacts(settings["blacklist"])
                    mc = "「%i」User Blacklist" % len(ragets)
                    line.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ki.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kk.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kc.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ke.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kt.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              
                elif text.lower() == 'reject':
                  if msg._from in admin:
                    gid = line.getGroupIdsInvited()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    if settings["lang"] == "JP":
                        line.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                    else:
                        line.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
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
                kt.leaveRoom(op.param1)
                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1) 
                kt.leaveRoom(op.param1) 
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
                    if "/ti/g/" in msg.text:
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
                                group = kt.findGroupByTicket(ticket_id)
                                kt.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                line.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                            else:
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
