#!/bin/zsh
# Серии кадров и видео круга 6. Запуск из корня сайта при поднятом сервере 127.0.0.1:8765.
# Вывод: design/kadry-dvizhenie/E6-*.jpg (листы) и E6-*.mp4. Промежуточные кадры — в $1 (папка вне репозитория).
T=$1; U=http://127.0.0.1:8765/design/dvizhenie-E6.html; K=design/kadry-dvizhenie; C=design/instrumenty/cdp.mjs
vid(){ ffmpeg -loglevel error -y -framerate $3 -i $1/%03d.jpg -vf "crop=$4,scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p -crf 26 $2 }
for v in a b c; do
  for w in 1440 375; do
    h=$([ $w = 1440 ] && echo 900 || echo 812); d=$T/p$v$w; mkdir -p $d
    node $C scrub "$U?pyatna=$v" $w $h $d 60 p0 p1 140 >/dev/null
    vid $d $K/E6-pyatna-$v-$w.mp4 10 "iw:ih:0:0"
  done
  python3 -I design/instrumenty/listy.py $T/p${v}1440 $K/E6-pyatna-$v-1440.jpg 0,0,1440,900 0,12,24,36,48,59 3 "прокрутка, кадр" >/dev/null
  python3 -I design/instrumenty/listy.py $T/p${v}375 $K/E6-pyatna-$v-375.jpg 0,0,375,812 0,12,24,36,48,59 6 "кадр" >/dev/null
done
for v in a c; do d=$T/y$v; mkdir -p $d; node $C frames "$U?god=$v" 1440 900 $d 48 90 .plan.year >/dev/null; vid $d $K/E6-god-$v.mp4 9 "800:520:320:20"; done
d=$T/yb; mkdir -p $d; node $C scrub "$U?god=b" 1440 900 $d 36 ".yr@0.95" ".yr@0.3" 150 >/dev/null; vid $d $K/E6-god-b.mp4 8 "iw:ih:0:0"
ls -la $K/E6-*
