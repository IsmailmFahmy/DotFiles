# vim: filetype=bash


xset -b
exec xrandr --output DisplayPort-2 --mode 1920x1080 --rate 144.00 &
xinput set-prop '9' 'libinput Accel Speed' -0.5


exec unclutter -idle 3 -grab &
exec  nitrogen --restore &
exec  greenclip daemon &
# exec picom -b &


exec  dunst &
pamixer --set-volume 100 &
# exec udiskie -ans &       # mount script bound to "F10"


exec syncthing --no-browser &
rsync -au --partial ~/Documents/Obsidian ~/.backup/ &   # Backup Obsidian Vault


exec  sxhkd &
exec  qtile start
