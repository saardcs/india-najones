import streamlit as st
import qrcode
import io

st.title("India Najones Lunchtime Special")
st.image("india-najones.jpg", width=400)
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

all_combos = [(m, d) for m in mains for d in desserts]
total_possible = len(all_combos)

if "selected_combos" not in st.session_state:
    st.session_state.selected_combos = []

# Sidebar with QR code
st.sidebar.header("Scan This QR Code to View Menu Online")

qr_link = "https://india-najones.streamlit.app"  # Replace with your actual URL
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)

st.sidebar.image(buf, width=300, caption=qr_link)

# Main UI
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

    if len(st.session_state.selected_combos) == total_possible:
        st.balloons()
        st.success("🎉 Congratulations! You found all 25 meal combos! 🎉")
