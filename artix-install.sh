#!/bin/sh

User_Home=$(eval echo -e ~${SUDO_USER})
conf=$User_Home/.config
date=$(date +%d-%m)

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White
Error='\033[0;31m'
Success='\033[0;32m'
File='\033[0;34m'

{
{
    git submodule update --init && echo -e "${Success}Updating submodules${Color_Off}\n"
} || {
    echo -e "${Error}Error updating submodules\n"
}

} && {  # sync repos first

function backup {


    # { # create Backup Folder
    #     [ -e "$conf/BackupOf-$date"] || { mkdir $conf/BackupOf-$date >> /dev/null 2>&1 && \
    #                                     echo -e "${Success}Created $conf/BackupOf-$date${Color_Off}\n" }               
    # }
    if [[ ! -e "$conf/BackupOf-$date" ]]; then
        mkdir $conf/BackupOf-$date >> /dev/null 2>&1
        echo -e "${Success}Created $conf/BackupOf-$date${Color_Off}\n"
    fi

    
    if [[ -e $conf/BackupOf-$date/$1 ]] ||[[ -L $conf/BackupOf-$date/$1 ]] ; then
        echo -e "${File}$1 ${Error}is already backed up"
    else
        {
            mv $conf/$1 "$conf/BackupOf-$date/" >> /dev/null 2>&1 &&
            echo -e "Moved ${File}$1 ${Color_Off}to BackupOf-$date"
        } || {
            echo -e "${Error}Error moving ${File}$1 ${Error}to BackupOf-$date"
        }
    fi
}

function service {
{
    # sudo ln -s /etc/sv/$1 /var/service/$1 >> /dev/null 2>&1 &&
    # sudo rc-update add $1
    sudo systemctl enable $1
    echo -e "Created link for ${File}$1${Color_Off}\n"
} || {
    echo -e "${Error}Error enabling service for ${File}$1${Color_Off}\n"
}

}

function process {
{
    if [[ -e $conf/$1 ]]; then 
        backup "$1"
    fi
    ln -rs $1 $conf/ >> /dev/null 2>&1 &&
    echo -e "Created link for ${File}$1${Color_Off}\n"
} || {
    echo -e "${Error}Error copying ${File}$1${Color_Off}\n"
}
}

# create ~/.config file if it does not exits

files=(
".xinitrc"
"nvim"
"qtile"
"dunst"
"fish"
"rofi"
"kitty"
"lf"
"starship.toml"
"picom.conf"
"gtk-2.0"
"gtk-3.0"
".gtkrc-2.0"
".Xresources"
"Thunar"
"btop"
"nitrogen"
"neofetch"
"pavucontrol.ini"
"zathura"

)

[ -e $conf ]   ||    { mkdir $conf && echo -e "${Success}Created $conf${Color_Off}\n" ;}
for config_file in ${files[@]}
do
    process $config_file
done

# ADD GITHUB CONFIG
read -n1 -rep 'Would you like to change your gh folder? (y,N) ' CFG
printf '\n'
if [[ $CFG == "Y" || $CFG == "y" ]]; then
    process "gh"
fi

# ADD ARCH PACKAGES
read -n1 -rep 'Would you like to add the arch repos? (y,N) ' CFG
printf '\n'
if [[ $CFG == "Y" || $CFG == "y" ]]; then
    sudo pacman -Syu --noconfirm 

    sudo pacman -S wget --needed --noconfirm
    sudo wget "https://github.com/archlinux/svntogit-packages/raw/packages/pacman-mirrorlist/trunk/mirrorlist" -O /etc/pacman.d/mirrorlist-arch

    sudo echo "[universe]" >> /etc/pacman.conf
    sudo echo "Server = https://universe.artixlinux.org/$arch" >> /etc/pacman.conf
    sudo echo "Server = https://mirror1.artixlinux.org/universe/$arch" >> /etc/pacman.conf
    sudo pacman -Syu --noconfirm 
    sudo pacman -S artix-archlinux-support --noconfirm --needed

    sudo echo "# Arch" >> /etc/pacman.conf
    sudo echo "[extra]" >> /etc/pacman.conf
    sudo echo "Include = /etc/pacman.d/mirrorlist-arch" >> /etc/pacman.conf
    sudo echo "" >> /etc/pacman.conf
    sudo echo "[community]" >> /etc/pacman.conf
    sudo echo "Include = /etc/pacman.d/mirrorlist-arch" >> /etc/pacman.conf
    sudo echo "" >> /etc/pacman.conf
    sudo echo "#[multilib]" >> /etc/pacman.conf
    sudo echo "Include = /etc/pacman.d/mirrorlist-arch" >> /etc/pacman.conf
    sudo pacman -Syu --noconfirm 

fi

# INSTALLING PACKAGES
read -n1 -rep 'Would you like to download the required packages? (y,N) ' CFG
printf '\n'
if [[ $CFG == "Y" || $CFG == "y" ]]; then
    sudo pacman -Syu --noconfirm 
    sudo pacman -S --needed --noconfirm - < pacman.txt
    # xbps-install -Su
    # xbps-install -S $(cat pacman.txt)
    pip install Pillow iwlib
fi 

# read -n1 -rep 'Would you like to Enable the services ( runit )? (y,N) ' CFG
# printf '\n'
# if [[ $CFG == "Y" || $CFG == "y" ]]; then
#     service "NetworkManager"
#     service "cups"
#     service "udisks2"
# fi 

xrdb $conf/.Xresources
}