# 📷 Instagram Follower Checker (Using Selenium)

This Python script allows you to **automatically log in to Instagram**, **retrieve your followers and following lists**, and **identify users who don't follow you back** using Selenium WebDriver.

---

## 🚀 Features

- Log in to Instagram with your credentials.
- Navigate to your profile.
- Extract the list of followers and followings.
- Compare and identify accounts that you follow but who don’t follow you back.
- Uses Selenium for browser automation.

---

## DEMO

[Screencast from 2025-04-08 18-58-44.webm](https://github.com/user-attachments/assets/9f8cc4c7-f141-48c7-89a6-ebfc93752896)


---

## 🛠️ Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver compatible with your Chrome version
- Selenium package

### 📦 Install Dependencies

```bash
pip install selenium
```

---

## 🖥️ How to Run It Locally

1. **Clone the repository or copy the script** into your working directory.

2. **Update your credentials and username**:

   - Replace `'-------'` with your Instagram username and password.
   - Replace the username in the profile URL (`https://www.instagram.com/-------`) with your Instagram username.

3. **Ensure the ChromeDriver path is correct**:

   ```python
   chrome_driver_path = "/usr/bin/chromedriver"
   ```
   Change this path if your `chromedriver` is located elsewhere.

4. **Run the script**:

   ```bash
   python instagram_follower_checker.py
   ```

5. **Manual intervention**:
   Sometimes you may need to manually click or confirm parts of the UI if Selenium can't find the button.

---

## ⚠️ Important Notes

- **Instagram frequently changes its UI**: Selectors may break, requiring future updates.
- **Two-factor authentication (2FA)**: This script does not currently support login flows involving 2FA.
- **Rate Limiting / Ban Risk**: Excessive automation may flag your account. Use responsibly.

---

## 🔧 Possible Improvements for the Future

- ✅ Add support for **headless mode** to run the browser in the background.
- ✅ Add **error handling** for unexpected page layout changes.
- ✅ Save results to a **CSV or JSON file** for record-keeping.
- ✅ Convert follower counts using **Instagram Graph API** (requires API access).
- ✅ Create a **GUI interface** or **web interface** for user-friendliness.

---

## 🧑‍💻 Disclaimer

This tool is intended for educational purposes only. Automating social media accounts may violate Instagram's Terms of Service. Use at your own risk.

---

## 📚 Contributing

Contributions are welcome! Whether it's a bug fix, feature suggestion, or enhancement, feel free to open an issue or submit a pull request.

To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add new feature'`
5. Push to your branch: `git push origin feature-name`
6. Submit a pull request.

Please ensure your code follows the existing style and includes relevant test cases or documentation if applicable.



