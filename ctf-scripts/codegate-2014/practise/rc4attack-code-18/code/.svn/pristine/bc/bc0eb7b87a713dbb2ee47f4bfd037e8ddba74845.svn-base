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

#ifndef HASHTABLE_H_
#define HASHTABLE_H_
#include "debug.h"

#define HASH_TABLE_DEBUG __DEBUG

#include <stdint.h>
#include <sys/types.h>
#include <stdbool.h>
#include "list.h"

#define DEFAULT_RESIZE_LOAD 0.75
#define DEFAULT_AFTER_RESIZE_LOAD 0.40

struct hash_element
{
	void *data;
	uint32_t hash;

	struct hash_table *hash_table;
};

struct hash_entry
{
	void *tree; /* Tree of struct hash_element */

	int count; /* Elements in the tree */
};

struct hash_table
{
	struct hash_entry **table;

	size_t size;
	size_t used;

	float resize_load; /* Resize table when load reach this */
	float after_resize_load; /* Load after resize */

	uint32_t (*hash_fun)(void *, size_t);
	int (*cmp_fun)(const void *, const void *);

	void *foo;
	list del_list;
};

extern void hash_table_init(struct hash_table *, size_t,
			    uint32_t (*)(void *, size_t),
			    int (*)(const void *, const void *));
extern void hash_table_set_resize_load(struct hash_table *, float);
extern void hash_table_set_load_after_resize(struct hash_table *, float);
extern int hash_table_get_size(struct hash_table *);
extern int hash_table_get_used(struct hash_table *);
extern int hash_table_get_collisions(struct hash_table *);
extern float hash_table_get_load(struct hash_table *);
extern float hash_table_get_collision_rate(struct hash_table *);
extern void hash_table_insert(struct hash_table *, void *, size_t);
extern void *hash_table_search(struct hash_table *, void *, size_t);
extern int hash_table_delete(struct hash_table *, void *, size_t);
extern void hash_table_walk(struct hash_table *, void (*)(void *));
extern void hash_table_free(struct hash_table *, void (*)(void *));
extern void hash_table_print_info(struct hash_table *);

#if HASH_TABLE_DEBUG
extern void hash_table_assert_integrity(struct hash_table *);
#endif

#endif
