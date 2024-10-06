import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import random
##deklarasi batas batas nilai 
ph = ctrl.Antecedent(np.arange(0.0, 15.0, 0.1), 'ph')
suhu = ctrl.Antecedent(np.arange(0.0, 100.0, 0.1), 'suhu')
do = ctrl.Antecedent(np.arange(0.0, 11.0, 0.1), 'do')

##deklarasi kualitas air
kualitas_air = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'kualitas_air')


# ##deklarasi ph
# ph['asam'] = fuzz.trimf(ph.universe, [0.0, 0.0, 7.0])
# ph['netral'] = fuzz.trimf(ph.universe, [6.0, 7.0, 8.0])
# ph['basa'] = fuzz.trimf(ph.universe, [7.0, 14.0, 14.0])

ph['optimal'] = fuzz.trapmf(ph.universe, [7.0, 7.2, 7.4, 7.6])
ph['moderate'] = fuzz.trapmf(ph.universe, [6.5, 7.0, 7.6, 8.0])
ph['poor'] = fuzz.trapmf(ph.universe, [5.5, 6.0, 6.5, 7.0])
ph['very_poor'] = fuzz.trapmf(ph.universe, [0.0, 0.5, 5.5, 6.0])

# ##deklarasi suhu
# suhu['dingin'] = fuzz.trimf(suhu.universe, [9.0, 20.0, 25.0])
# suhu['normal'] = fuzz.trimf(suhu.universe, [20.0, 25.0, 30.0])
# suhu['panas'] = fuzz.trimf(suhu.universe, [25.0, 30.0, 30.0])

suhu['optimal'] = fuzz.trapmf(suhu.universe, [22.0, 23.0, 25.0, 26.0])
suhu['moderate'] = fuzz.trapmf(suhu.universe, [18.0, 22.0, 26.0, 28.0])
suhu['poor'] = fuzz.trapmf(suhu.universe, [14.0, 18.0, 28.0, 30.0])
suhu['very_poor'] = fuzz.trapmf(suhu.universe, [0.0, 10.0, 30.0, 40.0])

# ##deklarasi do
# do['rendah'] = fuzz.trimf(do.universe, [3.0, 5.0, 6.0])
# do['normal'] = fuzz.trimf(do.universe, [5.0, 6.0, 7.0])
# do['tinggi'] = fuzz.trimf(do.universe, [7.0, 10, 10])

do['optimal'] = fuzz.trapmf(do.universe, [6.0, 7.0, 9.0, 10.0])
do['moderate'] = fuzz.trapmf(do.universe, [4.0, 5.0, 7.0, 8.0])
do['poor'] = fuzz.trapmf(do.universe, [2.0, 3.0, 5.0, 6.0])
do['very_poor'] = fuzz.trapmf(do.universe, [0.0, 1.0, 3.0, 4.0])


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

rule1 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['optimal'], kualitas_air['bagus'])
rule2 = ctrl.Rule(ph['moderate'] & suhu['moderate'] & do['moderate'], kualitas_air['buruk'])
rule3 = ctrl.Rule(ph['poor'] & suhu['poor'] & do['poor'], kualitas_air['buruk'])
rule4 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['very_poor'], kualitas_air['buruk'])

rule5 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule6 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])
rule7 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])

rule8 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule9 = ctrl.Rule(ph['optimal'] & suhu['poor'] & do['optimal'], kualitas_air['buruk'])
rule10 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])

rule11 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['optimal'], kualitas_air['buruk'])
rule12 = ctrl.Rule(ph['poor'] & suhu['optimal'] & do['optimal'], kualitas_air['buruk'])
rule13 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['optimal'], kualitas_air['buruk'])

# Aturan tambahan
rule14 = ctrl.Rule(ph['moderate'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule15 = ctrl.Rule(ph['moderate'] & suhu['poor'] & do['optimal'], kualitas_air['buruk'])
rule16 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['moderate'], kualitas_air['buruk'])
rule17 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule18 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['moderate'], kualitas_air['buruk'])

# Aturan untuk kondisi kombinasi yang lebih kritis
rule19 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule20 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
rule21 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['optimal'], kualitas_air['buruk'])

# Aturan untuk kombinasi yang cukup baik
rule22 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])
rule23 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
# Melanjutkan dari aturan yang sudah ada

# 24 hingga 100
rule24 = ctrl.Rule(ph['optimal'] & suhu['poor'] & do['moderate'], kualitas_air['buruk'])
rule25 = ctrl.Rule(ph['optimal'] & suhu['poor'] & do['very_poor'], kualitas_air['buruk'])
rule26 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule27 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])
rule28 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule29 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule30 = ctrl.Rule(ph['poor'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule31 = ctrl.Rule(ph['poor'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])
rule32 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['very_poor'], kualitas_air['buruk'])
rule33 = ctrl.Rule(ph['very_poor'] & suhu['poor'] & do['optimal'], kualitas_air['buruk'])
rule34 = ctrl.Rule(ph['very_poor'] & suhu['poor'] & do['moderate'], kualitas_air['buruk'])
rule35 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
rule36 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['optimal'], kualitas_air['bagus'])
rule37 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule38 = ctrl.Rule(ph['moderate'] & suhu['poor'] & do['moderate'], kualitas_air['buruk'])
rule39 = ctrl.Rule(ph['moderate'] & suhu['poor'] & do['poor'], kualitas_air['buruk'])
rule40 = ctrl.Rule(ph['poor'] & suhu['optimal'] & do['optimal'], kualitas_air['buruk'])
rule41 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule42 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule43 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])
rule44 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule45 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
rule46 = ctrl.Rule(ph['very_poor'] & suhu['poor'] & do['very_poor'], kualitas_air['buruk'])
rule47 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])
rule48 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
rule49 = ctrl.Rule(ph['optimal'] & suhu['poor'] & do['optimal'], kualitas_air['buruk'])
rule50 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])

# Aturan 51-100
rule51 = ctrl.Rule(ph['moderate'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
rule52 = ctrl.Rule(ph['moderate'] & suhu['poor'] & do['very_poor'], kualitas_air['buruk'])
rule53 = ctrl.Rule(ph['poor'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])
rule54 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['very_poor'], kualitas_air['buruk'])
rule55 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule56 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule57 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])
rule58 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['very_poor'], kualitas_air['buruk'])
rule59 = ctrl.Rule(ph['very_poor'] & suhu['poor'] & do['optimal'], kualitas_air['buruk'])
rule60 = ctrl.Rule(ph['very_poor'] & suhu['poor'] & do['moderate'], kualitas_air['buruk'])
rule61 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule62 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule63 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule64 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule65 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule66 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule67 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule68 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule69 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule70 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule71 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule72 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule73 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['moderate'], kualitas_air['bagus'])
rule74 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])
rule75 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule76 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])
rule77 = ctrl.Rule(ph['poor'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule78 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule79 = ctrl.Rule(ph['poor'] & suhu['moderate'] & do['moderate'], kualitas_air['buruk'])
rule80 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['moderate'], kualitas_air['buruk'])
rule81 = ctrl.Rule(ph['very_poor'] & suhu['optimal'] & do['poor'], kualitas_air['buruk'])
rule82 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['optimal'], kualitas_air['buruk'])
rule83 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['moderate'], kualitas_air['buruk'])
rule84 = ctrl.Rule(ph['very_poor'] & suhu['moderate'] & do['poor'], kualitas_air['buruk'])
rule85 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule86 = ctrl.Rule(ph['optimal'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule87 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule88 = ctrl.Rule(ph['moderate'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule89 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule90 = ctrl.Rule(ph['poor'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule91 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['moderate'], kualitas_air['buruk'])
rule92 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['poor'], kualitas_air['buruk'])
rule93 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['optimal'], kualitas_air['bagus'])
rule94 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['optimal'], kualitas_air['bagus'])
rule95 = ctrl.Rule(ph['moderate'] & suhu['optimal'] & do['optimal'], kualitas_air['bagus'])
rule96 = ctrl.Rule(ph['optimal'] & suhu['moderate'] & do['moderate'], kualitas_air['bagus'])
rule97 = ctrl.Rule(ph['moderate'] & suhu['moderate'] & do['optimal'], kualitas_air['bagus'])
rule98 = ctrl.Rule(ph['optimal'] & suhu['optimal'] & do['very_poor'], kualitas_air['buruk'])
rule99 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['optimal'], kualitas_air['buruk'])
rule100 = ctrl.Rule(ph['very_poor'] & suhu['very_poor'] & do['very_poor'], kualitas_air['buruk'])


kualitas_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
    rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
    rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
    rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
    rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70,
    rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80,
    rule81, rule82, rule83, rule84, rule85, rule86, rule87, rule88, rule89, rule90,
    rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99, rule100
])

kualitas = ctrl.ControlSystemSimulation(kualitas_ctrl)

random_ph = random.uniform(0, 8) 
random_suhu = random.uniform(0, 40)
random_do = random.uniform(0, 10)

kualitas.input['ph'] =  random_ph                          
kualitas.input['suhu'] = random_suhu
kualitas.input['do'] = random_do

kualitas.compute()

# Print input yang dihasilkan
print(f"Input pH: {random_ph}")
print(f"Input Suhu: {random_suhu}")
print(f"Input DO: {random_do}")

# Debugging output
print(f"Output: {kualitas.output}")

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

print(f"Kualitas Air dengan nilai yang di bulatkan: {label2}")