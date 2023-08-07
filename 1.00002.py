###  根据词典生成密码字符串

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

#  可以打印出来瞅瞅
#print(dict_temp)
#请输入字符串 请输入你需要加密的文字
y_string = input("请输入你需要加密的文字:")
#y_string = "你好啊未来"
end_string = ""
for i_string in y_string:
    #print(i_string)   
    for k,v in dict_temp.items():
        #print(v)
        #print(k)
        if i_string == v:
            end_string += k
print (end_string)