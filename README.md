# 🎫 Support CRM System

A fully functional Customer Support Ticket Management System built with Python FastAPI, SQLite, and HTML Tailwind CSS.

## 🌐 Live Demo
**Live App:** https://support-crm-6o8u.onrender.com  
**API Docs:** https://support-crm-6o8u.onrender.com/docs  
**GitHub:** https://github.com/HarshadaBidaye/support-crm  

---

## 📋 Features
- ✅ Create support tickets with customer info
- ✅ Auto-generated unique Ticket IDs (TKT-001)
- ✅ Dashboard with real-time stats
- ✅ Live search by name, email, ID, subject
- ✅ Filter tickets by status
- ✅ View and update ticket details
- ✅ Add notes/comments to tickets
- ✅ REST API with Swagger documentation
- ✅ Mobile responsive UI

---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python FastAPI |
| Database | SQLite + SQLAlchemy |
| Frontend | HTML + Tailwind CSS |
| Templates | Jinja2 |
| Deployment | Render.com |

---

## 📁 Project Structure
```
support-crm/
├── main.py          # FastAPI app, all routes
├── database.py      # Database connection setup
├── models.py        # Database table definitions
├── schemas.py       # Data validation schemas
├── templates/
│   ├── index.html        # Home dashboard
│   ├── create.html       # Create ticket form
│   └── ticket_detail.html # Ticket detail page
├── static/          # Static files
├── requirements.txt # Python dependencies
└── README.md
```

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/HarshadaBidaye/support-crm.git
cd support-crm
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
uvicorn main:app --reload
```

### 5. Open browser
---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tickets` | Get all tickets |
| POST | `/api/tickets` | Create new ticket |
| GET | `/api/tickets/{ticket_id}` | Get one ticket |
| PUT | `/api/tickets/{ticket_id}` | Update ticket |

---

## 🗄️ Database Schema

**Tickets Table**
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| ticket_id | String | Unique ID (TKT-001) |
| customer_name | String | Customer name |
| customer_email | String | Customer email |
| subject | String | Issue subject |
| description | String | Issue description |
| status | String | Open/In Progress/Closed |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last update timestamp |

**Notes Table**
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| ticket_id | String | Foreign key to tickets |
| note_text | String | Note content |
| created_at | DateTime | Creation timestamp |

---

## ⚙️ Environment Variables

Create a `.env` file:
---

## 🎯 Assignment Requirements Met

| Requirement | Status |
|-------------|--------|
| Create tickets | ✅ |
| List all tickets | ✅ |
| Search functionality | ✅ |
| Filter by status | ✅ |
| View and update tickets | ✅ |
| Notes/comments | ✅ |
| Deployed live | ✅ |
| GitHub repository | ✅ |
| Demo video | ✅ |

---

## 🙏 Note on AI Usage
This project was built with the help of AI tools. As the assignment encouraged, AI tools are how real developers work today. All code has been understood, debugged, and deployed by me.

---

## 👩‍💻 Author
**Harshada Bidaye**  
B.Sc. Data Science — KES Shroff College Mumbai  
GitHub: [@HarshadaBidaye](https://github.com/HarshadaBidaye)
