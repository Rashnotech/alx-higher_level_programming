#include <Python.h>
/**
 * print_python_bytes - Print a basic info about bytes obj
 * @p: PyBytesObject pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, length;
	PyBytesObject *list = (PyBytesObject *)p;
	char *str;

	if (PyBytes_Check(p))
	{
		length = PyBytes_Size(p);
		bytes = length + 1;

		if (bytes > 10)
			bytes = 10;
		str = list->ob_sval;
		printf("[.] bytes object info\n");
		printf(" size: %ld\n", size);
		printf(" trying string: %s\n", str);
		printf(" first %ld bytes: ", bytes);
		for (i = 0; i < bytes - 1; i++)
			printf("%02x ", (unsigned char) list->ob_sval[i]);
		printf("%02x\n", list->ob_sval[i]);
	}
	else
		printf(" [ERROR] Invalid Bytes Object\n");
}
