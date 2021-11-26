import asyncio
import random
import time
from pyppeteer import launch
from pyppeteer_stealth import stealth


async def run():
    driver = await launch({
        # 'executablePath': 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
        'executablePath': 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        # Pyppeteer 默认使用的是无头浏览器,所以要显示需要给False
        'headless': False,
        'args': ['--no-sandbox', '--window-size=1024, 768']
    })

    page = await driver.newPage()
    await page.setViewport({'width': 1024, 'height': 768})

    await stealth(page)
    await page.goto('https://www.wjx.cn/m/54783446.aspx')

    await page.select('select#q1', '11')
    # input name
    await page.type('#q2', '李吉峰')
    # get date selection as today
    date01 = await page.querySelector("#q3")
    await date01.click()

    frame = page.frames
    print(frame[1])
    date02 = await frame[1].querySelector("#selectTodayButton")
    await date02.click()

    radio5 = await page.querySelector("#div5 > div.ui-controlgroup > div:nth-child(2) > span > a")
    await radio5.click()
    radio6 = await page.querySelector("#div6 > div.ui-controlgroup > div:nth-child(2) > span > a")
    await radio6.click()
    radio7 = await page.querySelector("#div7 > div.ui-controlgroup > div:nth-child(2) > span > a")
    await radio7.click()
    radio8 = await page.querySelector("#div8 > div.ui-controlgroup > div:nth-child(2) > span > a")
    await radio8.click()
    radio9 = await page.querySelector("#div9 > div.ui-controlgroup > div:nth-child(2) > span > a")
    await radio9.click()
    radio10 = await page.querySelector("#div10 > div.ui-controlgroup > div:nth-child(2) > span > a")
    await radio10.click()

    print("3333333333333333333333333333333")

    # await page.type('#q4', '北京-北京市-朝阳区')
    addpop = await page.querySelector("#q4")
    print("4444444444444444444444444444444444")
    await addpop.click()
    print("5555555555555555555555555555555555")
    time.sleep(3)
    print("6666666666666666666666666666666666")

    # frame = page.frames
    print("77777777777777777777777777777777777")

    print("88888888888888888888888888888888888")
    print(frame[1])
    popup = await page.querySelector("#yz_popTanChu")
    print(popup)
    print(page)
    print(date01)

    frame = page.frames

    await frame[2].select('select#province', '北京')
    time.sleep(1)
    await frame[2].select('select#city', '北京市')
    time.sleep(1)
    await frame[2].select('select#area', '朝阳区')
    time.sleep(1)

    btnSave = await frame[2].querySelector("body > div.content > div.save_btn > a")
    await btnSave.click()
    print("9999999999999999999999999999999999")

    # btnsave = await frames[1].querySelector("body > div.content > div.save_btn > a")
    # await btnsave.click()

    time.sleep(3)
    # btnsubmit = await page.querySelector("#ctlNext")
    # await btnsubmit.click()

    await asyncio.sleep(10)  # 页面延迟2s看是否提交成功
    await driver.close()

    time.sleep(1)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(run())
