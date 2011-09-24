def path_memo(p, m, n):
	if p[n-1][m-1] == -1: 
		p[n-1][m-1] = path(m, n-1) + path(m-1, n)
	return p[n-1][m-1]

def path(m, n):
	p = [[-1 for col in range(m)] for row in range(n)]
#	for row in p: print row
	for i in range(n):
		p[i][0] = 1
	for j in range(m):
		p[0][j] = 1

	return path_memo(p, m, n)

if __name__ == '__main__':
	fin = open("./p1_input")
	fout = open("./p1_output", "w")
	for line in fin.readlines():
		if line.startswith("0"): break
		n = int(line.split()[0])
		m = int(line.split()[1])
		fout.write(str(path(m, n)))
		fout.write('\n')

	fin.close()
	fout.close()

