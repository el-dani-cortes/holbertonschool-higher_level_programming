#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of linked list
 * @number: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *advance = NULL, *new_node = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	tmp = *head;
	if (!tmp)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	if (tmp->n > number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	advance = (*head)->next;
	while (advance && number > advance->n)
	{
		tmp = tmp->next;
		advance = advance->next;
	}
	new_node->next = advance;
	tmp->next = new_node;
	return (new_node);
}
