#include <stdio.h>
#include <cs50.h>

int main(void)

{
    printf("Hello, World!\n");

    string question = get_string("What is your name? ");
    printf("Hello, %s!\n", question);
    
    for (int i = 0; i < 3; i++) {
        printf("Hi!\n");
    }
}