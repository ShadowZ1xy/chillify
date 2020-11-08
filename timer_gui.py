import tkinter as tk


def show_timer_window(timer,
                      w_size, h_size,
                      timer_text_color, timer_text_font_and_size, timer_text_bg_color,
                      text, text_color, text_font_and_size, text_bg_color,
                      bg_color):
    root = tk.Tk()
    root.overrideredirect(1)
    root.configure(bg=bg_color)
    root.after(timer * 1000, lambda: root.destroy())
    root.resizable(False, False)
    __window_to_center(root, w_size, h_size)

    timer_label = tk.Label(root)
    timer_label.pack()
    timer_label.config(font=timer_text_font_and_size, fg=timer_text_color)
    timer_label.configure(bg=timer_text_bg_color)
    timer_label.place(relx=0.5,
                      rely=0.2,
                      anchor='center')

    text_label = tk.Label(root)
    text_label.pack()
    text_label["text"] = text
    text_label.config(font=text_font_and_size, fg=text_color)
    text_label.configure(bg=text_bg_color)
    text_label.place(relx=0.5,
                     rely=0.5,
                     anchor='center')

    __countdown(timer, timer_label, root)
    root.mainloop()


def __window_to_center(root, window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height,
                                       x_coordinate, y_coordinate))


def __countdown(count, label, root):
    label['text'] = "Осталось {0} секунд".format(count)
    if count > 0:
        root.after(1000, __countdown, count - 1, label, root)
