# Phishing URL Detector

## Overview

A cybersecurity web application that analyzes URLs and identifies whether they are safe or potentially malicious phishing links.

The project uses rule-based phishing detection techniques and calculates a risk score based on suspicious indicators found in the URL.

---

## Features

* URL Validation
* Rule-Based Phishing Detection
* Risk Score Meter (0–100%)
* Safe / Suspicious Classification
* Scan History Tracking
* Downloadable PDF Reports
* Dashboard Statistics
* Responsive Dark-Themed UI
* Flask Backend

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Libraries

* ReportLab

---

## Detection Rules

The application checks for:

* Presence of '@' symbol
* Suspicious keywords:

  * login
  * verify
  * bank
  * secure
* HTTP instead of HTTPS
* Long URL length

---

## Project Structure

phishing-detector/

├── app.py

├── detector.py

├── requirements.txt

├── templates/

│ └── index.html

├── static/

│ ├── style.css

│ └── script.js

└── README.md

---

## Installation

```bash
git clone <repository-url>

cd phishing-detector

pip install -r requirements.txt

python app.py
```

Open:

http://127.0.0.1:5000

---

## Screenshots

Add screenshots of:

* Home Page
* Safe URL Detection
* Suspicious URL Detection
* Scan History
* PDF Report

---

## Future Improvements

* Google Safe Browsing API Integration
* PhishTank Integration
* Machine Learning Based Detection
* User Authentication
* Threat Intelligence Dashboard

---

## Author

Arshdeep
