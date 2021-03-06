from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import primefac
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)








def cal (pow, val, MOD):
        if (pow == 0):
                return 1
        v = cal(pow/2, val, MOD)
        if (pow % 2 == 0):
                return (v * v) % MOD
        else:
                return (((v * val) % MOD) * v) % MOD


def egcd(a,b):
        if a == 0:
                return (b,0,1)

        g,y,x = egcd(b%a, a)
        return (g, x - (b//a) * y, y)

def modinv(a,m):
        g,x,y = egcd(a,m)
        if g is not 1:
                raise Exception('No moodular inverse')
        return (x % m)










class EncryptionData:

	Sea = db.Column(db.Integer)

        Emm = db.Column(db.Integer)

        Enn = db.Column(db.Integer)

        Eee = db.Column(db.Integer)

	def __init__(self, m, n, e):
		
		self.Emm = m
		self.Enn = n
		self.Eee = e

		#Calculating C
		self.Sea  = cal(int(e), int(m), int(n))
		print("Hi im in clfunc.py")
		print(self.Sea)
		print("Done")
	def getC():
		return Sea

	def getPublicKey():

		#(n, e)
		publicKey = [ Enn, Eee]
		return publicKey
	def isAllOk():
	
		if Sea > 0 and Emm > 0 and Enn > 0 and Eee > 0:
			return True

		return False

class DecryptionData:

        Sea = db.Column(db.Integer)

        Pee = db.Column(db.Integer)

        Quu = db.Column(db.Integer)

        Eee = db.Column(db.Integer)

        Dee = db.Column(db.Integer)

	Emm = db.Column(db.Integer)

	def __init__(self, p, q, e, c):

		self.Sea = c
		self.Pee = p
		self.Quu = q
		self.Eee = e
		

		n = int(p) * int(q)

		phiN = (int(p) - 1) * (int(q) - 1)


		#(d)(e) triple bar 1 mod phiN
	
		d = None
		m = None
		d = modinv(int(e), int(phiN))

		print (c)
		print (d)
		print(phiN)

		m = cal(int(d), int(c),int(n))

		self.Dee = d
		self.Emm = m

	
	def getPrivateKey():
		return Dee

	def getPublicKey():
		#(n,e)

		publicKey = [ ( Pee * Quu), Eee]

		return publicKey

	def isAllOk():
		
		if p != q and gcd(e, phiN) != 1 and (p > 0 and q > 0 and Sea > 0 and Eee >0):
			return True

		return False






		
		

		



