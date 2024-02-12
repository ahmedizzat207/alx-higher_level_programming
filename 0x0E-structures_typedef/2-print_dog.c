#include <stdio.h>
#include "dog.h"

/**
 * print_dog - The function prints a struct dog
 * @d: a pointer to a sturcture named dog
 */

void print_dog(struct dog *d)
{
	if (d != NULL)
	{
		if ((*d).name != NULL)
			printf("Name: %s\n", (*d).name);
		else
			printf("Name: (nil)\n");
		if ((*d).owner != NULL)
			printf("Owner: %s\n", (*d).owner);
		else
			printf("Owner: (nil)\n");
		if ((*d).age != NULL)
			printf("Age: %f\n", (*d).age);
		else
			printf("Age: (nil)\n");
	}
}