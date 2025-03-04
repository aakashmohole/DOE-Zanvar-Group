
# DOE Zanvar Group - Django Project Setup

## Prerequisites
Ensure you have the following installed:
- Python (>=3.10)
- PostgreSQL (if using a database)
- Git (optional)

## Setup Instructions

### 1. Clone the Repository (If applicable)
```sh
git clone https://github.com/aakashmohole/DOE-Zanvar-Group
cd doeproject
```

### 2. Set Up Virtual Environment
```sh
python -m venv doeenv  # Create virtual environment
source doeenv/Scripts/activate  # Activate (Windows)
# OR
source doeenv/bin/activate  # Activate (Mac/Linux)
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure `.env` File
Create a `.env` file in the project's root directory and add the following variables:

```env
DATABASE_URL=postgresql://doedb_owner:npg_********ep-delicate-bread-a8f9v51h-pooler.eastus2.azure.neon.tech/doedb?sslmode=require


EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
EMAIL_USE_TLS=True
```

Make sure to replace values accordingly.

### 5. Apply Migrations & Run Server
```sh
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

### 🔑 **Authentication Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/api/auth/register/` | Register a new user |
| **POST** | `/api/auth/login/` | User login (returns token) |
| **POST** | `/api/auth/logout/` | Logout user |
| **GET** | `/api/auth/user/` | Get authenticated user details |

### 📊 **DOE Data Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/api/doe-data/` | Retrieve all DOE data |
| **GET** | `/api/doe-data/{id}/` | Retrieve a specific DOE record |
| **POST** | `/api/doe-data/` | Create a new DOE record |
| **PUT** | `/api/doe-data/{id}/` | Update a DOE record |
| **DELETE** | `/api/doe-data/{id}/` | Delete a DOE record |
| **GET** | `/api/filter-doe/?Tool_Diameter={value}` | Filter DOE data by tool diameter |

---

### 6. API Documentation
For **Swagger UI** (if using `drf-yasg`):
```sh
http://127.0.0.1:8000/swagger/
```

For **Redoc UI**:
```sh
http://127.0.0.1:8000/redoc/
```

To generate API schema (if using `drf-spectacular`):
```sh
python manage.py spectacular --color --file schema.yaml
```

---

🚀 **Your Django project is now ready to use!**
```

Let me know if you need more details! 🚀
