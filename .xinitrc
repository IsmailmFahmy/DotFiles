xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &
exec nitrogen --restore &
exec picom -b &
exec qtile start

