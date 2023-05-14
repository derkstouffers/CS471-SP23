/*  Deric Shaffer
    CS471 - PA1
    Due Date: Feb. 7th, 2023

    Inputs: Integer array consisting of 4 byte ascii values in each position
    Outputs: Prints out the integer array that was cast as a char*
*/

#include <stdio.h>

#define SIZE 100
#define INT_SIZE 256

// pre: int array consisting of 4 byte ascii values in each position
// post: prints out name that was made by casting the integer array as a char*
int main(){
    // variables
    int arr[SIZE];
    char* s;
    
    // fill int array with values
    // Deri
    arr[0] = 'D' + INT_SIZE * ('e' + INT_SIZE * ('r' + (INT_SIZE * 'i')));

    // c Sh
    arr[1] = 'c' + INT_SIZE * (' ' + INT_SIZE * ('S' + (INT_SIZE * 'h')));

    // affe
    arr[2] = 'a' + INT_SIZE * ('f' + INT_SIZE * ('f' + (INT_SIZE * 'e')));

    // r.
    arr[3] = 'r' + (INT_SIZE * '.') ;
    
    // end character
    arr[4] = 0;

    // cast int array to char*
    s = (char*) &arr;

    // print out my name
    printf("My name is %s\n", s);
}// end of main