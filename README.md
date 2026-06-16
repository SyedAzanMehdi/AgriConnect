# AgriConnect 

A Comprehensive Agriculture Marketplace & AI Crop Disease Detection Platform

## Overview

AgriConnect is a modern web-based agriculture marketplace designed to connect farmers directly with buyers while providing AI-powered crop disease diagnosis, regional market insights, and government agricultural scheme information.

The platform focuses on supporting smallholder farmers in Pakistan, particularly in the Mianwali region, by eliminating unnecessary middlemen and improving transparency in agricultural trade.

## Key Features

### Farmer Portal

* Crop inventory management
* Marketplace listing creation
* Offer and bid management
* AI crop disease diagnosis
* Scan history tracking

### Buyer Portal

* Browse marketplace listings
* Search and filter crops
* Submit price offers
* Track negotiation status
* View farmer contact information

### Admin Dashboard

* User approval management
* Disease library management
* Government schemes management
* System moderation tools

### AI Disease Detection

* Client-side image analysis
* Leaf disease identification
* Urdu & English diagnosis reports
* Treatment recommendations
* Offline fallback support

## Technology Stack

| Layer              | Technology                   |
| ------------------ | ---------------------------- |
| Frontend           | HTML5, CSS3, JavaScript ES6+ |
| Charts             | Chart.js                     |
| Backend            | PHP 8.x                      |
| Database           | MySQL / MariaDB              |
| AI Engine          | JavaScript Canvas API        |
| Optional AI Server | Python Flask                 |

## Project Structure

```text
AgriConnect/
│
├── index.html
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── SRS.pdf
│   ├── ERD.png
│   ├── Architecture.png
│   └── UserManual.pdf
│
├── css/
│   └── styles.css
│
├── js/
│   ├── main.js
│   ├── app.js
│   ├── dashboard.js
│   ├── ai-disease.js
│   └── data.js
│
├── php/
│   ├── api.php
│   ├── setup.php
│   └── run_sql.php
│
├── sql/
│   ├── database.sql
│   └── regional_data.sql
│
├── assets/
│   ├── images/
│   ├── icons/
│   └── screenshots/
│
└── ai-server/
    ├── ai_server.py
    ├── crop_analysis.py
    └── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/agriconnect.git
cd agriconnect
```

### Database Setup

1. Start Apache and MySQL.
2. Open:

```text
http://localhost/agriconnect/php/setup.php
```

3. Database will be automatically created and seeded.

### Run Application

```text
http://localhost/agriconnect/
```

## Contributors

* Azan Mehdi (BIT-F24-M14)
* Usman Saif (BIT-F24-M06)

University of Mianwali

## License

This project is developed for educational and academic purposes under CSC-271 Database Systems.
