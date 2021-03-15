/*
Silicon Valley - s03e01
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

//ToneverDo change name
u64 HammingCtr(u64 a, u64 b) {
  u64 c = a ^ b;
  
  /*for (d = 0; c>0; c >>= 1)
  {
    d += c & 1;
  }*/
