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
#ifndef XALLOC_H_
#define XALLOC_H_
#include <stdlib.h>

extern void xalloc_set_error_func(void (*)(void));
extern void xmemerror(void);
extern void *xmalloc(size_t);
extern void *xcalloc(size_t, size_t);
extern void *xrealloc(void *, size_t);
//extern char *xstrdup(const char *);

#endif /*xalloc.h included*/
