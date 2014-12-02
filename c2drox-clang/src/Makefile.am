AM_CFLAGS = @CFLAGS@
AM_LDFLAGS = @LDFLAGS@ -rpath @prefix@

bin_PROGRAMS = clang2drox

clang2drox_SOURCES = \
	visitor.c \
	emit.c \
	main.c

noinst_HEADERS = \
	visitor.h \
	emit.h
