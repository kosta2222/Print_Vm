from vm_print import b_c, console, vm_proc_print
import numpy as np

gl=4
console()


def main_x():

    a=7
    l=[1,2,3,4]
    vm_proc_print(b_c,locals(),globals())
def func():
     k=9
     a1=np.zeros((2,7))
     l2=[1,5,7,9]
     vm_proc_print(b_c,locals(),globals())

vm_proc_print(b_c,locals(),globals())





main_x()
func()
