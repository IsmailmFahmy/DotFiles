set fish_greeting
export EDITOR="nvim"
export VISUAL="nvim"
fish_add_path -a ~/.cargo/bin
fish_add_path -a ~/.local/bin
set -gx GIT_CONFIG_GLOBAL ~/.config/gh/.gitconfig
set -gx GTK2_RC_FILES ~/.config/.gtkrc-2.0
set -gx XINITRC ~/.config/.xinitrc
set -g fish_prompt_suffix_root '#'

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
if status is-login
    if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
        exec startx -- -keeptty
    end
end
#===================================== ALIASES ==========================================

abbr conf 'nvim ~/.config/fish/config.fish'
abbr Sconf 'source ~/.config/fish/config.fish'
abbr lfrc "nvim ~/.config/lf/lfrc"
abbr binds "nvim ~/.config/sxhkd/sxhkdrc"

alias vim='nvim'
# Changing "ls" to "exa"
alias ls='exa -al --color=always --group-directories-first --icons' # my preferred listing
alias la='exa -a --color=always --group-directories-first --icons'  # all files and dirs
alias ll='exa -l --color=always --group-directories-first --icons'  # long format
alias lt='exa -aT --color=always --group-directories-first --icons' # tree listing
alias l.='exa -al --color=always --group-directories-first --icons | grep -E "\W\.\w" '

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

function ptf
        eval (xclip -se c -o > "$1")
end

function sobs
     rsync -Prau ~/Documents/Obsidian/ /run/media/Fahmy/4062/Documents/Obsidian/; and notify-send "RSYNC" "Local Obsidian synced with usb"; or notify-send "RSYNC" "Failed Sync"
end


#========================================================================================
starship init fish | source
#========================================================================================
