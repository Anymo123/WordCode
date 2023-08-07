##  翻译密码文本

import re

# 声明一个空字典，来保存文本文件数据
dict_temp = {}

# 打开文本文件
f = open('20230807154418WordCode.txt','r',encoding='utf-8')

# 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for line in f.readlines():
    line = line.strip("").replace ('\n', '')
    #键值对用空格分隔
    k = line.split(' ')[0]
    v = line.split(' ')[1]
    dict_temp[k] = v

# 依旧是关闭文件
f.close()

#y_code = 'i.T~pUt;4/>$g8K0j91"`9?(`beTle/e.s)+1"`9?('
y_code = input("请输入你需要翻译的词典密码:")
y_number = int(float(input('请输入几位的加密')))
#y_number = 6
#print(y_code)
end_code = ''
#分割字符串  任意字符  按长度分割
# 且最后不足位的（无法匹配到y_number个位点），直接舍弃。
st2 = re.findall(r'.{%d}' % (y_number) , y_code)
print(st2)
print(r'.{6}')
# 遍历数组st2 与词典比较

for i_string in st2:
    #print(i_string)   
    for k,v in dict_temp.items():
        #print(v)
        #print(k)
        if i_string == k:
            end_code += v
print (end_code)