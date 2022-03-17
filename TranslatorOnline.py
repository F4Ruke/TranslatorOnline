from keyboard import add_hotkey, wait, write, send
from googletrans import Translator
from pyperclip import paste
from time import sleep

translator = Translator()


def cut():
    """Вырезка напечатанного текста"""
    send("ctrl+a")
    send("ctrl+x")


def translate():
    """Перевод текста с последующей вставкой"""
    cut()
    sleep(0.05)
    write(translator.translate(paste()).text)


def translate_paste():
    """Вставка скопированного и переведеннго текста"""
    write(translator.translate(paste(), dest="ru").text)


if __name__ == "__main__":
    add_hotkey("f12", translate)
    add_hotkey("f11", translate_paste)
    wait()
