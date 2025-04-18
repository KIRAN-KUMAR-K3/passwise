# 🔐 Passwise

**Passwise** is a modern, professional password strength checker that evaluates password complexity, entropy, and uniqueness in real-time. It provides detailed feedback, suggestions, and visual indicators to help users create secure and robust passwords.

![Passwise Screenshot](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpFNK2dFoAyFvyrx5_Twt9F3leuop0hv_m3cGDPkGL1nACE6r9g6oZzI_t6GuBtWi8F9A&usqp=CAU) <!-- optional: replace with your image link -->

---

## 🚀 Features

- ✅ Real-time password strength analysis
- ✅ Entropy calculation for estimating password unpredictability
- ✅ Checks for uppercase, lowercase, digits, symbols
- ✅ Identifies common and weak passwords
- ✅ Provides improvement suggestions
- ✅ Clean, responsive dark-themed UI
- ✅ Lightweight and easy to run locally

---

## 📸 Demo

> Coming soon: Live demo or GIF here...

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **HTML5/CSS3**
- **WTForms (optional)**
- **Regex**
- **Entropy Calculation**

---

## 📂 Project Structure

```
passwise/
├── static/
│   └── style.css              # Custom styling
├── templates/
│   └── index.html             # Main UI template
├── app.py                     # Flask application
├── password_checker.py        # Password analysis logic
├── common_passwords.txt       # List of weak/common passwords
└── requirements.txt           # Project dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/KIRAN-KUMAR-K3/passwise.git
cd passwise
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

### 4. Open in Browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📌 Example Output

- **Strength:** Very Strong  
- **Entropy:** 78.23 bits  
- **Suggestions:** Avoid dictionary words, use symbols, increase length, etc.

---

## 🧠 How It Works

1. Analyzes password using regex and entropy formula
2. Checks against a list of the most common 10,000 passwords
3. Calculates a strength score and returns user feedback
4. Displays results with styled feedback for clarity

---

## 🔒 Future Enhancements

- [ ] Integration with [HaveIBeenPwned](https://haveibeenpwned.com/API) API
- [ ] Add password generator tool
- [ ] Deploy on Render/Vercel
- [ ] Visual entropy meter (progress bar or graph)
- [ ] Support for browser extension

---

## 🙌 Credits

Developed with 💻 by [Kiran Kumar K](https://github.com/KIRAN-KUMAR-K3)  
Inspired by cybersecurity practices and secure web design principles.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

> 🔗 **GitHub Repo**: [github.com/KIRAN-KUMAR-K3/passwise](https://github.com/KIRAN-KUMAR-K3/passwise)

```
