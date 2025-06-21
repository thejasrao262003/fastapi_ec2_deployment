# 🚀 FastAPI Product Service on EC2

A minimal FastAPI application with routes and services to simulate product creation and retrieval. This version uses in-memory storage (no database) and is ready to be deployed on an EC2 instance.

---

## 📦 Features

- Create a product (with ID, name, and price)
- Retrieve product details by ID
- Simple modular structure (routes + services)
- No database required (uses in-memory store)
- Easy to extend to real-world use cases

---

## 🗂️ Project Structure

```
fastapi_app/
├── main.py                   # Entry point
├── models.py                 # Product schema (Pydantic)
├── routes/
│   └── product_routes.py     # API endpoints
├── services/
│   └── product_service.py    # Business logic (in-memory store)
```

---

## 🛠️ Installation & Run (Local or EC2)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-ec2-demo.git
cd fastapi-ec2-demo
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4️⃣ Run the Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🔌 API Endpoints

### ➕ Create Product

```http
POST /products/
Content-Type: application/json
```

**Sample JSON:**

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 599.99
}
```

### 📦 Get Product

```http
GET /products/1
```

**Response:**

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 599.99
}
```

---

## 📚 Swagger UI

Once the app is running, visit:

```
http://<your-ec2-ip>:8000/docs
```

---

## ☁️ Deploy on EC2

1. SSH into your EC2 instance
2. Install Python, pip, and Git
3. Clone this repo and run using Uvicorn or use Gunicorn + Nginx (optional)
4. Open port 8000 in your EC2 security group to allow traffic

---

## 🔒 Security Note

This demo uses in-memory storage and is not production-safe. For a real app:
- Use a database (PostgreSQL, MongoDB, etc.)
- Add proper validation & auth
- Use environment variables for config
