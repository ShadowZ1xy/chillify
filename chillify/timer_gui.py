import tkinter as tk

from chillify.timer_config import *


def show_timer_window(timer, text):
    root = tk.Tk()
    root.overrideredirect(1)
    root.title("Chillify")
    root.configure(bg=background_color)
    root.after(timer * 1000, lambda: root.destroy())
    root.resizable(False, False)
    root.attributes('-topmost', True)
    root.update()
    __window_to_center(root, alert_window_width, alert_window_height)

    timer_label = tk.Label(root)
    __label_configure(timer_label,
                      0.5, 0.2,
                      time_font_and_size,
                      time_font_color, background_color)

    text_label = tk.Label(root)
    __label_configure(text_label,
                      0.5, 0.5,
                      hint_text_font_and_size,
                      hint_text_color, background_color,
                      text)

    __countdown(timer, timer_label, root)
    root.mainloop()


def __label_configure(label,
                      x, y,
                      font_and_size,
                      text_color, bg_color,
                      text=""):
    label.pack()
    label.config(font=font_and_size, fg=text_color)
    label['text'] = text
    label.configure(bg=bg_color)
    label.place(relx=x,
                rely=y,
                anchor='center')


def __countdown(count, label, root):
    label['text'] = "Осталось {0} секунд".format(count)
    if count > 0:
        root.after(1000, __countdown, count - 1, label, root)


def __window_to_center(root, window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height,
                                       x_coordinate, y_coordinate))
