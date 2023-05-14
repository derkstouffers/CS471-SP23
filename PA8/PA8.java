/*
 *  Deric Shaffer
 *  CS471 - PA8
 *  Due Date - April 26th, 2023
 *  Purpose - Convert a Grade Distribution program made in ADA into Java, and properly
 *      get the exception handling to be the only thing updated the values in the freq array based on 
 *      user inputted values.
 */

import java.util.Scanner;

public class PA8 {
    public static int[] freq = new int[11];
    public static int new_grade, index, limit1, limit2;
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // fill freq array with 0's at each index
        for (int i = 0; i < freq.length; i++)
            freq[i] = 0;

        while (true) {
            new_grade = scan.nextInt();

            // if number entered is a negative number, no longer take input
            if (new_grade < 0)
                break;
            
            index = (new_grade / 10) + 1;

            try {
               if (new_grade >= 0) 
                throw new Exception();
            } catch (Exception e) {
                if (new_grade == 100)
                    freq[10]++;
                else if (new_grade < 100)
                    freq[index]++;
                else
                    System.out.println("Error -- New Grade: " + new_grade + " is out of range");
            }
        }
        
        System.out.printf("%n%-10s\t%s%n%n", "Limits", "Frequency");

        for(int i = 0; i <= 9; i++){
            limit1 = 10 * i;
            limit2 = limit1 + 9;

            if(i == 9)
                limit2 = 100;
            
            System.out.printf("%-10s\t%5d%n", limit1 + "-" + limit2, freq[i + 1]);
        }
        
        scan.close();
        
    }// end of main
}// end of class