from pathlib import Path
import collections 
import sys

if len(sys.argv) < 2:
	print ("Usage: %s\ndisplays number of files and total size of files per extension in the specified path." % sys.argv[0])
	exit(1)
nf =[]  #name file
sf =[]  #list for size file
folder = Path(sys.argv[1])
for p in folder.iterdir():
	nf.append(p.suffix)
	sf.append(p.stat().st_size)
#print (sf)
zipped = zip(nf, sf)

d = collections.defaultdict(list)
for k ,v in zipped:
	d.setdefault(k,[]).append(v)
od = collections.OrderedDict(sorted(d.items()))
#print (od)

for item in od:
	print (item[1:], len(od[item]), sum(od[item]))
#for k, v in od.items(): print k ,v

	



