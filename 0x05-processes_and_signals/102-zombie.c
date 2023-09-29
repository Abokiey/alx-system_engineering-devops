#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - Creates an infinite loop to 
 * make the program hang.
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Creates 5 zombie processes from the parent process.
 * Return: (0)
 */
int main(void)
{
	pid_t pid;
	char i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i++;
	}
	else
		exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
