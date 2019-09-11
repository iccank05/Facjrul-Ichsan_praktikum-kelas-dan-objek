class KelilingLingkaran(object) :
	def __init__ (self, r, p) :
		self.jarijari = r
		self.phi = p
	def hitungKeliling (self) :
		return 2 * self.phi * self.jarijari
	def cetakData (self) :
		print ("jari-jari\t: ", self.jarijari)
		print ("phi\t: ", self.phi)
	def cetakKeliling (self) :
		print ("Keliling\ t= ", self.hitungKeliling())

def main():

	KLingkaran1 = KelilingLingkaran (45,3.14)
	print ("objek Lingkaran1")
	KLingkaran1.cetakData () 
	KLingkaran1.cetakKeliling ()


	KLingkaran2 = KelilingLingkaran (49,22/7)
	print ("\nobjek Lingkaran2")
	KLingkaran2.cetakData ()
	KLingkaran2.cetakKeliling ()

if __name__ == "__main__":
	main () 

class LuasLingkaran(object) :
	def __init__(self, r, p) :
		self.jarijari = r
		self.phi = p
	def hitungLuas (self) :
		return self.phi * self.jarijari * self.jarijari
	def cetakData (self) :
		print ("jari-jari\t:", self.jarijari)
		print ("phi\t: ", self.phi)
	def cetakLuas (self) :
		print ("luas\t= ", self.hitungLuas())

def main():

	LLingkaran1 = LuasLingkaran(17,3.14)
	print ("objek Lingkaran")
	LLingkaran1.cetakData () 
	LLingkaran1.cetakLuas ()


	LLingkaran2 = LuasLingkaran(31,22/7)
	print("\nobjek Lingkaran2")
	LLingkaran2.cetakData ()
	LLingkaran2.cetakLuas ()

if __name__ == "__main__":
	main () 