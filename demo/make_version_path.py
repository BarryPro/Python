import os
import shutil

def make_version_path(path,version):
	if version == 0:
		return path
	else:
		path+"."+str(version)
def rotate(path,version = 0):
	old_path = make_version_path(path,version)
	if not os.path.exists(old_path):
		raise IOError("'%s' doesn't exists" %path)
	new_path = make_version_path(path,version+1)
	if os.path.exists(new_path):
		rotate(path,version+1)
	shutil.move(old_path,new_path)
