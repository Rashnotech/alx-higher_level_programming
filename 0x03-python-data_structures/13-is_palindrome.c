#include "lists.h"
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: a struct node pointer
 * Return: an integer 0 if it's not a palindrome otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *next, *prev;

	slow = fast = *head;
	next = prev = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast)
		slow = slow->next;
	while (slow && prev)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}
	return (1);
}
