#!/bin/sh
# zmodload zsh/zprof    # startup time test
export GIT_CONFIG_GLOBAL=~/.config/gh/.gitconfig
export ZDOTDIR=${XDG_CONFIG_HOME:-$HOME/.config}/zsh
export ZSH_COMPDUMP=$HOME/.config/zsh/.zcompdump
#======================================= ALIASES ============================================

alias vim='nvim'
alias ls='logo-ls'
alias la='logo-ls -a'
# alias rc='vim ${XDG_CONFIG_HOME:-$HOME/.config/zsh}/.zshrc'
alias p10k='vim ~/.config/powerlevel10k/.p10k.zsh'
alias dot="/usr/bin/git --git-dir=$HOME --work-tree=$HOME"

if test -f "$HOME/.config/zsh/.zshrc" ; then
  alias rc='vim $HOME/.config/zsh/.zshrc'
else
  alias rc='vim $HOME/.zshrc'
fi

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

HISTFILE=~/.cache/.zsh_history
HISTSIZE=1000000
SAVEHIST=1000000
export EDITOR="nvim"



# Enable colors and change prompt:
#autoload -U colors && colors && PS1="%B%{$fg[red]%}[%{$fg[green]%}%n %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}λ%b: "

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
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
source ~/.config/powerlevel10k/powerlevel10k.zsh-theme
[[ ! -f ~/.config/powerlevel10k/.p10k.zsh ]] || source ~/.config/powerlevel10k/.p10k.zsh
#============================================================================================

# zprof    # startup time test
