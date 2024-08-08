import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.title}: {self.description}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Title")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # Description
        self.desc_label = tk.Label(self.root, text="Description")
        self.desc_label.grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.root, width=50)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add Button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, height=15, width=80)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)

        # Update Button
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # Delete Button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title and description:
            self.tasks.append(Task(title, description))
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.view_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter both title and description.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            title = self.title_entry.get()
            description = self.desc_entry.get()
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            self.view_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.view_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def on_task_select(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, task.title)
            self.desc_entry.delete(0, tk.END)
            self.desc_entry.insert(0, task.description)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
