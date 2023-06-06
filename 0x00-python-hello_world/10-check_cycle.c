#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list
 * Return: true if the list has a cycle, otherwise false
 */
bool check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (list == NULL)
                return (false);

        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (true);
        }

        return (false);
}

