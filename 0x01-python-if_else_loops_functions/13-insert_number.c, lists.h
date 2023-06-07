#include <stdlib.h>

/**
 * struct listint_s - linked list
 * @n: int
 * @next: pointer to nxt node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * create_node - Create new node with given number
 * @number: num to store in new node
 *
 * Return: new node address, NULL if mem alloc failed
 */
listint_t *create_node(int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	return new_node;
}

/**
 * insert_node - Inserts new node to the given list
 * @head: Pointer to head of the linked list
 * @number: to be inserted
 *
 * Return: Address of new node, or NULL if me
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = create_node(number);

	if (new_node == NULL)
		return NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && number > current->next->n)
			current = current->next;

		new_node->next = current->next;
		current->next = new_node;
	}

	return new_node;
}
