# import tkinter as tk
# from tkinter import messagebox
# import random
# from rx import interval
# from rx.operators import map
#
#
# class TemperatureMonitor:
#     def __init__(self, master):
#         self.master = master
#         master.title("Temperature Monitor")
#
#         self.temperature_label = tk.Label(master, text="Current Temperature: ")
#         self.temperature_label.pack()
#
#         self.temperature_value_label = tk.Label(master, text="")
#         self.temperature_value_label.pack()
#
#         self.start_button = tk.Button(master, text="Start", command=self.start_monitoring)
#         self.start_button.pack()
#
#         self.stop_button = tk.Button(master, text="Stop", command=self.stop_monitoring)
#         self.stop_button.pack()
#         self.stop_button.config(state="disabled")
#
#         self.monitoring = False
#         self.temperature_subscription = None
#
#     def start_monitoring(self):
#         self.monitoring = True
#         self.start_button.config(state="disabled")
#         self.stop_button.config(state="normal")
#
#         # Create temperature data stream
#         temperature_stream = interval(3).pipe(map(lambda _: self.read_temperature()))
#
#         # Subscribe to the stream and perform temperature check
#         self.temperature_subscription = temperature_stream.subscribe(lambda temp: self.check_temperature(temp))
#
#     def stop_monitoring(self):
#         self.monitoring = False
#         self.start_button.config(state="normal")
#         self.stop_button.config(state="disabled")
#
#         # Check if there's a subscription before trying to dispose it
#         if self.temperature_subscription:
#             self.temperature_subscription.dispose()  # Unsubscribe from the data stream
#
#     def read_temperature(self):
#         # Simulate temperature reading
#         return random.randint(0, 100)
#
#     def check_temperature(self, temp):
#         self.temperature_value_label.config(text=str(temp) + "°C")
#
#         # Check critical values
#         if temp >= 80:
#             messagebox.showwarning("Warning", "High temperature detected!")
#         elif temp <= 10:
#             messagebox.showwarning("Warning", "Low temperature detected!")
#
#
# root = tk.Tk()
# app = TemperatureMonitor(root)
# root.mainloop()
