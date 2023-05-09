#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;
	listint_t *prev;

	curr = list;
	prev = list;
	while (list && curr && curr->next)
	{
		list = list->next;
		curr = curr->next->next;

		if (list == curr)
		{
			list = prev;
			prev =  curr;
			while (1)
			{
				curr = prev;
				while (curr->next != list && curr->next != prev)
				{
					curr = curr->next;
				}
				if (curr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
