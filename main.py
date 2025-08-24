from db_setup import init_db, connect_db

init_db()


# Adding student 

def add_student(name,age,grade):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",(name,age,grade))

    conn.commit()
    conn.close()

# viewing student list

def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    if rows:
        print("Student List:")
        print("-"*40)
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")
    else:
        print("No students found in database.")


# Search student

def search_student():
    term = input("search by name (full or part): ").strip()
    if not term:
        print("Empty search - try again.")
        return
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, grade FROM students WHERE name LIKE ? ORDER BY id", (f"%{term}%",))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(f"no match for '{term}'")
        return
    
    print(f"\nResults for '{term}':")
    print("-"*30)
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")
              

# Delete student

def delete_student():
    try:
        name = input("Enter the student name to search for deletion: ")

        conn = connect_db()
        cursor = conn.cursor()

        # Search student by name
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))

        results = cursor.fetchall()

        if not results:
            print(f"no student found with name containing '{name}'.")
            conn.close()
            return
        
        # Display results
        print("\nSearch Results:")
        for row in results:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")

        try:
            student_id = int(input("Enter the ID of the student you want to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a valid id number")
            conn.close()
            return
        
        # confirmation of student in db

        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print(f"No student found with ID{student_id}.")
            conn.close()
            return
        
        # confirm before delete

        confirm = input(f"Are you sure you want to delete student '{student[1]}' (ID: {student[0]})? (y/n): ").lower()
        if confirm in ["y", "yes"]:
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
        conn.close()
    except ValueError:
        print("Invalid value. try again.")
                       



# Main Menu

def show_menu():
    while True:
        print("\n|---  Student Management System   ---|")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice,try again.")

# def main():
#     show_menu()


# Starting point

if __name__ == "__main__":
    show_menu()

