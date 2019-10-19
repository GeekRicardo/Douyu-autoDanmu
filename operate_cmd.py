# -*- coding: utf-8 -*-
# @Author: Ricardo
# @Date:   2019-10-18 17:51:36
# @Last Modified by:   Ricardo
# @Last Modified time: 2019-10-19 19:19:52

from flask import Flask, render_template, request


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
    '手游就玩焚仙诀',
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


@app.route('/')
def index():
    return render_template('index.html', msgs=msgs, types=('success', 'info', 'warning', 'danger'))


@app.route('/add/<msg>')
def addmsg(msg):
    print('add', msg)
    with open('cmd.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n')
        f.writelines('add|' + msg + '')
    return 'ok'


@app.route('/send/<msg>')
def sendone(msg):
    print('send', msg)
    f = open('cmd.txt', 'a', encoding='utf-8')
    f.writelines('\n')
    f.writelines('send|' + msg.strip() + '')
    f.close()
    return 'ok'


@app.route('/sendrandom/<t>')
def sendrandom(t):
    print('random', t)
    f = open('cmd.txt', 'a', encoding='utf-8')
    f.writelines('\n')
    f.writelines('sendrandom|' + t.strip() + '')
    f.close()
    return 'ok'


@app.route('/sendchoice/<mi>')
def sendchoice(mi):
    print('choice', mi)
    f = open('cmd.txt', 'a', encoding='utf-8')
    f.writelines('\n')
    f.writelines('send_by_choice|' + mi.strip() + '')
    f.close()
    return 'ok'


@app.route('/sendcircle/<msg>')
def sendcircle(msg):
    print('circle', msg)
    cmd = 'send_incircle|' + msg
    f = open('cmd.txt', 'a', encoding='utf-8')
    f.writelines('\n')
    f.writelines(cmd + '')
    f.close()
    return 'ok'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=55599, debug=True)
