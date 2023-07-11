xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &
exec udiskie -ans &
exec nitrogen --restore &
exec greenclip daemon &
exec sxhkd &
exec picom -b &
exec dunst &
exec unclutter --timeout 4 &
exec qtile start
# exec dwm

