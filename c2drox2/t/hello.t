use v6;
use Test;
use C::StdC11Parser;
plan 3;

my $source = q:to<EOS>;
  int puts(const char *s);
  int main() {
      puts("Hello World");
      return 0;
  }
EOS

my $match = C::StdC11Parser.parse($source);

# 1
isa_ok $match, 'Match', 'Match object returned';

# 2
ok $match<translation-unit><external-declaration>[0]<declaration><init-declarator-list>[0]<init-declarator><declarator><direct-declarator><direct-declarator-first><ident>.Str eq 'puts', 'First part is declaration';

# 3
ok $match<translation-unit><external-declaration>[1]<function-definition><compound-statement><block-item-list>[0]<block-item>[1]<statement><jump-statement><expression>.Str eq '0', 'Second part is function-definition';




