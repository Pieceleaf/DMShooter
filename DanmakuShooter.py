import json
import time, random
from Sender import Sender
import re
import sys

#来自一个彩笔：void星葉
#PS:虽然这玩意写的跟屎一样，但好在能用
class DmShooter:
    def postDm0(self,pocess,duration,msg):
        xx = random.random()
        yy = random.random()
        sendResult=(sender.sendMod7(
            msg='[' + '%.2f' % xx + ',' + '%.2f' % yy + ',"1-0.5",' + duration + ',"' + msg + '",0,0,' + '%.2f' % xx + ',' + '%.2f' % yy + ',200,0,0,"仿宋",1]',
            videotim=pocess, fontsize='30', color='16777215').content.decode('utf-8'))
        return sendResult
        pass

    def auto_created_DM(self, pocess_, duration_, msg):
        pocess=int(pocess_)
        duration=float(duration_)
        xx = random.random()*0.75+0.05
        yy = random.random()
        summ=len(msg)
        tictoc= (duration)/summ
        count = 0
        x=0
        fontSize=35
        for char in msg:
            reqResult = 1
            if ord(char)>=0x4E00 and ord(char) <=0x9FA5:
                #char是汉字
                fontSize=random.randint(40,52)
                pass
            elif (ord(char)>=0x3040 and ord(char) <=0x309F) or (ord(char)>=0x30A0 and ord(char) <=0x30FF) :
                #char是假名
                fontSize=random.randint(25,30)
                pass
            else:
                #char是英文、数字
                fontSize=random.randint(35,45)
                pass
            while (reqResult != 0):
                sendResult = (sender.sendMod7(
                    msg='[' + '%.2f' % ((xx + x)*750) + ',' + '%.2f' % (((yy*0.7+0.1)-fontSize*0.35*(random.random()+3)/700)*900)+ ',"1-1",' + '%.2f' % (
                                (duration) - tictoc * count + 3) + ',"' + char + '",0,0,' + '%.2f' % ((
                                    xx + x)*750) + ',' + '%.2f' % (((yy*0.7+0.1)-fontSize*0.35*(random.random()+1)/700)*900)  + ',100,0,0,"仿宋",0]',
                    videotim='%d' % (pocess + tictoc * count * 1000), fontsize='%d' % fontSize,
                    color='16777215').content.decode('utf-8'))
                print(r"Return: "+sendResult)
                reqResult=json.loads(sendResult).get("code")
                print(r"code: "+'%d' % reqResult)
                if(reqResult != 0):
                    time.sleep(60.1 + random.random())
                    pass
                else:
                    time.sleep(5.1 + random.random())
                    pass
            '''
            time.sleep(5.1 + random.random())
            sendResult = (a.sendMod7(
                msg='[' + '%.2f' % (xx + x) + ',' + '%.2f' % (yy) + ',"1-0",0.5,"' + char + '",0,0,' + '%.2f' % (
                                xx + x) + ',' + '%.2f' % yy + ',150,350,0,"黑体",1]',
                videotim='%d' % ((pocess) + (duration) * 1000), fontsize='%d' % fontSize,
                color='16777215').content.decode('utf-8'))
            print(sendResult)
            '''
            x+=fontSize/700
            count+=1
        return reqResult
        pass

    def create_mode7(self, pocess_='0', x0_='0', y0_='0', alpha0_='1', alpha1_='1', duration_='4.5', msg_='', rotateZ_='0', rotateY_='0', x1_='0', y1_='0', mov_duration_='500', mov_delay_='0', stroke_='0', font_='黑体', font_size_='25', acc_='1', color_='FFFFFF'):
        #"时间轴(ms)","起始x","起始y","起始透明度-结束透明度","生存时间(s)","文字","z轴旋转","y轴旋转","结束x","结束y","运动耗时(ms)","运动延迟时间(ms)",0/1（文字描边）,"字体",0/1（线性加速）,颜色
        #(x,y坐标小于1时，为相对坐标，大于1时，为绝对坐标)
        #本功能的调用还没做，是用来发全参数自定义m7弹幕的
        reqResult = 1
        while (reqResult != 0):
            sendResult = (sender.sendMod7(
                msg='[' + x0_ + ',' + y0_ + ',"' + alpha0_ +'-' + alpha1_ + '",' + duration_ + ',"' + msg_ + '",' + rotateZ_ + ',' + rotateY_ + ',' + x1_ + ',' + y1_ +
                    ',' + mov_duration_ + ',' + mov_delay_ + ',' + stroke_ + ',"' + font_ + '",' + acc_ + ']',
                videotim=pocess_, fontsize=font_size_,
                color=int(color_,16)).content.decode('utf-8'))
            print(r"Return: "+sendResult)
            reqResult=json.loads(sendResult).get("code")
            print(r"code: "+'%d' % reqResult)
            if(reqResult != 0):
                time.sleep(60.1 + random.random())
                pass
            else:
                time.sleep(5.1 + random.random())
                pass
        return reqResult
        pass

class Tools():
    def load_cookie(self):
        try:
            f = open('cookie.txt', 'r')
            cookie = f.readline()
            f.close
            return cookie
        except IOError:
            return '0'
            pass

    def get_cookie(self):
        cookie ='SESSDATA=' + input("请输入SESSDATA\n获取方法：点击chrome浏览器网址栏左侧的锁，点击'Cookie',\n点击'bilibili.com'选项左侧的三角，再点击子选项'Cookie'左侧的三角\n找到'SESSDATA'，复制'内容'的值粘贴进本窗口并回车\n")
        cookie += '; bili_jct=' + input(
            "请输入bili_jct\n获取方法同上，\n找到bili_jct，复制'内容'的值粘贴进本窗口并回车\n")
        f = open('cookie.txt', "w")
        f.truncate()
        f.write(cookie)
        f.close
        return cookie

    def load_progress(self,file_name):
        try:
            f = open('record.txt', 'r')
            line_num = f.readline()
            ass_name = f.readline()
            f.close
            if ass_name != file_name:
                print('将覆盖上传记录：'+ass_name+'  第'+line_num+'行')
                line_num = '0'
            return line_num
        except IOError:
            return '0'
            pass

    def save_progress(self,msg):
        f=open('record.txt',"w")
        f.truncate()
        f.write(msg)
        f.close
        pass

    def getVideoId(self, html):
        htmlList = html.split("\n")
        linenum = 0
        for lineItem in htmlList:
            if ('cid' in lineItem) and ('bvid' in lineItem):
                linenum += 1
                pattenStr = r"bvid=(\w+)&cid=(\d+)&"
                patten = re.compile(pattenStr)
                idList = patten.findall(lineItem)[0]
                global bvid
                global cid
                bvid = idList[0]
                cid = idList[1]
                print("视频 cid = %s, bvid = %s" % (cid, bvid))
                return True
            else:
                print("未获取到视频信息，请重试")
                return False

bvid = '' #'BV1hp411f7me'
cid = ''  #'261793445'
ds=DmShooter();
tool=Tools()
gotVideoId = False
useCookie = ''
endFlag=0
cookie=""

cookie = tool.load_cookie()
if cookie != '0':
    useCookie = input("是否使用记录的cookie？Y/N\n")
    while endFlag==0:
        if useCookie == 'y' or useCookie == 'Y':
            print('使用记录的cookie:'+cookie)
            endFlag = 1
            continue
        elif useCookie == 'n' or useCookie == 'N':
            endFlag = 1
            cookie=tool.get_cookie()
            continue
        else:
            useCookie = input("请输入Y或N\n")
            continue
    pass
else:
    cookie = tool.get_cookie()
    pass

while bvid=='':
    html=''
    html=input('\n请粘贴目标视频网页端播放页面分享的嵌入代码：\n')
    gotVideoId=tool.getVideoId(html)

sender = Sender(bvid, cid, cookie)
xx = random.random()
yy = random.random()
text = "Danmaku Content"
fileNmae = ''
while not (fileNmae.endswith('.ass') or fileNmae.endswith('.m7')):
    fileNmae = input("请输入歌词文件路径，可直接将歌词文件拖进本窗口：\n")  # 输入歌词文件名
    if fileNmae.endswith('.ass') or fileNmae.endswith('.m7'):
        pass
    else:
        print("不支持此格式文件")

try:
    file_object = open(fileNmae, 'r', encoding='UTF-8')
except IOError:
    print("exit because the file don't exist")
    exit()
loadLine = int(tool.load_progress(fileNmae))
if loadLine>0:
    endFlag=0
    choose = input("发现写入记录:第" + '%d' % loadLine + "行，是否从上次中断的部分继续发送弹幕？Y/N\n")
    while endFlag==0:
        if choose == 'y' or choose == 'Y':
            print('从上次断点继续发送弹幕')
            endFlag = 1
            continue
        elif choose == 'n' or choose == 'N':
            print('从头开始发送弹幕')
            endFlag = 1
            loadLine=0
            continue
        else:
            choose = input("请输入Y或N")
            continue
    pass
countLine = 0
lyric_lines = file_object.readlines()
file_object.close()
for lintItem in lyric_lines[loadLine:]:
    if fileNmae.endswith('.ass'):
        if lintItem.count('Dialogue') == 1:
            currentLine = (lintItem.split('\n')[0]).split(",")
            '''
            ass字幕，自动生成逐字特效发射
            '''
            begin_time = currentLine[1].split(':')
            end_time = currentLine[2].split(':')
            beginTimeMark = float(begin_time[0]) * 3600 + float(begin_time[1]) * 60 + float(begin_time[2])
            endTimeMark = float(end_time[0]) * 3600 + float(end_time[1]) * 60 + float(end_time[2])
            duration = (endTimeMark - beginTimeMark)
            # print(currentLine[1],'%6f'% timeMark, currentLine[9])
            msg = currentLine[10].replace("120)}", "")
            if len(currentLine)>11:
                i=0
                while len(currentLine)-i>11:
                    i+=1
                    msg+=","+currentLine[10+i]
                    pass
                pass
            pass
            postText =ds.auto_created_DM('%d' % (beginTimeMark * 1000), '%.2f' % duration, msg)
        else:
            countLine += 1
            continue
    else:
        '''
        m7弹幕，直接按照自定义参数发射
        出现时间,结束时间,起始x,起始y,结束x,结束y,起始透明度,结束透明度,z轴角度,y轴角度,运动耗时(ms),运动延迟时间(ms),0/1(线性加速),字体,字体大小,颜色,0/1(文字描边),弹幕内容
        '''
        currentLine = (lintItem.split('\n')[0]).split(",")
        begin_time = currentLine[0].split(':')
        end_time = currentLine[1].split(':')
        x0 = currentLine[2]
        y0 = currentLine[3]
        x1 = currentLine[4]
        y1 = currentLine[5]
        alpha0 = currentLine[6]
        alpha1 = currentLine[7]
        rotateZ = currentLine[8]
        rotateY = currentLine[9]
        mov_duration = currentLine[10]
        mov_delay = currentLine[11]
        acc = currentLine[12]
        font = currentLine[13]
        font_size=currentLine[14]
        color = currentLine[15]
        stroke = currentLine[16]
        msg = currentLine[17]

        if len(currentLine) > 18:
            i = 0
            while len(currentLine) - i > 18:
                i += 1
                msg += "," + currentLine[17 + i]
                pass
            pass
        pass

        if len(begin_time)==3:
            beginTimeMark = float(begin_time[0]) * 3600 + float(begin_time[1]) * 60 + float(begin_time[2])
        elif len(begin_time)==2:
            beginTimeMark = float(begin_time[0]) * 60 + float(begin_time[1])
        elif len(begin_time)==1:
            beginTimeMark = float(begin_time[0])
        else:
            print("时间格式不正确")
            exit()

        if len(end_time) == 3:
            endTimeMark = float(end_time[0]) * 3600 + float(end_time[1]) * 60 + float(end_time[2])
        elif len(begin_time) == 2:
            endTimeMark = float(end_time[0]) * 60 + float(end_time[1])
        elif len(begin_time) == 1:
            endTimeMark = float(end_time[0])
        else:
            print("时间格式不正确")
            exit()

        duration = (endTimeMark - beginTimeMark)
        # print(currentLine[1],'%6f'% timeMark, currentLine[9])
        postText = ds.create_mode7(pocess_='%d' % (beginTimeMark * 1000),
                                   x0_=x0, y0_=y0,
                                   x1_=x1, y1_=y1,
                                   alpha0_=alpha0, alpha1_=alpha1, duration_='%.2f' % duration,
                                   msg_=msg, rotateZ_=rotateZ, rotateY_=rotateY, mov_duration_=mov_duration,
                                   mov_delay_=mov_delay, stroke_=stroke, font_=font, font_size_=font_size, acc_=acc,
                                   color_=color)
    print(postText)
    countLine+=1
    thisLine ='%d' % (countLine + loadLine)
    tool.save_progress(thisLine+"\n"+fileNmae)
    pass
pass
