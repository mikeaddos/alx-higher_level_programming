#include <stdio.h>
#include <Python.h>
#include <string.h>
/**
 * print_python_string - function that Prints strings
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{

        PyObject *strg, *repr;

        (void)repr;
        printf("[.] string object info\n");

        if (strcmp(p->ob_type->tp_name, "strg"))
        {
                printf("  [ERROR] Invalid String Object\n");
                return;
        }

        if (PyUnicode_IS_COMPACT_ASCII(p))
                printf("  type: compact ascii\n");
        else
                printf("  type: compact unicode object\n");

        repr = PyObject_Repr(p);
        strg = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
        printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
        printf("  value: %s\n", PyBytes_AsString(strg));
}
