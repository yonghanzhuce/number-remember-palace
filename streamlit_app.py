import streamlit as st
import random

# 设置页面标题
st.title('数字记忆训练')

# 初始化session_state
if 'show_numbers' not in st.session_state:
    st.session_state.show_numbers = False
if 'random_numbers' not in st.session_state:
    st.session_state.random_numbers = []

# 用于切换显示状态的函数
def toggle_visibility():
    st.session_state.show_numbers = not st.session_state.show_numbers

# 生成随机数字并更新显示状态
def generate_numbers():
    st.session_state.random_numbers = [str(random.randint(100000, 999999)) for _ in range(5)]
    st.session_state.show_numbers = True

# 在HTML中添加自定义样式
# st.markdown("""
# <style>
# div.stButton > button:first-child {
#     margin: 2px 2px 2px 0px;
#     background-color: #008CBA; 
#     color: white;
# }
# div.stButton > button:nth-child(2) {
#     margin: 2px;
#     background-color: #e7e7e7; 
#     color: black;
# }
# </style>""", unsafe_allow_html=True)

# 创建并排的两个按钮
col1, col2 = st.columns([1, 4])
with col1:
    generate_button = st.button('生成随机数字')
with col2:
    toggle_button = st.button('隐藏/显示数字')

if generate_button:
    generate_numbers()

if toggle_button:
    toggle_visibility()

# 检查是否需要显示数字
if st.session_state.show_numbers:
    st.write('记住这些数字:')
    for number in st.session_state.random_numbers:
        st.write(number)

# 输入框，用于用户输入记忆的数字
user_input = st.text_input('输入你记忆的数字（用空格分隔）:')

# 校验按钮和功能
if st.button('校验记忆的数字'):
    # 分割用户输入，转换为列表
    user_numbers = user_input.split()
    # 开始校验
    if user_numbers == st.session_state.random_numbers:
        st.success('恭喜！你记得非常准确。')
    else:
        st.error('记忆有误，请再接再厉！')
        # 对比正确与错误的数字，并构建带有颜色标记的HTML字符串
        corrected_numbers_html = []
        for orig_num, user_num in zip(st.session_state.random_numbers, user_numbers):
            # 分别比较每一位数字
            corrected_num = "".join(
                [f"<span style='color:red'>{u}</span>" if u != o else o for u, o in zip(user_num.ljust(6, ' '), orig_num)]
            )
            corrected_numbers_html.append(corrected_num)
        
        # 对于用户忘记输入的数字，显示整个数字并标红
        for i in range(len(user_numbers), len(st.session_state.random_numbers)):
            corrected_numbers_html.append(f"<span style='color:red'>{st.session_state.random_numbers[i]}</span>")

        # 用join方法将列表合成字符串并用空格分隔，然后用markdown显示
        st.markdown(' '.join(corrected_numbers_html), unsafe_allow_html=True)
