import streamlit as st
import time

# 固定用户
valid_users = {
    "李乾坤": "123456"
}

# 登录有效时长（秒）
SESSION_TIMEOUT = 1800  # 30分钟

# 初始化 session_state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user = ""
    st.session_state.login_time = 0

# 检查是否超时
if st.session_state.authenticated:
    if time.time() - st.session_state.login_time > SESSION_TIMEOUT:
        st.warning("登录会话已过期，请重新登录。")
        st.session_state.authenticated = False
        st.session_state.user = ""
        st.session_state.login_time = 0

# 登录界面
if not st.session_state.authenticated:
    st.title("📘 学生信息查询系统 - 登录")
    name = st.text_input("请输入姓名").strip()
    password = st.text_input("请输入访问密码", type="password")
    if st.button("登录"):
        if name in valid_users and password == valid_users[name]:
            st.session_state.authenticated = True
            st.session_state.user = name
            st.session_state.login_time = time.time()
            st.success(f"欢迎，{name}！登录成功。请继续操作 ↓")
        else:
            st.error("用户名或密码错误。")

# 登录后的主界面
if st.session_state.authenticated:
    st.title(f"🎓 欢迎使用，{st.session_state.user}")
    selected = st.selectbox("请选择班级", ["1班", "2班"])
    if selected == "1班":
        st.info("1班：文科重点班，年级第3")
    else:
        st.info("2班：理科实验班，年级第1")

    s_name = st.text_input("请输入学生姓名")
    t_name = st.text_input("请输入老师姓名")
    if st.button("查询学生信息"):
        if selected == "1班" and s_name == "小明":
            st.write("年龄：13岁")
            st.write("成绩：语文88，数学95，英语90")
            st.write(f"{t_name} 对 {s_name} 的评价：努力认真，口语需加强")
        else:
            st.warning("未找到该班该学生信息")

    if st.button("退出登录"):
        st.session_state.authenticated = False
        st.session_state.user = ""
        st.session_state.login_time = 0
        st.success("您已退出登录。")
        st.experimental_rerun()
