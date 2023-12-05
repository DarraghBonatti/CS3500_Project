import tkinter as tk
from household import Household
from room import Room
from tkinter import messagebox
from tkinter import ttk
import datetime

class App:
    def __init__(self, master):
        '''
        Initializes the App object.

        Parameters:
        - master (tk.Tk): The Tkinter root window.
        '''
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
        '''
        Creates the main widgets for the start of the application application.
        '''
        
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
        '''
        Retrieves and validates the family name entered by the user.

        If the family name is valid, it initializes the Household object and
        prompts the user to enter the number of rooms.

        If the family name is invalid, displays an error message.

        Raises:
        - tk.messagebox.showerror: If the family name is invalid.
        '''
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
        '''
        Creates widgets for entering the number of rooms.
        '''
        self.room_count_entry = tk.Entry(self.master)
        self.room_count_entry.pack()
        self.room_count_entry.configure(highlightbackground="#66AC91")

        self.submit_rooms_button = tk.Button(self.master, text="Submit", command=self.get_room_count)
        self.submit_rooms_button.pack(pady=10)
        self.submit_rooms_button.configure(highlightbackground="#66AC91")

    def get_room_count(self):
        '''
        Retrieves and validates the total number of rooms entered by the user.

        If the number is valid, prompts the user to enter room information.

        If the number is invalid, displays an error message.

        Raises:
        - tk.messagebox.showerror: If the number of rooms is invalid.
        '''
        try:
            self.total_rooms = int(self.room_count_entry.get())
            if self.total_rooms > 0 and self.total_rooms <9 :
                self.label.config(text="Enter Room Information:")
                self.room_count_entry.destroy()
                self.submit_rooms_button.destroy()
                self.create_individual_room_widgets()
            else:
                messagebox.showerror("Error", "Please enter a valid number of rooms between 1-8.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number .")

    def create_individual_room_widgets(self):
        '''
        Creates widgets for entering information about individual rooms.
        '''
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
        '''
        
        Submits the information about an individual room.

        Adds the room to the household and updates the UI accordingly.

        Raises:
        - tk.messagebox.showerror: If the entered room information is invalid.
        '''
        
        room_name = self.room_name_entry.get()
        sensor_type = self.sensor_type_var.get()

        if len(room_name) <=20 and len(room_name) >=1 and sensor_type:
            self.household.add_room(room_name, sensor_type)
            self.roooms.append(self.household.get_room(room_name))
            self.rooms.append((room_name, sensor_type))
            self.room_count += 1

            if self.room_count < self.total_rooms:
                self.room_name_entry.delete(0, tk.END)
                self.sensor_type_var.set("Radiator")
            else:
                
                self.show_results()
                self.household.init_rooms_temp()
        else:
            messagebox.showerror("Error", "Please enter a valid room name between 1-20 characters.")



    def update_counter(self, room, value):
        '''
        Updates the desired temperature of a room based on the provided value.

        Parameters:
        - room (str): The name of the room.
        - value (int): The value to adjust the temperature.

        Raises:
        - tk.messagebox.showerror: If the desired temperature is out of range.
        '''
        roomObj = self.household.get_room(room)

        new_temperature = roomObj.desired_temperature + value

        if roomObj.sensor_type == "Radiator":
            if 15 <= new_temperature <= 30:
                self.counters[room].set(self.counters[room].get() + value)
                roomObj.desired_temperature = new_temperature
            else:
                messagebox.showerror("Error", "Desired Temperature must be between 15-30°C")
        if roomObj.sensor_type == "Boiler":
            if 40 <= new_temperature <= 65:
                self.counters[room].set(self.counters[room].get() + value)
                roomObj.desired_temperature = new_temperature
            else:
                messagebox.showerror("Error", "Desired Temperature must be between 40-65°C")


    def update_counter_for_scheduler(self,room_name,value):
        '''
        Updates the desired temperature for scheduling purposes.

        Parameters:
        - room_name (str): The name of the room.
        - value (int): The value to adjust the temperature.

        Raises:
        - tk.messagebox.showerror: If the desired temperature is out of range.
        '''
        roomObj = self.household.get_room(room_name)
        scheduled_temp = roomObj.desired_temperature + value
        if roomObj.sensor_type == "Radiator":
            if 15 <= scheduled_temp <= 30:
                self.counter_value.set(self.counter_value.get()+value)
            else:
                messagebox.showerror("Error", "Desired Temperature must be between 15-30°C")
        if roomObj.sensor_type == "Boiler":
            if 40 <= scheduled_temp <= 65:
                self.counter_value.set(self.counter_value.get()+value)
            else:
                messagebox.showerror("Error", "Desired Temperature must be between 40-65°C")
                


    def update_temperature_labels(self):
        '''
        Updates the temperature labels for all rooms.
        '''
        
        for room_name in self.rooms:
            current_temp = self.household.get_room(room_name[0])
            temp_to_show = current_temp.room_temperature
            self.temperature_vars[room_name[0]].set(f"Temperature: {temp_to_show}")
            self.master.after(1000, self.update_temperature_labels)

    def updateDesiredTemps(self):
        '''
        Updates the desired temperatures based on scheduling.
        '''
        for room in self.rooms:
            roomObj = self.household.get_room(room[0])
            print(roomObj.schedule_start)
            print(self.household.time_string)
            if roomObj.scheduler_active and roomObj.schedule_start <= self.household.time:
                print("start time is less")
                print(f"desired temp var{roomObj.desired_temperature}")
                print(f"counter variable: {self.counters[room[0]].get()}")
                if roomObj.schedule_desired_temp != self.counters[room[0]].get():
                    print("desired time is less")
                    self.counters[room[0]].set(roomObj.scheduled_desired_temp)


    def delete_room(self):
        '''
        Deletes the currently selected room and its corresponding tab.
        '''
        current_index = self.notebook.index(self.notebook.select())
        if current_index >= 0:
            room_name = self.rooms[current_index][0]
            frame = self.frames[current_index]
            del self.rooms[current_index], frame
            self.household.delete_room(room_name)
            # Remove the selected tab
            self.notebook.forget(current_index)
            rooms_value = self.household.rooms
            for i in rooms_value:
                print(i)

    def updateTimeLabel(self):
        '''
        Updates the label displaying the current time.
        '''
        self.time = self.household.time.strftime('%Y-%m-%d %H:%M:%S')
        self.time_label.config(text=self.time)

    def updateTemp(self):
        '''
        Updates the temperature-related information periodically (every 1 second).
        Keeps UI updated with backend information.
        '''

        self.household.update_rooms_temp()
        self.updateTempsLabels()
        self.updateTimeLabel()
        self.updateRadOutput()
        self.updateDesiredTemps()
        self.master.after(1000, self.updateTemp)
        

    def add_to_tabs(self):
        """
        Adds temperature labels to each tab frame.

        Creates labels for current temperature and appends them to the labels list.
        """
        for frame in self.frames:
            lout = tk.Label(frame, text="Current Temp:")
            lout.pack()
            Label = tk.Label(frame, text="")
            self.labels.append(Label)
            Label.pack()

    def add_to_tabs2(self):
        """
        Adds radiator output labels to each tab frame.

        Creates labels for radiator output and appends them to the labels2 list.
        """
        for frame in self.frames:
            lout = tk.Label(frame, text="Radiator Output:")
            l = tk.Label(frame, text="")
            self.labels2.append(l)
            lout.pack()
            l.pack()

    def updateTempsLabels(self):
        """
        Updates the displayed room temperatures on the UI.

        Retrieves room temperatures and updates corresponding labels.
        """
        for counter , frame in enumerate(self.frames):
            roomToDisplay = self.roooms[counter]
            tempText = roomToDisplay.room_temperature
            updateLabel = self.labels[counter]
            updateLabel.config(text=tempText)

        
    def updateRadOutput(self):
        """
        Updates the displayed radiator outputs on the UI.

        Retrieves radiator settings and updates corresponding labels.
        """
        for counter2,room in enumerate(self.roooms):
            outputToOutput = room.radiator_setting
            updateLabel = self.labels2[counter2]
            updateLabel.config(text=outputToOutput)

    
    def scheduling(self):
        """
        Opens a new window for scheduling based on the selected tab or room.

        Creates a new window with options to schedule desired temperature and time.
        """
        # This function opens a new window for scheduling based on the selected tab or room.
        current_index = self.notebook.index(self.notebook.select())

        if current_index >= 0:
            room_name = self.rooms[current_index][0]
            print(room_name)
            room_obj = self.household.get_room(room_name)

            # Create a new window for scheduling
            schedule_window = tk.Toplevel(self.master)
            schedule_window.title("Schedule Room")

            posvalue = 1
            negvalue = -1

            # Label and variable for temperature selection
            temp_label = tk.Label(schedule_window, text="Select Desired Temp:")
            temp_label.pack()
            self.counter_value = tk.IntVar(value=room_obj.desired_temperature)

            # Plus button
            plus_button = tk.Button(schedule_window, text="+", command=lambda: self.update_counter_for_scheduler(room_name,posvalue))
            plus_button.pack()

            # Label for displaying the selected temperature
            temp_display_label = tk.Label(schedule_window, textvariable=self.counter_value)
            temp_display_label.pack()

            # Minus button
            minus_button = tk.Button(schedule_window, text="-", command=lambda:self.update_counter_for_scheduler(room_name, negvalue))
            minus_button.pack()

            # Label and variable for time selection
            time_label = tk.Label(schedule_window, text="Select Time:")
            time_label.pack()

            selected_time = tk.IntVar()

            tk.Radiobutton(schedule_window, text="30 minutes", variable=selected_time, value=30).pack()
            tk.Radiobutton(schedule_window, text="60 minutes", variable=selected_time, value=60).pack()
            tk.Radiobutton(schedule_window, text="2 hours", variable=selected_time, value=120).pack()

            # Submit button
            submit_button = tk.Button(schedule_window, text="Submit", command=lambda: self.submit_schedule(schedule_window, room_name, selected_time.get()))
            submit_button.pack(pady=10)

    def submit_schedule(self, schedule_window, selected_room, selected_time):
        """
        Submits the scheduled temperature for a room.

        Updates the room's desired temperature and schedules it for the specified time.

        Parameters:
        - schedule_window (tk.Toplevel): The scheduling window.
        - selected_room (str): The name of the room to be scheduled.
        - selected_time (int): The selected time for scheduling.
        """
        if  selected_time:

            room_Obj = self.household.get_room(selected_room)
            tempToSchedule = self.counter_value.get()

            schedule_time = self.household.time + datetime.timedelta(minutes=float(selected_time))
            room_Obj.schedule_desired_temp(tempToSchedule, schedule_time)
           
            messagebox.showinfo("Schedule", f"Room: {selected_room}, Time: {selected_time} minutes scheduled.")
            schedule_window.destroy()
        else:
            messagebox.showerror("Error", "Please select both room, temp and time.")

            
    
    def show_results(self):
        """
        Displays information about the rooms in the UI.

        Creates labels and buttons for each room, allowing temperature adjustments.
        """

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
            
            
            roomObj = self.household.get_room(room[0])
            InitialDisplayTemp = roomObj.desired_temperature
            print("this is the inital temp of room:",InitialDisplayTemp)


            
            # counter_value = tk.IntVar(InitialDisplayTemp)
            
            counter_value = tk.IntVar()
            counter_value.set(InitialDisplayTemp)
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


        self.schedule_button = tk.Button(self.master, text="Schedule", command=self.scheduling)
        self.schedule_button.pack(pady=10)
        self.schedule_button.configure(highlightbackground="#66AC91")
        

        self.time_label = tk.Label(root, text="", font=('Helvetica', 24))
        self.time_label.pack()
        self.time_label.configure(highlightbackground="#66AC91")
       
        self.add_to_tabs()
        self.add_to_tabs2()
        
        self.updateTemp()
        



   

    def add_new_room(self):
        """
        Opens a new window for adding a new room.

        Creates a window with options to input a new room's name and sensor type.
        """
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

        '''
        Submits the information about an individual room.

        Adds the room to the household object and creates labels for room in UI.

        Raises:
        - tk.messagebox.showerror: If the entered room information is invalid.
        '''
        room_name = room_name_entry.get()
        if len(room_name) >20 or len(room_name) <1:
            messagebox.showerror("Please Enter valid room name between 1-20 chars.")


        sensor_type = sensor_type_var.get()

        if room_name and sensor_type:
            new_room_window.destroy()
            
            self.household.add_room(room_name, sensor_type)
            roomObj = self.household.get_room(room_name)
            roomObj.init_room_temp()
            self.rooms.append((room_name, sensor_type))
            self.room_count += 1

            # Create a new tab for the added room
            room_frame = tk.Frame(self.notebook)
            label = tk.Label(room_frame, text=f"Room: {room_name} - Sensor Type: {sensor_type}")
            label.pack(pady=10)

            roomObj = self.household.get_room(room_name)
            InitialDisplayTemp = roomObj.desired_temperature
            
            counter_value = tk.IntVar()
            counter_value.set(InitialDisplayTemp)
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

            roomObj = self.household.get_room(room_name)
            lout = tk.Label(room_frame, text="Current Temp")
            lout.pack()
            Label = tk.Label(room_frame, text="")
            Label.pack()
            lout2 = tk.Label(room_frame, text="Radiator Output:")
            lout2.pack()
            l = tk.Label(room_frame, text="")
            l.pack()


            self.frames.append(room_frame)
            self.labels.append(Label)
            self.labels2.append(l)
            self.roooms.append(roomObj)
            
            


        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() 
