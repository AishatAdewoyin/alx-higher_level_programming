#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - linked list
 * @n: int
 * @next: points to next node
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
listint_t *create_node(int number);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
