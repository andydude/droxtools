use v6;
use Test;
use C::StdC11Parser;
plan 1;

my $source = q:to<EOS>;
  int main() {
      return 0;
  }
EOS

my $match = C::StdC11Parser.parse($source);

# 1
isa_ok $match, 'Match', 'Match object returned';

# 2
#ok $match<translation-unit><external-declaration>[0]<function-definition><compound-statement><block-item-list>[0]<block-item><statement><jump-statement><expression>.Str eq '0', 'The function-definition's statement returns zero';


