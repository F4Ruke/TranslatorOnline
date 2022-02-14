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


def translate_paste():
    """Вставка скопированного и переведеннго текста"""
    write(translator.translate(paste(), dest="ru").text)


def main():
    add_hotkey("ctrl + f12", translate)
    add_hotkey("ctrl + f11", translate_paste)
    wait()


if __name__ == "__main__":
    main()
