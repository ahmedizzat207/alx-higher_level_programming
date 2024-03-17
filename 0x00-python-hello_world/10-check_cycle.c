#include "lists.h"


/**
 * check_cycle - The funciton checks a singly linked list for any cycles in it
 * @list: a pointer to certain position in the list to start of (usually the
 * list head)
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *check;
	unsigned int currcount, checkcount;

	for (current = list, currcount = 1; current; currcount++)
	{
		for (check = list, checkcount = 0; checkcount < currcount; checkcount++)
		{
			if (check == current->next)
				return (1);
			check = check->next;
		}
		current = current->next;
	}
	return (0);
}
