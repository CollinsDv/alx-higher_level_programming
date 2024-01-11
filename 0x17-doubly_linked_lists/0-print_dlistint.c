#include "lists.h"

/*
 * print_dlistint - prints elements of a linked list
 *
 * @h: head node pointer
 *
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *temp = NULL;
	size_t nodes = 0;

	if (!h)
		return (0);

	temp = h;
	while (temp)
	{
		printf("%d\n", temp->n);
		nodes++;
		temp = temp->next;
	}
	return (nodes);
}
