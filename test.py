import config
import gui

gui.show_timer_window(5, config.alert_window_width, config.alert_window_height,
                      config.time_font_color, config.time_font_and_size, config.background_color,
                      "Просто приляг и поспи", config.hint_text_color, config.hint_text_font_and_size,
                      config.background_color, config.background_color)
