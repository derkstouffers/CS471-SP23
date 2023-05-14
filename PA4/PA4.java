/* 
 * Deric Shaffer
 * CS471 - PA4
 * Due Date: March 22nd, 2023
 * Purpose: Remove corrupted data from a file and return a cleaned/updated new file in Java
*/

import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;

public class PA4{
    public static void main(String[] args){
        // CONTROL-B and CONTROL-C ASCII values
        char control_b = 2;
        char control_c = 3;

        // indicator variable starter CONTROL-C
        boolean flag = false;

        try{
            // variables
            FileReader original = new FileReader("control-char.txt");
            FileWriter updated = new FileWriter("java-out.txt");
            Scanner scan = new Scanner(original);
            String line;

            while(scan.hasNext()){
                line = scan.nextLine();

                for(int i = 0; i < line.length(); i++){
                    // when the first/starting CONTROL-C is found, update flag
                    if(line.charAt(i) == control_c && flag == false)
                        flag = true;
                    
                    // when the ending CONTROL-B is found, update flag and skip/continue to not write it to new file
                    if(line.charAt(i) == control_b && flag == true){
                        flag = false;
                        continue;
                    }
                    
                    // character in line is not part of the corrupted data, write to new/updated file
                    if(flag == false)
                        updated.write(line.charAt(i));
                }// end of for

                // add \n to updated file
                if(flag == false)
                    updated.write("\n");
            }// end of while

            // close Scanner and FileWriter used for updated file
            scan.close();
            updated.close();

            // Confirmation Print Statement
            System.out.println("Data Removal is Done");
        }catch(Exception e){
            e.getStackTrace();
        }// end of try/catch
    }// end of main
}// end of class