#! /usr/bin/env python3

from scss.namespace import Namespace
from scss.types import String
from scss import compiler
import glob
import os

scss_list = glob.glob("gnome-shell/*.scss")
print("\nSCSS_FILES:", scss_list)
for scss_path in scss_list:
	css_path = scss_path.replace("scss", "css")
	print("\nscss path:", scss_path)
	print("css path:", css_path)
	
	namespace = Namespace()
	namespace.set_variable("$variant", String("dark"))
	css_data = compiler.compile_file(scss_path, namespace=namespace)
	with open(css_path, "w") as css_file:
		css_file.write(css_data)

