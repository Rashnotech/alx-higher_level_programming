#include "lists.h"
/**
 * insert_node - Insert a number into a sorted linked list
 * @head: node pointer of list
 * @number: an integer value
 * Return: a new node of list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *cur, *prev;

	cur = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	while (cur->next && cur->n < number)
	{
		prev = cur;
		cur = cur->next;
	}
	prev->next = new;
	new->next = cur;
	return (head);

}
