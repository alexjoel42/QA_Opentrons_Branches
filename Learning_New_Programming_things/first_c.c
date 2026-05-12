#include <stdio.h>

int main() { 
    // 1. Initialize variables
    int age = 0;
    float gpa = 0.0f;
    char grade = 'A'; 
    char name[30] = "Student";

    // 2. Get User Input
    printf("Enter your age: ");
    scanf("%d", &age); // & is the address-of operator, it tells scanf where to store the data

    // 3. Display Results
    printf("\n--- Results ---\n");
    printf("Age: %d\n", age);
    printf("GPA: %.2f\n", gpa); // %.2f limits output to 2 decimal places
    printf("Grade: %c\n", grade);
    printf("Name: %s\n", name);

    return 0; // The program ends here
}