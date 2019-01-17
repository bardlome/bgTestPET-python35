import pydicom
import math
import workery
import matplotlib.pyplot as plt #downloaded
import numpy as np
import pylab
import obliczaczkolka
import przegladacz
from time import sleep as uspij #niedownloaded
import bgTestNU_PET
import multiprocessing

def ogladanie(Apka):
        #root.update()
        #pixmm=814.57/256
        numerwarstwy=1
        srednicafantomu=17.5
        NUimax=0
        NUinumerwarstwy=0
        CVimax=0
        tabelawartoscibez0VOL=[]



        nazwa=""
        nazwa=Apka.probnanazwa
        if nazwa=="":
                print ("brak nazwy, ustalam domyslna")     
                Apka.probnanazwa="IM-0056-0001.dcm"
                nazwa=Apka.probnanazwa

        if Apka.sciezka=="":
                print ("jestem w folderze domyslnym")
        else:
                print ("jestem w : %s" % Apka.sciezka)
        print ("plik : %s" % nazwa)
        while numerwarstwy<1000:
                
                if numerwarstwy<10:
                        nazwapliku=nazwa[:-5] + str(numerwarstwy) + ".dcm"
                elif numerwarstwy<100:
                        nazwapliku=nazwa[:-6] + str(numerwarstwy) + ".dcm"
                elif numerwarstwy<1000:
                        nazwapliku=nazwa[:-7] + str(numerwarstwy) + ".dcm"
                try:
                        mojdataset = pydicom.read_file(Apka.sciezka + nazwapliku)
                except IOError:
                        print ("nie znalazlem (kolejnych) plikow .dcm w tym folderze")
                        break

                #INICJACJA ZMIENNYCH dodatkowych
                if numerwarstwy==1 and Apka.pixyniejednorodne3==1:
                        try:
                                print ("odleglosci siatki beda rowne x, x+1 , x , x , x+1 itp.")
                                rozdzielczosc=mojdataset.data_element("Rows").value #lub columns
                                pixmm=float(mojdataset.data_element("PixelSpacing").value[0]) #bo sa ["valx","valy"]        
                                siatkacm=int(math.ceil(rozdzielczosc/pixmm))
                                siatkacmdol=int(math.floor(rozdzielczosc/pixmm))

                                #zerowanie arrajow
                                Apka.SLAJSY3=np.zeros((siatkacm,siatkacm,1))#shape=(81,81,6) 
                                Apka.SLAJSY2=np.zeros((siatkacm,siatkacm,1))#shape=(81,81,6)
                        except IOError:
                                print ("problem z odczytaniem rozdzielczosci itp")
                                break
                elif numerwarstwy==1 and Apka.pixyniejednorodne3==2:
                        try:
                                print ("odleglosci siatki beda rowne x")
                                rozdzielczosc=mojdataset.data_element("Rows").value
                                pixmm=math.floor(1/(mojdataset.data_element("PixelSpacing").value[0])*10) #1 pixel- ile to mm? #a nie-ile pixeli to 1 cm, zaokraglenie w dol      
                                siatkacm=int(math.ceil(rozdzielczosc/pixmm)) #ile ROI na kolumne/rzad  
                                siatkacmdol=int(math.floor(rozdzielczosc/pixmm)) #ile ROI na kolumne/rzad, zaokraglone w dol
                                stosunekcm=pixmm/float(1/(mojdataset.data_element("PixelSpacing").value[0])*10) #ile w rzeczywistosci ma to, co uznajemy za 1 cm
                                srednicafantomu=17.5/stosunekcm #ile powinien miec fantom z uwzglednieniem pikseli na cm
                                

                                print(rozdzielczosc)
                                print(pixmm)
                                print(siatkacm)
                                print(siatkacmdol)
                                print(stosunekcm)
                                print(srednicafantomu)

                                #zerowanie arrajow
                                Apka.SLAJSY3=np.zeros((siatkacm,siatkacm,1))#shape=(81,81,6) 
                                Apka.SLAJSY2=np.zeros((siatkacm,siatkacm,1))#shape=(81,81,6)

                        except IOError:
                                print ("problem z odczytaniem rozdzielczosci itp")
                                break

                #pylab.imshow(mojdataset.pixel_array, cmap=pylab.cm.bone)
                face=mojdataset.pixel_array #(gray=True)


                #+wizualizacjiabezporawek
                if numerwarstwy==1:
                        intpixmm=[]
                        intsiatka=0
                        while intsiatka<rozdzielczosc :
                                intsiatka2=int(intsiatka)
                                intpixmm.append(intsiatka2)
                                intsiatka+=pixmm
                        obrazraw=plt.plot()
                        #obrazraw.add_subplot(1,1,1)
                        odlegloscisiatkipixmm = np.array(intpixmm)
                        Iksypixmm,Igrekipixmm = np.meshgrid(odlegloscisiatkipixmm,odlegloscisiatkipixmm)
                        plt.plot(Iksypixmm-0.5,Igrekipixmm-0.5, marker='+', color='white', linestyle='none')

                        #print Igrekipixmm
                #do poprawy,zlewyswietleniesiatkiwfig1                
                        pylab.imshow(face)

                if numerwarstwy==1:
                        print ("zliczam eventy w sektorach/ROIach")        
                numerkolumny=0
                numerkwadratu=1
                pozycjawy=0
                wynikarraja2=np.ndarray(shape=(siatkacm,siatkacm))
                #maxarraja2=np.ndarray(shape=(siatkacm,siatkacm))
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
                                #if numerwarstwy==1:
                                        #print "kwadrat %d : rzad pikselow %d, kolumna pixelow %d: licba zliczen SUM: %d AVE: %d MIN: %d MAX: %d" % (numerkwadratu, numerrzedu, numerkolumny,wynikarraja,avearraja,minarraja,maxarraja)
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
                #if numerwarstwy==1:        
                        #print "powyzej przyklad otrzymanych l zliczen z pliku dicom"


                #srodek finder - jako rzad/kolumna o najwiekszej l zliczen, wykonany tylko dla w1 gdyz po wielu usprawnieniach funckja szukajaca i tak w kazdej warstwie zaczela wskazywac ten sam srodek, a funkcja ta bada kazda mozliwosc, co troche jej zajmuje
                
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

                #+wizualizacjiabezporawek
                if numerwarstwy==1:
                        obrazbezpop, plotenko = plt.subplots()
                        odlegloscisiatki = np.array(range(1,siatkacmdol));
                        Iksy,Igreki = np.meshgrid(odlegloscisiatki,odlegloscisiatki)
                        plt.plot(Iksy-0.5,Igreki-0.5, marker='+', color='white', linestyle='none')
                        kolko = plt.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)                
                        plotenko.add_artist(kolko)
                        pylab.imshow(wynikarraja2)


                
                #3d
                starynump2=np.ndarray(shape=(siatkacm,siatkacm,numerwarstwy))
                starynump2[:,:,:]=Apka.SLAJSY2
                Apka.SLAJSY2.resize((siatkacm,siatkacm,numerwarstwy+1))
                Apka.SLAJSY2[:,:,numerwarstwy]=wynikarraja2
                Apka.SLAJSY2[:,:,:numerwarstwy]=starynump2

                #odrzucenie skjajnych
                pozycjawx=0
                while pozycjawx<siatkacm:
                        pozycjawy=0
                        while pozycjawy<siatkacm:
                                tales1=(pozycjawx-srodekkolkay+0.5)**2 + (pozycjawy-srodekkolkax+0.5)**2#zamienione celowo, bo gdzies indziej tez sie zamienilo
                                tales2=(pozycjawx-srodekkolkay+0.5)**2 + (pozycjawy-srodekkolkax-0.5)**2
                                tales3=(pozycjawx-srodekkolkay-0.5)**2 + (pozycjawy-srodekkolkax+0.5)**2
                                tales4=(pozycjawx-srodekkolkay-0.5)**2 + (pozycjawy-srodekkolkax-0.5)**2
                                if tales1>=(srednicafantomu/2)**2 or tales2>=(srednicafantomu/2)**2 or tales3>=(srednicafantomu/2)**2 or tales4>=(srednicafantomu/2)**2 :
                                        wynikarraja2[pozycjawx,pozycjawy]=0
                                pozycjawy+=1
                        pozycjawx+=1
                #+wizualizacjia
                if numerwarstwy==1:
                        obrazwkwadratyzkolem, plotno = plt.subplots()
                        odlegloscisiatki = np.array(range(1,siatkacmdol));
                        Iksy,Igreki = np.meshgrid(odlegloscisiatki,odlegloscisiatki)
                        plt.plot(Iksy-0.5,Igreki-0.5, marker='+', color='white', linestyle='none')
                        kolko = plt.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)
                        plotno.add_artist(kolko)
                        pylab.imshow(wynikarraja2)


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
                        print ("nr of ROIs per slice: %d" % len(tabelawartoscibez0))

                if tabelawartoscibez0!=[]:
                        #nowynump[:,:,:numerwarstwy]=Apka.SLAJSY1
                        #Apka.SLAJSY1.reshape(())
                        #Apka.SLAJSY1=starynump

                        starynump3=np.ndarray(shape=(siatkacm,siatkacm,numerwarstwy))
                        #if Apka.SLAJSY1.any()!=0:
                        starynump3[:,:,:]=Apka.SLAJSY3
                        Apka.SLAJSY3.resize((siatkacm,siatkacm,numerwarstwy+1))
                        Apka.SLAJSY3[:,:,numerwarstwy]=wynikarraja2
                        Apka.SLAJSY3[:,:,:numerwarstwy]=starynump3

                        numerwarstwy+=1

        if tabelawartoscibez0VOL!=[]:
                print ("nr of total ROIs in Volume: %d" % len(tabelawartoscibez0))
                print ("przyklad: rys 1=RAW data, 2=converted na siatke 10mm, 3=converted+wyzerowanie wszystkiego poza fantomem")
                print ("indeks non-uniformity bazuje na niezerowych wartosciach z danych przedstawionych w obrazie 3")
                





                kolko = plt.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)
                figurka3, Apka.ax3 = plt.subplots(1, 1)
                Apka.ax3.add_artist(kolko)
                #figurka.add_subplot(siateczka)
                tracker3 = przegladacz.IndexTracker(Apka.ax3, Apka.SLAJSY3)
                figurka3.canvas.mpl_connect('scroll_event', tracker3.onscroll)

                kolko = plt.Circle((srodekkolkax,srodekkolkay),srednicafantomu/2, color='r', fill=False)
                figurka2, Apka.ax2 = plt.subplots(1, 1)
                Apka.ax2.add_artist(kolko)
                #figurka.add_subplot(siateczka)
                tracker2 = przegladacz.IndexTracker(Apka.ax2, Apka.SLAJSY2)
                figurka2.canvas.mpl_connect('scroll_event', tracker2.onscroll)

                #tk.Tk().withdraw()

                                
                #p = multiprocessing.Process(target=bgTestNU_PET.powrotzmartwych, args=(Apka.grid_slaves(),Apka))
                #jobs.append(p)
                #p.start()
                plt.show()
                #plt.show(tracker2)


                """
                pylab.show()
                plt.clf()
                root.update()
                """
        
