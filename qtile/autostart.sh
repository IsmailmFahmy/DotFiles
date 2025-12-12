#! /usr/bin/env bash

xset -b

# exec xrandr --output DisplayPort-3 --mode 1920x1080 --rate 144.00 &
# xrandr --output HDMI-1 --scale 1.25x1.25 --panning 2880x1800  &


#xinput set-prop '9' 'libinput Accel Speed' -0.5

xinput set-prop "ASUE140D:00 04F3:31B9 Touchpad" "libinput Natural Scrolling Enabled" 1 # Invert scroll direction

# xrdb -merge ~/.config/.Xresources
xrdb -merge ~/.config/theming/macchiato.Xresources

exec unclutter -idle 3 -grab &    # Fade cursor after 3 seconds
exec nitrogen --restore &         # Wallpaper Manager
exec greenclip daemon &           # Clipboard Manager
#exec picom -b &                   # window blur/animations/rounded corners
exec kdeconnectd &
exec otd-daemon &                 # OpenTabletDriver Daemon
exec sxhkd &                      # Keybinds

exec dunst &                      # Notification Manager
exec nm-applet                    # Network Manager icon
exec blueman-applet               # Bluetooth icon
exec xss-lock slock &             # Run slock on suspend
# powertop & auto-cpufreq are configured as services in systemd
# Idle Lock, dim after 5 min, suspend after another 30s
xidlehook \
    --not-when-fullscreen \
    --not-when-audio \
    --timer 300 \
    'light -O;light -U 30' \
    'light -I' \
    --timer 30 \
    'light -I; systemctl suspend' \
    '' & 

# pamixer --set-volume 100 &
# exec udiskie -ans &             # mount script bound to "F10"

exec /usr/lib/polkit-kde-authentication-agent-1 & # Polkit for running root services in userspace

exec syncthing --no-browser &
rsync -au --partial ~/Documents/Obsidian ~/.backup/ &   # Backup Obsidian Vault
