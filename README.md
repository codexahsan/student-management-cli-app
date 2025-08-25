# 🎓 Student Management CLI App

A simple **Command Line Interface (CLI) app** built with **Python** and **SQLite** to manage student records.  
This project is designed for learning **databases + Python basics**, and can be extended into larger applications.

---

## 📌 Features
- ➕ **Add a student** (Name, Age, Grade)
- 📃 **View all students** in the database
- 🔎 **Search students** by full or partial name
- ❌ **Delete a student** safely (search by name → confirm ID → delete)
- ✏  **Update a student** safely (search by name → Confirm ID → edit details)
- 💾 **Persistent storage** with SQLite (`students.db` file)

---

## 🛠️ Technologies Used
- **Python 3** (CLI + database operations)
- **SQLite3** (lightweight embedded database)

---

## 📂 Project Structure
Student-Management-CLI-App/
│
├── db_setup.py # Database initialization and connection helpers
├── main.py # Main CLI app (menu system + CRUD functions)
├── students.db # SQLite database (created automatically if not exists)
└── README.md # Project documentation


## 🚀 Getting Started

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/student-management-cli-app.git
cd student-management-cli-app
2️⃣ Run the app
Make sure you have Python 3.10+ installed, then run:


python main.py

3️⃣ Example menu

|---  Student Management System   ---|
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Exit

💡 Example Usage
Add a student → Enter details (name, age, grade)

View students → Lists all with IDs

Search → Enter partial name, see results

Delete → Search by name, pick correct ID, confirm before delete

Update → Search by name, pick correct ID, edit details

📖 Learning Goals
This project is part of my Python + Web Development journey.
Key skills learned:

How to use SQLite in Python

Writing modular code (db_setup.py vs main.py)

Building an interactive menu-driven CLI app

Performing CRUD operations (Create, Read, Update, Delete)

🔮 Future Improvements
Update student records (edit age/grade)

Export students to CSV/Excel

Add authentication (admin login)

Build a Flask web version of the app 🌐

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch

Submit a pull request 

📜 License
This project is open-source and available under the MIT License.

