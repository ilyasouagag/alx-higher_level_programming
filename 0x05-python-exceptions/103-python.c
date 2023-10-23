#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double vl = 0;
	char *arr = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	vl = ((PyFloatObject *)p)->ob_fval;
	arr = PyOS_double_to_string(vl, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  vl: %s\n", arr);
}
/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = 0, j = 0;
	char *arr = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	printf("  len: %zd\n", len);
	arr = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying arr: %s\n", arr);
	printf("  first %zd bytes:", len < 10 ? len + 1 : 10);
	while (j < len + 1 && j < 10)
	{
		printf(" %02hhx", arr[j]);
		j++;
	}
	printf("\n");
}
/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len = 0;
	PyObject *item;
	int j = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		len = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", len);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (j < len)
		{
			item = PyList_GET_ITEM(p, j);
			printf("Element %d: %s\n", j, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			j++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
