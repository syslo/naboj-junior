import generator as g
import glob

g.set_target_root(os.path.join(os.pardir,os.pardir,"www","orgs"))

g.enqueue("index.htm")
g.enqueue("pridajmiesto.htm")
g.enqueue("pridajulohu.htm")

for f in glob.glob("bootstrap/*"):
	g.include(f)

g.generate()