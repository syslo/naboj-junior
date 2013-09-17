sk_root = "http://naboj-junior.fks.sk/"
orgs_root = "http://naboj-junior.fks.sk/orgs/"
cz_root = "http://naboj-junior.fks.sk/cz/"
root = orgs_root
link_data = {
	"uvod": "index",
}

def link(target):
	if target in link_data:
		target = link_data[target]
	return '"'+root+target+'.html"'