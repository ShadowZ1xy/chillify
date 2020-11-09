# from threading import Timer
# from settings_directory import settings_gui as gui
# i = 0
#
#
# def test():
#     global i
#     print(i)
#     i += 1
#
#
# while True:
#     b = Timer(4, test)
#     b.run()
#     gui.settings_window_run()

# import config as c
# import timer_gui as gui
#
# gui.show_timer_window(5,
#                       c.alert_window_width,
#                       c.alert_window_height,
#                       c.time_font_color,
#                       c.time_font_and_size,
#                       c.background_color,
#                       "Просто приляг и поспи",
#                       c.hint_text_color,
#                       c.hint_text_font_and_size,
#                       c.background_color,
#                       c.background_color)
#
# import threading
# import time
#
#
# def thread_func_1(some_int):
#     i = 0
#     while 1:
#         print(some_int, i)
#         i += 1
#         time.sleep(3)
#
#
# def thread_func_2(some_str):
#     i = 0
#     while 2:
#         print(some_str, i)
#         i += 1
#         time.sleep(1.5)
#
#
# test = "test"
# temp = "temp"
# thread_1 = threading.Thread(target=thread_func_1, args=(test,))
# thread_2 = threading.Thread(target=thread_func_2, args=(temp,))
#
# thread_1.start()
# thread_2.start()
# thread_1.join()
# thread_2.join()
#
# import pystray
# from PIL import Image, ImageDraw
#
# def create_image():
#     # Generate an image and draw a pattern
#     image = Image.new('RGB', (50, 50), "blue")
#     dc = ImageDraw.Draw(image)
#     dc.rectangle(
#         (10 // 2, 0, 10, 10 // 2),
#         fill="black")
#     return image
#
# icon = pystray.Icon('test name')
# icon.icon = create_image()
# icon.run()