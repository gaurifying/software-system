import mysql.connector
import tkinter as tk

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database=" addsoftwarepackages",
    # auth_plugin="auth_socket"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to insert data into the database
def add_package():
    package_name = package_name_entry.get()
    description = description_entry.get("1.0", tk.END).strip()
    associated_nodes = nodes_entry.get()
    associated_files = files_entry.get()
    
    # Check if the package name already exists in the database
    cursor.execute("SELECT * FROM packages WHERE package_name = %s", (package_name,))
    existing_package = cursor.fetchone()
    
    if existing_package:
        status_label.config(text="Package is added in table")
    else:
        # Insert data into the database
        sql = "INSERT INTO packages (package_name, description, associated_nodes, associated_files) VALUES (%s, %s, %s, %s)"
        values = (package_name, description, associated_nodes, associated_files)
        cursor.execute(sql, values)
        db.commit()
        status_label.config(text="Package added successfully!")

def modify_package():
    package_name = package_name_entry.get()
    description = description_entry.get("1.0", tk.END).strip()
    associated_nodes = nodes_entry.get()
    associated_files = files_entry.get()

    cursor.execute("UPDATE packages SET description = %s, associated_nodes = %s, associated_files = %s WHERE package_name = %s",
                   (description, associated_nodes, associated_files, package_name))
    db.commit()
    status_label.config(text=f"Package '{package_name}' modified successfully!")


# GUI Setup
root = tk.Tk()
root.title("Software Package Management")

# Package Name Label and Entry
package_name_label = tk.Label(root, text="Package Name:")
package_name_label.pack()
package_name_entry = tk.Entry(root)
package_name_entry.pack()

# Description Label and Textbox
description_label = tk.Label(root, text="Description:")
description_label.pack()
description_entry = tk.Text(root, height=4, width=50)
description_entry.pack()

# Associated Nodes Label and Entry
nodes_label = tk.Label(root, text="Associated Nodes:")
nodes_label.pack()
nodes_entry = tk.Entry(root)
nodes_entry.pack()

# Associated Files Label and Entry
files_label = tk.Label(root, text="Associated Files:")
files_label.pack()
files_entry = tk.Entry(root)
files_entry.pack()

# Add Package Button
add_button = tk.Button(root, text="Add Package", command=add_package)
add_button.pack()

# Status Label
status_label = tk.Label(root, text="")
status_label.pack()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection
db.close()