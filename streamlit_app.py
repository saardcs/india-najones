import streamlit as st

st.title("India Najones Lunchtime Special")

mains = [
    "Chicken Tikka",
    "Lamb Vindaloo",
    "Keema Mattar",
    "Rogan Josh",
    "Biriyani"
]

desserts = [
    "Lemon Surprise",
    "Orange Surprise",
    "Mango Surprise",
    "Pineapple Surprise",
    "Banana Split"
]

if "selected_combos" not in st.session_state:
    st.session_state.selected_combos = []

selected_main = st.selectbox("Choose a main course:", mains)
selected_dessert = st.selectbox("Choose a dessert:", desserts)

if st.button("Add Combo"):
    combo = (selected_main, selected_dessert)
    if combo in st.session_state.selected_combos:
        st.warning("This combo has already been added!")
    else:
        st.session_state.selected_combos.append(combo)
        st.success(f"Added combo: {selected_main} + {selected_dessert}")

if st.session_state.selected_combos:
    st.header("Selected Combos:")
    for i, (m, d) in enumerate(st.session_state.selected_combos, 1):
        st.write(f"{i}. {m} + {d}")
