#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - print info about python
 * @p: pyobject list object
 */
void print_python_list(PyObject *p)
{
	int i;
	long int len = PyList_Size(p);

	PyListObject *object = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", object->allocated);
	for (i = 0; i < len; i++)
		type = object->ob_item[i]->ob_type->tp_name;
	printf("Element %i: %s\n", i, type);
	if (strcmp(type, "bytes") == 0)
		print_python_bytes(object->ob_item[i]);
}
/**
 * print_python_bytes - prints info about python
 * @p: pyobject byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("{.} bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p->ob_size));
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size);
	for (i = 0; < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
