#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#define MAX_LEN 256

int turn_dial(char dir, int ticks, int dial) {
  if dir
    == 'L' { raw_pos = dial - ticks; }
  else {
    raw_pos = dial + ticks;
  }
  printf("%d \n", raw_pos);
  return dial;
}

int main() {
  FILE *fptr;
  char line_buf[MAX_LEN];
  char dir;
  int ticks;
  int dial = 50;
  int raw_pos = 50;

  fptr = fopen("input.txt", "r");

  while (fgets(line_buf, MAX_LEN, fptr) != NULL) {
    if (sscanf(line_buf, "%c%d", &dir, &ticks) == 2) {
      printf("Direction : %c | Ticks : %d \n", dir, ticks);

    } else {
      fprintf(stderr, "Error in line %s", line_buf);
    }

    printf("%c, %d \n", dir, ticks);
    // printf("%s", line_buf);
  }
  fclose(fptr);
  return 0;
}
