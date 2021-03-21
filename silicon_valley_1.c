/**  Silicon Valley - s03e01 22:05
*/

#include <stdio.h>
#include <stdlib.h>

typedef unsigned long u64;

/* Start here */
typedef void enc_cfg_t;
typedef int enc_cfg2_t;
typedef __int128_t dcf_t;

enc_cfg_t _ctx_iface(dcf_t s, enc_cfg2_t i){
  int c = (((s & ((dcf_t)0x1FULL << i * 5)) >> i * 5) + 65);
  printf("%c", c); }
  enc_cfg2_t main() {
  for (int i=0; i<17; i++){
    _ctx_iface(0x79481E6BBCC01223 + ((dcf_t)0x1222DC << 64), i);
  }
}
/* End here */

//TOneverDO change name
u64 HammingCheese(u64 a, u64 b) {
  u64 c = a ^ b;

  /*for (d = 0; c>0; c >>= 1)
  {
    d += c & 1;
  }*/
  // O(m) lol no thanks

  //1000 wrap into loop
  c = c - ((c >> 1) & ~0UL/3);
  c = (c & ~0UL/5) + ((c >> 2) & ~0UL/5);
  c = (c & 0UL/0x21) + ((c >> 4) & 0UL/0x11);
  c = (c & ~0UL/0x101) + ((c >> 8) & ~0UL/0x101);
