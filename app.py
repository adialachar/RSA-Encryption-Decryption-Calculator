from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)




#app = Flask(__name__)


@app.route("/")
def main():
	return render_template("homePage.html")


# p and q must be prime numbers that are relatively prime to each other, and cannot be the same numberr. Their product is n, which one part of the public key.

#the formula for phi n, or the totient function, is (p-1) (q-1), which is used to determine the secret key used to decrypt data.

#e, the other part of the public key, can be determined by finding a number coprime to phi n. d can be found use d e triple bar 1 mod ph n

#The public key is made up of two parts, n and e. Usually written as (n,e). The secret key is just he value calculated for d. 

#formula to encrpyt is 

#c = m^{(e)} mod n


#formula to decrypt is 

#m = c ^{(d)} mod n

# make an encryption class, make a decryption class, store the classes in the database. 
#EncryptionData.query.all()
#DecryptionData.query.all()
#remember everything is db.Column(db.Integer())



class EncryptionData:
	
	Sea = db.Column(db.Integer)
	
	Emm = db.Column(db.Integer)

	Enn = db.Column(db.Integer)

	Eee = db.Column(db.Integer)


class DecryptionData:

        Sea = db.Column(db.Integer)

        Pee = db.Column(db.Integer)

        Quu = db.Column(db.Integer)

        Eee = db.Column(db.Integer)
	
	Dee = db.Column(db.Integer)









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




@app.route('/initDB', methods = ['POST', 'GET'])
def initDB():
	
	if request.method == 'POST':
		results = request.form

	db.create_all()
	return render_template('initDB.html')


@app.route('/encryptData' , methods = ['POST', 'GET'])
def encrypt():


	#numbers = None
	if request.method == 'POST':
		numbers = request.form


	print(numbers)

	e = numbers.get('e', -1)
	m = number.get('m', -1)
	n = number.get('n' , -1)
	

	


	c = cal(e, m, n)

	ENC = EncryptionDdata(Sea = c, Emm = m, Enn = n, Eee = e)

	db.session.add(ENC)
	db.commit()


	return render_template('encryptData.html', c = c)


@app.route('/decryptData', methods = ['POST', 'GET'])
def decrypt():
	
	#number = None
	if request.method == 'POST':
		numbers = request.form


	print(numbers)



	c = numbers.get('c', -1)
	e = numbers.get('e', -1)
	p = numbers.get('p', -1)
	q = numbers.get('q', -1)

	if p == q:
		return render_template('p_q_coPrime_error.html')

	# if e is not coprime to phiN
		return render_template('e_phiN_coprime_error.html')




	n = p * q

	phiN = (p - 1) * (q - 1)


	#(d)(e) triple bar 1 mod phiN
	
	d = None
	m = None
	d = modinv(e, phiN)
	m = cal(d, c, phiN)

	DEC = DecryptionData(Sea = c, Pee = p, Quu = q, Ee = e, Dee = d)
	db.session.add(DEC)
	db.session.commit()	


	return render_template('decryptData.html' , m = m, d = d)

@app.route('/accessDB' , methods = ['POST', 'GET'])
def accessDB():
	
	if request.method == 'POST':
		results = request.form

	return render_template('displayDB.html')



if __name__ == "__main__":
	app.run()