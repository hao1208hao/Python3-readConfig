import configparser

# 加载现有配置文件
conf = configparser.ConfigParser()
conf.read("config.ini")

'''
# 写入配置文件
conf.add_section('config') #添加section
# 添加值
conf.set('config', 'v1', '100')
conf.set('config', 'v2', 'abc')
conf.set('config', 'v3', 'true')
conf.set('config', 'v4', '123.45')
# 写入文件
with open('conf.ini', 'w') as fw:
    conf.write(fw)
    
'''    

# 读取配置信息
''' 
v1 = conf.getint('config', 'v1')
v2 = conf.get('config', 'v2')
v3 = conf.getboolean('config', 'v3')
v4 = conf.getfloat('config', 'v4')
'''

v11 = conf.get('config', 'v1')
v22 = conf.get('config', 'v2')
v33 = conf.get('config', 'v3')
v44 = conf.get('config', 'v4')

'''
print('v1:', v1)
print('v2:', v2)
print('v3:', v3)
print('v4:', v4)
'''


print('v11:', v11)
print('v22:', v22)
print('v33:', v33)
print('v44:', v44)

#input()
exit = input("按回车键退出...")
