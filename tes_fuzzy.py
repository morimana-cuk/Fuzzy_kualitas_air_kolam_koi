import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

##deklarasi batas batas nilai 
ph = ctrl.Antecedent(np.arange(0.0, 15.0, 0.1), 'ph')
suhu = ctrl.Antecedent(np.arange(9.0, 33.0, 0.1), 'suhu')
do = ctrl.Antecedent(np.arange(1.0, 11.0, 0.1), 'do')

##deklarasi kualitas air
kualitas_air = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'kualitas_air')


##deklarasi ph
ph['asam'] = fuzz.trimf(ph.universe, [0.0, 0.0, 7.0])
ph['netral'] = fuzz.trimf(ph.universe, [6.0, 7.0, 8.0])
ph['basa'] = fuzz.trimf(ph.universe, [7.0, 14.0, 14.0])

##deklarasi suhu
suhu['dingin'] = fuzz.trimf(suhu.universe, [9.0, 20.0, 25.0])
suhu['normal'] = fuzz.trimf(suhu.universe, [20.0, 25.0, 30.0])
suhu['panas'] = fuzz.trimf(suhu.universe, [25.0, 30.0, 30.0])

##deklarasi do
do['rendah'] = fuzz.trimf(do.universe, [3.0, 5.0, 6.0])
do['normal'] = fuzz.trimf(do.universe, [5.0, 6.0, 7.0])
do['tinggi'] = fuzz.trimf(do.universe, [7.0, 10, 10])

# Plotting Grafik untuk PH
# ph.view()

# Plotting Grafik untuk Suhu
# suhu.view()

# # # Plotting Grafik untuk DO
# do.view()

# # Menampilkan semua grafik
# plt.show()

## Deklarasi kualitas air
kualitas_air['bagus'] = fuzz.trimf(kualitas_air.universe, [0, 0, 0.5])
kualitas_air['buruk'] = fuzz.trimf(kualitas_air.universe, [0.5, 1, 1])

rule1 = ctrl.Rule(ph['netral'] & suhu['normal'] & do['tinggi'], kualitas_air['bagus'])
rule2 = ctrl.Rule(ph['basa'] & suhu['panas'] & do['normal'], kualitas_air['buruk'])
rule3 = ctrl.Rule(ph['asam'] & suhu['dingin'] & do['rendah'], kualitas_air['buruk'])


kualitas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
kualitas = ctrl.ControlSystemSimulation(kualitas_ctrl)

kualitas.input['ph'] = 7.5
kualitas.input['suhu'] = 25
kualitas.input['do'] = 9

kualitas.compute()


kualitas_nilai = kualitas.output['kualitas_air']
print(kualitas.output['kualitas_air'])

# Menampilkan output dan label
print(f"Nilai Kualitas Air: {kualitas_nilai:.4f}")

kualitas_bulat = round(kualitas_nilai)
print(kualitas_bulat)

# Menentukan label
if kualitas_nilai < 0.5:
    label = "Bagus"
else:
    label = "Buruk"

print(f"Kualitas Air: {label}")

# Menentukan label
if kualitas_bulat == 0:
    label2 = "Bagus"
else:
    label2 = "Buruk"

print(f"Kualitas Air dengna nilai yang di bulatkan: {label2}")