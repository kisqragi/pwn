#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/mman.h>

typedef union {
	char* char_ptr;
	int* int_ptr;
	long* long_ptr;
	void (*func_ptr)();
} SuperType;

int menu() {
	printf(
			"0: As char*, allocate\n"
			"1: As char*, printf\n"
			"2: As char*, input\n"
			"3: As int*, printf\n"
			"4: As long*, printf\n"
			"5: As func_ptr, execute\n"
		);
	printf("What do you do? :");
	int ret;
	scanf("%d%*c", &ret);

	return ret;
}

int main() {
	// set up for CTF
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  alarm(60);

	SuperType st;

	while(1) {
		int opt = menu();
		switch(opt) {
			case 0: {
				st.char_ptr = mmap(NULL, 0x1000, PROT_EXEC | PROT_WRITE | PROT_READ, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
				break;
			}
			case 1: {
				puts(st.char_ptr);
				break;
			}
			case 2: {
				fgets(st.char_ptr, 0x100, stdin);
				break;
			}
			case 3: {
				for(int i = 0;i < 0x100 / sizeof(int);i++) {
					printf("%d: %d\n", i, st.int_ptr[i]);
				}
				break;
			}
			case 4: {
				for(int i = 0;i < 0x100 / sizeof(long);i++) {
					printf("%d: %ld\n", i, st.long_ptr[i]);
				}
				break;
			}
			case 5: {
				st.func_ptr();
			}
		}
	}
}


