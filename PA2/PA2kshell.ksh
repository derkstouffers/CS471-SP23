# Deric Shaffer
# CS471 - PA2
# Due Date: Feb. 21st, 2023

#!/bin/ksh

# short circuit function
check(){
    echo "I have been evaluated"
    return 1
}

# variable declaration and initialization
i = 1

# if statement to determine if there is short circuit evaluation in this language
if [$i -eq 0] && check; then
    echo "True"
else
    echo "False"
fi