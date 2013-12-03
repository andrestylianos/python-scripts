import subprocess
import shlex


def now_playing():
    cmd = 'mpc current'
    music = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE)
    playing = music.communicate()[0].decode().split("\n")
    return playing

def display_lyr(music):
    cmdcat = 'cat "/home/pantera/.lyrics/'+music[0]+'.txt"'
    cmdcat = shlex.split(cmdcat)
    cmddmenu = 'dmenu -l 40 -fn "inconsolata-13" -p "Lyrics" -nb "#2B0123" -nf white -sb white -sf "#2B0123"'
    cmddmenu = shlex.split(cmddmenu)
    p1 = subprocess.Popen(cmdcat, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.Popen(cmddmenu,stdin=p1.stdout)

display_lyr(now_playing())
