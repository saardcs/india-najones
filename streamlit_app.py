import streamlit as st
import qrcode
import io

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

all_combos = [(m, d) for m in mains for d in desserts]
total_possible = len(all_combos)

if "selected_combos" not in st.session_state:
    st.session_state.selected_combos = []

# Sidebar for QR code and zoom slider
st.sidebar.header("Menu QR Code")
qr_link = "https://your-app-url.com"  # Replace with your actual URL

zoom = st.sidebar.slider("Zoom QR Code", min_value=100, max_value=400, value=200, step=50)

# Generate QR code with given size
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)

st.sidebar.image(buf, caption=qr_link, width=zoom)

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
