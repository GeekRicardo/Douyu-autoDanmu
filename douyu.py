# -*- coding: utf-8 -*-
# @Author: Ricardo
# @Date:   2019-10-17 15:09:22
# @Last Modified by:   GeekRicardo
# @Last Modified time: 2019-10-19 21:23:27
from selenium import webdriver
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
from flask import Flask, render_template, request
import random
import time
import os
import pdb
import qrcode_terminal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


app = Flask(__name__)

msgs = [
    '不要你觉得，要我觉得！',
    '666666',
    '2333',
    '2222 2222',
    '2222',
    '？？？？？？？？？！',
    # '好听♥♡好听♥♡好听♥♡好听♥♡好听♥♡好听♥♡好听♥♡好听♥♡',
    '好听好听好听',
    '水星记水星记水星记水星记水星记水星记',
    '手游只玩游仙记',
    '太难了',
    '你是真的秀！',
    '牛批',
    '哦 爱了爱了',
    'skr',
    '大气大气',
    '别别别 自己人',
    '想屁吃？？',
    'testtest',
    '我是机器人 我莫得感情',
    '卧槽 无情'
]


def drawqrcode():
    """扫码登陆

    使用扫码登陆，待补充
    """
    URL = decode(Image.open('111.png'), symbols=[
                 pyzbar.pyzbar.ZBarSymbol.QRCODE])

    qrcode_terminal.draw(URL)


def login():
    dr = webdriver.Chrome(
        executable_path="D:\Documents\Green\chromedriver_win32\chromedriver.exe")
    dr.get("https://www.douyu.com/2222")
    dr.maximize_window()
    # time.sleep(10)
    try:
        try:
            element = WebDriverWait(dr, 60).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "div.Header-right>div.Header-login-wrap a.public-DropMenu-link"))
            )
            element.click()
        except Exception as e:
            print(e)
            dr.quit()
        print(dr.title)
        # time.sleep(10)
        # 点击X号去掉广告，如果没有广告要注释这行代码
        # dr.find_element_by_xpath("/html/body/div[7]/div/div/div[2]").click()
        # time.sleep(10)
        # 切换到密码登录frame
        dr.switch_to.frame("login-passport-frame")
        time.sleep(1)
        # 点击密码登录
        # dr.find_element_by_xpath(
        # "//*[@id='loginbox']/div[2]/div[2]/div[3]/div/span[2]").click()
        # dr.find_element_by_link_text("密码登录").click()  还是不要用字符串定位元素好
        dr.find_element_by_class_name(
            'js-to-link').click()
        time.sleep(2)
        # 点击QQ图标
        # dr.find_element_by_xpath(
        # "//*[@id='loginbox']/div[3]/div[2]/div[2]/div[2]/a[1]").click()
        dr.find_element_by_class_name('third-icon-qq').click()
        time.sleep(3)

        # 获取当前窗口句柄（窗口A）
        handle = dr.current_window_handle
        print(handle)
        # 获取当前所有窗口句柄（窗口A、B）
        handles = dr.window_handles
        print(dr.current_window_handle)
        # pdb.set_trace()
        # 对窗口进行遍历
        for newhandle in handles:
            # if newhandle == handle:
            #     handle.close()
            # 筛选新打开的窗口B
            if newhandle != handle:
                # 切换到新打开的窗口B，关闭旧窗口A
                dr.close()
                dr.switch_to_window(newhandle)
                # 在新打开的窗口B中操作

                dr.switch_to.frame("ptlogin_iframe")
                time.sleep(1)
                ele = dr.find_element_by_id("switcher_plogin").click()
        dr.find_element_by_xpath("//*[@id='u']").send_keys("1921703278")
        dr.find_element_by_xpath("//*[@id='p']").send_keys("Ricardogeek.")
        dr.find_element_by_xpath("//*[@id='login_button']").click()
        time.sleep(3)
        dr.find_element_by_class_name('is-allChecked').click()
        print("登录成功")
        # dr.minimize_window()
        # dr.get("https://www.douyu.com/t/lpl")
        # dr.implicitly_wait(15)
        # print(dr.title)
        return dr
    except Exception as e:
        print(e)
        dr.quit()
        return None


t = time.time()
dr = login()
print('\n', '登陆用时:', time.time() - t)


def send(dr, msg):
    """发送弹幕

    发送一条消息

    Arguments:
        dr {driver} -- webdriver
        msg {str} -- 弹幕
    """
    dr.find_element_by_class_name(
        "ChatSend-txt").send_keys(msg)
    # time.sleep(2)
    dr.find_element_by_class_name("ChatSend-button").click()
    # 清空缓冲
    dr.find_element_by_class_name(
        "ChatSend-txt").clear()
    print(' > ' + msg + '\n')


def sendrandom(dr, t='1'):
    """随机发送一条n次

    在列表中选择一条发送n次

    Arguments:
        dr {driver} -- 登录态

    Keyword Arguments:
        t {number} -- 次数 (default: {1})
    """
    t = int(t)
    if t == 0:
        t = 10
    for i in range(0, t):
        msg = random.choice(msgs)
        send(dr, msg)
        time.sleep(random.choice(range(3, 10, 2)))


def send_by_choice(dr, mi):
    """
    在列表中选择一条发送

    Arguments:
        dr {webdriver} -- 登陆态
        mi {int} -- 列表index
    """
    # for msg in msgs:
    #     print(msgs.index(msg) + 1, '.', msg)
    # i = input('选择要发送的弹幕： ')
    send(dr, msgs[int(mi) - 1])


def send_incircle(dr, msg=''):
    # pdb.set_trace()
    mi = 0
    if is_number(msg):
        mi = int(msg)
    for i in range(1, 10):
        if mi:
            msg = msgs[int(mi) - 1]
        send(dr, msg)
        time.sleep(3)


def add(dr, msg):
    '''添加弹幕

    在列表中添加消息

    Arguments:
        dr  {None} -- 占位
        msg {str} -- 弹幕
    '''
    msgs.append(msg.strip())


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


func_name = {
    'send': send,
    'sendrandom': sendrandom,
    'send_by_choice': send_by_choice,
    'send_incircle': send_incircle,
    'add': add
}

if __name__ == '__main__':
    try:
        while 1:
            # last_time = os.stat('cmd.txt').st_mtime
            last = os.path.getsize('cmd.txt')
            time.sleep(3)
            if not dr:
                break
            # # 点击宝箱
            # try:
            #     dr.find_element_by_class_name('TreasureStatus-text').click()
            # except Exception:
            #     pass
            tttt = time.time()
            sizenow = os.path.getsize('cmd.txt')
            if(sizenow != last and sizenow != 0):
                # 有新的cmd
                with open('cmd.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if len(lines) != 0:
                        for l in lines:
                            # lines.remove(l)
                            if(l != '\n'):
                                try:
                                    # pdb.set_trace()
                                    s = l.replace('\n', '').split('|')
                                    print(s)
                                    func_name[s[0]](dr, s[1])
                                    # eval(l)
                                except Exception as e:
                                    print(l)
                                    print('eval error', e)
                with open('cmd.txt', 'w', encoding='utf-8') as f:
                    for l in lines:
                        f.truncate()
                print('这一轮:', time.time() - tttt)
    except Exception as e:
        print(e)
        dr.quit()
