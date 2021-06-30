/**
    Swordfish - 00:28:55
    
    Source:
      - http://www.foo.be/docs-free/eff-des-cracker/cracker-source/5/search.c
      - https://people.eecs.berkeley.edu/~daw/papers/hwkeysearch96-www/chap-10_local.html
*/

long ReadConfig(char *configFilespec) {
  char buffer[200];
  int basePort = -1;
  int board, chip, unit, i;
  int lastBoard = -1, lastChip = -1;
  long totalUnits = 0;
  CHIP_CTX *cp;
  FILE *fp;
  cp = CHIP_ARRAY;
