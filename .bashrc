# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Added by Canopy installer on 2016-03-14
# VIRTUAL_ENV_DISABLE_PROMPT can be set to '' to make the bash prompt show that Canopy is active, otherwise 1
alias activate_canopy="source '/home/amardeep/Enthought/Canopy_64bit/User/bin/activate'"
# VIRTUAL_ENV_DISABLE_PROMPT=1 source '/home/amardeep/Enthought/Canopy_64bit/User/bin/activate'
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
alias auto='source $HOME/auto/07p/cmds/auto.env.sh'
alias gal='sudo screen /dev/ttyUSB0 115200'
alias m='matlab'
alias c='clear'
alias nandan='cd ~/Desktop/IITM/AEROSPACE/Aero_Controls/Nandan_Sir'
alias books='cd ~/Desktop/IITM/AEROSPACE/Aero_Controls/imp_books'
alias arduino='cd ~/Desktop/CODING/arduino-1.6.0+Intel;./arduino'
alias nodesk='matlab -nodesktop'
alias processing='cd ~/bash_scripting; ./processing'
alias restart='sudo reboot'
alias mount_new_vol='test -d ~/mount_new_vol || mkdir ~/mount_new_vol && sudo mount /dev/sda7 ~/mount_new_vol'
alias unmount_new_vol='sudo umount /dev/sda7'
if_mount() {
if mountpoint -q ~/$1
then
echo "itz mounted"
else
echo "not mounted"
fi
}
alias multimedia='xdg-open'
mnt=mount_new_vol

pdf_opener() {
val1=$(locate -i $1 | grep pdf$ | wc -l)
val2=$(locate -i $1 | grep -i $2 | grep pdf$ | wc -l)
val3=$(locate -i $1 | grep -i $2 | grep -i $3 | grep pdf$ | wc -l)
if [ $val1 -eq 1 ]
then
evince "$(locate -i $1 | grep pdf$)"
elif [ $val2 -eq 1 ]
then
evince "$(locate -i $1 | grep -i $2 | grep pdf$)"
elif [ $val3 -eq 1 ]
then
evince "$(locate -i $1 | grep -i $2 | grep -i $3 | grep pdf$)"
else
echo "not possible"
fi
exit 0
}
export -f pdf_opener

file_on() {
var=$(ps aux | grep "$1" | grep "$2" | grep "$3" | wc -l)
if [ $var -ne 0 ]
then
echo "file is running"
else
echo "file is not running"
fi
}
export -f file_on
alias ins='sudo apt-get install'
alias repo='sudo apt-add-repository'
alias ssh_gal='ssh root@192.168.0.110'
alias mac_gal='98:4F:EE:05:57:16'
alias format_32='sudo mkfs.vfat /dev/"$1"'
#synclient TapButton1=1 TapButton2=3 TapButton3=2
alias mouse='xinput --list-props "SynPS/2 Synaptics TouchPad"'
alias search_ip='nmap 192.168.0.*'
alias drives='sudo fdisk -l'
alias time_server='ntpq -p'
alias upd='sudo apt-get update && sudo apt-get upgrade'
alias speed_analysis='systemd-analyze $1'
alias search_on_network='nmap 192.168.0.*'
alias blue_on='sudo service bluetooth start'
alias blue_off='sudo service bluetooth stop'
alias http_put_angle='http -b PUT 192.168.0.110:8888/put_angle/$1'
alias p='python'
read_sensor_data_from_dweet(){
while true
do
http -b https://dweet.io:443/get/latest/dweet/for/mpu6050_sensor_data_amardeep_mishra >> ~/dweet.txt
sleep 1
done }
alias dir_size='du -s "$1"'
alias remove='sudo apt-get remove "$1"'
alias auto-remove='sudo apt-get remove --auto-remove "$1"'
k() {
ps -aux | grep -i "$1" > ~/bash/process.txt
kill $(for i in "$(cat ~/bash/process.txt)" ;do echo $i ;done | awk '{print $2}')
}

alias lab='ssh -X amardeep@10.21.43.225'
f(){
sudo find ~/ -iname "*$2*" -a -iname "*$3*" -type $1
}

g(){
if [ $1 = "add" ]
	then
	git add "$2" && git commit -m "$3" && git push
elif [ $1 = "remove" ]
	then
	git rm "$2" && git commit -m "$3" && git push
fi
}
move(){
find $1 -maxdepth 1 -iname "$2" -a -iname "$3" -type f -exec mv {} $4 \;
}
swp_remover(){
var=$(pwd)
v=$(ls -a $var | grep swp | wc -l)
if [ $v -ne 0 ]
then
rm -r $var/.*.swp
else
echo no swp file exists
fi
}
