import socket


outputfile = open("out.txt", "w")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('misc.chal.csaw.io',4239))
s.recv(76)

for a in range(1000):
	print("\n" + str(a) + "\n")
	num = 0
	bitsin = s.recv(11)
	s.recv(1)
	print(bitsin)
	intarry = map(int, bitsin);
	intarry = intarry[1:10]
	for i in intarry:
		num = i + num

	if ((num%2) == 1):
		s.send("0")

	else:
		s.send("1")
		outstring = "".join(map(str, intarry[:-1]))
		outputfile.write(outstring)
		outputfile.write("\n")
	

