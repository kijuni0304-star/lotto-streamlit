import random

import streamlit as st

st.set_page_config(
    page_title="로또 번호 생성기",
    page_icon="🎯",
    layout="centered",
)

st.title("🎰 로또 번호 생성기 (보너스 포함)")
st.markdown("버튼을 누르면 **1~45** 중에서 **메인 6개 + 보너스 1개** 번호를 뽑아요! 🍀")

count = st.slider("몇 세트를 뽑을까요?", min_value=1, max_value=10, value=1)


def draw_one_set() -> tuple[list[int], int]:
    """서로 겹치지 않는 메인 번호 6개와 보너스 번호 1개를 뽑습니다."""
    numbers = random.sample(range(1, 46), 7)
    main_numbers = sorted(numbers[:6])
    bonus_number = numbers[6]
    return main_numbers, bonus_number


if st.button("🎲 로또 번호 뽑기", type="primary", use_container_width=True):
    for index in range(1, count + 1):
        main, bonus = draw_one_set()
        st.success(f"세트 {index} ➜ 🎯 메인: {', '.join(map(str, main))}")
        st.info(f"세트 {index} ➜ 💎 보너스: {bonus}")
    st.balloons()
else:
    st.caption("⬆️ 세트 개수를 정하고 버튼을 눌러보세요!")

st.markdown("---")
st.caption("Made with Streamlit · 행운 가득! 🍀")
