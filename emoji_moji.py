# coding: utf-8

import sys
import os

from PIL import Image, ImageDraw, ImageFont


FONT_PATH = os.environ.get("FONT_PATH", "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc")


class EmojiMoji():
    CANVAS_SIZE = 128
    FONT_SIZE = 64
    def __init__(self):
        self.canvas = self._get_canvas()

    def draw(self, text: str) -> 'EmojiMoji':
        font = self._get_font()
        drawer = ImageDraw.Draw(self.canvas)
        drawer.text((0, 0), text[:2], font=font, fill='#020011')
        drawer.text((0, 64), text[2:4], font=font, fill='#020011')
        return self

    def get_canvas(self) -> Image:
        return self.canvas

    def save(self, path: str, file_name: str) -> str:
        write_to = os.path.join(path, file_name)
        self.canvas.save(write_to, 'PNG')
        return write_to

    def _get_canvas(self) -> Image:
        return Image.new('RGBA', (self.CANVAS_SIZE, self.CANVAS_SIZE), (0, 0, 0, 0))

    def _get_font(self) -> ImageFont:
        return ImageFont.truetype(FONT_PATH, self.FONT_SIZE)


def main():
    params = sys.argv
    if len(params) != 2:
        print("[使い方 例]: python {} なるほど".format(params[0]))
        return
    text = params[1]
    EmojiMoji().draw(text).save(os.path.dirname(os.path.abspath(__file__)), '{}.png'.format(text))
    print("{}.png".format(text))
    print("https://lmnd.slack.com/admin/emoji に画像を登録してご利用下さい")
     

if __name__ == '__main__':
    main()
