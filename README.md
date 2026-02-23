🚀 Job Portal API (Production Ready)
🚀 Overview
A production-ready Job Portal REST API built with Django and Django REST Framework.
The system supports role-based authentication (Recruiter & Candidate), secure JWT login, job posting, job applications with resume upload, and search with pagination.
Live API:
https://job-portal-api-9m6m.onrender.com/api/jobs/
⚠️ Note: Hosted on Render (Free Plan). Initial request may take 20–30 seconds due to cold start.

📌 Features
🔐 JWT Authentication (Access & Refresh Tokens)
👤 Custom User Model (Recruiter & Candidate Roles)
🛂 Role-Based Authorization
📄 Job Posting (Recruiters Only)
📬 Job Application with Resume Upload (Candidates Only)
🔎 Search, Pagination & Ordering
🗄 PostgreSQL Database (Local + Cloud)
🌍 Production Deployment (Render)
📦 Static File Handling using WhiteNoise
⚙️ Environment Variable Based Configuration

🏗 Tech Stack
Python 3.11
Django
Django REST Framework
PostgreSQL
JWT (SimpleJWT)
Gunicorn
WhiteNoise
Render (Cloud Deployment)

📂 Important Endpoints
/admin/
POST /api/token/
GET /api/jobs/
POST /api/jobs/create/
POST /api/jobs/apply/

📈 Project Status
✔ Production Deployed
✔ Cloud Database Connected
✔ Role-Based Security Implemented
✔ Fully Functional REST API

