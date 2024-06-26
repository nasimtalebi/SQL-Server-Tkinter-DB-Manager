import tkinter as tk
from tkinter import filedialog, messagebox
import pyodbc
import pandas as pd
from datetime import datetime  # Added import for datetime

# Define function to check if table exists
def table_exists(cursor, table_name):
    cursor.execute(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}'")
    return cursor.fetchone()[0] > 0

# Define function to create table
def Create_Table():
    conn_str = (
        r'driver={SQL Server};'
        r'server=(local);'
        r'database=ODS;'
        r'trusted_connection=yes;'
    )
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()

    table_name = entry_tableName.get()

    if table_exists(cursor, table_name):
        messagebox.showwarning("Table Exists", f"The table '{table_name}' already exists!")
        return

    url = filedialog.askopenfilename()  # Prompt to select the file
    if not url:  # Check if the user cancels file selection
        return
    df = pd.read_excel(url)
    df.fillna('', inplace=True)
    
    # List of the column for creating the new table in SQL
    column_data_types = df.dtypes

    # Initialize an empty list to store column definitions
    column_definitions = []

    # Iterate over column names and data types
    for column, dtype in column_data_types.items():
        # Define the data type as VARCHAR(100) for all columns
        data_type = 'VARCHAR(250)'
        # Append the formatted column definition to the list
        column_definitions.append(f'[{column}] {data_type}')

    # Join the column definitions into a single string
    table_definition = ', '.join(column_definitions)

    # Generate the CREATE TABLE statement with column definitions
    create_table_query = f'''
    CREATE TABLE {table_name} (
        {table_definition}
    )
    '''

    # Execute the CREATE TABLE statement
    cursor.execute(create_table_query)
    cnxn.commit()
    cnxn.close()

    messagebox.showinfo("Success", "Table created successfully!")

#======================================================================


def Insert():
    conn_str = (
        r'driver={SQL Server};'
        r'server=(local);'
        r'database=ODS;'
        r'trusted_connection=yes;'
    )
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    url = filedialog.askopenfilename()  # Prompt to select the file
    if not url:  # Check if the user cancels file selection
        return
    df = pd.read_excel(url, index_col=None, header=None)
    df.fillna('', inplace=True)

    # Skip the first row
    df = df.iloc[1:]

    # Get table name from entry widget
    table_name = entry_tableName.get()

    # Generate the INSERT INTO query for main table
    insert_query = f'INSERT INTO {table_name} VALUES ({", ".join(["?" for _ in range(len(df.columns))])})'

    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

    # Get the information to insert into PythonFilesLog table
    log_data = [
        (table_name, url, len(df), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    ]

    # Generate the INSERT INTO query for PythonFilesLog table
    log_insert_query = f'INSERT INTO PythonFilesLog (TableName, FileName, CountRows, LoadDate) VALUES (?, ?, ?, ?)'

    # Execute the INSERT INTO query for PythonFilesLog table
    cursor.executemany(log_insert_query, log_data)

    cnxn.commit()
    cnxn.close()
    messagebox.showinfo("Success", "Table Inserted successfully!")
#===============================================================================
# Define function to truncate table
def Truncate():
    # Connect to the SQL Server database
    conn_str = (
        r'driver={SQL Server};'
        r'server=(local);'
        r'database=ODS;'
        r'trusted_connection=yes;'
    )
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()

    # Get table name from entry widget
    table_name = entry_tableName.get()

    # Execute the SQL statement to truncate the table
    truncate_query = f'TRUNCATE TABLE {table_name}'
    cursor.execute(truncate_query)

    # Commit the transaction
    cnxn.commit()

    # Close the cursor and connection
    cursor.close()
    cnxn.close()
    messagebox.showinfo("Success", "Table Truncated successfully!")
#===================================================================================
# Define function to truncate table
def Drop():
    # Connect to the SQL Server database
    conn_str = (
        r'driver={SQL Server};'
        r'server=(local);'
        r'database=ODS;'
        r'trusted_connection=yes;'
    )
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()

    # Get table name from entry widget
    table_name = entry_tableName.get()

    # Execute the SQL statement to truncate the table
    truncate_query = f'Drop TABLE {table_name}'
    cursor.execute(truncate_query)

    # Commit the transaction
    cnxn.commit()

    # Close the cursor and connection
    cursor.close()
    cnxn.close()
    messagebox.showinfo("Success", "Table Droped successfully!")


#===================================================================================
def DeleteRowFromPythonFilesLog():
    # Create a new tkinter window for input
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Row from PythonFilesLog")

    # Label and Entry widget for ID input
    tk.Label(delete_window, text="Enter Row ID:", font=("Arial", 10)).pack()
    entry_id = tk.Entry(delete_window)
    entry_id.pack()

    # Define function to perform deletion
    def delete_row():
        # Get the ID from the entry widget
        row_id = entry_id.get()

        # Connect to the SQL Server database
        conn_str = (
            r'driver={SQL Server};'
            r'server=(local);'
            r'database=ODS;'
            r'trusted_connection=yes;'
        )
        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()

        # Execute the SQL statement to delete the row
        delete_query = f'DELETE FROM PythonFilesLog WHERE ID = ?'
        cursor.execute(delete_query, (row_id,))

        # Commit the transaction
        cnxn.commit()

        # Close the cursor and connection
        cursor.close()
        cnxn.close()
        messagebox.showinfo("Success", "Row deleted successfully!")

        # Close the delete window after deletion
        
        delete_window.destroy()
       
    # Button to confirm deletion
    tk.Button(delete_window, text="Delete", command=delete_row).pack()


#===================================================================================





# Create tkinter window
window = tk.Tk()
window.title("Create & Insert Table INTO SQL Server")

#Frame DROP==================================
Frame1= tk.Frame(window)
Frame1.pack(expand=True, fill= "both" , side="bottom")

#tk.Label(Frame1, text= "Drop Table" , bg="gray" , fg="black").grid(row=0, column=0)
tk.Label(Frame1, text= "▲ Delete the table ▲", fg="dark red", font= ("tahoma" , 9)).pack()
buttonDrop = tk.Button(Frame1, text="DROP TABLE ▲ ", command=Drop,bg="pink" , fg="black" ,font= ("tahoma" , 9))
buttonDrop.pack()

#========================================
# Label and Entry widget for table name
tk.Label(window, text= "Table Name: ", fg="Black", font= ("tahoma" , 10)).pack()
entry_tableName = tk.Entry(window)
entry_tableName.pack()
tk.Label(window, text= "______________________________________", fg="white", font= ("tahoma" , 10)).pack()


# Button to create table
tk.Label(window, text= "Creating table INTO 'ODS' Database ", fg="dark green", font= ("tahoma" , 8)).pack()
button = tk.Button(window, text="Create Table in SQL ▬", command=Create_Table, bg="green")
button.pack()
tk.Label(window, text= "______________________________________", fg="white", font= ("tahoma" , 10)).pack()

# Button to insert data into table
tk.Label(window, text= "Insert the table with path ", fg="gray", font= ("tahoma" , 8)).pack()
tk.Label(window, text= "Insert INFO in [F:\DWH\Phyton] → 'PythonFilesLog' ", fg="gray", font= ("tahoma" , 8)).pack()
button2 = tk.Button(window, text="Insert Value ↑", command=Insert)
button2.pack()
tk.Label(window, text= "______________________________________", fg="white", font= ("tahoma" , 10)).pack()

# Button to truncate table
tk.Label(window, text= "Truncate Table ", fg="gray", font= ("tahoma" , 7)).pack()
button3 = tk.Button(window, text="Truncate Table  X", command=Truncate)
button3.pack()
tk.Label(window, text= "______________________________________", fg="white", font= ("tahoma" , 10)).pack()

#Delete Row
tk.Label(window, text= "▼ Deleting Rows ▼", fg="gray", font= ("tahoma" , 7)).pack()
button_delete = tk.Button(window, text="Delete Row from PythonFilesLog ∟", command=DeleteRowFromPythonFilesLog, bg="light yellow")
button_delete.pack()
tk.Label(window, text= "______________________________________", fg="white", font= ("tahoma" , 10)).pack()



window.geometry("400x400")
# Run the tkinter event loop
window.mainloop()



