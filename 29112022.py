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


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        # Username
        ttk.Label(self, text='Acceder').grid(column=0, row=0, sticky=tk.W)
        self.cajaUsername = ttk.Entry(self, width=30)
        self.cajaUsername.focus()
        self.cajaUsername.grid(column=1, row=0, sticky=tk.W)

        # Password:
        self.cajaPassword = ttk.Label(self, text='Password').grid(column=0, row=1, sticky=tk.W)
        self.cajaPassword = ttk.Entry(self, width=30)
        self.cajaPassword.grid(column=1, row=1, sticky=tk.W)

        boton = ttk.Button(text="Acceder", command=lambda: self.ValidarUsuario(self.cajaUsername.get(), self.cajaPassword.get()))
        boton.grid(row=3,column=1)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)
    def ValidarUsuario(self, username, password):
        print("Conectando a Oracle")
        sql = "SELECT * from usuaruio where username '"+username+' and pass......etc.'
        print("Validando datos username..."+username)
        print("Validando datos password..."+password)
        print("ACA VA LA CONSULTA Y LA VALIDACION DEL USUARIO" + sql)

'''
class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text='Accederd', command=lambda: print("BOTON CLICK")).grid(column=0, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
'''

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('User Login')
        self.geometry('400x150')
        self.resizable(0, 0)
        self.__create_widgets()

    def __create_widgets(self):
        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

        # create the button frame
        #button_frame = ButtonFrame(self)
        #button_frame.grid(column=1, row=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()