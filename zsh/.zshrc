#!/bin/sh

# zmodload zsh/zprof    # startup time test

export EDITOR="nvim"
export VISUAL="nvim"
export GIT_CONFIG_GLOBAL=~/.config/gh/.gitconfig
export ZDOTDIR=${XDG_CONFIG_HOME:-$HOME/.config}/zsh
export ZSH_COMPDUMP=$HOME/.config/zsh/.zcompdump

### SETTING OTHER ENVIRONMENT VARIABLES
if [ -z "$XDG_CONFIG_HOME" ] ; then
    export XDG_CONFIG_HOME="$HOME/.config"
fi
if [ -z "$XDG_DATA_HOME" ] ; then
    export XDG_DATA_HOME="$HOME/.local/share"
fi
if [ -z "$XDG_CACHE_HOME" ] ; then
    export XDG_CACHE_HOME="$HOME/.cache"
fi

#======================================= ALIASES ============================================

alias vim='nvim'
alias ls='logo-ls'
alias la='logo-ls -a'
alias ll='logo-ls -la'
alias p10k='vim ~/.config/powerlevel10k/.p10k.zsh'
alias dot="/usr/bin/git --git-dir=$HOME --work-tree=$HOME"


if test -f "$HOME/.config/zsh/.zshrc" ; then
  alias rc='vim $HOME/.config/zsh/.zshrc'
  export zsh=$HOME/.config/zsh/.zshrc
else
  alias rc='vim $HOME/.zshrc'
  export zsh=$HOME/.zshrc
fi

#============================================================================================

### ARCHIVE EXTRACTION
# usage: ex <file>
ex ()
{
  if [ -f "$1" ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

#============================================================================================


function meow () {
echo "              ＿＿"
echo "　　　　　🌸＞　　フ"
echo "　　　　　| 　_　 _ l"
echo "　 　　　／\`  ミ＿xノ"
echo "　　 　 /　　　 　 |     Nyā "
echo "　　　 /　 ヽ　　 ﾉ"
echo "　 　 │　　|　|　|"
echo "　／￣|　　 |　|　|"
echo "　| (￣ヽ＿_ヽ_)__)"
echo "　＼二つ"
}

export meow

HISTFILE=$XDG_CACHE_HOME/.zsh_history
HISTSIZE=1000000
SAVEHIST=1000000



# Enable colors and change prompt when p10k doesnt work
autoload -U colors && colors && PS1="%B%{$fg[red]%}[%{$fg[green]%}%n %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}λ%b: "

# Ignore case
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

#============================================================================================

if [[ ! -f ${ZDOTDIR:-${HOME}/.config/zsh}/.zcomet/bin/zcomet.zsh ]]; then
  command git clone https://github.com/agkozak/zcomet.git ${ZDOTDIR:-${HOME}/.config/zsh}/.zcomet/bin
fi
source ${ZDOTDIR:-${HOME}/zsh}/.zcomet/bin/zcomet.zsh

zcomet load "esc/conda-zsh-completion"
zcomet load "zsh-users/zsh-autosuggestions"
zcomet load "zsh-users/zsh-syntax-highlighting"


#============================================================================================

# if [[ ! -f ${ZDOTDIR:-${HOME}/.config/zsh}/.zcomet/bin/zcomet.zsh ]]; then
#   command git clone https://github.com/agkozak/zcomet.git ${ZDOTDIR:-${HOME}/.config/zsh}/.zcomet/bin
# fi

eval "$(starship init zsh)"
#============================================================================================

source "$HOME/.cargo/env"
# zprof    # startup time test

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
