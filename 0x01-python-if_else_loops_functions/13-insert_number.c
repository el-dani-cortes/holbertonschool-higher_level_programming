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
	listint_t *tmp, *advance, *new_node;

	if ((*head) == NULL)
		return (NULL);
	tmp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if ((*head)->next == NULL)
	{
		new_node->n = number;
		if ((*head)->n > number)
		{
			new_node->next = *head;
			*head = new_node;
		}
		else
		{
			new_node->next = NULL;
			(*head)->next = new_node;
		}
		return (new_node);
	}
	advance = (*head)->next;
	while (tmp && advance)
	{
		if (number > tmp->n && number < advance->n)
		{
			new_node->next = advance;
			new_node->n = number;
			tmp->next = new_node;
			return (new_node);
		}
		tmp = tmp->next;
		advance = advance->next;
	}
	return (NULL);
}
