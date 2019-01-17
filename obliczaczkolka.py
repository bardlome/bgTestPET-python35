#f uzyta w finderze srodka
def wyliczonezliczenia(pozwx,pozwy,arraj,scm,fanto):
	sumazliczen=0
	indekswx=0
	while indekswx<scm:
		indekswy=0
		while indekswy<scm:
			taleszliczen1=(indekswx-pozwx+0.5)**2 + (indekswy-pozwy+0.5)**2
			taleszliczen2=(indekswx-pozwx+0.5)**2 + (indekswy-pozwy-0.5)**2
			taleszliczen3=(indekswx-pozwx-0.5)**2 + (indekswy-pozwy+0.5)**2
			taleszliczen4=(indekswx-pozwx-0.5)**2 + (indekswy-pozwy-0.5)**2
			if taleszliczen1<=(fanto/2)**2 or taleszliczen2<=(fanto/2)**2 or taleszliczen3<=(fanto/2)**2 or taleszliczen4<=(fanto/2)**2 :
				sumazliczen += arraj[indekswx,indekswy]
			indekswy+=1
		indekswx+=1
	return sumazliczen	

