/*
This is how you write a comment in C, yippie 

what is stdio.h? It is a header file that contains functions for input and output, such as printf and scanf.
What are alternatives? 
- iostream: This is a C++ header file that contains functions for input and output, such as cout and cin.
- conio.h: This is a C header file that contains functions for console input and output, such as getch and clrscr. It is not part of the C standard library and
    is not available on all platforms.
- stdlib.h: This is a C header file that contains functions for memory allocation, process control, conversions, and other utilities. It does not contain functions for input and output, but it is often used in conjunction with stdio.h for tasks such as dynamic memory management and program termination.
- string.h: This is a C header file that contains functions for manipulating strings, such as strlen and strcpy. It does not contain functions for input and output, but it is often used in conjunction with stdio.h for tasks such as reading and writing strings to files or the console.
*/

# include <stdio.h>

int main()
{
    printf("Hello, this is a C program that uses stdio.h in order to print this message to the console.\n");
    // why would we return 0? 
    // In C, the main function is expected to return an integer value that indicates the success or failure of the program.
    // By convention, returning 0 indicates that the program executed successfully without any errors
    // Returning a non-zero value typically indicates that an error occurred during execution.
    //  The specific non-zero value can be used to indicate different types of errors,
    //  allowing other programs or scripts that call this program to understand what went wrong.
    return 1;
}