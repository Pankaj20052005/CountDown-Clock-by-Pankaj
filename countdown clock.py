import tkinter as tk
from datetime import timedelta

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pankaj's Countdown Watch")

        self.time_remaining = tk.StringVar()
        self.duration = timedelta(minutes=5) 
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(self.root, textvariable=self.time_remaining, font=("Helvetica", 36), bg="#B98EA7").pack(pady=20, fill="both", expand=True)

       
        tk.Button(self.root, text="Start", command=self.start_countdown, bg="#4caf50", fg="white").pack(side="left", padx=10)
        tk.Button(self.root, text="Pause", command=self.pause_countdown, bg="#f44336", fg="white").pack(side="left", padx=10)
        tk.Button(self.root, text="Reset", command=self.reset_countdown, bg="#2196f3", fg="white").pack(side="right", padx=10)

        
        self.time_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.time_entry.pack(side="right", padx=10)
        self.time_entry.insert(0, "5:00") 

        tk.Button(self.root, text="Adjust Time", command=self.adjust_time, bg="#fb9f15", fg="white").pack(side="right", padx=10)

        tk.Label(self.root, text="Pankaj's Countdown Watch", font=("Helvetica", 16, "bold"), bg="#B98EA7").pack(pady=10)

    def update_countdown(self):
        if not self.paused and self.duration.total_seconds() > 0:
            self.duration -= timedelta(seconds=1)
            self.time_remaining.set(str(self.duration).split(".")[0])
            self.root.after(1000, self.update_countdown)
        elif self.duration.total_seconds() == 0:
            tk.messagebox.showinfo("Countdown Complete", "Time's up!")

    def start_countdown(self):
        if not self.paused:
            self.reset_countdown()
        self.paused = False
        self.update_countdown()

    def pause_countdown(self):
        self.paused = True

    def reset_countdown(self):
        self.duration = timedelta(minutes=5)  # Reset to the initial duration
        self.time_remaining.set(str(self.duration).split(".")[0])
        self.paused = True

    def adjust_time(self):
        try:
            time_str = self.time_entry.get()
            minutes, seconds = map(int, time_str.split(":"))
            self.duration = timedelta(minutes=minutes, seconds=seconds)
            self.time_remaining.set(str(self.duration).split(".")[0])
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Please enter time in the format MM:SS")

def main():
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

