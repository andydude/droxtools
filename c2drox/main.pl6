use v6;
use C::StdC11Parser;
use DROX::DROXActions;
my $filename = @*ARGS[0];
my $source = '';
if ($filename eq '-') {
    $source = slurp($*IN);
} else {
    $source = slurp($filename);
}

my $actions = DROX::DROXActions.new();
my $match = C::StdC11Parser.parse($source, :$actions);
say $match.ast;
