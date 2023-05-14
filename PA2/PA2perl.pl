# Deric Shaffer
# CS471 - PA2
# Due Date: Feb. 21st, 2023

# short circuit function (subroutine = function in Perl)
sub check{
    print "I have been evaluated";
    return 1;
}

# variable declaration and initialization
$i = 1;

# if statement to determine if there is short circuit evaluation in this language
if($i eq 0 && check()){
    print "True";
}else{
    print "False";
}