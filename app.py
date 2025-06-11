import streamlit as st
import time

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

        # 班级选择
        class_choice = st.selectbox("请选择班级", ["1班", "2班"])
        if class_choice == "1班":
            st.info("文科重点班，年级第3")
        else:
            st.info("理科实验班，年级第1")

        # 输入学生和老师名
        student_name = st.text_input("请输入学生姓名")
        teacher_name = st.text_input("请输入老师姓名")

        if st.button("查询学生信息"):
            if class_choice == "1班" and student_name == "小明":
                st.success("查到信息如下：")
                st.write("年龄：13岁")
                st.write("成绩：语文88，数学95，英语90")
                st.write(f"{teacher_name} 的评价：认真负责，刻苦好学")
            elif class_choice == "2班" and student_name == "小红":
                st.success("查到信息如下：")
                st.write("年龄：14岁")
                st.write("成绩：语文90，数学88，英语92")
                st.write(f"{teacher_name} 的评价：聪明活泼，理解能力强")
            else:
                st.warning("没有找到该学生的信息")

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
