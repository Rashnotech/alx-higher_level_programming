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
	PyObject *item, *itemString;
	const char *itemValue;

	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %d\n", length);
	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		itemString = PyObject_Str(item);
		itemValue = PyUnicode_AsUTF8(itemString);
		printf("Element %d: %s\n", i, itemValue);
		Py_DECREF(itemString);
	}
}
