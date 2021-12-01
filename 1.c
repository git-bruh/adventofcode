#include <stdio.h>

int main() {
  int prev = -1;
  int num = 0;
  int c = EOF;

  int larger = 0;

  for (;;) {
    c = getchar();

    if (c == '\n' || c == EOF) {
      if (prev != -1 && num > prev) {
        larger++;
      }

      prev = num;
      num = 0;

      if (c == '\n') {
        continue;
      }

      /* EOF */
      break;
    }

    num = (num * 10) + (c - '0');
  }

  printf("Larger: %d\n", larger);
}
