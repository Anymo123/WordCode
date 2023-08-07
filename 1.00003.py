##  翻译密码文本

import re

# 声明一个空字典，来保存文本文件数据
dict_temp = {}

# 打开文本文件
f = open('20230807134305WordCode.txt','r',encoding='utf-8')

# 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for line in f.readlines():
    line = line.strip("").replace ('\n', '')
    #键值对用空格分隔
    k = line.split(' ')[0]
    v = line.split(' ')[1]
    dict_temp[k] = v

# 依旧是关闭文件
f.close()

y_code = 't*Gy/$J5qvT6v<tfF`Oy}sMk/@`*L}66aDVP`l`d'
#y_string = input("请输入你需要加密的文字:")
#y_number = int(input("请输入你使用了几位加密:"))
y_number = 8
print(y_code)
end_code = ''
#分割字符串  任意字符  按长度分割
# 且最后不足5位的（无法匹配到5个位点），直接舍弃。
st2 = re.findall(r'.{8}', y_code)

# 遍历数组st2 与词典比较

for i_string in st2:
    #print(i_string)   
    for k,v in dict_temp.items():
        #print(v)
        #print(k)
        if i_string == k:
            end_code += v
print (end_code)