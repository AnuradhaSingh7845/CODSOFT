import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring 
from datetime import datetime 

win=tk.Tk()
win.title("TO-DO-List")
win['bg']="#4636fa"
win.geometry("400x300")
equation=""
def delete():
    task_listbox.delete(tk.ANCHOR)
def add(event=None):
    global equation
    # Get the task from the Entry widget
    task = task_entry.get()
    # Add the task to the Listbox
    if task:  # Ensure that the task is not empty
        today_date = datetime.now().strftime("%Y-%m-%d")
        task_listbox.insert(tk.END, f"{task} [Date : {today_date}]")
        task_entry.delete(0, tk.END)
        
def mark_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
         selected_text = task_listbox.get(selected_task_index)
         display_text = f" {selected_text} [Completed]"
         task_listbox.insert(tk.END,display_text)
         task_listbox.delete(tk.ANCHOR)
    else:
        messagebox.showwarning("No Selection", "Please select a task to mark as completed.")

task_entry = tk.Entry(win, width=35,text="Enter Task",font=("arial", 20),bg="#6e75f6",fg="white")
task_entry.place(x=502,y=150)

frame = tk.Frame(win)
frame.pack(pady=10)

#SCROLL BUTTON DESIGNING
style = ttk.Style()
style.theme_use('default')

# Customize the scrollbar
style.configure('TScrollbar', 
                background='lightblue',  # Scrollbar background
                arrowcolor='#4636fa',      # Arrow color
                troughcolor='gray')     # Background of the scrollbar track


task_entry.bind('<Return>', add)
# Define and place a Listbox to display the tasks
task_listbox = tk.Listbox(win, width=50, height=10, font=("arial", 20),bg="#6e75f6",fg="white")
task_listbox.pack(padx=500,pady=200,ipadx=100,ipady=100)


scrollbar = ttk.Scrollbar(task_listbox, orient=tk.VERTICAL, style='TScrollbar')
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.TOP, fill=tk.BOTH)

tk.Button(win,text="ADD Task",width=10,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="#06ea0e",command=lambda:add()).place(x=580,y=550)
tk.Button(win,text="Delete Task",width=10,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="#ee1515",command=delete).place(x=800,y=550)
#l1=tk.Label(win,text="",width=40,height=5,font=("arial",20,"bold"),bg="#6e75f6")
#l1.pack(padx=500,pady=50,ipadx=10,ipady=120)

tk.Button(win,text="Mark Completed",width=15,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="#fe9037",command=mark_completed).place(x=650,y=650)
win.mainloop()
