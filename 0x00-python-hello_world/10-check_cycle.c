#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if there is a cycle in linked list
 * @list: pointer to linked list
 * Return: retrun 0 if there is cycle, otherwiwse 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
