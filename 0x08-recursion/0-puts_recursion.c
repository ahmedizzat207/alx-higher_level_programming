#include "main.h"
#include <stdio.h>

/**
 * _puts_recursion - print a string, followed by a newline
 * @s: the string to be printed
 *
 */

void _puts_recursion(char *s)
{
	if (*s == '\0')
	{
		putchar('\n');
	}
	else
	{
		putchar(*s);
		_puts_recursion(s + 1);
	}
}
