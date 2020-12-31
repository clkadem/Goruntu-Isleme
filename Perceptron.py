import numpy as np

class Perceptron(object):
    """"Implements a perceptron network"""
    def __init__(self, input_size, lr=1, epochs=10):
        self.W = np.zeros(input_size+1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr

    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    def fit(self, x, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                y = self.predict(x[i])
                e = d[i]-y
                self.W = self.W + self.lr * e * np.insert(x[i], 0, 1)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
d = np.array([0,0,0,1])
perceptron = Perceptron(input_size=2)
perceptron.W
print(perceptron.fit(X,d))
print(perceptron.W)

print(perceptron.predict(np.asarray([1,1])))

mp = Perceptron(5)
print(mp.W)
x = np.asarray([-10, -2, -30, 4, -50])
print(mp.predict(x))
print(mp.activation_fn(-10))

# Soru - 1
# ----- _init_ -----
# Ağırlık vektörü oluşturuyoruz.
# Öğrenme oranını ve dönem sayısını giriyoruz.

# ----- Activation_fn -----
# fonksiyonu gelen değer 0'dan büyük veya eşitse 1,
# eşit değil ve küçük ise 0 döndürür.

# ----- Predict -----
# Geleneksel olarak buna tahmin denir.
# Algılayıcı aracılığıyla bir girdi çalıştırmak ve bir çıkktı döndürmek
# içim ihtiyacımız olan işlevdir.
# İç çarpımı hesaplayıp activation_fn foksiyonunu uyguluyoruz.

# ----- Fit -----
# Birkaç dönem için ağırlıkları güncellemeye devam ediyoruz ve
# tüm eğitim setine uyguluyoruz. Ağırlık güncellemesini
# gerçekleştirirken girişe bias ekliyoruz.


# Soru - 2
# ----- XOR -----
# X = np.array([ [0,0], [0,1], [1,0], [1,1] ])
# d = np.array([0,1,1,0])
# print(X) - >> array([[0, 0], [0, 1], [1, 0], [1, 1]])
# print(d) ->> array([0, 1, 1, 0])
# perceptron = Perceptron(input_size=2)
# perceptron.W ->> array([0., 0., 0.])
# perceptron.fit(X,d)
# perceptron.W --> array([ 0., -1., 0.])
# print(perceptron.W) ->> [ 0. -1. 0.]
#
# burada birden fazla perceptron.predict(np.asarray([x,y]) denemesi sonuçları
# yer almaktadır
# perceptron.predict(np.asarray([0,0])) --> 1
# perceptron.predict(np.asarray([1,0])) --> 0
# perceptron.predict(np.asarray([0,1])) --> 1
# perceptron.predict(np.asarray([1,1])) --> 0
#
# Gözlem:
# Bu sonuçlardan anlaşıldığı üzere XOR işlemi yapıldığında predict
# sonuçlarımız doğru outputları vermedi. Bunun sebebi ise Algılayıcıların
# sınırlamasından kaynaklanmaktadır, yalnızca doğrusal ayrılabilen sorunları
# çözebilmektedirler. XOR ise doğrusal olarak ayrılamadığından tek katmanlı
# algılayıcıları xor kapısı için kullanamayız.