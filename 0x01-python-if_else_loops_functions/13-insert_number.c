#include "lists.h"

/**
 * insert_node - inserts num into list
 * @head: list ptr
 * @number: adds number
 * Return: added node addr else nothing
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *old, *new, *current;

  if (head == NULL)
    return (NULL);

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;
  old = NULL;
  current = *head;

  for (; current != NULL && current->n < number;)
    {
      old = current;
      current = current->next;
    }

  new->next = current;

  if (old != NULL)
    old->next = new;
  else
    *head = new;

  return (new);
}
