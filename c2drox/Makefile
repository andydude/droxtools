.PHONY: all build test install clean distclean purge

PERL6  = perl6-m
DESTDIR= 
PREFIX = /Users/ajr/.local/opt/nqp/install/languages/perl6/site
BLIB   = blib
P6LIB  = $(PWD)/$(BLIB)/lib:$(PWD)/lib:$(PERL6LIB)
CP     = cp -p
MKDIR  = mkdir -p


BLIB_COMPILED = $(BLIB)/lib/C/CAST.moarvm $(BLIB)/lib/C/CAST_dump.pl6 $(BLIB)/lib/C/StdC11Actions.moarvm $(BLIB)/lib/C/StdC11Lexer.moarvm $(BLIB)/lib/C/StdC11Parser.moarvm $(BLIB)/lib/DROX/DROXActions.moarvm

all build: $(BLIB_COMPILED)

$(BLIB)/lib/C/CAST.moarvm : lib/C/CAST.pm6
	$(MKDIR) $(BLIB)/lib/C/
	$(CP) lib/C/CAST.pm6 $(BLIB)/lib/C/CAST.pm6
	PERL6LIB=$(P6LIB) $(PERL6) --target=mbc --output=$(BLIB)/lib/C/CAST.moarvm lib/C/CAST.pm6

$(BLIB)/lib/C/CAST_dump.pl6 : lib/C/CAST_dump.pl6 $(BLIB)/lib/C/StdC11Parser.moarvm $(BLIB)/lib/C/StdC11Actions.moarvm
	$(MKDIR) $(BLIB)/lib/C/
	$(CP) lib/C/CAST_dump.pl6 $(BLIB)/lib/C/CAST_dump.pl6
	PERL6LIB=$(P6LIB) $(PERL6) --target=mbc --output=$(BLIB)/lib/C/CAST_dump.pl6 lib/C/CAST_dump.pl6

$(BLIB)/lib/C/StdC11Actions.moarvm : lib/C/StdC11Actions.pm6 $(BLIB)/lib/C/CAST.moarvm
	$(MKDIR) $(BLIB)/lib/C/
	$(CP) lib/C/StdC11Actions.pm6 $(BLIB)/lib/C/StdC11Actions.pm6
	PERL6LIB=$(P6LIB) $(PERL6) --target=mbc --output=$(BLIB)/lib/C/StdC11Actions.moarvm lib/C/StdC11Actions.pm6

$(BLIB)/lib/C/StdC11Lexer.moarvm : lib/C/StdC11Lexer.pm6
	$(MKDIR) $(BLIB)/lib/C/
	$(CP) lib/C/StdC11Lexer.pm6 $(BLIB)/lib/C/StdC11Lexer.pm6
	PERL6LIB=$(P6LIB) $(PERL6) --target=mbc --output=$(BLIB)/lib/C/StdC11Lexer.moarvm lib/C/StdC11Lexer.pm6

$(BLIB)/lib/C/StdC11Parser.moarvm : lib/C/StdC11Parser.pm6 $(BLIB)/lib/C/StdC11Lexer.moarvm
	$(MKDIR) $(BLIB)/lib/C/
	$(CP) lib/C/StdC11Parser.pm6 $(BLIB)/lib/C/StdC11Parser.pm6
	PERL6LIB=$(P6LIB) $(PERL6) --target=mbc --output=$(BLIB)/lib/C/StdC11Parser.moarvm lib/C/StdC11Parser.pm6

$(BLIB)/lib/DROX/DROXActions.moarvm : lib/DROX/DROXActions.pm6
	$(MKDIR) $(BLIB)/lib/DROX/
	$(CP) lib/DROX/DROXActions.pm6 $(BLIB)/lib/DROX/DROXActions.pm6
	PERL6LIB=$(P6LIB) $(PERL6) --target=mbc --output=$(BLIB)/lib/DROX/DROXActions.moarvm lib/DROX/DROXActions.pm6


test: build
	env PERL6LIB=$(P6LIB) prove -e '$(PERL6)' -r t/

loudtest: build
	env PERL6LIB=$(P6LIB) prove -ve '$(PERL6)' -r t/

timetest: build
	env PERL6LIB=$(P6LIB) PERL6_TEST_TIMES=1 prove -ve '$(PERL6)' -r t/

install: $(BLIB_COMPILED)
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) $(BLIB)/lib/C/CAST.pm6 $(DESTDIR)$(PREFIX)/lib/C/CAST.pm6
	$(CP) $(BLIB)/lib/C/CAST.moarvm $(DESTDIR)$(PREFIX)/lib/C/CAST.moarvm
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) $(BLIB)/lib/C/CAST_dump.pl6 $(DESTDIR)$(PREFIX)/lib/C/CAST_dump.pl6
	$(CP) $(BLIB)/lib/C/CAST_dump.pl6 $(DESTDIR)$(PREFIX)/lib/C/CAST_dump.pl6
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) $(BLIB)/lib/C/StdC11Actions.pm6 $(DESTDIR)$(PREFIX)/lib/C/StdC11Actions.pm6
	$(CP) $(BLIB)/lib/C/StdC11Actions.moarvm $(DESTDIR)$(PREFIX)/lib/C/StdC11Actions.moarvm
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) $(BLIB)/lib/C/StdC11Lexer.pm6 $(DESTDIR)$(PREFIX)/lib/C/StdC11Lexer.pm6
	$(CP) $(BLIB)/lib/C/StdC11Lexer.moarvm $(DESTDIR)$(PREFIX)/lib/C/StdC11Lexer.moarvm
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) $(BLIB)/lib/C/StdC11Parser.pm6 $(DESTDIR)$(PREFIX)/lib/C/StdC11Parser.pm6
	$(CP) $(BLIB)/lib/C/StdC11Parser.moarvm $(DESTDIR)$(PREFIX)/lib/C/StdC11Parser.moarvm
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/DROX/
	$(CP) $(BLIB)/lib/DROX/DROXActions.pm6 $(DESTDIR)$(PREFIX)/lib/DROX/DROXActions.pm6
	$(CP) $(BLIB)/lib/DROX/DROXActions.moarvm $(DESTDIR)$(PREFIX)/lib/DROX/DROXActions.moarvm
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) lib/C/CAST.pm6 $(DESTDIR)$(PREFIX)/lib/C/
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) lib/C/CAST_dump.pl6 $(DESTDIR)$(PREFIX)/lib/C/
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) lib/C/StdC11Actions.pm6 $(DESTDIR)$(PREFIX)/lib/C/
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) lib/C/StdC11Lexer.pm6 $(DESTDIR)$(PREFIX)/lib/C/
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/C/
	$(CP) lib/C/StdC11Parser.pm6 $(DESTDIR)$(PREFIX)/lib/C/
	$(MKDIR) $(DESTDIR)$(PREFIX)/lib/DROX/
	$(CP) lib/DROX/DROXActions.pm6 $(DESTDIR)$(PREFIX)/lib/DROX/


clean:
	rm -fr $(BLIB)

distclean purge: clean
	rm -r Makefile
