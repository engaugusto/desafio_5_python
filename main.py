# Carlos Augusto
# 29/03/2018
# Desafio de programcao
# https://osprogramadores.com/desafios/d05/
# _*_ coding:utf-8 _*_
import urllib
import simplejson as json
import pprint
import sys
import datetime
 
class itemArea:
	def __init__(self, val,nome,area,sobrenome,id):
		self.val = val
		self.nome = nome
		self.area = area
		self.sobrenome = sobrenome
		self.id = id
 
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
lstSobrenomes = {}

for item in jsonResponse['areas']:
	#se nao existe adiciona
	if not lstAreas.has_key(item['codigo']):
		for ar in jsonResponse['areas']:
			if item["codigo"] == ar["codigo"]:
				lstAreas[item['codigo']] = ar['nome'];
			
for item in jsonResponse['funcionarios']:
	#area
	if not lstAreasVal.has_key(item['area']):
		lstAreasVal[item["area"]] =  [ itemArea(item["salario"],"%s %s" % (item["nome"], item["sobrenome"]), item["area"], item["sobrenome"], item["id"] ) ]
	else:
		lstAreasVal[item["area"]].append( itemArea(item["salario"],"%s %s" % (item["nome"], item["sobrenome"]), item["area"], item["sobrenome"], item["id"] ) )
	if not lstSobrenomes.has_key(item['sobrenome']):
		lstSobrenomes[item["sobrenome"]] = [ itemArea(item["salario"],"%s %s" % (item["nome"], item["sobrenome"]), item["area"], item["sobrenome"], item["id"] ) ]
	else:
		lstSobrenomes[item["sobrenome"]].append( itemArea(item["salario"],"%s %s" % (item["nome"], item["sobrenome"]), item["area"], item["sobrenome"], item["id"] ) )

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

menos_emp = []
mais_emp = []
menos=0
maior=0
ik = 0

for key, value in lstAreasVal.iteritems():
	if ik==0:
		menos=len(value)
		maior=len(value)
		ik = ik+1
		
	if maior <= len(value):
		maior=len(value)
	if menos >= len(value):
		menos=len(value)

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

ik = 0
#menos=menos_emp[0]
#maior=mais_emp[0]

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
	print 'global_max|'"%0.2f" % max
for min in lstMin:
	print 'global_min|'"%0.2f" % min

print 'global_avg|'"%0.2f" % (avg)

ik = 0
lstMaiorSalSobrenome=[]
for key, value in lstSobrenomes.iteritems():
	#print "k"
	#print key
	#print "v"
	#print value
	if len(value) > 1:
		#encontrando o maior salario
		maiorSalSobre=0
		for ilm in value:
			#print "ilm"
			#print ilm.val
			if ilm.val >= maiorSalSobre:
				maiorSalSobre = ilm.val
		for nop in value:
			if maiorSalSobre == nop.val:
				lstMaiorSalSobrenome.append(nop)
			#print "v2"
			#print v2[0].val
			#if v2[k2].val >= maiorSalSobre:
			#	maiorSalSobre = v2[k2].val


#encontrado os outros

for key, value in lstAreasVal.iteritems():
	if menos == len(value):
		menos_emp.append("%s|%s"%(lstAreas[key] , len(value) ))
	if maior == len(value):
		mais_emp.append("%s|%s"%(lstAreas[key],   len(value) ))	

	for item in jsonResponse['funcionarios']:
		#key = item["area"]
		if key <> item["area"]:
			continue
		if item["salario"] == maxtmpArea[key].val and item["area"] == maxtmpArea[key].area:
			s="area_max|%s|%s|%s" % (lstAreas[key],"%s %s" % (item["nome"],item["sobrenome"] ),item["salario"])
			print s.encode("utf-8")
		if item["salario"] == mintmpArea[key].val and item["area"] == mintmpArea[key].area:
			s="area_min|%s|%s|%s" % (lstAreas[key],"%s %s" % (item["nome"],item["sobrenome"] ),item["salario"])
			print s.encode("utf-8")
	nnn='area_avg|%s|'"%0.2f" % (lstAreas[key], avgArea[key])
	print nnn.encode("utf-8")
#	print "area_max|%s|%s|%s|%s" % (lstAreas[item["area"]],item["nome"],item["sobrenome"],item["salario"])
#	for item in jsonResponse['funcionarios']:
#		if item["area"] <> key:
#			continue
#		print "area_max|%s|%s|%s|%s" % (lstAreas[item["area"]],item["nome"],item["sobrenome"],item["salario"])

for at in mais_emp:
	print "most_employees|%s"%at.encode("utf-8")
for at in menos_emp:
	print "least_employees|%s"%at.encode("utf-8")
	
for maiorSolSobrenome in lstMaiorSalSobrenome:
	s="last_name_max|%s|%s|%s"%(maiorSolSobrenome.sobrenome,maiorSolSobrenome.nome,maiorSolSobrenome.val)
	print s.encode("utf-8")
			
#	for k2,v2 in lstSobrenomes.iteritems():
#		
#	maiorTmp = 0
#	menorTmp = 0
#	print value[ik]
#	if len(value[ik] ) > 1:
#		if ik == 0:
#			maiorTmp=value[0]
#			menorTmp=value[0]
#		for i in value:
#			if maiorTmp <= i:
#				maiorTmp = i
#			if menorTmp >= i:
#				menorTmp = i
#		for i2 in value2:
#			if maiorTmp == i2:
#				lstMaiorSalSobrenome.append()
#	print key
#	print value
#	ik=ik+1

b = datetime.datetime.now()
c = b - a

#print ''
#print 'diff miliseconds' , c.total_seconds() * 1000 # milliseconds
#print 'diff seconds' , c.total_seconds() / 60 # seconds
#print 'diff min' , c.total_seconds() / 60 / 60 # min
