#include <stdio.h>

int main()
{
    char buffer[10]; /* Fixed size buffer */

    printf("Enter a word or any character: ")

    /* scanf() function is an unsafe input handling can overwrite adjacent memory when 
    the user input exceeds the allocated buffer size.
    This function does not check input length
    It writes beyong the allocated memory

    Secure alternalive

    use:

    scanf("%9s", buffer) or fgets(buffer,sizeof(buffer), stdin)

    */
    scanf("%s", buffer);

    printf("Your input is: %s\n", buffer);

    return 0;
}