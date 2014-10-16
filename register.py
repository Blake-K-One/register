import win32api
import win32con
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Software\Microsoft\Internet Explorer\Main', 0, win32con.KEY_ALL_ACCESS)
print('请输入你的指令')
print('提示如下：')
print('0：将网页设置为空白页')
print('1：设置新网址为www.baidu.com')
print('2：设置新网址为www.google.com')
print('3：设置新网址为www.xinnaweibo.com')
print('q:exit')
while(True):
    selectnum = input('Now enter a num: ')
    if(selectnum == '0'):
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, 'kongbai1')
    if(selectnum == '1'):
       win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, 'www.baidu.com')
    if(selectnum == '2'):
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, 'www.google.com')
    if(selectnum == '3'):
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, 'www.xinnaweibo.com')
    if(selectnum == 'q'):
        break
win32api.RegCloseKey(key)
print('hello world')
