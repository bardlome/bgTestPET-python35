import tkinter as tk
import szukamydicoma
import obliczamy
import texpdf
import infoo
import wizja

def tworzenieguzikow(Apka):
        Apka.szukaniedcm1 = tk.Button(Apka)
        Apka.szukaniedcm1["text"] = "Znajdz *.dcm"
        Apka.szukaniedcm1["command"] = lambda: szukamydicoma.szukaniedcm(Apka)
        Apka.szukaniedcm1.pack({"padx": "3"})
        Apka.szukaniedcm1.pack({"pady": "0"})
        Apka.szukaniedcm1.pack({"side": "left"})


        Apka.oblicznui1 = tk.Button(Apka)
        Apka.oblicznui1["text"] = "oblicz NU"
        Apka.oblicznui1["command"] = lambda: obliczamy.oblicznui(Apka.chcemymulti,Apka.probnanazwa,Apka.pixyniejednorodne3,Apka.sciezka,Apka.wynik1)
        Apka.oblicznui1.pack({"padx": "3"})
        Apka.oblicznui1.pack({"pady": "0"})
        Apka.oblicznui1.pack({"side": "left"})

        Apka.ogladanie1 = tk.Button(Apka)
        Apka.ogladanie1["text"] = "przegladaj warstwy"
        Apka.ogladanie1["command"] = lambda: wizja.ogladanie(Apka)
        Apka.ogladanie1.pack({"padx": "3"})
        Apka.ogladanie1.pack({"pady": "0"})
        Apka.ogladanie1.pack({"side": "left"})

        Apka.pdfreport1 = tk.Button(Apka)
        Apka.pdfreport1["text"] = "stworz raport .tex"
        Apka.pdfreport1["command"] = lambda: texpdf.pdfreport(Apka)
        Apka.pdfreport1.pack({"padx": "3"})
        Apka.pdfreport1.pack({"pady": "0"})
        Apka.pdfreport1.pack({"side": "left"})

        Apka.informacja1 = tk.Button(Apka)
        Apka.informacja1["text"] = "INFO"
        Apka.informacja1["command"] = lambda: infoo.informacja(Apka)
        Apka.informacja1.pack({"padx": "3"})
        Apka.informacja1.pack({"pady": "0"})
        Apka.informacja1.pack({"side": "left"})

        Apka.QUIT = tk.Button(Apka)
        Apka.QUIT["text"] = "Wyjscie"
        Apka.QUIT["fg"]   = "red"
        Apka.QUIT["command"] =  lambda: Apka.quit()
        Apka.QUIT.pack({"padx": "3"})
        Apka.QUIT.pack({"side": "right"})
        Apka.QUIT.pack({"pady": "0"})
