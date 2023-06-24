xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &
exec udiskie -ans &
exec nitrogen --restore &
exec copyq --start-server hide &
exec flameshot &
exec picom -b &
exec dunst &
exec qtile start

