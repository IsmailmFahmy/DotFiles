#! /bin/bash

exec  sxhkd &
xset -b

# exec xrandr --output DisplayPort-3 --mode 1920x1080 --rate 144.00 &
# xrandr --output HDMI-1 --scale 1.25x1.25 --panning 2880x1800  &


#xinput set-prop '9' 'libinput Accel Speed' -0.5

xinput set-prop "ASUE140D:00 04F3:31B9 Touchpad" "libinput Natural Scrolling Enabled" 1

xrdb -merge ~/.config/.Xresources

exec unclutter -idle 3 -grab &
exec nitrogen --restore &
exec greenclip daemon &
exec picom -b &
exec kdeconnectd &
exec otd-daemon &


exec dunst & # Notifications config
exec nm-applet    2>&1 > /dev/null & # Network manager icon
exec blueman-applet    2>&1 > /dev/null & # Bluetooth icon
exec xss-lock slock & # Run slock on suspend
# pamixer --set-volume 100 &
# exec udiskie -ans &       # mount script bound to "F10"

exec /usr/lib/polkit-kde-authentication-agent-1 &


exec syncthing --no-browser &
# rsync -au --partial ~/Documents/Obsidian ~/.backup/ &   # Backup Obsidian Vault
