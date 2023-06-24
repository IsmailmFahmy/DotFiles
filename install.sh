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
    git submodule update --init --recursive && echo -e "${Success}Updating submodules${Color_Off}\n"
} || {
    echo -e "${Error}Error updating submodules\n"
}

} && {  # sync repos first

function backup {

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

#move files into .config

process "nvim"

process "qtile"

process "dunst"

process "fish"

process "rofi"

read -n1 -rep 'Would you like to change your gh folder? (y,N) ' CFG
if [[ $CFG == "Y" || $CFG == "y" ]]; then
    process "gh"
fi

process "kitty"


process "lf"

process "starship.toml"

process ".xinitrc"

process "picom.conf"

read -n1 -rep 'Would you like to download the required packages? (y,N) ' CFG
if [[ $CFG == "Y" || $CFG == "y" ]]; then
    sudo pacman -Syu --noconfirm 
    sudo pacman -S --needed --noconfirm - < pacman.txt
    pip install Pillow iwlib
fi

}
