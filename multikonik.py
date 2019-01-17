import multiprocessing
from time import time as czasteraz #downloaded
import workery

def multikonikuwio(siatkacm,srednicafantomu,wynikarraja2):
        czasik1=czasteraz()
        print ("multiprocessing!")
        #global manager1
        """
        return_maksymalniekolko = []#?
        return_dictY = []
        return_dictX = []#?
        """
        liczbaprocesow=7



        #z przykladu probamulti.py
        manager = multiprocessing.Manager()
        return_dictY = manager.dict()
        return_dictX = manager.dict()
        return_maksymalniekolko = manager.dict()
        jobs = []
        print ("szukanie srodka fantomu (to moze troche potrwac)")
        for i in range(liczbaprocesow):
                print ("dodaje proces nr ", i)
                p = multiprocessing.Process(target=workery.workerszukaniesrodka, args=(i,liczbaprocesow,siatkacm,srednicafantomu,return_maksymalniekolko,return_dictY,return_dictX,wynikarraja2))
                #p = multiprocessing.Process(target=workery.workerszukaniesrodka2, args=(return_maksymalniekolko,return_dictY,return_dictX))
                jobs.append(p)
                p.start()
        for job in jobs:
                
                job.join()
        #suma=+suma1
        #print return_dict.values()
        #suma=0        
        #for i in range(0,2):
                #suma+=return_dict[i]





        #print "valueeee: ", return_maksymalniekolko.values()
        print ("valueeee: ", return_maksymalniekolko)
        vale=return_maksymalniekolko.values()
        maxzmax=vale.index(max(vale))
        #maxzmax=max(maksymalniekolko)lub z vale
        srodekkolkay=return_dictY[maxzmax]                
        srodekkolkax=return_dictX[maxzmax]        
        print ("srodek kola: x= %d ,y= %d (zalozenie, ze wymiary ROIa=1cm x 1cm)" %(srodekkolkax,srodekkolkay))
        czasik2=czasteraz()-czasik1
        print ("zajelo to: ", czasik2)
        return [srodekkolkay,srodekkolkax]
