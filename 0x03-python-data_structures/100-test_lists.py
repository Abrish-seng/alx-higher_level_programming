import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
ll = ['hello', 'World']
lib.print_python_list_info(ll)
del ll[1]
lib.print_python_list_info(ll)
ll = ll + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(ll)
m = []
lib.print_python_list_info(m)
m.append(0)
lib.print_python_list_info(m)
m.append(1)
m.append(2)
m.append(3)
m.append(4)
lib.print_python_list_info(m)
m.pop()
lib.print_python_list_info(m)
