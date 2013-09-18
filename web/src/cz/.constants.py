import roots as r
sk_root = r.sk_root
cz_root = r.cz_root
orgs_root = r.orgs_root
del r

root = cz_root
link_data = {
	"uvod": "index",
	"akopomoct": "akopomoct/index",
	"onaboji": "onaboji/index"
}

def link(target):
	if target in link_data:
		target = link_data[target]
	return '"'+root+target+'.html"'