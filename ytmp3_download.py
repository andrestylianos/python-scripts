from subprocess import Popen,PIPE
import shlex


def confirm_download(yt_link):
    cmd='printf "yes\nno"'
    cmd = shlex.split(cmd)
    question = Popen(cmd, stdout=PIPE)
    cmd = 'dmenu -p "Download '+yt_link+' ????" -i -nb "#2B0123" -nf white -sb white -sf "#2B0123" -fn red-13'
    cmd = shlex.split(cmd)
    confirmation = Popen(cmd, stdin=question.stdout, stdout=PIPE)
    confirmation = confirmation.communicate()[0].decode().split("\n")
    return confirmation[0]

cmd = 'clipit -c'
cmd = shlex.split(cmd)
clip = Popen(cmd, stdout=PIPE)
yt_link = clip.communicate()[0].decode()
if confirm_download(yt_link) == "yes":
    cmd = 'sh /home/pantera/repos/shell-scripts/ytmp3.sh '+yt_link
    cmd = shlex.split(cmd)
    print(cmd)
    Popen(cmd)

