# 发表到网上的内容有多少人客观评论的，能够纠正完善你的想法的？无数个没有自我意识的人在下意识的评论着，那些个客观的又他妈的隐藏自己。它们一边堵住你的鼻孔并说着你可以用嘴呼吸也不会死的虎狼之词，谁难受谁知道。创建一个密码本，人工智能无法学习和破解的。


#1，创建一个或多个词典
#2，删除特定字母，特定位置，生成一个随机代码方便逆序
#3，删除特定字母，特定位置，生成一个随机代码方便逆序
#4，删除标点符号，特定位置，生成一个随机代码方便逆序
#5，乱序字母转换，另一个词典逆序 （搞定人工智能通过学习你的习惯破解）
#6, 添加密钥（你复制密钥解开了也是乱码，哈哈哈哈，气不气）
#7，1-5再次执行，循环几次你自己记着


#  7步完成后自己忘了，上帝来了都解不开


###  后期一本书或几本书，一首歌或几首歌，名人名言，一个或多个图片等等作为密码

###  未来即使是自己找不到特定的书籍和图片都无法破解

## 你只需要记住循环的次数（无限制），和另一个词典

## 这样就简单完成了一个密码本


########### 1 第一步创建词典


## 创建引入一个chinese.txt 里面包括3500常用中文 utf-8，需要什么自己加

##  读取txt每个字作为值，每个字随机6位代码（多少个随你）作为键， 形成词典

import random
import string
import time
def rd_Key():
    #设定随机代码的个数
    rd_length = 8
    #rd_length = int(input('请输入需要几位加密'))
    #生成随机数 阿拉伯数字，ascii码，特殊符号
    rd_hub = string.digits + string.ascii_letters + string.punctuation
    # k =  不能省略，代表末尾参数  choices有很多参数
    rd_pw = ''.join(random.choices(rd_hub, k = rd_length))
    #生成随机8位键
    return rd_pw
## 执行生成key
#rd_Key()
tinydict = {}
with open('chinese.txt', 'r', encoding='utf-8') as f:
    data_value = f.read()
    # 关闭文件
f.close()
#rd_value()
for rd_value in data_value:
    #tinydict[rd_value] = rd_Key()
    tinydict[rd_Key()] = rd_value

#print(tinydict)
#rd_length = int(input('请输入要求的密码长度'))
#tinydict = {}

#跟随时间生成的文件名
now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
fName = now+"WordCode.txt"
# 生成文件
with open(fName, 'w', encoding='utf-8') as f:
    for key, value in tinydict.items():
        f.write(key)
        f.write(' ')
        f.write(str(value))
        f.write('\n')
f.close()

##  目前进度 是完成了 1.00001生成词典，1.00002和1.00003输入文字密码互换