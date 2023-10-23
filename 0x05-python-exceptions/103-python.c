#include <Python.h>
#include <stdio.h>

void print_python_float(PyObject *p) {
    double value = 0;

    fflush(stdout);
    printf("[.] Float object info\n");

    if (PyFloat_CheckExact(p)) {
        value = PyFloat_AsDouble(p);
        printf("  value: %f\n", value);
    } else {
        printf("  [ERROR] Invalid Float Object\n");
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] Bytes object info\n");

    if (PyBytes_CheckExact(p)) {
        size = PyBytes_Size(p);
        printf("  size: %zd\n", size);
        
        string = PyBytes_AsString(p);
        printf("  trying string: %s\n", string);
        
        printf("  first %zd bytes:", size < 10 ? size : 10);
        for (Py_ssize_t i = 0; i < size && i < 10; i++) {
            printf(" %02hhx", string[i]);
        }
        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_list(PyObject *p) {
    Py_ssize_t size = 0;
    int i = 0;

    fflush(stdout);
    printf("[*] Python list info\n");

    if (PyList_CheckExact(p)) {
        size = PyList_GET_SIZE(p);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        while (i < size) {
            PyObject *item = PyList_GET_ITEM(p, i);
            printf("Element %d: %s\n", i, item->ob_type->tp_name);

            if (PyBytes_Check(item)) {
                print_python_bytes(item);
            } else if (PyFloat_Check(item)) {
                print_python_float(item);
            }

            i++;
        }
    } else {
        printf("  [ERROR] Invalid List Object\n");
    }
}
