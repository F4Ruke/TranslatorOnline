from keyboard import press, release, add_hotkey, wait, write
from googletrans import Translator
from pyperclip import paste
from time import sleep

translator = Translator()


def press_button(button_1: str, button_2: str):
    """Нажимает сочетание 2-ух клавиш клавиатуры"""
    press(f"{button_1}")
    press(f"{button_2}")
    release(f"{button_2}")
    release(f"{button_1}")


def cut():
    """Вырезка выделенного текста"""
    press_button("ctrl", "a")
    press_button("ctrl", "x")


def translate():
    """Перевод текста с последующей вставкой"""
    cut()
    sleep(0.05)
    write(translator.translate(paste()).text)


if __name__ == "__main__":
    add_hotkey("f12", translate)
    wait()
