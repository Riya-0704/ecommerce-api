## HrOne Backend API — E-Commerce Backend with FastAPI & MongoDB
This is a sample E-Commerce Backend API built with:

🚀 FastAPI (Python)
🍃 MongoDB Atlas
⚡ Motor (Async MongoDB Driver)
📦 Python-dotenv for environment configuration

📌 Features

✅ Create, list, and filter Products

✅ Create and list Orders

✅ Pagination & filtering support on listing APIs

✅ MongoDB connection via environment variables (.env)

✅ Auto-generated API documentation via Swagger UI

## 🗂️ Project Structure

```
/HrOneBackend
│
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app entry point
│   ├── database.py     # MongoDB connection config
│   ├── models.py       # Pydantic models for validation
│   ├── products.py     # Products APIs
│   └── orders.py       # Orders APIs
│
├── requirements.txt
├── .env.example        # Sample env file
├── .gitignore
├── README.md
```


⚙️ Local Setup Instructions

1️⃣ Clone the Repository
git clone https://github.com/<your-github-username>/HrOneBackend.git
cd HrOneBackend

2️⃣ Create & Activate Virtual Environment

python -m venv venv
# On Windows (CMD):
venv\Scripts\activate
# On PowerShell:
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup MongoDB Atlas
Create a free cluster on MongoDB Atlas.

Get the connection URI.

5️⃣ Create a .env file in project root

MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true
Alternatively, duplicate .env.example and update credentials.

✅ .env.example

MONGO_URI=your_mongodb_connection_uri

✅ .gitignore
venv/
__pycache__/
.env

▶️ Running the Server
uvicorn app.main:app --reload
Server runs on http://127.0.0.1:8000

🧩 API Documentation
Swagger Docs
http://127.0.0.1:8000/docs

Redoc
http://127.0.0.1:8000/redoc

📬 API Endpoints

✅ Create Product
POST /products
json
{
    "name": "T-shirt",
    "description": "Cotton shirt",
    "price": 299,
    "sizes": ["S", "M", "L", "XL"]
}

✅ List Products
GET /products

Query Param	Description
name	Filter by product name (partial match)
size	Filter by size
limit	Number of results to return
offset	Number of documents to skip

Example:

GET /products?name=shirt&size=L&limit=5&offset=0

✅ Create Order
POST /orders

json
{
    "user_id": "user123",
    "products": ["<product_id>"],
    "total_price": 299
}

✅ List Orders by User

GET /orders/{user_id}?limit=5&offset=0

✅ Testing the APIs
1️⃣ Swagger UI
Visit:

http://127.0.0.1:8000/docs
Interactive testing interface

2️⃣ Postman
Import the following Postman collection for direct testing:

(You can export a Postman collection or create your own)

3️⃣ Curl Example
curl -X POST "http://127.0.0.1:8000/products" -H "Content-Type: application/json" -d "{\"name\": \"Shoes\", \"description\": \"Running Shoes\", \"price\": 499, \"sizes\": [\"7\", \"8\", \"9\"]}"

🚀 Deployment Guide
✅ Deploy on Render.com
Push your code to GitHub (public/private).

Go to Render.com, create a New Web Service.

Connect your GitHub repo.

Set:

Build Command: pip install -r requirements.txt

Start Command:

uvicorn app.main:app --host 0.0.0.0 --port 10000
Add Environment Variable:

MONGO_URI = your MongoDB connection string

✅ Deploy on Railway.app
Visit Railway.app.

Create a New Project > Deploy from GitHub.

Set your MONGO_URI in Environment Variables.

Railway will auto-deploy the FastAPI app.

🏁 Final Deliverables for Submission
✅ Public GitHub Repo URL

✅ Live API Base URL (e.g., https://hrone-backend-production.onrender.com)

✅ Ensure .env is excluded in repo via .gitignore.

✅ Best Practices Followed
Clean and modular code

.env for environment variables

Async DB operations

Paginated listing

Auto-generated API docs

✅ Future Improvements (Optional Enhancements)
User authentication

Update/delete product and order APIs

Better logging

Unit tests using Pytest

Dockerized deployment

✅ Author
Riya


