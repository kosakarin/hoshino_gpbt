import requests, os, re
from hoshino import Service, priv
from hoshino.typing import CQEvent
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


sv_help = '''狗屁不通'''

def get_page(kw, num):
    url = 'http://ovooa.com/API/dog/api.php?msg=' + kw + '&num=' + str(num) + '&type=text'
    try:
        response = requests.get(url,verify=False)
        response.content.decode("utf-8")
        return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)


sv = Service('狗屁不通', manage_priv=priv.ADMIN, enable_on_default=True, help_=sv_help)


@sv.on_prefix('狗屁不通')
async def dscf(bot, ev: CQEvent):
    kw = ev.message.extract_plain_text().strip()
    
    arr = kw.split(' ')
    flag =len(arr)
    if flag == 1:
        try:
            re = get_page(arr[0], 100)
            await bot.send(ev, '未指定字数，默认100字')
            await bot.send(ev, re)
        except:
            await bot.send(ev, '发送失败')
    elif flag == 2:
        try:
            flag = int(arr[1])
            if flag > 1000:
                await bot.send(ev, '请不要使用过多的字数')
            elif flag <= 10:
                await bot.send(ev, '请不要使用过少的字数')
            else:
                try:
                    re = get_page(arr[0], flag)
                    await bot.send(ev, re)
                except:
                    await bot.send(ev, '发送失败')
            except:
                await bot.send(ev, '格式错误')
    else:
        await bot.send(ev, '格式错误')
