from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)




#app = Flask(__name__)


@app.route("/")
def main():
	return render_template("newHomePage.html")


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





@app.route('/initDB', methods = ['POST', 'GET'])
def initDB():
	
	if request.method == 'POST':
		results = request.form

	db.create_all()
	return render_template('initDB.html')


@app.route('/encryptData' , methods = ['POST', 'GET'])
def encrypt():


	#numbers = None
	#if request.method == 'POST':
	#	numbers = request.form


	#print(numbers)

	#e = numbers.get('e', -1)
	#m = number.get('m', -1)
	#n = number.get('n' , -1)
	

	


	#c = cal(e, m, n)

	#ENC = EncryptionDdata(Sea = c, Emm = m, Enn = n, Eee = e)

	#db.session.add(ENC)
	#db.commit()


	return render_template('encryptData.html')


@app.route('/decryptData', methods = ['POST', 'GET'])
def decrypt():
	
	number = None
	if request.method == 'POST':
		numbers = request.form


	print(numbers)



	c = numbers.get('c', -1)
	e = numbers.get('e', -1)
	p = numbers.get('p', -1)
	q = numbers.get('q', -1)

	if p == q:
		return render_template('p_q_coPrime_error.html')

	 #if e is not coprime to phiN
	#	return render_template('e_phiN_coprime_error.html')




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


	return render_template('decryptData.html', DEC = DEC)

@app.route('/accessDB' , methods = ['POST', 'GET'])
def accessDB():
	
	if request.method == 'POST':
		results = request.form

	return render_template('displayDB.html')



if __name__ == "__main__":
	app.run()
