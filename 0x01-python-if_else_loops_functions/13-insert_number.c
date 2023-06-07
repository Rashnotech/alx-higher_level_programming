#include "lists.h"

/**
 * tranverse - Find the index of the found value
 * @node: linkded list
 * @number: value to check
 * Return: an integer value (index)
 */
int tranverse(listint_t *node, int number)
{
	int index = 0;
	while (node && node->n < number)
	{
		index++;
		node = node->next;
	}
	return (index);
}

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
	int index, i;

	cur = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		index = tranverse(*head, number);
		for (i = 0; i < index - 1; i++)
			*head = *head->next;
		prev->next = new;
		new->next = cur->next;
	}
	return (new);

}
