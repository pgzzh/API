from tkinter import *
import tkinter.filedialog
from aip import AipOcr
from datetime import datetime
from tkinter import filedialog
import base64
import re
from icon import img
import os

# 窗口创建与定义
win = Tk()
win.title("图片转文字 [吾爱破解_pgzzh]")
win.geometry('850x525+500+350')
win.resizable(0, 0) # 禁止窗口最大化和改变尺寸
win.iconbitmap(base64.b64decode(img))

# 插入icon.py中的ICO-base64
tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
win.iconbitmap('tmp.ico')#加图标
os.remove("tmp.ico")#捌脖临时文件

# 取当前日期时间
def date():
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    return dt_string

# 百度识别API调用
def sb():
    APP_ID = '25973582'
    API_KEY = 'yab52GzdtEjYB5Icb8HNzMSa'
    SECRET_KEY = 'xwV9OT7b8i4e7ID5cPYLAZRkwUC5Na0E'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(a2.get(), 'rb')
    img = i.read()
    msg = client.basicGeneral(img)
    alltxt = '\n' + '------------' + date() + '------------' + '\n'
    # msg是一个字典，其中words_result中包含了文字信息
    for i in msg.get('words_result'):
        print(i.get('words'))
        # 识别方法是一行一行的
        txt1 = i.get('words')
        if txt1[0].isdigit() == True:
            alltxt += txt1 + '\n'
            print('--------+1')
        elif txt1[-1] == '。':
            alltxt += txt1 + '\n'
        # elif txt1[0] == '(' or txt1[0] == '（':
        #     if txt1[1].isdigit() == True:
        #         alltxt += '\n' + txt1
        #         print('--------+2')
        else:
            alltxt += txt1
        # alltxt += txt1 + '\n'
    # log = c1.get("1.0", "end") #获取文本C1的内容
    # c1.delete(1.0, END) #清空原文本框
    # c1.insert(INSERT, alltxt + log)  #在文本后列加入原文本框内容
    c1.insert(INSERT, alltxt)

# "text.txt"选择位置保存
def save():
    win.withdraw()
    selected = filedialog.askdirectory()
    result = c1.get("1.0", "end") #获取文本C1的内容
    file = open(selected + "text.txt", 'a', encoding='utf-8')
    file.write(result)
    file.close()

# 获取读取文件完整地址
def lj():
    a2.delete(0, "end")
    path = tkinter.filedialog.askopenfilename()
    path = path.replace("/","\\")   # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取 #注意：\\转义后为\，所以\\\\转义后为\\
    a2.insert('insert',path)

a1 = Label(win, text="路径：")# 这是标签
a2 = Entry(win, width=40)# 这是输入框
# 定义三个Button
a3 = Button(win, text="选 择", command=lj)# 这是按键
b1 = Button(win, text="识 别", command=sb)# 这是按键
b2 = Button(win, text="保 存 为 ：text.txt", command=save)# 这是按键
d1 = Label(win, text="图片转文字 by H.z  版本：1.0", fg="#ff5a5a", bg="#d1d1d1")

# 插入单选框------开始

def updata():
    message = ''
    if hobby1.get():
        message += '智能换行\n'


    # 清除text中的所有内容(从头到尾）
    text.delete(0.0, tkinter.END)
    # 插入到文本框中
    text.insert(tkinter.INSERT, message)


# 要绑定的变量 布尔类型
hobby1 = tkinter.BooleanVar()

check1 = tkinter.Checkbutton(win, text='智能换行', variable=hobby1, command=updata)
# 插入单选框---结束

c1 = Text(win)
# 创建滚动条
scroll = tkinter.Scrollbar()
# 将滚动条填充
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y) # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
c1.pack(side=tkinter.LEFT,fill=tkinter.Y) # 将文本框填充进wuya窗口的左侧，
# 将滚动条与文本框关联
scroll.config(command=c1.yview) # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
c1.config(yscrollcommand=scroll.set) # 将滚动条关联到文本框

# 整体界面插件间距和结构--调整代码
a1.place(x=10, y=10, width=35, height=20) # 标签"路径"
a2.place(x=46, y=10, width=450, height=20) # 单行输入框
a3.place(x=500, y=7, width=55, height=25) # 按钮"选择"
b1.place(x=560, y=7, width=105, height=25)# 按钮"识别"
b2.place(x=670, y=7, width=155, height=25)# 按钮"保存"
c1.place(x=10, y=40, width=830, height=450)# 最后的多行文本框
d1.place(x=0, y=500, width=850, height=20)# 最后一行签名

win.mainloop()