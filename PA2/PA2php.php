<!-- 
    Deric Shaffer
    CS471 - PA2
    Due Date: Feb. 21st, 2023
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PA2 PHP Short Circuit Test</title>
</head>
<body>
    <!-- PHP short circuit evaluation -->
    <?php
        // short circuit function
        function check(){
            echo "I have been evaluated";
            return 1;
        }

        // variable declaration and initialization
        $i = 1;

        // if statement to determine if there is short circuit evaluation in this language
        if($i == 0 && check())
            echo "True";
        else
            echo "False";
    ?>
</body>
</html>