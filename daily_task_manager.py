Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
... label = tk.Label(root, text="Daily Task Manager", font=("Arial", 18, "bold"))
... label.pack(pady=10)
...
... # Entry Box
... entry = tk.Entry(root, width=30, font=("Arial", 12))
... entry.pack(pady=10)
...
... # Add Button
... add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
... add_btn.pack(pady=5)
...
... # Task Listbox
... listbox = tk.Listbox(root, width=35, height=10, font=("Arial", 12))
... listbox.pack(pady=15)
...
... # Remove Button
... remove_btn = tk.Button(root, text="Remove Task", width=15, command=remove_task)
... remove_btn.pack(pady=5)
...
... # Clear Button
... clear_btn = tk.Button(root, text="Clear All", width=15, command=clear_all)
... clear_btn.pack(pady=5)
...
... # Exit Button
... exit_btn = tk.Button(root, text="Exit", width=15, command=root.quit)
... exit_btn.pack(pady=20)
...
... # Run the App
... root.mainloop()
...
>>>
