import tkinter as tk
from tkinter import messagebox
import requests


class PyCarRentApp:
    def __init__(self, master):
        self.master = master
        master.title("PyCarRent GUI")

        self.label = tk.Label(master, text="Welcome to PyCarRent")
        self.label.pack()

        self.register_button = tk.Button(
            master, text="Register User", command=self.register_user)
        self.register_button.pack()

        self.login_button = tk.Button(
            master, text="Login User", command=self.login_user)
        self.login_button.pack()

        self.add_vehicle_button = tk.Button(
            master, text="Add Vehicle", command=self.add_vehicle)
        self.add_vehicle_button.pack()

        self.list_vehicles_button = tk.Button(
            master, text="List Vehicles", command=self.list_vehicles)
        self.list_vehicles_button.pack()

        self.book_rental_button = tk.Button(
            master, text="Book Rental", command=self.book_rental)
        self.book_rental_button.pack()

        self.update_profile_button = tk.Button(
            master, text="Update Profile", command=self.update_profile)
        self.update_profile_button.pack()

    def register_user(self):
        self.register_window = tk.Toplevel(self.master)
        self.register_window.title("Register User")

        self.username_label = tk.Label(self.register_window, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.register_window)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.register_window, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.register_window, show="*")
        self.password_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.register_window, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(self.register_window)
        self.email_entry.grid(row=2, column=1)

        self.register_button = tk.Button(
            self.register_window, text="Register", command=self.register_user_backend)
        self.register_button.grid(row=3, columnspan=2)

    def register_user_backend(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        payload = {
            "username": username,
            "password": password,
            "email": email
        }

        try:
            response = requests.post(
                "http://127.0.0.1:5000/register", json=payload)
            print(response)
            if response.status_code == 201:
                messagebox.showinfo("Success", "User registered successfully")
            else:
                messagebox.showerror("Error", "Failed to register user")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def login_user(self):
        self.login_window = tk.Toplevel(self.master)
        self.login_window.title("Login User")

        self.username_label = tk.Label(self.login_window, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(
            self.login_window, text="Login", command=self.login_user_backend)
        self.login_button.grid(row=2, columnspan=2)

    def login_user_backend(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(
                "http://127.0.0.1:5000/login", json=payload)
            if response.status_code == 200:
                user_data = response.json()["user"]
                messagebox.showinfo(
                    "Success", f"Login successful\nUser: {user_data['username']}\nEmail: {user_data['email']}")
            else:
                messagebox.showerror(
                    "Error", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_vehicle(self):
        self.add_vehicle_window = tk.Toplevel(self.master)
        self.add_vehicle_window.title("Add Vehicle")

        self.make_label = tk.Label(self.add_vehicle_window, text="Make:")
        self.make_label.grid(row=0, column=0)
        self.make_entry = tk.Entry(self.add_vehicle_window)
        self.make_entry.grid(row=0, column=1)

        self.model_label = tk.Label(self.add_vehicle_window, text="Model:")
        self.model_label.grid(row=1, column=0)
        self.model_entry = tk.Entry(self.add_vehicle_window)
        self.model_entry.grid(row=1, column=1)

        self.year_label = tk.Label(self.add_vehicle_window, text="Year:")
        self.year_label.grid(row=2, column=0)
        self.year_entry = tk.Entry(self.add_vehicle_window)
        self.year_entry.grid(row=2, column=1)

        self.registration_label = tk.Label(
            self.add_vehicle_window, text="Registration Number:")
        self.registration_label.grid(row=3, column=0)
        self.registration_entry = tk.Entry(self.add_vehicle_window)
        self.registration_entry.grid(row=3, column=1)

        self.daily_rate_label = tk.Label(
            self.add_vehicle_window, text="Daily Rate:")
        self.daily_rate_label.grid(row=4, column=0)
        self.daily_rate_entry = tk.Entry(self.add_vehicle_window)
        self.daily_rate_entry.grid(row=4, column=1)

        self.add_button = tk.Button(
            self.add_vehicle_window, text="Add", command=self.add_vehicle_backend)
        self.add_button.grid(row=5, columnspan=2)

    def add_vehicle_backend(self):
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()
        registration_number = self.registration_entry.get()
        daily_rate = self.daily_rate_entry.get()

        payload = {
            "make": make,
            "model": model,
            "year": year,
            "registration_number": registration_number,
            "daily_rate": daily_rate
        }

        try:
            response = requests.post(
                "http://127.0.0.1:5000/vehicles", json=payload)
            if response.status_code == 201:
                messagebox.showinfo(
                    "Success", "Vehicle added successfully")
                self.add_vehicle_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to add vehicle")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_vehicles(self):
        try:
            response = requests.get("http://127.0.0.1:5000/vehicles")
            if response.status_code == 200:
                vehicles = response.json()
                self.display_vehicles(vehicles)
            else:
                messagebox.showerror("Error", "Failed to fetch vehicles data")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_vehicles(self, vehicles):
        vehicles_window = tk.Toplevel(self.master)
        vehicles_window.title("List of Vehicles")

        tk.Label(vehicles_window, text="Make").grid(row=0, column=0)
        tk.Label(vehicles_window, text="Model").grid(row=0, column=1)
        tk.Label(vehicles_window, text="Year").grid(row=0, column=2)
        tk.Label(vehicles_window, text="Registration Number").grid(
            row=0, column=3)
        tk.Label(vehicles_window, text="Daily Rate").grid(row=0, column=4)

        for i, vehicle in enumerate(vehicles):
            tk.Label(vehicles_window, text=vehicle["make"]).grid(
                row=i+1, column=0)
            tk.Label(vehicles_window, text=vehicle["model"]).grid(
                row=i+1, column=1)
            tk.Label(vehicles_window, text=vehicle["year"]).grid(
                row=i+1, column=2)
            tk.Label(vehicles_window, text=vehicle["registration_number"]).grid(
                row=i+1, column=3)
            tk.Label(vehicles_window, text=vehicle["daily_rate"]).grid(
                row=i+1, column=4)

    def book_rental(self):
        try:
            response = requests.get("http://127.0.0.1:5000/vehicles")
            if response.status_code == 200:
                vehicles = response.json()
                self.display_vehicles_for_rent(vehicles)
            else:
                messagebox.showerror("Error", "Failed to fetch vehicles data")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_vehicles_for_rent(self, vehicles):
        self.book_rental_window = tk.Toplevel(self.master)
        self.book_rental_window.title("Book Rental")

        self.vehicle_id_label = tk.Label(
            self.book_rental_window, text="Select Vehicle:")
        self.vehicle_id_label.grid(row=0, column=0)

        # Creating a listbox to display the vehicles
        self.vehicle_listbox = tk.Listbox(
            self.book_rental_window, selectmode=tk.SINGLE)
        self.vehicle_listbox.grid(row=0, column=1)

        # Populating the listbox with vehicles
        for vehicle in vehicles:
            self.vehicle_listbox.insert(
                tk.END, f"{vehicle['make']} {vehicle['model']} ({vehicle['registration_number']})")

        # Labels and entry fields for other inputs
        self.start_date_label = tk.Label(
            self.book_rental_window, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.grid(row=1, column=0)
        self.start_date_entry = tk.Entry(self.book_rental_window)
        self.start_date_entry.grid(row=1, column=1)

        self.end_date_label = tk.Label(
            self.book_rental_window, text="End Date (YYYY-MM-DD):")
        self.end_date_label.grid(row=2, column=0)
        self.end_date_entry = tk.Entry(self.book_rental_window)
        self.end_date_entry.grid(row=2, column=1)

        self.total_cost_label = tk.Label(
            self.book_rental_window, text="Total Cost:")
        self.total_cost_label.grid(row=3, column=0)
        self.total_cost_entry = tk.Entry(self.book_rental_window)
        self.total_cost_entry.grid(row=3, column=1)

        self.book_button = tk.Button(
            self.book_rental_window, text="Book Rental", command=self.book_rental_backend)
        self.book_button.grid(row=4, columnspan=2)

    def book_rental_backend(self):
        selected_vehicle_id = self.vehicle_listbox.curselection()
        if not selected_vehicle_id:
            messagebox.showerror("Error", "Please select a vehicle")
            return

        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        total_cost = self.total_cost_entry.get()
        payload = {
            "user_id": 1,
            "vehicle_id": selected_vehicle_id[0]+1,
            "start_date": start_date,
            "end_date": end_date,
            "total_cost": total_cost
        }

        try:
            response = requests.post(
                "http://127.0.0.1:5000/rentals/book", json=payload)
            if response.status_code == 201:
                messagebox.showinfo(
                    "Success", "Rental booked successfully")
                self.book_rental_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to book rental")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_profile(self):
        self.update_profile_window = tk.Toplevel(self.master)
        self.update_profile_window.title("Update Profile")

        self.user_id_label = tk.Label(
            self.update_profile_window, text="User ID:")
        self.user_id_label.grid(row=0, column=0)
        self.user_id_entry = tk.Entry(self.update_profile_window)
        self.user_id_entry.grid(row=0, column=1)

        self.username_label = tk.Label(
            self.update_profile_window, text="New Username:")
        self.username_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(self.update_profile_window)
        self.username_entry.grid(row=1, column=1)

        self.password_label = tk.Label(
            self.update_profile_window, text="New Password:")
        self.password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(self.update_profile_window, show="*")
        self.password_entry.grid(row=2, column=1)

        self.email_label = tk.Label(
            self.update_profile_window, text="New Email:")
        self.email_label.grid(row=3, column=0)
        self.email_entry = tk.Entry(self.update_profile_window)
        self.email_entry.grid(row=3, column=1)

        self.update_button = tk.Button(
            self.update_profile_window, text="Update", command=self.update_profile_backend)
        self.update_button.grid(row=4, columnspan=2)

    def update_profile_backend(self):
        user_id = self.user_id_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        payload = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "email": email
        }

        try:
            response = requests.put(
                "http://127.0.0.1:5000/users/profile", json=payload)
            if response.status_code == 200:
                messagebox.showinfo(
                    "Success", "Profile updated successfully")
                self.update_profile_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to update profile")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PyCarRentApp(root)
    root.mainloop()
