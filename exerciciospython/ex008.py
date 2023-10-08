#Metros em km, hm, dan, cm, mm#
mdd = float(input('Digite uma medida em metros:'))
cm = mdd*100
mm = mdd*1000
km = mdd/1000
hm = mdd/100
dam = mdd/10
print('Sua medida de {} metros equivale a:\n {}km, {}hm, {}dam, {:.0f}cm, {:.0f}mm.'.format(mdd, km, hm, dam, cm, mm))

