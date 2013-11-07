import subprocess
import re
import shlex

def split_cmd(cmd):
	return cmd.split(" ")
	
def get_output(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = process.communicate()[0].decode()
    process.stdout.close()
    return out

def connected_monitor(xrandr):
	m = []
	for l in xrandr:
		if ' connected' in l:
			connected = l.split(" connected")
			m.append(connected[0])
	return m
	
def layout_opt(monitor):
	dmenargs = 'printf "Built-in\nExternal\nExtend\nMirror"'
	cmd1 = shlex.split(dmenargs)
	dmenopt = 'dmenu -p "'+monitor[1]+' / '+monitor[0]+'" -i -nb "#2B0123" -nf white -sb white -sf "#2B0123" -fn red-13'
	cmd2 = shlex.split(dmenopt)
	printf = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
	dmenu = subprocess.Popen(cmd2, stdin=printf.stdout ,stdout=subprocess.PIPE)
	chosen = dmenu.communicate()[0].decode()
	print(chosen)
	layouts = {'Built-in\n': builtin,
	 'External\n': external,
	 'Extend\n': extend,
	 'Mirror\n': mirror}
	layouts[chosen](monitor)

def change_layout(config):
	cmd = shlex.split(config)
	subprocess.Popen(cmd)		

def builtin(monitor):
	xrandrconfig = "xrandr --output "+monitor[1]+" --auto --output "+monitor[0]+" --off"
	change_layout(xrandrconfig)

def external(monitor):
	xrandrconfig = "xrandr --output "+monitor[0]+" --auto --output "+monitor[1]+" --off"
	change_layout(xrandrconfig)
	
def extend(monitor):
	xrandrconfig = "xrandr --output "+monitor[1]+" --auto --primary --output "+monitor[0]+" --auto --left-of "+monitor[1]
	change_layout(xrandrconfig)
	
def mirror(monitor):
	xrandrconfig = "xrandr --output "+monitor[1]+" --auto --output "+monitor[0]+" --auto --same-as "+monitor[1]
	change_layout(xrandrconfig)
	
def main():
	xrandrquery = get_output(split_cmd("xrandr -q")).split("\n")
	monitor = connected_monitor(xrandrquery)
	print(monitor)
	layout_opt(monitor)
	
	
main()
