/*
 *  GPL
 *
 *  Written by Diogo Sousa aka orium
 *  Copyright (C) 2008 Diogo Sousa
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef LIST_H_
#define LIST_H_

#include <stddef.h>

typedef struct list_node
{
	void *data;

	struct list_node *next;
	struct list_node *prev;
} list_node;

typedef struct list
{
	struct list_node *head;
	struct list_node *tail;

	size_t size;
} list;

extern list* list_init();
extern size_t list_size(list *);

extern list_node *list_head(list *);
extern list_node *list_tail(list *);

extern list_node *list_add(list *, void *);
extern list_node *list_add_head(list *, void *);
extern list_node *list_add_tail(list *, void *);
extern list_node *list_add_after(list* l, list_node*, void*);
extern list_node *list_add_before(list* l, list_node*, void*);

extern void *list_del(list *, list_node *);

extern void list_free(list *, void (*callback)(void *));

#define list_node_data(list_node,type) (*((type *)(list_node)->data))
#define list_node_data_ptr(list_node,type) ((type *)(list_node)->data)
#define list_node_next(list_node) ((list_node)->next)
#define list_node_prev(list_node) ((list_node)->prev)

#endif
