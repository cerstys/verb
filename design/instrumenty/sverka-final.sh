#!/bin/zsh
# Сверка сайта (itoroapps.com/verbisto/ с локального сервера 127.0.0.1:8766 — README itoroapps-site) с принятым E9: одни и те же места страницы, RM=1 (без движения — кадры сравнимы).
# zsh design/instrumenty/sverka-final.sh → design/shots/final-E9/<lang>-<w>-<den|noch>-<p>-{e9,final}.jpg
cd "${0:A:h}/../.."; R=$PWD; O=design/shots/final-E9
for lang in ru en; do
  [[ $lang == ru ]] && { E=design/dvizhenie-E9.html; F=http://127.0.0.1:8766/verbisto/ru/ } || { E=design/dvizhenie-E9-en.html; F=http://127.0.0.1:8766/verbisto/ }
  for w in 1440 375; do [[ $w == 1440 ]] && { h=900; sc=1 } || { h=812; sc=2 }
    for t in den noch; do [[ $t == noch ]] && D=1 || D=
      for p in p0 p0.2 p0.4 p0.6 p0.8 p1; do
        RM=1 DARK=$D node design/instrumenty/cdp.mjs shot "file://$R/$E" $w $h $O/$lang-$w-$t-$p-e9.jpg $p $sc 900 >/dev/null
        RM=1 DARK=$D node design/instrumenty/cdp.mjs shot "$F" $w $h $O/$lang-$w-$t-$p-final.jpg $p $sc 900 >/dev/null
      done; done; done; done
python3 -I - <<'PY'
from PIL import Image, ImageChops; import glob
worst=0
for a in sorted(glob.glob('design/shots/final-E9/*-e9.jpg')):
    b=a.replace('-e9.jpg','-final.jpg'); A,B=Image.open(a).convert('L'),Image.open(b).convert('L')
    if A.size!=B.size: print('РАЗМЕР', a, A.size, B.size); continue
    d=ImageChops.difference(A,B); px=sum(1 for v in d.getdata() if v>40)/(A.size[0]*A.size[1])*100
    worst=max(worst,px); print(f'{a.split("/")[-1][:-7]:26} отличных пикселей {px:.2f} %')
print('худший:', f'{worst:.2f} %')
PY
