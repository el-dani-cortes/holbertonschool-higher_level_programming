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
	listint_t *tmp;
	listint_t *advance;
	listint_t *new_node;

	tmp = *head;
	advance = (*head)->next;
	while (tmp && advance)
	{
		if (number > tmp->n && number < advance->n)
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
				return (NULL);
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
