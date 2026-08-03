from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(5)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):



    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1, pady=(5, 15))

start_button = Button(text="Start", font=(FONT_NAME, 16), command=start_timer)
start_button.grid(column=0, row=2)

pause_button = Button(text="Pause", font=(FONT_NAME, 16))
pause_button.grid(column=1, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 16))
reset_button.grid(column=2, row=2)

tally_label = Label(text="✔", font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
tally_label.grid(column=1, row=3, pady=(10, 10))


window.mainloop()