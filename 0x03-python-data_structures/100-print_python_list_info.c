#include <lists.h>

/**
 * print_python_list_info - function that prints
 * info about  python list
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size, m;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (m = 0; m < size; m++)
	{
		item = PyList_GetItem(p, m);
		printf("Element %ld: %s\n", m, Py_TYPE(item)->tp_name);
	}
}
