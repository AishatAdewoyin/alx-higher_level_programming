#ifndef LISTS_H
#define LISTS_H

#include <stdbool.h>
#include <stdlib.h>

/* structure */
typedef struct listint_s listint_t;

struct listint_s
{
/* the integer */
  int n;
  /* pointer to the next node */
    struct listint_s *next;
};
/* the prints the element in the linked list */
size_t print_listint(const listint_t *h);

/* adds a new node at the beginning of a linked list */
listint_t *add_nodeint(listint_t **head, const int n);

/* frees linked list */
void free_listint(listint_t *head);

/* checks for cycle in a linked list  */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
