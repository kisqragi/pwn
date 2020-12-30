#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<setjmp.h>

jmp_buf buffer;

void set_buffer_internal() {
	setjmp(buffer);
}

void set_buffer() {
	char tmp[0x200];
	set_buffer_internal();
}

void jump_buffer() {
	longjmp(buffer, 1);
}

void hello() {
	char name[0x250];
	printf("name at %p\n", name); 
	read(0, name, 0x250 - 1);
	name[0x250 - 1] = 0;
	
	printf("Hello %s\n", name);
}

void menu() {
	puts("1: Set buffer");
	puts("2: Jump buffer");
	puts("3: Hello");

}

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
	alarm(60);

	while(1) {
		int opt;
		menu();
		printf("Enter option:");
		scanf("%d%*c", &opt); 
		switch(opt) {
			case 1: {
				set_buffer();
				break;
			}
			case 2: {
				jump_buffer();
				break;
			}
			case 3: {
				hello();
				break;
			}
			default: {
				exit(0);
			}
		}

	}
}

