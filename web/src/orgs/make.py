import generator as g
import glob

g.set_target_root("../../www/orgs")

g.enqueue("index.htm")
g.enqueue("pridajmiesto.htm")
g.enqueue("pridajulohu.htm")

for f in glob.glob("bootstrap/*"):
	g.include(f)

g.generate()