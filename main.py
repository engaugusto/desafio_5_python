import urllib
import simplejson as json
import pprint
import sys
import datetime
 
class itemArea:
	def __init__(self, val,nome,area):
		self.val = val
		self.nome = nome
		self.area = area
 
a = datetime.datetime.now()
lstMin = []
lstMax = []
avg = 0;

lstAreaMin = []
lstAreaMax = []
avgArea = 0;

#print 'oi'
data = sys.stdin.read()
jsonResponse = json.loads(data)
#print "leu com sucesso"
#print jsonResponse['areas']
#pprint.pprint(jsonResponse)
#print 'oi2'

i=0
mintmp = 0
maxtmp = 0
sumMedia = 0

lstAreas = {}

lstAreasVal = {}

for item in jsonResponse['areas']:
	#se nao existe adiciona
	if not lstAreas.has_key(item['codigo']):
		for ar in jsonResponse['areas']:
			if item["codigo"] == ar["codigo"]:
				lstAreas[item['codigo']] = ar['nome'];
			
for item in jsonResponse['funcionarios']:
	#area
	if not lstAreasVal.has_key(item['area']):
		lstAreasVal[item["area"]] =  [ itemArea(item["salario"],"%s %s" % (item["nome"], item["sobrenome"]), item["area"]  ) ]
	else:
		lstAreasVal[item["area"]].append( itemArea(item["salario"],"%s %s" % (item["nome"], item["sobrenome"]), item["area"] ) )

	sumMedia = sumMedia + item['salario']
	i=i+1
	if i == 1:
		mintmp = item['salario']
		maxtmp = item['salario']
		continue
	if item['salario']< mintmp:
		mintmp = item['salario']
	if item['salario'] > maxtmp:
		maxtmp = item['salario']
avg = sumMedia/i

mintmpArea = {}
maxtmpArea = {}
avgArea = {}
i = 0
for key, value in lstAreasVal.iteritems():
	if not mintmpArea.has_key(key) :
		mintmpArea[key] = value[0]
	if not maxtmpArea.has_key(key) :
		maxtmpArea[key] = value[0]
	if not avgArea.has_key(key) :
		avgArea[key] = 0
	
	for j in value:
		avgArea[key] = avgArea[key] +  j.val
		if j.val < mintmpArea[key].val:
			mintmpArea[key] = j
		if j.val >  maxtmpArea[key].val:
			maxtmpArea[key] = j
	avgArea[key] = avgArea[key]/len(value)
			#print o.nome
#for key in lstAreas.iteritems():
	#print key
#for key,val in maxtmpArea.iteritems():
	#print val.nome
	#print val.val
#for key,val in mintmpArea.iteritems():
	#print val.nome
#for k in lstAreasVal:
	#for g in lstAreasVal[k]:
		#print g.val


for item in jsonResponse['funcionarios']:
	if item['salario'] == mintmp:
		lstMin.append(mintmp)
	if item['salario'] == maxtmp:
		lstMax.append(maxtmp)

#lstMin.append(mintmp)
#lstMax.append(maxtmp)

for max in lstMax:
	print 'global_max|'"%0.2f" %max	
for min in lstMin:
	print 'global_min|'"%0.2f" %min

print 'global_avg|'"%0.2f" % (avg)

		
#encontrado os outros

for key, value in lstAreasVal.iteritems():
	for item in jsonResponse['funcionarios']:
		#key = item["area"]
		if key <> item["area"]:
			continue
		if item["salario"] == maxtmpArea[key].val and item["area"] == maxtmpArea[key].area:
			print "area_max|%s|%s|%s" % (lstAreas[key],"%s %s" % (item["nome"],item["sobrenome"] ),item["salario"])
		if item["salario"] == mintmpArea[key].val and item["area"] == mintmpArea[key].area:
			print "area_min|%s|%s|%s" % (lstAreas[key],"%s %s" % (item["nome"],item["sobrenome"] ),item["salario"])
	print 'area_avg|%s|'"%0.2f" % (lstAreas[key], avgArea[key])
#	print "area_max|%s|%s|%s|%s" % (lstAreas[item["area"]],item["nome"],item["sobrenome"],item["salario"])
#	for item in jsonResponse['funcionarios']:
#		if item["area"] <> key:
#			continue
#		print "area_max|%s|%s|%s|%s" % (lstAreas[item["area"]],item["nome"],item["sobrenome"],item["salario"])
	
	
	
b = datetime.datetime.now()
c = b - a
print 'diff miliseconds' , c.total_seconds() * 1000 # milliseconds