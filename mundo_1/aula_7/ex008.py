# Conversor de Medidas
medida = float(input('Digite o valor em metros que deseja converter: '))
km = medida / 1000
hm = medida /100
dam = medida /10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('\n{} m corresponde a:\n\n{:.3f} km\n{:.2f} hm\n{:.1f} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm'.format(medida, km, hm, dam, dm, cm ,mm))
