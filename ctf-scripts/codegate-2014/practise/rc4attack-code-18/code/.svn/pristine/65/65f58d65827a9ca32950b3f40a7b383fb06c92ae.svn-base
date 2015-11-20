
#include <stdio.h>
#include <stdlib.h>
#include <search.h>
#include <math.h>
#include "assert.h"
#include "xalloc.h"
#include "hashtable.h"

static void realloc_hash_table(struct hash_table *, size_t);
static void set_hash_table_empty(struct hash_table *, int, int);
static void set_hash_element(struct hash_table *, struct hash_element *);
static int hash_data_cmp(const void *, const void *);
static void hash_tree_walk(const void *, const VISIT, const int);
static void hash_tree_free_node(void *);
static struct hash_element *get_hash_element(struct hash_table *, void *,
					     size_t);
static void hash_tree_walk_table_resize(const void *, const VISIT, const int);
#if HASH_TABLE_DEBUG
static void hash_tree_walk_assert_integrity(const void *, const VISIT,
					    const int);
#endif
static void delete_elements_from_tree(struct hash_table *, void **);

static void
realloc_hash_table(struct hash_table *hash, size_t size)
{
	hash->table=(struct hash_entry**)xrealloc(hash->table,sizeof(*hash->table)*size);
	hash->size=size;

	DEBUG_PRINT("Resized hash to %d\n",size);
}

static void
set_hash_table_empty(struct hash_table *hash, int b, int e)
{
	for (; b <= e; b++)
		hash->table[b]=NULL;
}

void
hash_table_init(struct hash_table *hash, size_t size,
		uint32_t (*hash_fun)(void *, size_t),
		int (*cmp_fun)(const void *, const void *))
{
	hash->table=NULL;
	realloc_hash_table(hash,size);
	set_hash_table_empty(hash,0,hash->size-1);
	hash->used=0;
	hash->resize_load=DEFAULT_RESIZE_LOAD;
	hash->after_resize_load=DEFAULT_AFTER_RESIZE_LOAD;

	hash->hash_fun=hash_fun;
	hash->cmp_fun=cmp_fun;

	hash->foo=NULL;
}

void
hash_table_set_resize_load(struct hash_table *hash, float load)
{
	hash->resize_load=load;
}

void
hash_table_set_load_after_resize(struct hash_table *hash, float load)
{
	hash->after_resize_load=load;
}

int
hash_table_get_size(struct hash_table *hash)
{
	return (int)hash->size;
}

int
hash_table_get_collisions(struct hash_table *hash)
{
	int c=0;
	unsigned int i;

	for (i=0; i < hash->size; i++)
		if (hash->table[i] != NULL)
			c+=(hash->table[i]->count > 1) ?
				hash->table[i]->count : 0;

	return c;
}

float
hash_table_get_load(struct hash_table *hash)
{
	if (!hash->size)
		return 1.0;

	return (float)hash->used/(float)hash->size;
}

float
hash_table_get_collision_rate(struct hash_table *hash)
{
	if (!hash->used)
		return 0.0;

	return (float)hash_table_get_collisions(hash)/(float)hash->used;
}

int
hash_table_get_used(struct hash_table *hash)
{
	return (int)hash->used;
}

static int
hash_data_cmp(const void *p1, const void *p2)
{
	const struct hash_element *e1=(const struct hash_element*)p1;
	const struct hash_element *e2=(const struct hash_element*)p2;

	return e1->hash_table->cmp_fun(e1->data,e2->data);
}

static void
set_hash_element(struct hash_table *hash, struct hash_element *element)
{
	int p;

	p=element->hash%hash->size;

	if (hash->table[p] == NULL)
	{
		hash->table[p]=(struct hash_entry*)xmalloc(sizeof(*hash->table[p]));
		hash->table[p]->tree=NULL;
		hash->table[p]->count=0;
	}

	element->hash_table=hash;

	if (tsearch(element,&hash->table[p]->tree,hash_data_cmp) == NULL)
		xmemerror();

	hash->table[p]->count++;

	//DEBUG_PRINT("0x%x: hash %lu: Now in position %d\n",
	//     (unsigned int)element->data,(unsigned long)element->hash,p);

}

static void
hash_tree_walk_table_resize(const void *nodep, const VISIT which,
			    const int depth)
{
	if (which == postorder
	    || which == leaf)
	{
		struct hash_element *element;
		struct hash_table *hash;
		unsigned int p;

		element=*(struct hash_element **)nodep;
		hash=element->hash_table;
		p=*(int *)hash->foo;

		if (element->hash%hash->size != p)
		{
			list_add(&hash->del_list,element);

			set_hash_element(hash,element);
		}
	}
}

static void
delete_elements_from_tree(struct hash_table *hash, void **tree)
{
	list_node *i;

	for (i=list_head(&hash->del_list); i != NULL; i=list_node_next(i))
		tdelete(list_node_data_ptr(i,struct hash_element),tree,
			hash_data_cmp);
}

/* Takes O(N)
 */
int
hash_table_resize(struct hash_table *hash, float new_load)
{
	int i;
	int size;

	if (new_load < hash->resize_load)
		return -1;

	if (!hash_table_get_used(hash))
		return -1;

	while (hash->foo != NULL)
		;

	size=hash->size;

	realloc_hash_table(hash,(size_t)ceilf((float)hash->used/new_load));

	set_hash_table_empty(hash,size,hash->size-1);

	for (i=0; i < size; i++)
		if (hash->table[i] != NULL)
		{
			hash->foo=&i;

			list_init(&hash->del_list);

			twalk(hash->table[i]->tree,hash_tree_walk_table_resize);

			delete_elements_from_tree(hash,&hash->table[i]->tree);

			hash->table[i]->count-=list_size(&hash->del_list);

			list_free(&hash->del_list,NULL);

			if (hash->table[i]->tree == NULL)
			{
				free(hash->table[i]);
				hash->table[i]=NULL;
			}
		}

	hash->foo=NULL;

#if HASH_TABLE_DEBUG
	hash_table_assert_integrity(hash);
#endif

	return 0;
}

void
hash_table_insert(struct hash_table *hash, void *data, size_t size)
{
	struct hash_element *element;

	element=(struct hash_element*)xmalloc(sizeof(*element));

	element->data=data;

	element->hash=hash->hash_fun(data,size);

	set_hash_element(hash,element);

	hash->used++;

	if (hash->resize_load > 0.0
	    && hash_table_get_load(hash) >= hash->resize_load)
		hash_table_resize(hash,hash->resize_load);
}

static struct hash_element *
get_hash_element(struct hash_table *hash, void *needle, size_t size)
{
	int p;
	struct hash_element tree_needle;
	struct hash_element **found;

	p=hash->hash_fun(needle,size)%hash->size;

	if (hash->table[p] == NULL)
		return NULL;

	tree_needle.data=needle;
	tree_needle.hash_table=hash;

	found=(struct hash_element **)tfind(&tree_needle,&hash->table[p]->tree,
					    hash_data_cmp);

	return (found == NULL) ? NULL : *found;
}

void *
hash_table_search(struct hash_table *hash, void *needle, size_t size)
{
	struct hash_element *found;

	found=get_hash_element(hash,needle,size);

	return (found == NULL) ? NULL : found->data;
}

int
hash_table_delete(struct hash_table *hash, void *needle, size_t size)
{
	int p;
	struct hash_element tree_needle;
	struct hash_element *found;

	p=hash->hash_fun(needle,size)%hash->size;

	if (hash->table[p] == NULL)
		return -1;

	tree_needle.data=needle;
	tree_needle.hash_table=hash;

	found=get_hash_element(hash,needle,size);

	if (found == NULL)
		return -1;

	if (tdelete(&tree_needle,&hash->table[p]->tree,hash_data_cmp) == NULL)
		return -1;

	hash->table[p]->count--;
	hash->used--;

	free(found);

	if (hash->table[p]->tree == NULL)
	{
		assert(!hash->table[p]->count);
		free(hash->table[p]);
		hash->table[p]=NULL;
	}

#if HASH_TABLE_DEBUG
	hash_table_assert_integrity(hash);
#endif

	return 0;
}

static void
hash_tree_walk(const void *nodep, const VISIT which, const int depth)
{
	if (which == postorder || which == leaf)
	{
		const struct hash_element **node;
		void (*action)(void *);

		node=(const struct hash_element **)nodep;
		action=(void (*)(void*))(*node)->hash_table->foo;

		action((*node)->data);
	}
}

void
hash_table_walk(struct hash_table *hash, void (*action)(void *))
{
	unsigned int i;

	/* For thread safety */
	while (hash->foo != NULL)
		;

	hash->foo=(void*)action;

	for (i=0; i < hash->size; i++)
		if (hash->table[i] != NULL)
			twalk(hash->table[i]->tree,hash_tree_walk);

	hash->foo=NULL;
}

static void
hash_tree_free_node(void *node)
{
	struct hash_element *element=(struct hash_element*)node;
	void (*action)(void *)=(void (*)(void*))element->hash_table->foo;

	if (action != NULL)
		action(element->data);

	free(element);
}

void
hash_table_free(struct hash_table *hash, void (*action)(void *))
{
	unsigned int i;

	/* For thread safety */
	while (hash->foo != NULL)
		;

	hash->foo=(void*)action;

	for (i=0; i < hash->size; i++)
		if (hash->table[i] != NULL)
		{
			tdestroy(hash->table[i]->tree,hash_tree_free_node);
			free(hash->table[i]);
		}

	free(hash->table);
}

void
hash_table_print_info(struct hash_table *hash)
{
	int collisions;

	collisions=hash_table_get_collisions(hash);

	printf("Size:           %d\n",hash_table_get_size(hash));
	printf("Used:           %d\n",hash_table_get_used(hash));
	printf("Load:           %.3f\n",hash_table_get_load(hash));
	printf("Collisions:     %d\n",collisions);
	printf("Collision Rate: %.3f\n",(float)collisions/(float)hash->used);
}


#if HASH_TABLE_DEBUG

static void
hash_tree_walk_assert_integrity(const void *nodep, const VISIT which,
				const int depth)
{
	if (which == postorder || which == leaf)
	{
		const struct hash_element *element;

		element=*(const struct hash_element **)nodep;

		if ((int)(element->hash%element->hash_table->size) !=
		    *(int *)element->hash_table->foo)
		{
			fprintf(stderr,"HASH INTEGRITY TEST FAILD\n");
			abort();
		}
	}
}

void
hash_table_assert_integrity(struct hash_table *hash)
{
	unsigned int i;
	int used=0;

	/* For thread safety */
	while (hash->foo != NULL)
		;

	for (i=0; i < hash->size; i++)
		if (hash->table[i] != NULL)
		{
			hash->foo=&i;
			twalk(hash->table[i]->tree,
			      hash_tree_walk_assert_integrity);
			used+=hash->table[i]->count;
		}

	if (used != hash->used)
	{
		fprintf(stderr,"HASH INTEGRITY TEST FAILD\n");
		abort();
	}

	fprintf(stderr,"HASH OK\n");

	hash->foo=NULL;
}

#endif
