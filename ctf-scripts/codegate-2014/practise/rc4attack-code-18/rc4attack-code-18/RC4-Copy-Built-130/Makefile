CC=gcc
INCDIR= -I./include/  -I./include/meschach/
CFLAGS= -m32 -c -Wall -std=c99 $(INCDIR)
INTRDIR=./intr
SRCDIR=./src
EXEDIR=./bin
DLL_DIR=./dll
DLL_NAME=$(DLL_DIR)/RC4.so
LIB_FILE=RC4.a
LFLAGS= -lm -m32
POST_FLAGS=  meschach.a
SOURCES=xalloc.c list.c hashtable.c RC4.c algo.c attack.c determinant.c
EXE_SRCS= hashtable_test.c main.c RC4test.c
OBJECTS=$(addprefix $(INTRDIR)/,$(SOURCES:.c=.o)) 
#OBJECTSFORRUN=$(addprefix $(INTRDIR)/,$(OBJECTS))
EXECUTABLE=$(EXEDIR)/attack.exe


all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) $(INTRDIR)/main.o
	$(CC) -m32 -o $@ $(OBJECTS) $(INTRDIR)/main.o $(POST_FLAGS) $(LFLAGS)

$(DLL_NAME): dll
so: dll
lib: dll
dll: $(OBJECTS)
	#ar rcs $(DLL_DIR)/$(LIB_FILE) $(OBJECTS)
	$(CC) -shared -o $(DLL_DIR)/RC4.so $(OBJECTS) $(POST_FLAGS)

$(INTRDIR)/%.o : $(SRCDIR)/%.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm $(INTRDIR)/* $(EXEDIR)/* $(DLL_DIR)/*
	