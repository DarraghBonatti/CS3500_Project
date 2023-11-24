import tkinter as tk
from room import Room
from sensor import Temperature, Sensor
from household import Household




class App:

    ####################################################################################################################################
    #INIT FUNCTION - 
    def __init__(self, root):
        self.root = root
        self.root.title("My House Heating Controller")
        self.rooms = []
        self.entered_values = []

        self.create_fam_name()
    ####################################################################################################################################
    #CREATE INPUT LABEL FOR FAMILY NAME
    def create_fam_name(self):
        # Label
        tk.Label(self.root, text="Enter your family name:").pack(pady=10)

        # Entry Widget
        self.family_name_entry = tk.Entry(self.root)
        self.family_name_entry.pack(pady=10)

        # Submit Button
        tk.Button(self.root, text="Submit", command=self.submit_family_name).pack()

    ####################################################################################################################################
    #CREATE INPUT LABEL FOR NUMBER OF ROOMS
    def create_rooms(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Enter the number of Rooms:").pack(pady=10)

        self.num_rooms = tk.Entry(self.root)
        self.num_rooms.pack(pady=10)
        

        tk.Button(self.root, text="Submit", command=self.make_rooms).pack()
        
    ####################################################################################################################################
    #CREATE SUBMISSION FOR FAMILY NAME
    def submit_family_name(self):
        family_name = self.family_name_entry.get()

        if family_name:
            self.household = Household(family_name)
            self.create_rooms()
        else:
            print("Hello")


    ####################################################################################################################################
    #FOR NUMBER OF ROOMS - TAKE INPUT FOR ROOM NAMES AND ACCEPT SUBMISSION   
    def make_rooms(self):
        self.num_of_rooms = int(self.num_rooms.get())
        if self.num_of_rooms:
            for i in range(self.num_of_rooms):
                tk.Label(self.root, text=f"Enter name of Room:  {i + 1}:").pack(pady=10)
                entry = tk.Entry(self.root)
                entry.pack(pady=10)
                self.rooms.append(entry)

            tk.Button(self.root, text="Submit", command=self.submit_rooms).pack(pady=10)
    ####################################################################################################################################
    #TAKE INPUT AS NAMES AND CREATE ROOM/SENSOR INSTANCES - ADD THESE TO HOUSEHOLD OBJECT
    def submit_rooms(self):
        if len(self.rooms) == self.num_of_rooms :
            self.entered_values = [entry.get() for entry in self.rooms]
            for i in self.entered_values:
                ########## what to add to household.add_rooms, what types for sensor and room???? name or object ? ##############
                room = Room(i)
                sensor = Sensor(i)
                self.household._add_room(room,sensor)

            self.show_room_names()

    ####################################################################################################################################
    #DISPLAY ALL ROOM NAMES - NEEDS UPDATING
    def show_room_names(self):
        # Clear the screen by destroying the widgets related to room entry
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display the submitted room names in a Listbox
        tk.Label(self.root, text="Submitted Room Names:").pack(pady=10)
        room_listbox = tk.Listbox(self.root)
        room_listbox.pack(pady=10)
        for room in self.entered_values:
            room_listbox.insert(tk.END, room)
            

     
        



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


    
    
