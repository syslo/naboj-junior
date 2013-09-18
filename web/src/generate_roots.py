import os
import os.path
import posixpath
import shutil

def _split_path(path):
	result = []
	while path:
		path, name = os.path.split(path)
		result.append(name)
		if name == "":
			result.append(path)
			break
	result.reverse()
	return result

root = posixpath.join(*_split_path(os.path.abspath(os.path.join(os.pardir,"www"))))
sk_root = posixpath.join(root,"")
orgs_root = posixpath.join(root,"orgs","")
cz_root = posixpath.join(root,"cz","")

f = open("roots.py","w")
f.write("sk_root = '"+sk_root+"'\n")
f.write("cz_root = '"+cz_root+"'\n")
f.write("orgs_root = '"+orgs_root+"'\n")
f.close()

shutil.copy("roots.py",os.path.join("sk","roots.py"))
shutil.copy("roots.py",os.path.join("cz","roots.py"))
shutil.copy("roots.py",os.path.join("orgs","roots.py"))

os.remove("roots.py")