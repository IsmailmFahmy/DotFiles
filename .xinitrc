xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &
xinput set-prop '9' 'libinput Accel Speed' -0.5


# exec picom -b &
exec dbus-launch --exit-with-session nitrogen --restore &
exec dbus-launch --exit-with-session greenclip daemon &


# exec udiskie -ans &       # mount script bound to "F10"
exec dbus-launch --exit-with-session dunst &
exec unclutter --timeout 4 &
exec syncthing --no-browser &
rsync -au --partial ~/Documents/Obsidian ~/.backup/ &   # Backup Obsidian Vault

# exec sxhkd &

exec dbus-launch --exit-with-session sxhkd &
exec dbus-launch --exit-with-session i3
