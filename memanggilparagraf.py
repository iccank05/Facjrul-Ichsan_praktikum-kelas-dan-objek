class MyFile(object):
	def __init__ (self, namafile):
		print("Membuka file %s... \n" % namafile)
		self.file = open(namafile)
	def __del__(self):
		print("\nMenutup file...")
		self.file.close()
	def bacadata (self):
		for baris in self.file:
			print(baris, end="")

def main():
	f = MyFile("D:/Teknik Komputer/Semester 3/Pemrograman lanjut/memanggilparagraf.txt")
	f.bacadata()
if __name__=="__main__":
	main()