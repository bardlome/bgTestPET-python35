import math
#from time import time as czasteraz #downloaded
import obliczaczkolka

#multiprocesing szukanie srodka
def workerszukaniesrodka(num,liczbaproc,siatkacm,srednicafantomu,return_maksymalniekolko,return_dictY,return_dictX,wynikarraja2):
	#czasik1=czasteraz()

	pozycjawx=num+math.ceil(srednicafantomu)
	srodekkolkax=0
	srodekkolkay=0
	maksymalniekolko=0
	maksymalniekolkopoprzednie=-1
	#procentowo=0
	while pozycjawx<(siatkacm-math.ceil(srednicafantomu)):	
		pozycjawy=math.ceil(srednicafantomu)
		while pozycjawy<(siatkacm-math.ceil(srednicafantomu)):
			"""#procenty
			pr=procentowo*100/((siatkacm-math.ceil(srednicafantomu))**2)
			print "%f procent complete" %pr
			procentowo+=1
			"""
			sumakolko=obliczaczkolka.wyliczonezliczenia(pozycjawx,pozycjawy,wynikarraja2,siatkacm,srednicafantomu)
			if sumakolko>maksymalniekolko:
				maksymalniekolko=sumakolko
				srodekkolkay=pozycjawy		
				srodekkolkax=pozycjawx			
			pozycjawy+=1			
		pozycjawx+=liczbaproc	
	#print "srodek kola-proc [ %d ] : x= %d ,y= %d (zalozenie, ze wymiary ROIa=1cm x 1cm)" %(num,srodekkolkax,srodekkolkay)
	#czasik2=czasteraz()-czasik1
	#print "zajelo to: ", czasik2

	return_maksymalniekolko[num] = maksymalniekolko
	return_dictY[num] = srodekkolkay
	return_dictX[num] = srodekkolkax	

