# 🍽️ Guntur Hotel – Restaurant Ordering & Billing App

A **Streamlit-based Restaurant Ordering and Billing Application** that allows users to browse a categorized menu, place orders, and generate a **professional invoice-style PDF bill** with GST and discount calculations.

💻 **Live Demo:** [Guntur Restaurant App](https://restaurentapp-4cvatfbrln22qdptod7pr7.streamlit.app/)

---

## 🚀 Features

* 📋 Categorized restaurant menu (Beverages, Snacks, Main Course)
* 🛒 Add items to cart with quantity control
* 🧠 Session-based order management
* 💰 Automatic bill calculation
* 🧾 Invoice-style billing format
* 📄 PDF invoice download
* 🧮 GST (5%) and discount logic
* 🎨 Clean and responsive Streamlit UI
* 🔐 Local session handling

---

## 🏗️ Application Flow

1. User selects a **category** and **food item**
2. Adds items to the **order cart**
3. Order is stored using **Streamlit session state**
4. **Subtotal** is calculated automatically
5. **GST and discount** applied
6. Invoice is displayed in a **table format**
7. **PDF invoice** can be downloaded for records

---

## 🛠️ Tech Stack

| Component            | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Web Framework        | Streamlit               |
| PDF Generation       | ReportLab               |
| State Management     | Streamlit Session State |
| UI Styling           | Custom CSS              |
| Deployment           | Streamlit Cloud         |

---

## 📂 Project Structure

```
Guntur-Hotel-App/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/guntur-hotel-app.git
cd guntur-hotel-app
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📦 Dependencies (`requirements.txt`)

```
streamlit==1.30.0
reportlab==4.0.4
```

Optional (for future enhancements):

```
pandas==2.1.0
numpy==1.27.0
```

---

## ✨ Future Enhancements

* 🔐 User login & admin dashboard
* 📊 Daily sales and revenue analytics
* 🗄️ Database integration (SQLite / PostgreSQL)
* 🧾 Order history tracking
* 🌐 Online deployment with custom domain

---

## 👤 Author

**Shaik Abdul Shahansha**
🎓 MCA Student | Data & AI Enthusiast | Python & Streamlit Developer

📫 Feel free to connect and collaborate!

---

## ⭐ Feedback & Support

If you like this project, give it a ⭐ and share your fee
