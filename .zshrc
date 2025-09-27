#!/usr/bin/env zsh
# zmodload zsh/zprof    # startup time test

export EDITOR="nvim"
export VISUAL="nvim"
export QT_QPA_PLATFORMTHEME="qt6ct"
export TERM="xterm-256color"

export GIT_CONFIG_GLOBAL="${HOME}/.config/gh/.gitconfig"
export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:-$HOME/.cache}"

export ZDOTDIR="${XDG_CONFIG_HOME:-$HOME/.config}/zsh"
export ZSH_COMPDUMP="$XDG_CACHE_HOME/.zcompdump"

export GTK2_RC_FILES="${HOME}/.config/theming/.gtkrc-2.0"
export GTK3_RC_FILES="${HOME}/.config/theming/.gtkrc-3.0"
export XINITRC="~/.config/.xinitrc"
export ENCRYPTED_FILE="~/Documents/Important_Files/Less Important"

path+=("${HOME}/.local/bin/")
path+=("${HOME}/.cargo/bin/")
path+=("${HOME}/.wasmedge/bin")
path+=("/home/xda/platform-tools")

#======================================= ALIASES ============================================

alias vim='nvim'
alias ls="exa -la --color=always --group-directories-first --icons" # my preferred listing
alias la="exa -a --color=always --group-directories-first --icons"  # all files and dirs
alias ll="exa -l --color=always --group-directories-first --icons"  # long format
alias lt="exa -aT --color=always --group-directories-first --icons" # tree listing
alias l.="exa -al --color=always --group-directories-first --icons | grep -E "\W\.\w" "

if test -f "$HOME/.config/zsh/.zshrc" ; then
  alias rc='vim $HOME/.config/zsh/.zshrc'
  export zsh=$HOME/.config/zsh/.zshrc
else
  alias rc='vim $HOME/.zshrc'
  export zsh=$HOME/.zshrc
fi

HISTFILE=$XDG_CACHE_HOME/.zsh_history
HISTSIZE=1000000
SAVEHIST=1000000



### Zinit plugins
ZINIT_HOME="${XDG_DATA_HOME:-$HOME/.local/share}/zinit/zinit.git"
if [[ ! -d $ZINIT_HOME ]]; then
  mkdir -p "$(dirname $ZINIT_HOME)"
  git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi
source "$ZINIT_HOME/zinit.zsh"

### Plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-history-substring-search
# zinit light kutsan/zsh-system-clipboard # Aparently doesn't work with X11
zinit light zsh-vi-more/vi-motions
zinit light junegunn/fzf
zinit light joshskidmore/zsh-fzf-history-search


# =================================================

# Ignore case
autoload -Uz zkbd
autoload -Uz compinit && compinit
zmodload zsh/complist   # enables the 'menuselect' keymap
# zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
# Enable menu selection with arrow keys
zstyle ':completion:*' menu select
bindkey -M menuselect '^[[Z' reverse-menu-complete  # optional: Shift-Tab to go backwards


bindkey -v # enable vi mode

eval "$(starship init zsh)"
source "$HOME/.cargo/env"
# zprof    # startup time test

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
