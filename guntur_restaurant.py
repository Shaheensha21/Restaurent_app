import streamlit as st
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import tempfile

st.set_page_config(page_title="Guntur Hotel", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.header {
    color: #7b006b;
    font-size: 2em;
    font-weight: bold;
    background: #ffe6fb;
    padding: 10px;
    border-radius: 12px;
    text-align: center;
}
.invoice-box {
    background: #fff4fc;
    padding: 20px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<div class="header">🍽️ Welcome to Guntur Hotel</div>', unsafe_allow_html=True)

# ================= MENU =================
MENU = {
    "Beverages ☕": {
        "Tea": 20, "Coffee": 50, "Coke": 70, "Pepsi": 50, "Water Bottle": 20
    },
    "Snacks 🍔": {
        "Samosa": 20, "Burger": 50, "Gulab Jamun": 30, "Jalebi": 30
    },
    "Main Course 🍛": {
        "Veg Biryani": 120,
        "Chicken Biryani": 150,
        "Mutton Biryani": 300,
        "Jumbo Bucket Biryani": 500,
        "Pizza": 150
    }
}

QUOTES = [
    "Good food, good mood 🍽️",
    "Life is short, eat well 😋",
    "Every meal is a celebration 🎉",
    "Food tastes better when shared ❤️"
]

# ================= SESSION STATE =================
if "order" not in st.session_state:
    st.session_state.order = {}

# ================= LAYOUT =================
left, right = st.columns(2, gap="large")

# -------- MENU --------
with left:
    st.subheader("📋 Menu")
    for category, items in MENU.items():
        st.markdown(f"### {category}")
        for item, price in items.items():
            st.write(f"**{item}** — ₹{price}")

# -------- ORDER --------
with right:
    st.subheader("🛒 Place Your Order")

    category = st.selectbox("Select Category", list(MENU.keys()))
    item = st.selectbox("Select Item", list(MENU[category].keys()))
    qty = st.number_input("Quantity", 1, 10, 1)

    st.info(random.choice(QUOTES))

    if st.button("➕ Add to Order"):
        st.session_state.order[item] = st.session_state.order.get(item, 0) + qty
        st.success(f"{qty} × {item} added")

# ================= INVOICE =================
if st.session_state.order:
    st.markdown("---")
    st.subheader("🧾 Invoice")

    invoice_data = [["Item", "Qty", "Price", "Total"]]
    subtotal = 0

    for item, qty in st.session_state.order.items():
        price = next(MENU[c][item] for c in MENU if item in MENU[c])
        total = price * qty
        subtotal += total
        invoice_data.append([item, qty, f"₹{price}", f"₹{total}"])

    gst = subtotal * 0.05
    discount = 50 if subtotal >= 500 else 0
    grand_total = subtotal + gst - discount

    invoice_data.extend([
        ["", "", "Subtotal", f"₹{subtotal}"],
        ["", "", "GST (5%)", f"₹{gst:.2f}"],
        ["", "", "Discount", f"-₹{discount}"],
        ["", "", "Grand Total", f"₹{grand_total:.2f}"]
    ])

    st.markdown('<div class="invoice-box">', unsafe_allow_html=True)
    st.table(invoice_data)
    st.markdown('</div>', unsafe_allow_html=True)

    # ================= PDF INVOICE =================
    def generate_pdf():
        file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        doc = SimpleDocTemplate(file.name, pagesize=A4)
        styles = getSampleStyleSheet()

        elements = [
            Paragraph("🧾 Guntur Hotel Invoice", styles["Title"]),
            Paragraph("Thank you for dining with us!", styles["Normal"]),
        ]

        table = Table(invoice_data)
        table.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.purple),
            ("BACKGROUND", (0,0), (-1,0), colors.lavender),
            ("ALIGN", (1,1), (-1,-1), "CENTER")
        ]))

        elements.append(table)
        doc.build(elements)
        return file.name

    pdf_path = generate_pdf()
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download Invoice (PDF)", f, file_name="Guntur_Invoice.pdf")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("❌ Clear Order"):
            st.session_state.order = {}
            st.experimental_rerun()

    with col2:
        st.success("✅ Order Ready!")

st.markdown("### 😊 Thank you! Visit Again")
st.balloons()
