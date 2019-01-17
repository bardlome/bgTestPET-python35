import pylab #niedownloaded
import numpy as np #alreadydow
import scipy #downloaded
#from os import system #niedownloaded
#import datetime
#import bgTestNU_PET
from time import time as czasteraz #downloaded
import pydicom
import math
import multiprocessing
import workery
import statistics
import datetime
from tkinter import messagebox as tkMessageBox
import obliczaczkolka
import multikonik
"""
def oblicznuithread(a,b,c,d,e):
        print "threeeead" 
        thread.start_new_thread(oblicznui(a,b,c,d,e), ())
"""#SEEMS THAT jakis import blokuje thready i processingi
def oblicznui(chcemymulti,probnanazwa,pixyniejednorodne3,sciezka,wynik1):

        startowytime = czasteraz()


        #plt=matplotlib.pyplot
        # ile pixeli przypada na 10 mm?
        # pixmm=3.1819(...)
        #pixmm=814.57/256
        numerwarstwy=1
        srednicafantomu=17.5

        NUimax=0
        NUinumerwarstwy=0
        CVimax=0
        tabelawartoscibez0VOL=[]
        nazwa=""
        
        nazwa=probnanazwa
        if nazwa=="":
                print ("brak nazwy, ustalam domyslna")        
                probnanazwa="IM-0056-0001.dcm"
                nazwa=probnanazwa

        if sciezka=="":
                print ("jestem w folderze domyslnym")
        else:
                print ("jestem w : %s" % sciezka)
        print ("plik : %s" % nazwa)
        opcja1=0 #tkMessageBox.askyesno("Pytanie","pokazac przykladowa obrobke?"), i wiekszy verbose
        #root.update() 12.09.2018#

        while numerwarstwy<1000:
                
                if numerwarstwy<10:
                        nazwapliku=nazwa[:-5] + str(numerwarstwy) + ".dcm"
                elif numerwarstwy<100:
                        nazwapliku=nazwa[:-6] + str(numerwarstwy) + ".dcm"
                elif numerwarstwy<1000:
                        nazwapliku=nazwa[:-7] + str(numerwarstwy) + ".dcm"
                try:
                        mojdataset = pydicom.read_file(sciezka + nazwapliku)
                except IOError:
                        print ("nie znalazlem (kolejnych) plikow .dcm w tym folderze")
                        break
                

                #INICJACJA ZMIENNYCH dodatkowych
                if numerwarstwy==1 and pixyniejednorodne3==1:
                        try:
                                print ("odleglosci siatki beda rowne x, x+1 , x , x , x+1 itp.")
                                rozdzielczosc=mojdataset.data_element("Rows").value #lub columns
                                pixmm=float(mojdataset.data_element("PixelSpacing").value[0]) #bo sa ["valx","valy"]        
                                siatkacm=int(math.ceil(rozdzielczosc/pixmm))
                                siatkacmdol=int(math.floor(rozdzielczosc/pixmm))


                        except IOError:
                                print ("problem z odczytaniem rozdzielczosci itp")
                                break
                elif numerwarstwy==1 and pixyniejednorodne3==2:
                        try:
                                """
                                print ("odleglosci siatki beda rowne x")
                                rozdzielczosc=mojdataset.data_element("Rows").value #lub columns
                                pixmm=math.floor(mojdataset.data_element("PixelSpacing").value[0]) #bo sa ["valx","valy"]        
                                siatkacm=int(math.ceil(rozdzielczosc/pixmm))
                                siatkacmdol=int(math.floor(rozdzielczosc/pixmm))
                                stosunekcm=pixmm/float(mojdataset.data_element("PixelSpacing").value[0])
                                srednicafantomu=17.5/stosunekcm
                                """
                                print ("odleglosci siatki beda rowne x")

                                rozdzielczosc=mojdataset.data_element("Rows").value
                                pixmm=math.floor(1/(mojdataset.data_element("PixelSpacing").value[0])*10) #zamiana wartosci -mm w pixelach- na -pixele na centymetr-
                                siatkacm=int(math.ceil(rozdzielczosc/pixmm)) #ile ROI na kolumne/rzad  
                                siatkacmdol=int(math.floor(rozdzielczosc/pixmm)) #ile ROI na kolumne/rzad, zaokraglone w dol
                                stosunekcm=pixmm/float(1/(mojdataset.data_element("PixelSpacing").value[0])*10) #ile w rzeczywistosci ma to, co uznajemy za 1 cm
                                srednicafantomu=17.5/stosunekcm #ile powinien miec fantom z uwzglednieniem pikseli na cm
                                

                        except IOError:
                                print ("problem z odczytaniem rozdzielczosci itp")
                                break


                #pylab.imshow(mojdataset.pixel_array, cmap=pylab.cm.bone)
                face=mojdataset.pixel_array #(gray=True)


                #+wizualizacjiabezporawek
                if opcja1==1 and numerwarstwy==1:
                        intpixmm=[]
                        intsiatka=0
                        while intsiatka<rozdzielczosc :
                                intsiatka2=int(intsiatka)
                                intpixmm.append(intsiatka2)
                                intsiatka+=pixmm
                        obrazraw=plt.figure()
                        #obrazraw.add_subplot(1,1,1)
                        odlegloscisiatkipixmm = np.array(intsiatka2)
                        Iksypixmm,Igrekipixmm = np.meshgrid(odlegloscisiatkipixmm,odlegloscisiatkipixmm)
                        plt.plot(Iksypixmm-0.5,Igrekipixmm-0.5, marker='+', color='white', linestyle='none')

                        #print Igrekipixmm        
                        pylab.imshow(face)
                """
                if numerwarstwy==1 and opcja1==1:
                        print "zliczam eventy w sektorach/ROIach (siata co 3.18 pixeli (3 lub 4) ~ 1cm)"        
                        sleep(5)
                """

                numerkolumny=0
                numerkwadratu=1
                pozycjawy=0
                wynikarraja2=np.ndarray(shape=(siatkacm,siatkacm))
                #maxarraja2=np.ndarray(shape=(siatkacm,siatkacm))
                #sumaarraja2=np.ndarray(shape=(siatkacm,siatkacm))
                #minarraja2=np.ndarray(shape=(siatkacm,siatkacm))
                #avearraja2=np.ndarray(shape=(siatkacm,siatkacm))
                while numerkolumny<rozdzielczosc:
                        numerintkolumny=numerkolumny
                        numerrzedu=0
                        pozycjawx=0
                        while numerrzedu<rozdzielczosc:
                                numerintrzedu=numerrzedu
                                #sumaarraja=face[(int(numerintrzedu)):(int(numerintrzedu+pixmm)),(int(numerintkolumny)):(int(numerintkolumny+pixmm))].sum()
                                #maxarraja=face[(int(numerintrzedu)):(int(numerintrzedu+pixmm)),(int(numerintkolumny)):(int(numerintkolumny+pixmm))].max()
                                #minarraja=face[(int(numerintrzedu)):(int(numerintrzedu+pixmm)),(int(numerintkolumny)):(int(numerintkolumny+pixmm))].min()
                                avearraja=face[(int(numerintrzedu)):(int(numerintrzedu+pixmm)),(int(numerintkolumny)):(int(numerintkolumny+pixmm))].mean()
                                if opcja1==1 and numerwarstwy==1:
                                        print ("kwadrat %d : rzad pikselow %d, kolumna pixelow %d: licba zliczen SUM: %d AVE: %d MIN: %d MAX: %d" % (numerkwadratu, numerrzedu, numerkolumny,wynikarraja,avearraja,minarraja,maxarraja))
                                #sumaarraja2[pozycjawx,pozycjawy]=sumaarraja
                                #maxarraja2[pozycjawx,pozycjawy]=maxarraja
                                #minarraja2[pozycjawx,pozycjawy]=minarraja
                                #avearraja2[pozycjawx,pozycjawy]=avearraja
                                wynikarraja2[pozycjawx,pozycjawy]=avearraja
                                numerrzedu +=pixmm
                                numerkwadratu +=1
                                pozycjawx+=1
                        numerkolumny +=pixmm
                        pozycjawy+=1
                if opcja1==1 and numerwarstwy==1:        
                        print ("powyzej przyklad otrzymanych l zliczen z pliku dicom")


                #srodek finder - jako rzad/kolumna o najwiekszej l zliczen, wykonany tylko dla w1 gdyz po wielu usprawnieniach funckja szukajaca i tak w kazdej warstwie zaczela wskazywac ten sam srodek, a funkcja ta bada kazda mozliwosc, co troche jej zajmuje
                #if __name__ == '__main__' and chcemymulti==1:
                if chcemymulti==1:
                        if numerwarstwy==1:




                                mojewyniki = multikonik.multikonikuwio(siatkacm,srednicafantomu,wynikarraja2)
                                srodekkolkay=mojewyniki[0]
                                srodekkolkax=mojewyniki[1]


                                #srodekkolkay=42                
                                #srodekkolkax=42    
                                print ("a jednak srodek kola: x= %d ,y= %d (zalozenie, ze wymiary ROIa=1cm x 1cm)" %(srodekkolkax,srodekkolkay))




                else:
                        czasik1=czasteraz()
                        if numerwarstwy==1:
                                print ("szukanie srodka fantomu (to moze troche potrwac)")
                                pozycjawx=math.ceil(srednicafantomu)
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
                                        pozycjawx+=1        
                                print ("srodek kola: x= %d ,y= %d (zalozenie, ze wymiary ROIa=1cm x 1cm)" %(srodekkolkax,srodekkolkay))          

                        czasik2=czasteraz()-czasik1
                        print ("zajelo to: ", czasik2)

                
                #+wizualizacjiabezporawek
                if opcja1==1 and numerwarstwy==1:
                        obrazbezpop, plotenko = plt.subplots()
                        odlegloscisiatki = np.array(range(1,siatkacmdol));
                        Iksy,Igreki = np.meshgrid(odlegloscisiatki,odlegloscisiatki)
                        plt.plot(Iksy-0.5,Igreki-0.5, marker='+', color='white', linestyle='none')
                        kolko = plt.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)                
                        plotenko.add_artist(kolko)
                        pylab.imshow(wynikarraja2)


                #odrzucenie skjajnych
                pozycjawx=0
                while pozycjawx<siatkacm:
                        pozycjawy=0
                        while pozycjawy<siatkacm:
                                tales1=(pozycjawx-srodekkolkax+0.5)**2 + (pozycjawy-srodekkolkay+0.5)**2#zamienione celowo, bo gdzies indziej tez sie zamienilo,niewiem 
                                tales2=(pozycjawx-srodekkolkax+0.5)**2 + (pozycjawy-srodekkolkay-0.5)**2
                                tales3=(pozycjawx-srodekkolkax-0.5)**2 + (pozycjawy-srodekkolkay+0.5)**2
                                tales4=(pozycjawx-srodekkolkax-0.5)**2 + (pozycjawy-srodekkolkay-0.5)**2
                                if tales1>=(srednicafantomu/2)**2 or tales2>=(srednicafantomu/2)**2 or tales3>=(srednicafantomu/2)**2 or tales4>=(srednicafantomu/2)**2 :
                                        wynikarraja2[pozycjawx,pozycjawy]=0
                                pozycjawy+=1
                        pozycjawx+=1
                #+wizualizacjia
                if opcja1==1 and numerwarstwy==1:
                        obrazwkwadratyzkolem, plotno = plt.subplots()
                        odlegloscisiatki = np.array(range(1,siatkacmdol));
                        Iksy,Igreki = np.meshgrid(odlegloscisiatki,odlegloscisiatki)
                        plt.plot(Iksy-0.5,Igreki-0.5, marker='+', color='white', linestyle='none')
                        kolko = plt.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)
                        #kolko = matplotlib.pyplot.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)                
                        plotno.add_artist(kolko)
                        pylab.imshow(wynikarraja2)
                        print ("przyklad: rys 1=RAW data, 2=converted na siatke 10mm, 3=converted+wyzerowanie wszystkiego poza fantomem")                
                        print ("indeks non-uniformity bazuje na niezerowych wartosciach z danych przedstawionych w obrazie 3")
                        pylab.show()
                        plt.clf()
                        root.update()

                #wartosciprzepisanedopostacilisty        
                tabelawartoscibez0=[]
                pozycjawx=0
                while pozycjawx<siatkacm:
                        pozycjawy=0
                        while pozycjawy<siatkacm:
                                if wynikarraja2[pozycjawx,pozycjawy]>0:
                                        tabelawartoscibez0.append(wynikarraja2[pozycjawx,pozycjawy])
                                        tabelawartoscibez0VOL.append(wynikarraja2[pozycjawx,pozycjawy])
                                pozycjawy+=1
                        pozycjawx+=1
                if numerwarstwy==1:
                        print ("nr of ROIs: %d" % len(tabelawartoscibez0))

                #obliczanieNUi
                if tabelawartoscibez0!=[]:

                        nonconformity1=100*(max(tabelawartoscibez0) - statistics.mean(tabelawartoscibez0)) / statistics.mean(tabelawartoscibez0)
                        nonconformity2=100*(statistics.mean(tabelawartoscibez0) - min(tabelawartoscibez0)) / statistics.mean(tabelawartoscibez0)
                        nonconform=[nonconformity1,nonconformity2]
                        nonconformity=max(nonconform)
                        podpierwiastkiem=0
                        a1=(len(tabelawartoscibez0) - 1)
                        for wartosc in tabelawartoscibez0:
                                #print "wartosc %f" % wartosc
                                #print "a1 %f" % a1
                                a2=(wartosc-statistics.mean(tabelawartoscibez0))**2
                                #print "a2 %f" % a2
                                podpierwiastkiem += (1.0/a1)*(a2)        
                        #print "podpierwiastkiem %f" % podpierwiastkiem
                        sdi=math.pow(podpierwiastkiem,0.5)
                        #print sdi
                        cvalue=100 * sdi/statistics.mean(tabelawartoscibez0)
                        print ("numer warstwy: %d non-uniformity NU_(%d) = %f CV_(%d) = %f sdi_(%d) = %f" %(numerwarstwy,numerwarstwy,nonconformity,numerwarstwy,cvalue,numerwarstwy,sdi))
                        if nonconformity > NUimax:
                                #print "znalazlem"
                                NUimax=nonconformity
                                NUinumerwarstwy=numerwarstwy
                                CVimax=cvalue
                        numerwarstwy+=1

        #wynikmax
        if tabelawartoscibez0VOL!=[]:
                if NUimax>0:
                        print ("MAX NUi: numer warstwy: %d non-uniformity NU_(%d) = %f CV_(%d) = %f" %(NUinumerwarstwy,NUinumerwarstwy,NUimax,NUinumerwarstwy,CVimax))
                #obliczanieNUj
                nonunVOL1=100*(max(tabelawartoscibez0VOL) - statistics.mean(tabelawartoscibez0VOL)) / statistics.mean(tabelawartoscibez0VOL)
                nonunVOL2=100*(statistics.mean(tabelawartoscibez0VOL) - min(tabelawartoscibez0VOL)) / statistics.mean(tabelawartoscibez0VOL)
                nonunV=[nonunVOL1,nonunVOL2]
                nonunVOL=max(nonunV)
                podpierwiastkiem=0
                print ("zliczam NU_(vol) , CV_(vol) , moze chwile zajac")
                a1=(len(tabelawartoscibez0VOL) - 1)
                procentowo=0
                popproc=0
                sredniazwartoscibez0=statistics.mean(tabelawartoscibez0VOL)
                for wartosc in tabelawartoscibez0VOL:
                        if ((procentowo*100/len(tabelawartoscibez0VOL))-popproc)>=5 or procentowo==0:
                                popproc=procentowo*100/len(tabelawartoscibez0VOL)
                                print ("%f procent complete" % (procentowo*100/len(tabelawartoscibez0VOL)))
                        procentowo+=1
                        #print "wartosc %f" % wartosc        
                        #print "a1 %d" % a1
                        a2=(wartosc-sredniazwartoscibez0)**2
                        #print "a2 %f" % a2
                        podpierwiastkiem += (1.0/a1)*(a2)        
                #print "podpierwiastkiem %f" % podpierwiastkiem
                sdi=math.pow(podpierwiastkiem,0.5)
                print ("srednia : %f " % statistics.mean(tabelawartoscibez0))
                print ("sdi : %f " % sdi)
                cvalue=100 * sdi/statistics.mean(tabelawartoscibez0)

        #log
        try:
                print ("zapisuje logBGPetTest.txt")
                log=open(sciezka+"logBGPetTest.txt","a")
                stary=datetime.date.today().strftime("%d-%m-%Y")+":"
                stary+="\nObliczono z %d plikow, poczynajac od %s" %(numerwarstwy-1,probnanazwa)
                if chcemymulti==1:
                        stary+="\n wynik obliczony multiprocessingiem"
                stary+="\nsrodek fantomu wg pliku *.dcm: x= %d cm ,y= %d cm (zalozenie, ze wymiary ROIa=1cm x 1cm)" %(srodekkolkax,srodekkolkay)
                stary+="\nnr of ROIs: %d" % len(tabelawartoscibez0)
                stary+="\nMax NUi: NU_(%d) = %f CV_(%d) = %f \n SD_i = %f \n NU_(vol) = %f CV_(vol) = %f " %(NUinumerwarstwy,NUimax,NUinumerwarstwy,CVimax,sdi,nonunVOL,cvalue)
                stary+="\n ROI (1cm x 1cm) odpowiada kwadratowi: %f x %f pikseli\n \n" % (pixmm,pixmm)
                wynik1="Zrobiony"
                log.write(stary)
                log.close()
                print ("czas obliczen [s]:")
                print (czasteraz()-startowytime)
        except UnboundLocalError:
                print ("Test niewykonany")
                try:
                        log=open(sciezka+"logBGPetTest.txt","a")
                        stary=datetime.date.today().strftime("%d-%m-%Y")+":"
                        stary+="\nNie znaleziono odpowiednich plikow\n"
                        log.write(stary)
                        log.close()
                except UnboundLocalError:
                        pass
        try:
                print ("non-uniformity volume NU_(vol) = %f CV_(vol) = %f" %(nonunVOL,cvalue))
                tkMessageBox.showinfo("Skonczylem!","Max NUi: NU_(%d) = %f \n CV_(%d) = %f \n NU_(vol) = %f \n CV_(vol) = %f" %(NUinumerwarstwy,NUimax,NUinumerwarstwy,CVimax,nonunVOL,cvalue))
                print ("Max NUi: NU_(%d) = %f \n CV_(%d) = %f \n NU_(vol) = %f \n CV_(vol) = %f" %(NUinumerwarstwy,NUimax,NUinumerwarstwy,CVimax,nonunVOL,cvalue))
                print ("srodek fantomu wg pliku *.dcm: x= %d cm ,y= %d cm (zalozenie, ze wymiary ROIa=1cm x 1cm)" %(srodekkolkax,srodekkolkay))
                print ("ROIs: %d" % len(tabelawartoscibez0))
                print ("Max NUi: NU_(%d) = %f CV_(%d) = %f SD_i = %f \n NU_(vol) = %f CV_(vol) = %f " %(NUinumerwarstwy,NUimax,NUinumerwarstwy,CVimax,sdi,nonunVOL,cvalue))
                #print ("Reconstruction Method: ", mojdataset.data_element("Reconstruction Method").value)
                print (mojdataset.values)
                #print ("Patient's Name: ", mojdataset.data_element("Patient's Name").value)
                #print ("Attenuation Correction Method: ", mojdataset.data_element("Attenuation Correction Method").value)
                                
                
                
        except UnboundLocalError:
                pass
