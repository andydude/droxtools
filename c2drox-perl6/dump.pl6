#!PERL6LIB=lib perl6 
use v6;
use Grammar::Debugger;
use C::StdC11Parser;
my $filename = @*ARGS[0];
my $source = '';
if ($filename eq '-') {
    $source = slurp($*IN);
} else {
    $source = slurp($filename);
}

say C::StdC11Parser.parse($source);
