import streamlit as st
import random

# 设置页面标题
st.title('数字记忆训练')

# 用于切换显示状态的函数
def toggle_visibility():
    # 如果状态标记存在且为True（即数字被显示），则切换为False
    if 'show_numbers' in st.session_state and st.session_state.show_numbers:
        st.session_state.show_numbers = False
    else:
        # 否则设置为True
        st.session_state.show_numbers = True

# 当按钮被点击时，生成随机数字
if st.button('生成随机数字'):
    # 生成5个随机的6位数字
    st.session_state.random_numbers = [str(random.randint(100000, 999999)) for _ in range(5)]
    # 默认显示数字
    st.session_state.show_numbers = True

# 隐藏/显示数字按钮
if st.button('隐藏/显示数字'):
    toggle_visibility()

# 检查是否需要显示数字
if 'show_numbers' in st.session_state and st.session_state.show_numbers:
    st.write('记住这些数字:')
    for number in st.session_state.random_numbers:
        st.write(number)

# 输入框，用于用户输入记忆的数字
user_input = st.text_input('输入你记忆的数字（用空格分隔）:')

# 校验按钮和功能
if st.button('校验记忆的数字'):
    # 分割用户输入，转换为列表
    user_numbers = user_input.split()
    # 检索之前存储的随机数字
    original_numbers = st.session_state.random_numbers if 'random_numbers' in st.session_state else []

    # 开始校验
    if user_numbers == original_numbers:
        st.success('恭喜！你记得非常准确。')
    else:
        st.error('记忆有误，请再接再厉！')
        # 对比正确与错误的数字，并构建带有颜色标记的HTML字符串
        corrected_numbers_html = []
        for orig_num, user_num in zip(original_numbers, user_numbers):
            # 分别比较每一位数字
            corrected_num = "".join(
                [f"<span style='color:red'>{u}</span>" if u != o else o for u, o in zip(user_num.ljust(6, ' '), orig_num)]
            )
            corrected_numbers_html.append(corrected_num)
        
        # 对于用户忘记输入的数字，显示整个数字并标红
        for i in range(len(user_numbers), len(original_numbers)):
            corrected_numbers_html.append(f"<span style='color:red'>{original_numbers[i]}</span>")

        # 用join方法将列表合成字符串并用空格分隔，然后用markdown显示
        st.markdown(' '.join(corrected_numbers_html), unsafe_allow_html=True)
