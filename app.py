import tkinter as tk
from household import Household
from room import Room
from tkinter import messagebox
from tkinter import ttk
import datetime


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Room Sensor Input")
        self.master.configure(bg="#66AC91")

        self.room_count = 0
        self.total_rooms = 0
        self.rooms = []
        self.counters = {}
        self.temperature_vars = {}
        self.counter = 0
        self.tempCounter = 0
        self.desiredtempCounter = 0
        self.labels = {}
        self.frames = []
        self.time = 0
        self.roooms = []
        self.labels = []
        self.labels2 = []
        self.counter_value = 0
        

        
        self.create_widgets()

    def create_widgets(self):
        
        self.label = tk.Label(self.master, text="Enter your family name:")
        self.label.pack(pady=10)
        self.label.configure(highlightbackground="#66AC91")

        self.family_name_entry = tk.Entry(self.master)
        self.family_name_entry.pack()
        self.family_name_entry.configure(highlightbackground="#66AC91")

        self.submit_family_button = tk.Button(self.master, text="Submit", command=self.get_family_name)
        self.submit_family_button.pack(pady=10)
        self.submit_family_button.configure(highlightbackground="#66AC91")
        
    def get_family_name(self):
        self.family_name = self.family_name_entry.get()
        if self.family_name and isinstance(self.family_name, str) and 1 <= len(self.family_name) <= 20:
            self.household = Household(self.family_name)
            self.household.time = datetime.datetime.now()
            self.label.config(text="Enter the number of rooms:")
            self.family_name_entry.destroy()
            self.submit_family_button.destroy()
            self.create_room_widgets()
        else:
            messagebox.showerror("Error", "Please enter a valid family name. It should be a string between 1 and 20 characters.")

    def create_room_widgets(self):
        self.room_count_entry = tk.Entry(self.master)
        self.room_count_entry.pack()
        self.room_count_entry.configure(highlightbackground="#66AC91")

        self.submit_rooms_button = tk.Button(self.master, text="Submit", command=self.get_room_count)
        self.submit_rooms_button.pack(pady=10)
        self.submit_rooms_button.configure(highlightbackground="#66AC91")

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
        self.room_name_label.configure(highlightbackground="#66AC91")

        self.room_name_entry = tk.Entry(self.master)
        self.room_name_entry.pack()
        self.room_name_entry.configure(highlightbackground="#66AC91")

        self.sensor_type_var = tk.StringVar()
        self.sensor_type_var.set("Radiator")

        self.radio_frame = tk.Frame(self.master)
        self.radio_frame.pack()
        self.radio_frame.configure(highlightbackground="#66AC91")

        self.radiator_radio = tk.Radiobutton(self.radio_frame, text="Radiator", variable=self.sensor_type_var, value="Radiator")
        self.radiator_radio.pack(side=tk.LEFT)
        self.radiator_radio.configure(highlightbackground="#66AC91")

        self.boiler_radio = tk.Radiobutton(self.radio_frame, text="Boiler", variable=self.sensor_type_var, value="Boiler")
        self.boiler_radio.pack(side=tk.LEFT)
        self.boiler_radio.configure(highlightbackground="#66AC91")

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_room)
        self.submit_button.pack(pady=10)
        self.submit_button.configure(highlightbackground="#66AC91")

        self.finish_button = tk.Button(self.master, text="Finish", command=self.master.quit)
        self.finish_button.pack()
        self.finish_button.configure(highlightbackground="#66AC91")

    def submit_room(self):
        room_name = self.room_name_entry.get()
        sensor_type = self.sensor_type_var.get()

        if room_name and sensor_type:
            self.household.add_room(room_name, sensor_type)
            self.roooms.append(self.household.get_room(room_name))
            self.rooms.append((room_name, sensor_type))
            self.room_count += 1

            if self.room_count < self.total_rooms:
                self.room_name_entry.delete(0, tk.END)
                self.sensor_type_var.set("Radiator")
            else:
                
                self.show_results()

    def update_counter(self, room, value):
        self.counters[room].set(self.counters[room].get() + value)
        # self.desiredtempCounter += value
        # self.desiredtempCounter = float(self.desiredtempCounter)
        if room in self.household.rooms:
            self.household.rooms[room].desired_temperature += 1
        print(self.household.rooms[room].desired_temperature)


    def update_temperature_labels(self):
        for room_name in self.rooms:
            current_temp = self.household.get_room(room_name[0])
            temp_to_show = current_temp.room_temperature
            #print("temperature vars")
            self.temperature_vars[room_name[0]].set(f"Temperature: {temp_to_show}")
            #print("after method")
            self.master.after(8000, self.update_temperature_labels)


    def update_counter_for_schedule(self,value,room):
            self.counter_value.set(self.counter_value.get() + value)
            # if room in self.household.rooms:
            #     self.household.rooms[room].desired_temperature += value
           
         

  
    # def update_temperature_labels(self):
    #     for room_name in self.rooms:
    #         current_temp = self.household.get_room(room_name[0])
    #         temp_to_show = current_temp.room_temperature
    #         #print("temperature vars")
    #         self.temperature_vars[room_name[0]].set(f"Temperature: {temp_to_show}")
    #         #print("after method")
    #         self.master.after(8000, self.update_temperature_labels)


    def delete_room(self):
        current_index = self.notebook.index(self.notebook.select())
        if current_index >= 0:
            room_name = self.rooms[current_index][0]
            del self.rooms[current_index]
            self.household.delete_room(room_name)  # You need to implement _remove_room method in your Household class if not already done

            # Remove the selected tab
            self.notebook.forget(current_index)
            rooms_value = self.household._rooms
            for i in rooms_value:
                print(i)

    # def update_time(self):
    #     if self.counter < len(self.household.temps):
    #        # print(self.counter)
       
    #         #current_time = self.household.time  # Get time from household object
    #         self.current_time  = self.household.temps[self.counter][0]
    #         print(self.current_time)
    #         self.time_label.config(text=self.current_time)
    #         self.counter+=self.room_count
            
    #         self.master.after(1000, self.update_time)  # Update time every 1000 ms (1 second)
    def updateTimeLabel(self):
        self.time = self.household.time
        self.time_label.config(text=self.time)

    def updateTemp(self):

        self.household.update_rooms_temp()
        self.updateTempsLabels()
        self.updateTimeLabel()
        self.updateRadOutput()
        self.master.after(5000, self.updateTemp)

    def add_to_tabs(self):
        for frame in self.frames:
            Label = tk.Label(frame, text="")
            self.labels.append(Label)
            Label.pack()

    def add_to_tabs2(self):
        for frame in self.frames:
            l = tk.Label(frame, text="")
            self.labels2.append(l)
            l.pack()

    def updateTempsLabels(self):
        for counter , frame in enumerate(self.frames):
            roomToDisplay = self.roooms[counter]
            tempText = roomToDisplay.room_temperature
            #print(self.labels[counter])
            print(counter)
            updateLabel = self.labels[counter]
            updateLabel.config(text=tempText)

        
    def updateRadOutput(self):
        for counter2,room in enumerate(self.roooms):
            outputToOutput = room.radiator_setting
            print(counter2)
            print(self.labels2)
            updateLabel = self.labels2[counter2]
            updateLabel.config(text=outputToOutput)

    def schedule_room(self):
        schedule_window = tk.Toplevel(self.master)
        schedule_window.title("Schedule Room")

        # Label and variable for room selection
        room_label = tk.Label(schedule_window, text="Select Room:")
        room_label.pack(pady=10)

 

        selected_room = tk.StringVar()
        for room in self.rooms:
            tk.Radiobutton(schedule_window, text=room[0], variable=selected_room, value=room[0]).pack()


        self.counter_value = tk.IntVar(value=25)
         # Plus button
        plus_button = tk.Button(schedule_window, text="+", command=lambda room=room[0]: self.update_counter_for_schedule(1,room))
        plus_button.pack(pady=5)
        
        # Label and variable for time selection
        temperature_label = tk.Label(schedule_window, textvariable=self.counter_value)
        temperature_label.pack(pady=10)

        # Minus button
        minus_button = tk.Button(schedule_window, text="-", command=lambda room=room[0]: self.update_counter_for_schedule(-1,room))
        minus_button.pack(pady=5)



        time_label = tk.Label(schedule_window, text="Select Time:")
        time_label.pack()

        selected_time = tk.IntVar()

        tk.Radiobutton(schedule_window, text="30 minutes", variable=selected_time, value=30).pack()
        tk.Radiobutton(schedule_window, text="60 minutes", variable=selected_time, value=60).pack()
        tk.Radiobutton(schedule_window, text="2 hours", variable=selected_time, value=120).pack()

        # Submit button
        submit_button = tk.Button(schedule_window, text="Submit", command=lambda: self.submit_schedule(schedule_window, selected_room.get(), selected_time.get()))
        submit_button.pack(pady=10)

    def submit_schedule(self, schedule_window, selected_room, selected_time):
        if selected_room and selected_time:
            room_Obj = self.household.get_room(selected_room)
            tempToSchedule = self.counter_value.get()

            schedule_time = datetime.datetime.now() + datetime.timedelta(minutes=float(selected_time))

            room_Obj.schedule_desired_temp(tempToSchedule, schedule_time)
            print(f"Now: {datetime.datetime.now().strftime('%Y-%m-%d %H: %M: %S')}")
            print(f"Scheduled Time: {schedule_time.strftime('%Y-%m-%d %H: %M: %S')}\n Temp: {tempToSchedule}")
            
            # Store the selected values (you can modify this part based on your requirements)
            print(f"Room: {selected_room}, Time: {selected_time} minutes")
            messagebox.showinfo("Schedule", f"Room: {selected_room}, Time: {selected_time} minutes scheduled.")
            schedule_window.destroy()
        else:
            messagebox.showerror("Error", "Please select both room and time.")

            
    
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
            self.frames.append(room_frame)
            label = tk.Label(room_frame, text=f"Room: {room[0]} - Sensor Type: {room[1]}")
            label.pack(pady=10)
            
            # temp_label = tk.Label(room_frame, text="" ,font=('Helvetica', 24))
            # temp_label.pack(pady=10)
            
           
            
            counter_value = tk.IntVar(value=25)
            self.counters[room[0]] = counter_value

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

        self.notebook.pack(pady=10)

        

         

    # + button to add a new room
        add_button = tk.Button(self.master, text="+ Add Room", command=self.add_new_room)
        add_button.pack(pady=10)
        add_button.configure(highlightbackground="#66AC91")
        delete_button = tk.Button(self.master, text="- Delete Room", command=self.delete_room)
        delete_button.pack(pady=10)
        delete_button.configure(highlightbackground="#66AC91")
        self.schedule_button = tk.Button(self.master, text="Schedule", command=self.schedule_room)
        self.schedule_button.pack(pady=10)
        self.schedule_button.configure(highlightbackground="#66AC91")

        self.time_label = tk.Label(root, text="", font=('Helvetica', 24))
        self.time_label.pack()
        self.time_label.configure(highlightbackground="#66AC91")
        # self.update_time()  # Initial call to update time
        self.add_to_tabs()
        self.add_to_tabs2()
        # self.updateTemp()
        self.updateTemp()
        



   

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
            self.household.add_room(room_name, sensor_type)
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
            plus_button.pack(pady=5)

            # Counter label
            counter_label = tk.Label(room_frame, textvariable=counter_value)
            counter_label.pack(pady=5)

            # Minus button
            minus_button = tk.Button(room_frame, text="-", command=lambda room=room_name: self.update_counter(room, -1))
            #minus_button.pack(side=tk.LEFT, padx=5)
            minus_button.pack(pady=5)
            

            self.notebook.add(room_frame, text=f"{room_name}")
            self.notebook.pack(pady=10)

            roomObj = self.household.get_room(room_name)
            Label = tk.Label(room_frame, text="")
            l = tk.Label(room_frame, text="")
            self.frames.append(room_frame)
            self.labels.append(Label)
            self.labels2.append(l)
            self.roooms.append(roomObj)
            self.updateTempsLabels()
            self.updateRadOutput()


        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() 
