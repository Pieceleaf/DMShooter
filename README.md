#  [DMShooter](https://github.com/Pieceleaf/DMShooter)    
## bilibili 高级弹幕发送器    
* 本弹幕机可以将.ass字幕转换为逐字弹幕并进行自动发射，也可发射完全自定义的mode7弹幕，自定义mode7弹幕文件后缀规定为.m7，文件编码为UTF-8。   
* .m7 弹幕文件每行记录一条m7弹幕，需要对所有值进行设定，每行m7弹幕的格式及说明如下：   
>**出现时间,结束时间,起始x,起始y,结束x,结束y,起始透明度,结束透明度,z轴角度,y轴角度,运动耗时(ms),运动延迟时间(ms),0/1(线性加速),字体,字体大小,颜色,0/1(文字描边),弹幕内容**   
↓   
说明：   
***出现时间*** 和***结束时间*** 相差最多10秒，格式可以为 时:分:秒 / 分:秒 / 秒 ，支持小数，最末位单位均为“秒”    
***x*** ,***y*** 的值介于0-1时，代表相对坐标，x,y大于1时，为绝对坐标   
***透明度*** 为0-1之间的任意值       
***角度*** 单位为度，不使用弧度制   
***线性加速*** 为 0 时，实际效果不是匀速，而是线性减速   
运动相关的两个毫秒时间值不支持小数设定   
项目中没考虑数值格式验证和对空值的修正，请在制作.m7文件时保证格式正确   
    
   
### 注意！弹幕机需要python3环境，windows安装python3的方法为：   
1. 打开 WEB 浏览器访问 https://www.python.org/downloads/windows/ 点击第一行的“Latest Python 3 Release - Python 3.x.x”   
2. 在最下面的Files下载列表中选择 Windows installer (64-bit) 安装包（不会吧不会吧，不会还有人用32位系统吧）。   
3. 下载后，双击下载包，进入 Python 安装向导，安装非常简单，你只需要使用默认的设置一直点击"下一步"直到安装完成即可。   
4. 安装完成后，双击弹幕机文件夹内的“启动弹幕机.bat”即可运行弹幕机   
   
# 使用方法
**需要提前购买好视频的高级弹幕权限，否则将发送失败**  

提前打开目标视频页面，根据弹幕机的提示将Cookie、视频分享链接粘贴进弹幕机，再将.ass或自制的.m7弹幕文件拖进弹幕机即可。弹幕机可以保存上次使用的Cookie，但视频分享链接每次运行时都需要输入一遍。   

若在发送中途关闭掉窗口，只要在再次打开时选取与上次路径相同名字相同的歌词/弹幕文件即可在上次发送的中断位置继续发送。.ass逐字弹幕会从中断句的第一个字开始发送，需要自行删除上次发送的当句文字弹幕。

本项目参考了 [biliDmShooter](https://github.com/opheliaKyouko/biliDmShooter)和[bilibili-API-collect ](https://github.com/SocialSisterYi/bilibili-API-collect)   
