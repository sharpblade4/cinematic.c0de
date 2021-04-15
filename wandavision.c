/*
  WandaVision s01e06 25:11
  
  Source: 
    - https://github.com/torvalds/linux/commit/30639b6af85a92491b22dd14c17b14ca11da60e6#diff-1512c1aba152e691ee057b387bf535d86bba869a70ce7974ef9fe5ebe0118f1c
    - https://hackertyper.net
*/

struct group_info init_groups = { .usage = ATOMIC_INIT(2) };

struct group_info *groups_alloc(int gidsetsize)
{
	struct group_info *group_info;
	int nblocks;
	int i;

	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
	/* Make sure we always allocate at least one indirect block pointer */
	nblocks = nblocks ? : 1;
	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
	if (!group_info)
		return NULL;
	group_info->ngroups = gidsetsize;
	group_info->nblocks = nblocks;
  
  / / / DATABASE ACCESS ROUTINE / / / / 
