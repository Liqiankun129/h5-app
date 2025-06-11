import streamlit as st
import hashlib
import time
import inspect
# import Niki.web_H5_ceshi
# 这个函数是你自己的脚本逻辑，比如输入名字，返回打招呼

class H5_URL():

    # 测试内容：

    # ------------------------------------------------------------------------
    def token_md5(text):
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        encrypted_text = md5.hexdigest()
        return encrypted_text

    def test_url(name,num):
        url = "https://h5-imniki.akamaized.net"
        url1 = "https://dp3xcm62z0hzt.cloudfront.net"
        user = f"uid={name}&token={H5_URL.token_md5(f'bfC3a72D83B9749b{name}')}&lang=zh-CN"

        if num == 1:

            s =  f"{url}/livetask/index.html?{user}&roomid=0&_app=niki&platform=iphone&version=14&version_code=522&v=4\n"
        if num == 2:
            s =f"https://dp3xcm62z0hzt.cloudfront.net/club/task?{user}&_app=niki\n"
        if num == 3:
            s =f"{url}/ghmanage/ghmanage/index.html?{user}\n"
        if num == 4:
            s =f"提现， {url}/tixian2023/withdrawal.html?{user}\n"
        if num == 5:
            s =  f"{url}/pay-discounts/indexnew.html?{user}&roomid=0&_app=niki&platform=iphone&version=14&version_code=528&v=20221228\n"

        if num == 6:
            s =f"{url}/coinDealers/index.html?{user}\n"
        if num == 7:
            s =f"{url}/pay2206/bishang.html?{user}\n"
        if num == 8:
            s =f"{url}/pay-discounts-bishang/indexnew.html?{user}&_app=niki\n"
        if num == 9:
            s =  f"{url}/zkGame/index.html?from=live&data_id=63418294&cdnVersion=1.2&{user}&version=&v=20230807&roomid=0&_app=niki&platform=&version_code=562\n"

        if num == 10:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/rank?deviceSystemName=iPhone&iosVersion=15.3&sys_country=zh_CN&{user}&_device=iPhone&_app=niki&deviceid=h93b5cea99bfe5b42a6627ee19c66331c&sys_lang=zh-Hans&version_code=196&_buvid=3000004_75c8ce8086fcdfc74418b4292999e51b&adid=&mv=20230724\n"

        if num == 11:
            s =f"{url}/surpriseWednesday/index.html?{user}&_app=niki\n"
        if num == 12:
            s =f"{url}/zouxingActive/thisWeek.html?{user}\n"
        if num == 13:
            s =  f"{url}/skyLadderGame/index.html?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 14:
            s =  f"{url}/skyLadderLucky/index.html?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 15:
            s =  f"{url1}/activity/glorySummit?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 16:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/club/activity/vitality?deviceSystemName=iPhone&iosVersion=15.3&sys_country=zh_CN&{user}&_device=iPhone&_app=niki&deviceid=h93b5cea99bfe5b42a6627ee19c66331c&sys_lang=zh-Hans&version_code=196&_t=1695455623866&_buvid=3000004_75c8ce8086fcdfc74418b4292999e51b&adid=&mv=20230724\n"

        if num == 17:
            s =  f"{url}/craze1/index.html?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 18:
            s =  f"{url}/craze2/index.html?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 19:
            s =  f"{url}/craze3/index.html?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 20:
            s =  f"{url}/feedback/index.html?{user}&version=&v=20230807&roomid=0&_app=niki&platform=iPhone&version_code=196\n"

        if num == 21:
            s =f"https://dp3xcm62z0hzt.cloudfront.net/activity/amusement?{user}&mv=20230724\n"
        if num == 22:
            s =f"{url}/activity/anniversary?{user}&_app=niki\n"
        if num == 23:
            s =f"https://dp3xcm62z0hzt.cloudfront.net/club/pk?{user}&_app=niki&gid=101872\n"
        if num == 24:


            s =  f"https://d34kziiug05v0a.cloudfront.net/event/jump/baishun_finsh_star?{user}&_app=niki&lang=zh-TW&version_code=584&sys_lang=zh&from=live\n"

        if num == 25:
            s =  f"https://nproject302.akamaized.net/game_racing/detail.html?{user}&id=game_racing&source=&v1=7&version=&v=1225&roomid=0&lang=&_app=&platform=&version_code=\n"



        if num == 26:
            s =  f"https://nproject302.akamaized.net/sanxiao/index.html?{user}&from=&data_id=0&cdnVersion=1.2&version=&v=204&roomid=0&lang=zh-TW&_app=niki&platform=iPhone&version_code=212\n"



        if num == 27:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/activity/love20240214?{user}&deviceSystemName=iPhone&sys_country=zh_CN&iosVersion=16.1&_device=iPhone&_app=niki&sys_lang=zh-Hans&lang=zh-TW&version_code=213&mv=2041\n"


        if num == 28:
            s =  f"https://d2dla3j9pnmg0q.cloudfront.net/jump/mobile/activity/love20240214?{user}&deviceSystemName=iPhone&sys_country=zh_CN&iosVersion=16.1&_device=iPhone&_app=niki&sys_lang=zh-Hans&lang=zh-TW&version_code=213&_buvid=3000004_833\n"

        if num == 29:
            s =  f"https://d34kziiug05v0a.cloudfront.net/jump/static/zegoMiniGame/index.html?gameId=FishJoy&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=589&sys_lang=zh\n"



        if num == 30:
            s =  f"https://d19453g5ncmd1k.cloudfront.net/tixian2024/withdrawal.html?{user}&_app=niki&lang=zh-TW&version_code=589&sys_lang=zh\n"

        if num == 31:
            s =  f"https://d19453g5ncmd1k.cloudfront.net/tixian2024/duihuan.html?{user}&_app=niki&lang=zh-TW&version_code=589&sys_lang=zh\n"


        if num == 32:
            s =  f"https://h5-imniki.akamaized.net/coinDealers/exchange.html?{user}&_app=niki&lang=zh-TW&version_code=589&sys_lang=zh\n"


        if num == 33:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/task/home?{user}&roomid=0&_app=niki&platform=iphone&version=14&version_code=522&v=4&mv=240321\n"

        if num == 34:
            s =  f"https://d34kziiug05v0a.cloudfront.net/jump/mobile/game/home?{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh\n"

        if num == 35:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1041&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"
        if num == 36:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1042&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"
        if num == 37:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1038&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"
        if num == 38:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1043&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"
        if num == 39:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1046&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"
        if num == 40:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1004&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"
        if num == 41:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1037&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"

        if num == 42:
            s =  f"https://d19453g5ncmd1k.cloudfront.net/ghmanage/ghmanage/index.html?{user}&lang=zh-CN&_app=niki\n"

        if num == 43:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/anchor/home?{user}&_app=niki\n"

        if num == 44:
            s =  f"https://nproject302.akamaized.net/inviteFriendsV2/index.html?{user}&_app=niki\n"
        if num == 45:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/activity/glorySummit?{user}&_app=niki\n"

        if num == 46:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=1023&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"

        if num == 47:
            s =  f"https://d19453g5ncmd1k.cloudfront.net/baishunMiniGame/index.html?{user}&_app=niki&gameId=1031&gameMode=2&data_id=605435&from=live\n"
        if num == 48:
            s =  f"https://nproject302.akamaized.net/live2/record/index.html?{user}&version=&v=125&roomid=0&_app=niki&platform=iPhone&version_code=211\n"

        if num == 49:
            s =  f"https://nproject302.akamaized.net/luckyTuesday/index.html?{user}\n"
        if num == 50:
            s =  f"{url}/lucky/detail.html?{user}&_app=niki\n"
        if num == 51:
            s =  f"https://nproject302.akamaized.net/zoo/index.html?from=live&data_id=61693871&cdnVersion=1.2&gameid=201&{user}&version=&v=240401&roomid=0&_app=niki&platform=iPhone&version_code=218\n"

        if num == 52:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/live/gift/lucky/data?from=live&data_id=61693871&cdnVersion=1.2&gameid=201&{user}&version=&v=240401&roomid=0&_app=niki&platform=iPhone&version_code=218\n"

        if num == 53:
            s =  f"https://nproject302.akamaized.net/luckyTuesday/index.html?from=live&data_id=61693871&cdnVersion=1.2&gameid=201&{user}&version=&v=240401&roomid=0&_app=niki&platform=iPhone&version_code=218\n"

        if num == 54:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/help/home?{user}&lang=zh-CN\n"

        if num == 55:
            s =  f"https://d19453g5ncmd1k.cloudfront.net//game_num/detail.html?{user}&lang=zh-CN& _app = niki\n"

        if num == 56:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=2010&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"

        if num == 57:
            s =  f"https://nproject302.akamaized.net/baishunMiniGame/index.html?gameId=2001&gameMode=3&{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"

        if num == 58:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/activity/randomPk?{user}&_app=niki&version_code=604\n"
        if num == 59:
            s =  f"https://d2tx70chhmzs07.cloudfront.net/jump/mobile/activity/rich?{user}&_app=niki&version_code=604\n"

        if num == 60:
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/activity/home?{user}&_app=niki\n"

        if num == 61:
            print(f"https://dp3xcm62z0hzt.cloudfront.net/user/my/gloryBag?{user}&_app=niki\n")
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/user/my/gloryBag?{user}&_app=niki\n"

        if num == 62:
            s =  f"https://d2tx70chhmzs07.cloudfront.net/jump/mobile/activity/return?{user}&_app=niki\n"

        if num == 63:
            s =  f"http://mobile.niki-development.svc.cluster.local/activity/anniversary2?{user}&_app=niki\n"
        if num == 64:
            print()
            s =  f"https://d2tx70chhmzs07.cloudfront.net/jump/static/ga/sz/index.html?{user}&_app=niki&lang=zh-TW&version_code=604&sys_lang=zh&mv=24042516\n"

        if num == 65:
            print(
                f"https://dp3xcm62z0hzt.cloudfront.net/user/my/level/home?{user}&_app=niki&lang=zh-TW&sys_lang=zh&mv=24042516\n")
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/user/my/level/home?{user}&_app=niki&lang=zh-TW&sys_lang=zh&mv=24042516\n"

        if num == 66:
            print(
                f"https://dp3xcm62z0hzt.cloudfront.net/game/pass?{user}&_app=niki&lang=zh-TW&sys_lang=zh&mv=240819\n")
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/game/pass?{user}&_app=niki&lang=zh-TW&sys_lang=zh&mv=240819\n"
        if num == 67:
            # 添加家族id
            print(
                f"https://dp3xcm62z0hzt.cloudfront.net/club/pk?{user}&&lang=zh-CN&_app=niki&gid=133412\n")
            s =  f"https://dp3xcm62z0hzt.cloudfront.net/club/pk?{user}&&lang=zh-CN&_app=niki&gid=133412\n\n"

        return s

# 页面标题user

if __name__ == '__main__':



    # 模拟账号密码
    valid_users = {
        "李乾坤": "123456"
    }

    # 登录会话有效期：30分钟
    SESSION_TIMEOUT = 1800

    # 初始化会话状态
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user = ""
        st.session_state.login_time = 0

    # 登录超时检测
    if st.session_state.authenticated:
        if time.time() - st.session_state.login_time > SESSION_TIMEOUT:
            st.session_state.authenticated = False
            st.session_state.user = ""
            st.session_state.login_time = 0
            st.warning("登录超时，请重新登录。")

    # 占位容器
    placeholder = st.empty()


    def show_login():
        with placeholder.container():
            st.title("🎓 学生信息系统 - 登录")
            name = st.text_input("请输入用户名").strip()
            pwd = st.text_input("请输入密码", type="password")
            if st.button("登录"):
                if name in valid_users and pwd == valid_users[name]:
                    st.session_state.authenticated = True
                    st.session_state.user = name
                    st.session_state.login_time = time.time()
                    placeholder.empty()  # 清空登录界面
                    show_main_page()  # 显示主页面
                else:
                    st.error("用户名或密码错误")


    def show_main_page():
        with placeholder.container():
            st.title(f"欢迎 {st.session_state.user} 🎉")



        # 退出按钮
        if st.button("退出登录"):
            st.session_state.authenticated = False
            st.session_state.user = ""
            st.session_state.login_time = 0
            placeholder.empty()
            show_login()

# 初始展示
if st.session_state.authenticated:
    show_main_page()
else:
    show_login()
