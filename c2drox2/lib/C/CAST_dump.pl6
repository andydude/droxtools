use v6;
use C::StdC11Parser;
use C::StdC11Actions;

my $source = @*ARGS[0];
my $actions = C::StdC11Actions.new();
say C::StdC11Parser.parse($source, :$actions);
