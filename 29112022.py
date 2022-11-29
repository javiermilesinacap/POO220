'''
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('adb.sa-santiago-1.oraclecloud.com', '1522', service_name='g9cd7530b8a8613_db20220530152721_high.adb.oraclecloud.com') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'admin', password=r'CLAVEORACLE', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('select * from productos') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()
'''
import tkinter as tk
from tkinter import ttk
class Sistema():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("800x600")
    def login(self):
        self.estilo = ttk.Style
        self.etiqueta = tk.Label(text="hola")
        self.etiqueta.grid(row=0,column=0)
class Menu(tk.Frame):
    def __init__(self):
        super().__init__()
        self.ventana = tk.Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Menu del Sistema")
class Usuario: 
    def addUser(self):
        sql = "INSERT INTO ..-..."
        #conexion.execute(sql)
main = Sistema()
main.login()
if(True):
    menu = Menu()
main.ventana.mainloop()

# Create Tkinter Object
root = tk.Tk()

# Set Geometry
root.geometry("400x400")

# Frame 1
frame1 = tk.Frame(root,bg="black",width=500,height=300)
frame1.pack()

# Frame 2
frame2 = tk.Frame(frame1,bg="red",width=100,height=100)
frame2.pack(pady=20,padx=20)

# Execute Tkinter
root.mainloop()