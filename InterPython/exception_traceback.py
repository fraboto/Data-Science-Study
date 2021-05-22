# This file is to understand the way Python raise and manage uncontrolled exceptions. 
# The order to read the comments on each function is to start by function3 where the exception is generated in the first place.


def run():
    # Here we have the same scenario as function1 and function2, 
    # so the exception is raised to the module's entrypoint where run was called.
    function1()


def function1():
    # Here we have the same scenario as fucntion2, 
    # so the exception is raised to function run where function1 was called.
    function2()


def function2():
    # Here, as no exception is controlled, when the exception is raised, 
    # it is raised again to function1 where function2 was called
    function3() 


def function3():
    # Here the Exception is generated. As it is not controlled, Python starts to raise it,
    # until it is controlled or the first called function is reached. 
    # So the exception is raised to function2 where function3 was called.
    exception_coe = 1 / 0 


if __name__ == '__main__':
    # Finally, here is where Python finish the code execution and raise the exception traceback to the console.
    run()