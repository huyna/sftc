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

#include "list.h"
#include "xalloc.h"

list*
list_init()
{
	list *res=(list*)xmalloc(sizeof(list));
	if(res==NULL){
		return res;
	}
	res->head=NULL;
	res->tail=NULL;
	res->size=0;
	return res;
}

size_t
list_size(list *list)
{
	return list->size;
}

list_node *
list_head(list *list)
{
	return list->head;
}

list_node *
list_tail(list *list)
{
	return list->tail;
}

list_node *
list_add(list *list, void *data)
{
	return list_add_tail(list,data);
}

list_node *
list_add_head(list *list, void *data)
{
	list_node *_list_node;

	_list_node=(list_node*)xmalloc(sizeof(list_node));
	_list_node->data=data;
	_list_node->next=list->head;
	_list_node->prev=NULL;

	if (list->head == NULL)
		list->head=_list_node;
	else
		list->head->prev=_list_node;

	list->head=_list_node;

	list->size++;

	return _list_node;
}

list_node *
list_add_tail(list *list, void *data)
{
	list_node *_list_node;

	_list_node=(list_node*)xmalloc(sizeof(list_node));
	_list_node->data=data;
	_list_node->next=NULL;
	_list_node->prev=list->tail;

	if (list->head == NULL)
		list->head=_list_node;
	else
		list->tail->next=_list_node;

	list->tail=_list_node;

	list->size++;

	return _list_node;
}

list_node *list_add_after(list* l, list_node* node, void* data){
	list_node *_list_node;

	_list_node=(list_node*)xmalloc(sizeof(list_node));
	_list_node->data=data;
	_list_node->next=node->next;
	_list_node->prev=node;
	if(node==l->tail){
		l->tail=_list_node;
	}else{
		node->next->prev=_list_node;
	}
	node->next=_list_node;
	l->size++;

	return _list_node;
}

list_node *list_add_before(list* l, list_node* node , void* data){
	list_node *_list_node;

	_list_node=(list_node*)xmalloc(sizeof(list_node));
	_list_node->data=data;
	_list_node->next=node;
	_list_node->prev=node->prev;
	if(node==l->head){
		l->head=_list_node;
	}else{
		node->prev->next=_list_node;
	}
	node->prev=_list_node;
	l->size++;
	return _list_node;
}

void *
list_del(list *list, list_node *node)
{
	void *data;

	if (node->next != NULL)
		node->next->prev=node->prev;

	if (node->prev != NULL)
		node->prev->next=node->next;

	if (list->tail == node)
		list->tail=node->prev;

	if (list->head == node)
		list->head=node->next;

	list->size--;

	data=node->data;

	free(node);

	return data;
}

void
list_free(list *list, void (*callback)(void *))
{
	struct list_node *i;
	struct list_node *next;

	for (i=list_head(list); i != NULL; i=next)
	{
		if (callback != NULL)
			callback(i->data);

		next=i->next;

		free(i);
	}
}
