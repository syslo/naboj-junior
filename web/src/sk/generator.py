import re
import os
import shutil
import os.path
import posixpath
import codecs

_default_ext = "html"
_src_root = os.path.abspath(os.curdir)
_tar_root = os.path.abspath(os.curdir)
_searcher = re.compile("<!--#(.*?): (.*?)-->", re.M);
_compiled_path_data = {}
_translated_documents = {}
_queued_documents = {}
_to_move = {}

def _norm_path(path):
	return os.path.normcase(os.path.abspath(path))

def _compiled_path(path):
	if path in _compiled_path_data :
		return _compiled_path_data[path]
	else :
		i = 0
		while True:
			test = path + os.extsep + str(i)
			if not os.path.exists(test):
				_compiled_path_data[path] = test
				return test
			i=i+1


def _translate_document(path):
	if path not in _translated_documents:
		with codecs.open(path, 'r',"utf-8") as infile :
			with codecs.open(_compiled_path(path), 'w',"utf-8") as outfile :
				_translated_documents[path] = DocumentTranslator(infile, outfile, path)
				_translated_documents[path].translate()
	return _translated_documents[path]

def _clean():
	for path in _translated_documents:
		gen_path = _compiled_path_data[path]
		if path in _queued_documents:
			_to_move[gen_path] = _queued_documents[path]
	for path in _to_move:
		tar_path = _to_move[path]
		tar_path = os.path.join(_tar_root, os.path.relpath(tar_path,_src_root))
		try:
			os.makedirs(os.path.dirname(tar_path))
		except:
			pass
		shutil.copy(path,tar_path)
	for path in _translated_documents:
		gen_path = _compiled_path_data[path]
		os.remove(gen_path)

def enqueue(source_path, target_path = None):
	source_path = _norm_path(source_path)
	if target_path == None:
		target_path = os.path.splitext(source_path)[0]+os.extsep+_default_ext
	else:
		target_path = _norm_path(target_path)
	_queued_documents[source_path] = target_path

def include(source_path, target_path = None):
	source_path = _norm_path(source_path)
	if target_path == None:
		target_path = source_path
	else:
		target_path = _norm_path(target_path)
	_to_move[source_path] = target_path

def set_target_root(path):
	global _tar_root
	_tar_root = _norm_path(path)

def generate():
	for path in _queued_documents:
		_translate_document(path)
	_clean()
	_queued_documents.clear()


class DocumentTranslator:

	def __init__(self, source, target, source_path, data = {}):
		self.source = source
		self.target = target
		self.curdir, self.filename = os.path.split(os.path.abspath(source_path))
		self.data = data
		self.finished = False

	def _parseCommand(self, command, value):
		if command == "get":
			self.target.write(str(self.data[value]));

		if command == "let":
			try:
				exec(value , self.data);
			except:
				pass

		if command == "eval":
			try:
				self.target.write(str(eval(value , self.data)));
			except:
				pass

		if command == "include":
			path = self._normalise_include_path(value)
			self.data.update(
				_translate_document(path).data)
			self._write_file(_compiled_path(path))
			
		if command == "insert":
			path = self._normalise_include_path(value)
			self._write_file(path)

		if command == "template":
			path = self._normalise_include_path(value)
			with codecs.open(path, 'r', "utf-8") as infile :
				t = DocumentTranslator(infile, self.target, path, self.data)
				t.translate()

		if command == "python":
			path = self._normalise_include_path(value)
			with codecs.open(path, 'r', "utf-8") as infile :
				try:
					exec(infile.read() , self.data);
				except Exception as e:
					print(str(e))
		
	def _write_file(self, path):
		with codecs.open(path, 'r', "utf-8") as infile :
			for line in infile :
				self.target.write(line)


	def translate(self):
		if self.finished:
			return
		self.run_line = 0;
		for line in self.source:
			last = 0;
			for match in _searcher.finditer(line):
				self.target.write(line[last:match.start()])
				last = match.end()
				self._parseCommand(match.group(1),match.group(2))
			self.target.write(line[last:])
			self.run_line = self.run_line+1
		self.finished = True

	def _split_path(self, path, pathmodule):
		result = []
		while path:
			path, name = pathmodule.split(path)
			result.append(name)
			if name == "":
				result.append(path)
				break
		result.reverse()
		return result

	def _normalise_include_path(self, path):
		splited = self._split_path(path, posixpath)
		if posixpath.isabs(path):
			return _norm_path(os.path.join(_src_root, *(splited[1:])))
		else:
			return _norm_path(os.path.join(self.curdir, *splited))




