
from tkinter import filedialog as tkFileDialog
from tkinter import messagebox as tkMessageBox
from os import listdir #niedownloaded

def szukaniedcm(Apka):

        Apka.sciezka=tkFileDialog.askdirectory(title="podaj sciezke do *.dcm")
        if Apka.sciezka=="":
                if Apka.sciezkapoprzednia=="":
                        return
                else:
                        Apka.sciezka=Apka.sciezkapoprzednia
        if Apka.sciezka.endswith("/"):
                pass
        else :
                Apka.sciezka+="/"
                
        print ("wczytana zawartosc folderu: %s" % Apka.sciezka)
        Apka.sciezkapoprzednia=Apka.sciezka        
        listafolderu=[]
        if Apka.sciezka!="":
                for file in listdir(Apka.sciezka):
                        if file.endswith(".dcm"):
                                listafolderu.append(file)
                if listafolderu==[]:
                        print ("nie znalazlem plikow .dcm w tym folderze")
                        tkMessageBox.showinfo("Pusto tutaj...","nie znalazlem plikow .dcm w podanym folderze")
                        Apka.sciezka=""
                        
        if listafolderu!=Apka.listafolderu2:
                Apka.listafolderu2=listafolderu
                if listafolderu:
                        #Apka.probnanazwa
                        Apka.probnanazwa=min(listafolderu)
                        print ("znaleziono *.dcm")
                        Apka.sciezkapoprzednia==Apka.sciezka
                        tkMessageBox.showinfo("Znalazlem!","znaleziono *.dcm w folderze: \n %s" %Apka.sciezka)
