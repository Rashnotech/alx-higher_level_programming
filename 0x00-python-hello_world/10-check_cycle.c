#include "lists.h"
/**
 * check_cycle - checked if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: an integer value 0 otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
