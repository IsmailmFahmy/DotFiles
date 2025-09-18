set fish_greeting
export EDITOR="nvim"
export VISUAL="nvim"
export QT_QPA_PLATFORMTHEME="qt6ct"
export TERM="xterm-256color"

fish_add_path -a ~/.cargo/bin
fish_add_path -a ~/.local/bin
fish_add_path -a /home/xda/platform-tools
fish_add_path -a ~/.nix-profile/bin
fish_add_path -a /home/fahmy/.wasmedge/bin
fish_add_path -a /home/fahmy/Code/esp/xtensa-esp32-elf/bin

set -gx GIT_CONFIG_GLOBAL ~/.config/gh/.gitconfig
set -gx GTK2_RC_FILES ~/.config/theming/.gtkrc-2.0
set -gx GTK3_RC_FILES ~/.config/theming/.gtkrc-3.0
set -gx XINITRC ~/.config/.xinitrc
set -gx ZDOOTDIR ~/.config/zsh
set -g fish_prompt_suffix_root '#'
set -gx ENCRYPTED_FILE $HOME/.local
set -gx ENCRYPTED_FILE "~/Documents/Important_Files/Less Important"
set -gx GITLAB_VOL ~/.local/gitlab



set -Ux LIBRARY_PATH /home/fahmy/.wasmedge/lib
set -Ux WASMEDGE_LIB_DIR /home/fahmy/.wasmedge/lib
set -Ux C_INCLUDE_PATH /home/fahmy/.wasmedge/include
set -Ux LD_LIBRARY_PATH /home/fahmy/.wasmedge/lib
set -Ux CPLUS_INCLUDE_PATH /home/fahmy/.wasmedge/include


fish_vi_key_bindings
fzf_key_bindings
# fish_default_key_bindings




### SETTING OTHER ENVIRONMENT VARIABLES
if [ -z "$XDG_CONFIG_HOME" ] ; 
    set -gx XDG_CONFIG_HOME "$HOME/.config"
end
if [ -z "$XDG_DATA_HOME" ] ; 
    set -gx XDG_DATA_HOME "$HOME/.local/share"
end
if [ -z "$XDG_CACHE_HOME" ] ; 
    set -gx XDG_CACHE_HOME "$HOME/.cache"
end
#===================================== Profile ==========================================
# # Start X at login
# if status --is-login
#   # if test -z "$DISPLAY" -a $XDG_VTNR = 1
#     exec startx -- -keeptty
#   # end
# end
#===================================== ALIASES ==========================================

abbr    conf    "nvim ~/.config/fish/config.fish"
abbr    vconf    "nvim ~/.config/nvim"
abbr    Sconf   "source ~/.config/fish/config.fish"
abbr    lfrc    "nvim ~/.config/lf/lfrc"
abbr    binds   "nvim ~/.config/sxhkd/sxhkdrc"
abbr    drv     "pushd /run/media/fahmy"


alias vim='nvim'

# Changing "ls" to "exa"
alias ls='eza -al --color=always --group-directories-first --icons' # my preferred listing
alias la='eza -a --color=always --group-directories-first --icons'  # all files and dirs
alias ll='eza -l --color=always --group-directories-first --icons'  # long format
alias lt='eza -aT --color=always --group-directories-first --icons' # tree listing
alias l.='eza -al --color=always --group-directories-first --icons | grep -E "\W\.\w" '

#========================================================================================

function meow 
echo "              ＿＿"
echo "　　　　　✿ >　　   >"
echo "　　　　　| 　_　 _ l"
echo "　 　　　／`  ミ＿xノ"
echo "　　 　 /　　　 　 |     Nyā 󰄛 "
echo "　　　 /　 ヽ　　 ﾉ"
echo "　 　 │　　|　|　|"
echo "　／￣|　　 |　|　|"
echo "　| (￣ヽ＿_ヽ_)__)"
echo "　＼二つ"
end
export meow

# function chbg
#     feh --bg-scale $argv[1]
# end
# function killtty
#     systemctl stop getty@tty$argv[1].service
# end

function view
    for i in $argv
        kitty +kitten icat $i
    end
end



function sobs
    rsync -auvP ~/Documents/Obsidian/ /run/media/fahmy/4062/Obsidian ; and notify-send "RSYNC" "Local Obsidian synced with usb"; or notify-send "RSYNC" "Failed Sync"
end


#========================================================================================
starship init fish | source
#========================================================================================







function gp
    set dir (find ~/Code -maxdepth 2 -type d | fzf +m)
    if test -n "$dir"
        cd "$dir"
    end
end
