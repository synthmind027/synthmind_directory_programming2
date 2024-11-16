

dpl = list() # directorial programming language
cwd = 0


root_dir = {'_nm': 'root', '.': 0, '..':0, '_chld':dict(), '_dat':'', '_exec':''}
dpl.append(root_dir)


def new_dir(dds, idx_par, nm): # directory data structure: dpl
	idx_new = len(dds)
	dds[idx_par]['_chld'][nm] = idx_new 
	dpl.append({'_nm': nm, '.': idx_new, '..': idx_par, '_chld': dict(), '_dat': '', '_exec':''})
	

def path(dds, pth):
	idx = 0
	for nm in path.split('/'):
		if nm not in dds[idx]:
			new_dir(dds, idx, nm)
		idx = dds[idx]['_chld'][nm]	

def root_string(dds, idx):
	pth = list()
	while idx != 0:
		pth.append(dds[idx]['_nm'])
		idx = dds[idx]['..']
	return '/'+'/'.join(pth[::-1])

def ls(dds, idx):
	print(f'[DIR] {root_string(dds,idx)}')
	print(f'[DAT] {dds[idx]['_dat']}')
	print(f'[CHLD]')
	for x in dds[idx]['_chld']:
		print(f'{x}:{dds[dds[idx]['_chld'][x]]['_dat']}')