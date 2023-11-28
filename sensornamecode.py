import tkinter as tk
from household import Household
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Room Sensor Input")

        self.room_count = 0
        self.total_rooms = 0
        self.rooms = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter your family name:")
        self.label.pack(pady=10)

        self.family_name_entry = tk.Entry(self.master)
        self.family_name_entry.pack()

        self.submit_family_button = tk.Button(self.master, text="Submit", command=self.get_family_name)
        self.submit_family_button.pack(pady=10)

    def get_family_name(self):
        family_name = self.family_name_entry.get()
        if family_name:
            self.household = Household(family_name)
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

    def show_results(self):
        result_text = "Room Information:\n"
        for room in self.rooms:
            result_text += f"{room[0]} - Sensor Type: {room[1]}\n"

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack(pady=10)

      

        for room, rooom in self.household._rooms.items():
            print(room, rooom)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
