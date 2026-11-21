# Лист кадров: python3 -I listy.py <папка> <выход.jpg> <x0,y0,x1,y1> <номера через запятую> [столбцов] [подпись-приставка]
import sys
from PIL import Image, ImageDraw
d, out, box, idx = sys.argv[1:5]
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 3
box = tuple(int(v) for v in box.split(',')); idx = [int(v) for v in idx.split(',')]
ims = [Image.open(f'{d}/{i:03d}.jpg').convert('RGB').crop(box) for i in idx]
w, h = ims[0].size; rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * w + (cols - 1) * 8, rows * (h + 26)), 'white'); dr = ImageDraw.Draw(sheet)
for k, im in enumerate(ims):
    x, y = (k % cols) * (w + 8), (k // cols) * (h + 26)
    sheet.paste(im, (x, y + 26)); dr.text((x + 4, y + 6), f'{sys.argv[6] if len(sys.argv) > 6 else "кадр"} {idx[k]}', fill=(90, 90, 90))
sheet.save(out, quality=84); print(out, sheet.size)
