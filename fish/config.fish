set fish_greeting
export EDITOR="nvim"
export VISUAL="nvim"
set -gx GIT_CONFIG_GLOBAL ~/.config/gh/.gitconfig


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

#======================================= ALIASES ============================================

abbr conf 'nvim ~/.config/fish/config.fish'
abbr Sconf 'source ~/.config/fish/config.fish'

alias vim='nvim'
# Changing "ls" to "exa"
alias ls='exa -al --color=always --group-directories-first' # my preferred listing
alias la='exa -a --color=always --group-directories-first'  # all files and dirs
alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
alias l.='exa -a | egrep "^\."'

#============================================================================================


function meow () 
echo "              ＿＿"
echo "　　　　　🌸＞　　フ"
echo "　　　　　| 　_　 _ l"
echo "　 　　　／\`  ミ＿xノ"
echo "　　 　 /　　　 　 |     Nyā 󰄛"
echo "　　　 /　 ヽ　　 ﾉ"
echo "　 　 │　　|　|　|"
echo "　／￣|　　 |　|　|"
echo "　| (￣ヽ＿_ヽ_)__)"
echo "　＼二つ"
end
export meow

#============================================================================================
starship init fish | source
#============================================================================================

# source "$HOME/.cargo/env"
