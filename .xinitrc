xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &
# exec udiskie -ans &       # mount script bound to "F10"
exec greenclip daemon &
# exec picom -b &
exec dunst &
exec nitrogen --restore &
exec unclutter --timeout 4 &
exec sxhkd &
exec qtile start
# exec dwm
