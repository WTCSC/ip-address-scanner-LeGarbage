import sys,subprocess as b,ipaddress as a
from rich import box,live,table
t=table.Table("IP","Status","Response",box=box.ASCII_DOUBLE_HEAD)
with live.Live(t)as l:
	try:
		for i in map(str,a.ip_network(sys.argv[1],0).hosts()):
			try:o=b.run("ping -c 1 "+i,timeout=5,stdout=-1);u=("UP",o.stdout.decode().split("time=")[1].split()[0])if o.stdout else("DOWN","No response")
			except b.TimeoutExpired:u="ERROR","Connection timeout"
			t.add_row(i,*u)
	except KeyboardInterrupt:l.stop()