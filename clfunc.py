

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

