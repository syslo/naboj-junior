import roots as r
sk_root = r.sk_root
cz_root = r.cz_root
orgs_root = r.orgs_root
del r

root = cz_root

link_data = {
	"uvod": "index.html",
	"akopomoct": "akopomoct/index.html",
	"onaboji": "onaboji/index.html",
	"registracia": "registracia.php",
	"registracia-timy": "registracia-timy.php",
}

def link(target):
	if target in link_data:
		target = link_data[target]
	else:
		target = target+'.html'
	return '"'+root+target+'"'

def download(target):
	return '"'+sk_root+'downloads/'+target+'"'