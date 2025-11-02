import streamlit as st
import random
import io
st.set_page_config(layout="wide")

# ========== CSS ==========
st.markdown("""
<style>
.my-marquee {
    color: #b400c1;
    font-size: 1.9em;
    font-weight: bold;
    padding: 6px 0;
    background: #ffe0fb;
    border-radius: 10px;
    margin-bottom: 8px;
}
.bill-table td, .bill-table th {
    background: #fff4fc !important;
    color: #32024f !important;
}
</style>
""", unsafe_allow_html=True)

# ========== WELCOME ==========
st.markdown("""
<div class="my-marquee">
<marquee>🎉 Welcome to Guntur Hotel! 🍽️ Enjoy your meal! 🎉</marquee>
</div>
""", unsafe_allow_html=True)

# ========== MENU ==========
menu = {
    'Tea':20,'Coffee':50,'Samosa':20,'Gulab Jamun':30,'Jalebi':30,'Khichdi':70,
    'Chicken Biryani':150,'Mutton Biryani':300,'Jumbo Bucket Biryani':500,
    'Water Bottle':20,'Thums Up':50,'Pepsi':50,'Coke':70,'Limca':50,
    'Veg Biryani':120,'Chicken or Veg Pizza':150,'Burger':50
}

# ========== QUOTES ==========
quotes = [
    "Enjoy your meal and have a great day!",
    "The secret ingredient is always love.",
    "Food is happiness on a plate.",
    "Good food makes good mood!",
    "Savor every bite!",
    "Great choices! Your appetite thanks you.",
    "A flavorful journey awaits.",
    "Happiness is homemade.",
    "Life is short, eat dessert first.",
    "Good friends, good food, good times!",
    "Taste the joy in every dish.",
    "Fresh flavors, happy hearts.",
    "May your plate always be full.",
    "Every meal is a celebration!",
    "Let the feast begin!",
    "Bon appétit – taste the magic!",
    "Nourish your soul with goodness.",
    "Delicious moments ahead.",
    "Wholesome bites for a happy life.",
    "Eat well, laugh often, love much.",
    "Welcome to your happy place!",
    "Where taste meets tradition.",
    "Eating well is a form of self-respect.",
    "Raise your forks for good fortune!",
    "May your cravings always be satisfied.",
    "Good things come to those who eat!",
    "Treat yourself to greatness.",
    "Life happens, food helps.",
    "You’re one bite away from a good mood.",
    "Let delicious memories be made today."
]

# ========== LAYOUT ==========
left, right = st.columns(2, gap="large")

# ----------- MENU LEFT -----------
with left:
    st.title("📋 Menu")
    for item, price in menu.items():
        col1, col2 = st.columns([3,1])
        with col1:
            st.write(f"**{item}**")
        with col2:
            st.write(f"₹{price}")

# ---------- ORDER RIGHT ----------
with right:
    st.title("🛒 Place Your Order")
    order_item = st.selectbox("Select a food item:", list(menu.keys()))
    order_qty = st.number_input(f"How many plates of {order_item}?", min_value=1, max_value=10, step=1)

    # Show a random quote every time the order section is visible or rerun
    quote = random.choice(quotes)
    st.info(quote)

    if "order" not in st.session_state:
        st.session_state.order = {}

    if st.button("Add to Order", key="addorderbtn"):
        if order_item in st.session_state.order:
            st.session_state.order[order_item] += order_qty
        else:
            st.session_state.order[order_item] = order_qty
        st.success(f"✅ {order_qty} × {order_item} added!")

# --------- BILL SECTION (Below) -------------
if st.session_state.order:
    st.markdown("---")
    st.subheader("🧾 Your Bill")
    bill_items = []
    total = 0

    bill_text = "----- Your Bill -----\n\n"
    for food, qty in st.session_state.order.items():
        amount = menu[food] * qty
        total += amount
        bill_items.append([food, qty, menu[food], amount])
        bill_text += f"{food:20} x{qty:<2} ₹{menu[food]:<3} ₹{amount}\n"

    bill_text += f"\nGrand Total: ₹{total}\n"

    st.markdown(
        "<table class='bill-table'><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr>" +
        "".join([f"<tr><td>{i[0]}</td><td>{i[1]}</td><td>₹{i[2]}</td><td>₹{i[3]}</td></tr>" for i in bill_items]) +
        "</table>",
        unsafe_allow_html=True
    )
    st.write(f"### 💰 Grand Total: **₹{total}**")

    # ----- Download bill button -----
    bill_file = io.StringIO(bill_text)
    st.download_button(label="Download Bill", data=bill_file.getvalue(), file_name="Guntur_Bill.txt", mime="text/plain")

    if st.button("Clear Order", key="clearbtn"):
        st.session_state.order = {}
        st.warning("Order cleared!")

st.markdown("### ✅ Thank you! Visit Again 😊")
st.balloons()
