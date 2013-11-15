import generator as g
import glob
import os.path
import os

g.set_target_root(os.path.join(os.pardir,os.pardir,"www"))

g.enqueue("index.htm")
g.enqueue("kontakt.htm")
g.enqueue("registracia.htm","registracia.php")
g.enqueue("registracia-timy.htm","registracia-timy.php")
g.enqueue("registracia-ok.htm")
g.enqueue("miesta.htm")
g.enqueue("materialy.htm")

g.enqueue(os.path.join("onaboji","index.htm"))
g.enqueue(os.path.join("onaboji","pravidla.htm"))
g.enqueue(os.path.join("onaboji","harmonogram.htm"))
#g.enqueue(os.path.join("onaboji","faq.htm"))

g.enqueue(os.path.join("akopomoct","index.htm"))
g.enqueue(os.path.join("akopomoct","zs-ucitel.htm"))
g.enqueue(os.path.join("akopomoct","zs-skola.htm"))
g.enqueue(os.path.join("akopomoct","ss-ziak.htm"))
g.enqueue(os.path.join("akopomoct","ss-ucitel.htm"))
g.enqueue(os.path.join("akopomoct","ss-skola.htm"))
g.enqueue(os.path.join("akopomoct","firma.htm"))
g.enqueue(os.path.join("akopomoct","nadsenec.htm"))

for f in glob.glob(os.path.join("bootstrap","*")):
	g.include(f)

for f in glob.glob(os.path.join("downloads","*")):
	g.include(f)

for f in glob.glob(os.path.join("downloads","*","*")):
	g.include(f)

g.include(".kontakt.sk.htm")
g.include(".miesta.sk.htm")

g.include(os.path.join("img","logo-small.png"))
g.include(os.path.join("img","logo-big.png"))

g.generate()
