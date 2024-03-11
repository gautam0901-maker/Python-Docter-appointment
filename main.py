import os
import customtkinter as ctk
import tkinter as tk
import subprocess
# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System") 
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")    
 
appWidth, appHeight = 200, 300 
# App Class



def run_another_file():
    # Replace 'file_to_run.py' with the name of the Python file you want to run
    subprocess.run(['python', 'appointment.py'])
def delete():
    # Replace 'file_to_run.py' with the name of the Python file you want to run
    subprocess.run(['python', 'delete.py'])
def display():
    # Replace 'file_to_run.py' with the name of the Python file you want to run
    subprocess.run(['python', 'display.py'])
def update():
    # Replace 'file_to_run.py' with the name of the Python file you want to run
    subprocess.run(['python', 'update.py'])
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.title("Doc Appointment")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(False,False)
 
        # Name Label

 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Create Appointment",command = run_another_file)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.generateResultsButton1 = ctk.CTkButton(self,
                                         text="View Appointment",command = display)
        self.generateResultsButton1.grid(row=6, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.generateResultsButton2 = ctk.CTkButton(self,command = update ,text="Update Appointment")
        self.generateResultsButton2.grid(row=7, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.generateResultsButton3 = ctk.CTkButton(self,
                                         text="Delete Appointment",command = delete)
        self.generateResultsButton3.grid(row=8, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
 

 
if __name__ == "__main__":
    app = App()
    app.mainloop()