#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print a basic information
 * about python List
 * @p: Python List object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, length = PyList_Size(p);
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	int alloc = list->allocated;
	const char *itemValue;

	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		itemValue = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, itemValue);
	}
}
