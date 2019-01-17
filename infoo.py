# -*- coding: utf-8 -*-
from tkinter import messagebox as tkMessageBox

def informacja(self):
        tkMessageBox.showinfo("Test jednorodnosci fantomu PET","Pliki dicom powinny nazywac sie XXX1.dcm, XXX2.dcm itd, powinny byc w jednym folderze. Założony został fantom o średnicy 17.5 cm.\n\n Postepowanie: \n1. Za pomoca opcji 'Znajdz *.dcm' nalezy wybrac sciezke do folderu zawierajacego pliki DICOM. Jezeli folder bedzie zawieral takowe, program potwierdzi to stosownym komunikatem. \nJEZELI nie zostanie wybrana sciezka, program bedzie bazowal na folderze z ktorego zostal uruchomiony. \n2. W celu obliczenia jednorodnosci wszystkich warstw (wszystkich .dcm) we wskazanym folderze z punktu 1., nalezy kliknac 'oblicz NU'. Proces ten moze zajac do paru minut, w przypadku wielu warstw. \n3. Plik 'logBGPetTest.txt' z informacjami odnosnie testu zostanie utworzony (lub nadpisany, gdy juz istnieje) w folderze wybranym w punkcie 1. \n4. Dla pogladowej wizualizacji obrobki danych zapisanych jako obraz w formacie DICOM nalezy wybrac opcje 'przegladaj warstwy'. \n[5. <under construction> opcja 'stworz raport .tex' tworzy przykladowy kod do wrzucenia do Latex'a ALE nic pozatym.] \n\nStworzone przez Bartłomieja Gawełczyka, z użyciem darmowych modułów pythonowskich :) ")


