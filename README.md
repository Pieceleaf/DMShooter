# DMShooter   
## bilibili Mode7自动弹幕机   
* 本弹幕机可以将.ass字幕转换为逐字弹幕并进行自动发射，也可发射完全自定义的mode7弹幕，自定义mode7弹幕文件后缀规定为.m7，文件编码为UTF-8。   
* .m7 弹幕文件每行记录一条m7弹幕，需要对所有值进行设定，每行m7弹幕的格式如下：   
>**出现时间,结束时间,起始x,起始y,结束x,结束y,起始透明度,结束透明度,z轴角度,y轴角度,运动耗时(ms),运动延迟时间(ms),0/1(线性加速),字体,字体大小,颜色,0/1(文字描边),弹幕内容**

### 注意！弹幕机需要python3环境，windows安装python3的方法为：   
1. 打开 WEB 浏览器访问 https://www.python.org/downloads/windows/ 点击第一行的“Latest Python 3 Release - Python 3.x.x”   
2. 在最下面的Files下载列表中选择 Windows installer (64-bit) 安装包（不会吧不会吧，不会还有人用32位系统吧）。   
3. 下载后，双击下载包，进入 Python 安装向导，安装非常简单，你只需要使用默认的设置一直点击"下一步"直到安装完成即可。   
4. 安装完成后，双击弹幕机文件夹内的“启动弹幕机.bat”即可运行弹幕机   

本项目借鉴了 [biliDmShooter](https://github.com/opheliaKyouko/biliDmShooter)和[bilibili-API-collect ](https://github.com/SocialSisterYi/bilibili-API-collect)   
