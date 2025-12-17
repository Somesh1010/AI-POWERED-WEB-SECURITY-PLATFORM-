# WebGuardian Security Platform

## Overview
WebGuardian is an AI-powered web security platform that protects users from **malicious URLs, network anomalies, and malware threats**.

## Features
✔️ **Real-time URL scanning** via **VirusTotal API**  
✔️ **Browser Extension** to warn users while browsing  
✔️ **Web Dashboard** to view **detailed threat reports**  
✔️ **Machine Learning-based detection** *(Future Scope)*  

## How It Works
1️⃣ **User visits a website** → Extension **scans** for threats  
2️⃣ **If malicious**, it **displays a warning** + logs it for review  
3️⃣ **Clicking the alert** redirects to the **WebGuardian dashboard**  
4️⃣ The dashboard **shows VirusTotal's full analysis**  

## Installation & Setup
### **1. Install Web Application**
```sh
cd webapp
pip install -r requirements.txt
python app.py
(Runs Flask backend on http://127.0.0.1:5000)

2. Install Chrome Extension
Open chrome://extensions/

Enable Developer Mode

Click Load Unpacked → Select the extension folder

Technologies Used
🖥 Frontend: HTML, CSS, JavaScript
📡 Backend: Flask (Python)
🔍 Security API: VirusTotal
🌐 Browser Extension: JavaScript

Future Enhancements
🚀 ML-based Threat Classification
📊 Advanced Dashboard Graphs
🔄 Automated Threat Reporting

yaml
Copy
Edit
✅ This **README.md** provides a **clear project overview** and **installation guide**.

---

### **Step 3: Required Dependencies (`requirements.txt`)**
Create **`webapp/requirements.txt`**:

Flask requests

cpp
Copy
Edit
✅ **This allows easy installation** using:
```sh
pip install -r requirements.txt
Final Folder Structure
csharp
Copy
Edit
project/
│── extension/        # Chrome Extension Folder
│── webapp/           # Web Application
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── style.css
│   │   ├── script.js
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
Final Workflow
1️⃣ User browses a website → Extension checks VirusTotal
2️⃣ Safe? ✅ Green ✅ Malicious? ❌ Red ❌ + Dashboard Alert
3️⃣ Click alert → Redirect to Dashboard
4️⃣ Web Dashboard shows detailed VirusTotal analysis