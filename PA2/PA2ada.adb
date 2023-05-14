-- Deric Shaffer
-- CS471 - PA2
-- Due Date: Feb. 21st, 2023  

with Ada.Text_IO; 
use Ada.Text_IO;

procedure PA2ada is
    --  variable declaration and initialization
    i : Integer := 1;

    --  function used to check short circuit
    function check return Boolean is
    begin
        Put_Line("I have been evaluated");
        return true;
    end check;

--  if statement to determine if there is short circuit evaluation in this language
begin
    if i = 0 and check then
        Put_Line("True");
    else
        Put_Line("False");
    end if;

end PA2ada;