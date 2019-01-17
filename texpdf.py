# -*- coding: utf-8 -*-
import datetime
from tkinter import messagebox as tkMessageBox
def pdfreport(Apka):
        #pedeef=open("/home/gate/Desktop/fantom/raportpet.tex","w")
        #proc = subprocess.Popen(['pdflatex', pedeef])
        #proc.communicate()
        #system("pdflatex raportpet.tex")
        print ("schemat")
        schemat = r"""
        \documentclass{article}
        \usepackage[utf8]{inputenc}
        \title{Raport przyklad}
        \author{bard3lome }
        \usepackage{graphicx}
        \begin{document}
        \section{}
        \begin{center}
        \begin{flushleft}
        \begin{minipage}{140pt}
        includegraphics[scale=0.7]{universe}
        \end{minipage}
        \end{flushleft}
        \begin{flushright}\vspace{-40pt}
        \begin{minipage}{80pt}
        Gliwice, DATA
        \end{minipage}
        \end{flushright}
        \end{center}
        \vspace{50pt}
        \begin{center}
        {\fontsize{16pt}{1pt}\selectfont Raport z testu kontroli jakości PET}
        \end{center}
        \paragraph{}Raport został sporzadzony jako efekt testów przeprowadzonych w dniu DATA. Obejmował niżej wymienione testy:
        \begin{itemize}
        T1+
        \end{itemize}
        \paragraph{}Wyniki testów widoczne są poniżej:
        \begin{table}[h!]
        \centering
        \begin{tabular}{|c|c|}
        \hline
        Nazwa testu&        Rezultat\\ \hline
        Uniformity of the reconstructed image&    RESULT1\\ \hline
        Jakis inny test&    RESULT2\\ \hline
        Jeszcze inny test&    RESULT3\\ \hline
        \end{tabular}
          \label{table:wydajnosc}
        \end{table}    
        \end{document}

        """

        print (schemat)

        print ("ustalam wyniki")        
        ustalamw=schemat.find('DATA')
        schemat=schemat[:ustalamw] + datetime.date.today().strftime("%d-%m-%Y") + schemat[ustalamw+4:]
        ustalamw=schemat.find('T1+')
        t1=""
        t2=""
        t3=""
        if Apka.wynik1!="Not performed":
                t1="   \item Uniformity of the reconstructed image \n"
        if Apka.wynik2!="Not performed":
                t2="   \item Jakis inny test \n"
        if Apka.wynik3!="Not performed":
                t3="   \item Jeszcze inny test \n"

        schemat=schemat[:ustalamw] + t1 + t2 + t3 + schemat[ustalamw+3:]        
        ustalamw=schemat.find('RESULT1')
        schemat=schemat[:ustalamw] + Apka.wynik1 + schemat[ustalamw+7:]
        ustalamw=schemat.find('RESULT2')
        schemat=schemat[:ustalamw] + Apka.wynik2 + schemat[ustalamw+7:]
        ustalamw=schemat.find('RESULT3')
        schemat=schemat[:ustalamw] + Apka.wynik3 + schemat[ustalamw+7:]
        print ("usuwam taby")        
        ustalamw=schemat.find('\t')
        while ustalamw!=-1:        
                schemat=schemat[:ustalamw] + schemat[ustalamw+1:]
                ustalamw=schemat.find('\t')
        """print "usuwam enki"        
        ustalamw=schemat.find('\n')
        while ustalamw!=-1:        
                schemat=schemat[:ustalamw] + schemat[ustalamw+1:]
                ustalamw=schemat.find('\n')"""
        print ("zapisuje tex")

        #pdf, info = texcaller.convert(latex, 'LaTeX', 'PDF', 5)

        pedeef=open(Apka.sciezka+"raportpet.tex","w")
        pedeef.write(schemat)
        pedeef.close()
        tkMessageBox.showinfo("Skonczylem!","Plik Tex gotowy")
        
        """
        schemat2 = schemat.decode('utf8')
        latexowy=latex.escape(schemat2, fold_newlines=True)
        latex.build.build_pdf(self, latexowy)
        """

        #latexpages.make(Apka.sciezka+"raportpet.tex")#(config, processes=None, engine=None, cleanup=True, only=None)
        """
        schemat2 = schemat.decode('utf8')
        #schemat3 = schemat2.encode('cp1250')
        zawartoscdopdf = texconvert(schemat2, 'LaTeX', 'PDF', 5)
        pedeef2=open(Apka.sciezka+"raportpet.pdf","w")
        pedeef2.write(zawartoscdopdf)
        pedeef2.close()
        tkMessageBox.showinfo("Skonczylem!","Plik pdf gotowy")
        """

