/*
 *  GPL
 *
 *  Written by Diogo Sousa aka orium
 *  Copyright (C) 2007 Diogo Sousa
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
#include <stdlib.h>
#include <string.h>

void xalloc_set_error_func(void (*f)(void));
void xmemerror(void);
void *xmalloc(size_t size);
void *xcalloc(size_t nmemb, size_t size);
void *xrealloc(void *ptr, size_t size);
char *xstrdup(const char *s);

static void (*mem_error_func)(void)=xmemerror;

void xalloc_set_error_func(void (*f)(void))
{
        mem_error_func=f;
}

void xmemerror(void)
{
        fprintf(stderr,"Erro na alocação de memória\n");
        exit(EXIT_FAILURE);
}

void *xmalloc(size_t size)
{
        void *r;

        r=malloc(size);

        if (r == NULL)
                mem_error_func();

        return r;
}

void *xcalloc(size_t nmemb, size_t size)
{
        void *r;

        r=calloc(nmemb,size);

        if (r == NULL)
                mem_error_func();

        return r;
}

void *xrealloc(void *ptr, size_t size)
{
        void *r;

        r=realloc(ptr,size);

        if (r == NULL)
                mem_error_func();

        return r;
}
/*
char *xstrdup(const char *s)
{
        char *r;

        r=strdup(s);

        if (r == NULL)
                mem_error_func();

        return r;
}
*/
