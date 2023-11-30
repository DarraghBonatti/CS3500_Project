
import tkinter as tk
from household import Household
from tkinter import messagebox
from tkinter import ttk, messagebox


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Room Sensor Input")

        self.room_count = 0
        self.total_rooms = 0
        self.rooms = []
        self.counters = {}

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter your family name:")
        self.label.pack(pady=10)

        self.family_name_entry = tk.Entry(self.master)
        self.family_name_entry.pack()

        self.submit_family_button = tk.Button(self.master, text="Submit", command=self.get_family_name)
        self.submit_family_button.pack(pady=10)

    def get_family_name(self):
        self.family_name = self.family_name_entry.get()
        if self.family_name:
            self.household = Household(self.family_name)
            self.label.config(text="Enter the number of rooms:")
            self.family_name_entry.destroy()
            self.submit_family_button.destroy()
            self.create_room_widgets()
        else:
            messagebox.showerror("Error", "Please enter a family name.")

    def create_room_widgets(self):
        self.room_count_entry = tk.Entry(self.master)
        self.room_count_entry.pack()

        self.submit_rooms_button = tk.Button(self.master, text="Submit", command=self.get_room_count)
        self.submit_rooms_button.pack(pady=10)

    def get_room_count(self):
        try:
            self.total_rooms = int(self.room_count_entry.get())
            if self.total_rooms > 0:
                self.label.config(text="Enter Room Information:")
                self.room_count_entry.destroy()
                self.submit_rooms_button.destroy()
                self.create_individual_room_widgets()
            else:
                messagebox.showerror("Error", "Please enter a valid number of rooms.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def create_individual_room_widgets(self):
        self.room_name_label = tk.Label(self.master, text="Room Name:")
        self.room_name_label.pack()

        self.room_name_entry = tk.Entry(self.master)
        self.room_name_entry.pack()

        self.sensor_type_var = tk.StringVar()
        self.sensor_type_var.set("Radiator")

        self.radio_frame = tk.Frame(self.master)
        self.radio_frame.pack()

        self.radiator_radio = tk.Radiobutton(self.radio_frame, text="Radiator", variable=self.sensor_type_var, value="Radiator")
        self.radiator_radio.pack(side=tk.LEFT)

        self.boiler_radio = tk.Radiobutton(self.radio_frame, text="Boiler", variable=self.sensor_type_var, value="Boiler")
        self.boiler_radio.pack(side=tk.LEFT)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_room)
        self.submit_button.pack(pady=10)

        self.finish_button = tk.Button(self.master, text="Finish", command=self.master.quit)
        self.finish_button.pack()

    def submit_room(self):
        room_name = self.room_name_entry.get()
        sensor_type = self.sensor_type_var.get()

        if room_name and sensor_type:
            self.household._add_room(room_name, sensor_type)
            self.rooms.append((room_name, sensor_type))
            self.room_count += 1

            if self.room_count < self.total_rooms:
                self.room_name_entry.delete(0, tk.END)
                self.sensor_type_var.set("Radiator")
            else:
                self.show_results()

    def update_counter(self, room, value):
        self.counters[room].set(self.counters[room].get() + value)

    def show_results(self):

        widgets = root.winfo_children()

        # Destroy each widget
        for widget in widgets:
            widget.destroy()

        familyNameText = f'The {self.family_name} Heating Controller'
        FamilyName_label = tk.Label(self.master, text=familyNameText)
        FamilyName_label.pack(pady=10)

        result_text = "Room Information:\n"
        for room in self.rooms:
            result_text += f"{room[0]} - Sensor Type: {room[1]}\n"
           

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack(pady=10)

        self.notebook = ttk.Notebook(self.master)
        for room in self.rooms:
            room_frame = tk.Frame(self.notebook)
            label = tk.Label(room_frame, text=f"Room: {room[0]} - Sensor Type: {room[1]}")
            label.pack(pady=10)
            label1 = tk.Label(room_frame, text=f"Please Enter Desired Temperature")
            label1.pack(pady=10)

            counter_value = tk.IntVar(value=0)
            self.counters[room[0]] = counter_value
            ###### no initalised current value for rooms
            # current_temp = self.household._get_room(room[0])
            # temp_to_show = current_temp.room_temperature
            temptext = "Current Temperature is 18 degrees Celsius"

            currentTemp_label = tk.Label(room_frame, textvariable=temptext)
            currentTemp_label.pack(side=tk.LEFT, padx=5)


            # Plus button
            plus_button = tk.Button(room_frame, text="+", command=lambda room=room[0]: self.update_counter(room, 1))
            plus_button.pack(side=tk.LEFT, padx=5)

            # Counter label
            counter_label = tk.Label(room_frame, textvariable=counter_value)
            counter_label.pack(side=tk.LEFT, padx=5)

            # Minus button
            minus_button = tk.Button(room_frame, text="-", command=lambda room=room[0]: self.update_counter(room, -1))
            minus_button.pack(side=tk.LEFT, padx=5)

            self.notebook.add(room_frame, text=f"{room[0]}")

            #self.notebook.pack()
            #self.notebook.add(room_frame, text=f"{room[0]}")

        self.notebook.pack(pady=10)

         # ... existing code ...

    # + button to add a new room
        add_button = tk.Button(self.master, text="+ Add Room", command=self.add_new_room)
         
        add_button.pack(pady=10)



   

    def add_new_room(self):
        new_room_window = tk.Toplevel(self.master)
        new_room_window.title("Add New Room")

        room_name_label = tk.Label(new_room_window, text="Room Name:")
        room_name_label.pack()

        room_name_entry = tk.Entry(new_room_window)
        room_name_entry.pack()

        sensor_type_var = tk.StringVar()
        sensor_type_var.set("Radiator")

        radio_frame = tk.Frame(new_room_window)
        radio_frame.pack()

        radiator_radio = tk.Radiobutton(radio_frame, text="Radiator", variable=sensor_type_var, value="Radiator")
        radiator_radio.pack(side=tk.LEFT)

        boiler_radio = tk.Radiobutton(radio_frame, text="Boiler", variable=sensor_type_var, value="Boiler")
        boiler_radio.pack(side=tk.LEFT)

        submit_button = tk.Button(new_room_window, text="Submit", command=lambda: self.submit_new_room(new_room_window, room_name_entry, sensor_type_var))
        submit_button.pack(pady=10)

    def submit_new_room(self, new_room_window, room_name_entry, sensor_type_var):
        room_name = room_name_entry.get()
        sensor_type = sensor_type_var.get()

        if room_name and sensor_type:
            new_room_window.destroy()
            self.household._add_room(room_name, sensor_type)
            self.rooms.append((room_name, sensor_type))
            self.room_count += 1

            # Create a new tab for the added room
            room_frame = tk.Frame(self.notebook)
            label = tk.Label(room_frame, text=f"Room: {room_name} - Sensor Type: {sensor_type}")
            label.pack(pady=10)
            counter_value = tk.IntVar(value=0)
            self.counters[room_name] = counter_value

            # Plus button
            plus_button = tk.Button(room_frame, text="+", command=lambda room=room_name: self.update_counter(room, 1))
            plus_button.pack(side=tk.LEFT, padx=5)

            # Counter label
            counter_label = tk.Label(room_frame, textvariable=counter_value)
            counter_label.pack(side=tk.LEFT, padx=5)

            # Minus button
            minus_button = tk.Button(room_frame, text="-", command=lambda room=room_name: self.update_counter(room, -1))
            minus_button.pack(side=tk.LEFT, padx=5)

            self.notebook.add(room_frame, text=f"{room_name}")
            self.notebook.pack(pady=10)


        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
   