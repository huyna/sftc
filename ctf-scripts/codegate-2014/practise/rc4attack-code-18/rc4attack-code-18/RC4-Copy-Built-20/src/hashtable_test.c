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

#include <stdio.h>
#include "hashtable.h"

struct integer
{
        int n;
        char *english;
};

uint32_t jenkins_one_at_a_time_hash(void *data, size_t key_len)
{
	struct integer *myint=data;
	void *key=&myint->n;
	uint32_t hash=0;
	size_t i;

	/* We don't use the key_len arg */
	key_len=sizeof(myint->n);

	for (i=0; i < key_len; i++)
	{
		hash+=*((BYTE *)key+i);
		hash+=hash<<10;
		hash^=hash>>6;
	}

	hash+=hash<<3;
	hash^=hash>>11;
	hash+=hash<<15;

	return hash;
}

bool cmp(void *p1, void *p2)
{
	struct integer *i1=p1;
	struct integer *i2=p2;

	return i1->n == i2->n;
}

void my_walk_action(void *data)
{
	struct integer *i=data;

	printf("%d: %s\n",i->n,i->english);
}

int main(void)
{
	struct hash_table table;
	struct integer i1={1,"one"};
	struct integer i2={2,"two"};
	struct integer i3={3,"three"};
	struct integer i4={4,"four"};
	struct integer i5={5,"five"};
	struct integer *lost_i5;

	hash_table_init(&table,32,jenkins_one_at_a_time_hash,cmp);

	hash_table_insert(&table,&i1,0);
	hash_table_insert(&table,&i2,0);
	hash_table_insert(&table,&i3,0);
	hash_table_insert(&table,&i4,0);
	hash_table_insert(&table,&i5,0);

	lost_i5=hash_table_search(&table,&i5,0);

	printf("%d: %s\n",lost_i5->n,lost_i5->english);

	hash_table_delete(&table,&i5,0);

	lost_i5=hash_table_search(&table,&i5,0);

	hash_table_walk(&table,my_walk_action);

	hash_table_free(&table,NULL);

	return 0;
}
