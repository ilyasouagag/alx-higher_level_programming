#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the node
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current = *head;
    listint_t *temp;

    temp = malloc(sizeof(listint_t));
    if (!temp)
        return (NULL);
    temp->n = number;
    temp->next = NULL;
    if (temp->n < (*head)->n || *head == NULL)
    {
        temp->next = *head;
        *head = temp;
        return (*head);
    }
    while (current != NULL)
    {
        if (temp->n < current->next->n || current->next == NULL)
        {
            temp->next = current->next;
            current->next = temp;
            return (current);
        }
        current = current->next;
    }
    return (NULL);
}
