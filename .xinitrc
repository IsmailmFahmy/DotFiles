xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &

# exec udiskie -ans &       # mount script bound to "F10"
# exec picom -b &
exec greenclip daemon &

exec dunst &
exec nitrogen --restore &
exec unclutter --timeout 4 &

exec dbus-launch --exit-with-session sxhkd &

exec dbus-launch --exit-with-session qtile start
# exec dbus-launch --exit-with-session dwm
