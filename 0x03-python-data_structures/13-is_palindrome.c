#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * reverse - reverse a likned list
 * @head: pointer to first node
 * Return: pointer to new node
 */
void reverse(listint_t **head)
{
    listint_t *current = *head;
    listint_t *prev = NULL;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to adress of head
 * Return: return 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    listint_t *temp = *head;
    listint_t *link = *head;
    listint_t *rvs = NULL;
    int flag = 1;

    if (!(*head) || !(*head)->next)
        return (1);
    while (flag)
    {
        temp = temp->next->next;
        if (temp == NULL)
        {
            rvs = link->next;
            flag = 0;
        }
        if (temp->next == NULL)
        {
            rvs = link->next->next;
            flag = 0;
        }
        link = link->next;
    }
    reverse(&rvs);
    while (rvs != NULL && current != NULL)
    {
        if (current->n == rvs->n)
        {
            rvs = rvs->next;
            current = current->next;
        }
        else
            return (0);
    }
    if (rvs == NULL)
        return (1);
    return (0);
}
