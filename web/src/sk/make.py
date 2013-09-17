import generator as g
import glob

g.set_target_root("../../www/")

g.enqueue("index.htm")
g.enqueue("kontakt.htm")
g.enqueue("registracia.htm")
g.enqueue("miesta.htm")

g.enqueue("onaboji/index.htm")
g.enqueue("onaboji/pravidla.htm")
g.enqueue("onaboji/harmonogram.htm")
#g.enqueue("onaboji/faq.htm")

g.enqueue("akopomoct/index.htm")
g.enqueue("akopomoct/zs-ucitel.htm")
g.enqueue("akopomoct/zs-skola.htm")
g.enqueue("akopomoct/ss-ziak.htm")
g.enqueue("akopomoct/ss-ucitel.htm")
g.enqueue("akopomoct/ss-skola.htm")
g.enqueue("akopomoct/firma.htm")
g.enqueue("akopomoct/nadsenec.htm")

for f in glob.glob("bootstrap/*"):
	g.include(f)

g.include(".kontakt.sk.htm")
g.include(".miesta.sk.htm")

g.generate()