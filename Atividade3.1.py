PI = 3.141592
raio = float(input(""))
circunferencia = 2* PI * raio
a_circulo = PI * raio ** 2
a_esfera = 4 * PI * raio ** 2
vol_esfera = 4/3 * PI * raio ** 3
circunferencia_r = format(circunferencia,'.6f')
circulo_l = format(a_circulo,'.6f')
esfera_e = format(a_esfera,'.6f')
vol_esfera_s = format(vol_esfera,'.6f')
print(circunferencia_r)
print(circulo_l)
print(esfera_e)
print(vol_esfera_s)
