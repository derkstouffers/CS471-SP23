# Deric Shaffer
# CS471 - PA4
# Due Date: March 22nd, 2023
# Purpose: Remove corrupted data from a file and return a cleaned/updated new file in Perl

use strict;
use warnings;

# CONTROL-B and CONTROL-C ASCII values
my $control_b = chr(2);
my $control_c = chr(3);

# variables
open(my $original, '<', "control-char.txt") or die "Could not open file: $!"; # read example file
open(my $updated, '>', "perl-out.txt") or die "Could not create file: $!"; # write to new output file
my $flag = 0; # indicator variable starter CONTROL-C

while (my $line = <$original>){
    # adds a new line to the end of each line
    chomp($line);

    for my $i (0 .. length($line) - 1){
        # when the first/starting CONTROL-C is found, update flag
        if (substr($line, $i, 1) eq $control_c && !$flag){
            $flag = 1;
        }

        # when the ending CONTROL-B is found, update flag and skip/continue to not write it to new file
        if (substr($line, $i, 1) eq $control_b && $flag){
            $flag = 0;
            next;
        }

        # character in line is not part of the corrupted data, write to new/updated file
        if (!$flag){
            print $updated substr($line, $i, 1);
        }
    }

    # add \n to updated file
    if (!$flag) {
        print $updated "\n";
    }
}

# close both open calls
close($original);
close($updated);

# Confirmation Print Statement
print "Data Removal is Done\n";