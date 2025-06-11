import streamlit as st

# 固定账户：姓名→密码
valid_users = {
    "李乾坤": "123456"
}

st.title("📘 受限访问 • 学生信息查询系统")

name = st.text_input("请输入您的姓名").strip()
password = st.text_input("请输入访问密码", type="password")

if st.button("登录"):
    if name in valid_users and password == valid_users[name]:
        st.success(f"✅ 欢迎，{name}！认证通过")

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
    else:
        st.error("❗ 姓名或密码错误，请重试。")
