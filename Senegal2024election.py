# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 02:31:52 2024

@author: IAN CARTER KULANI
"""

#This software prompts the user to enter total number of published centers, total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward, it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.

print("==============================SENEGAL 2024 PRESIDENTIAL ELCTION==============================\n") 

Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered voters
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Valid Votes For Bassirous Diomaye Faye
Totalvalidvotesfor_Bassirous_Diomaye_Faye=int(input("Enter Total Valid For Bassirous Diomaye Faye:"))
#Get Total Valid Votes For Amadou Ba
Totalvalidvotesfor_Amadou_Ba=int(input("Enter Total Valid Votes For Amadou Ba:"))
#Get Total Valid Votes For Aliou Mamadou Dia
Totalvalidvotesfor_Aliou_Mamadou_Dia=int(input("Enter Total Valid Votes For Aliou Mamadou Dia:"))
#Get Total Valid Votes For Khalifa Sall
Totalvalidvotesfor_Khalifa_Sall=int(input("Enter Total Valid Votes For Khalifa Sall:")) 
#Get Total Valid Votes For Idrissa Seck
Totalvalidvotesfor_Idrissa_Seck=int(input("Enter Total Valid Votes For Idrissa Seck:"))
#Get Total Valid Votes For Thierno Alassane Sall
Totalvalidvotesfor_Thierno_Alassane_Sall=int(input("Enter Total Valid Votes For Thierno Alassane Sall:"))
#Get Total Valid Votes For Boubacar Camara
Totalvalidvotesfor_Boubacar_Camara=int(input("Enter Total Valid Votes For Boubacar Camara:"))
#Get Total Valid Votes For Aly Ngouille Ndiaye
Totalvalidvotesfor_Aly_Ngouille_Ndiaye=int(input("Enter Total Valid Votes For Aly Ngouille Ndiaye:"))
#Get Total Valid Votes For Papa Djibril Fall
Totalvalidvotesfor_Papa_Djibril_Fall=int(input("Enter Total Valid Votes For Papa Djibril Fall:"))
#Get Total Valid Votes For Serigne Mboup
Totalvalidvotesfor_Serigne_Mboup=int(input("Enter Total Valid Votes For Serigne Mboup:"))
#Get Total Valid Votes For Dethie Fall
Totalvalidvotesfor_Dethie_Fall=int(input("Enter Total Valid Votes For Dethie Fall:"))
#Get Total Valid Votes For Daouda Ndiaye
Totalvalidvotesfor_Daouda_Ndiaye=int(input("Enter Total Valid Votes For Daouda Ndiaye:"))
#Get Total Valid Votes For Anta Babocar Ngom
Totalvalidvotesfor_Anta_Babocar_Ngom=int(input("Enter Total Valid Votes For Anta Babocar Ngom:"))
#Get Total Valid Votes For Cheikh Tidians Dieye
Totalvalidvotesfor_Cheikh_Tidians_Dieye=int(input("Enter Total Valid Votes For Cheikh Tidians Dieye:"))
#Get Total Valid Votes For Momadou Diao
Totalvalidvotesfor_Momadou_Diao=int(input("Enter Total Valid Votes For Momadou Diao:"))
#Get Total Valid Votes For Mamadou Lamine Diallo
Totalvalidvotesfor_Mamadou_Lamine_Diallo=int(input("Enter Total Valid Votes For Mamadou Lamine Diallo:"))
#Get Total Valid Votes For Mahammed Dionne
Totalvalidvotesfor_Mahammed_Dionne=int(input("Enter Total Valid Votes For Mahammed Dionne:"))
#Get Total Valid Votes For Malick Gakou
Totalvalidvotesfor_Malick_Gakou=int(input("Enter Total Valid Votes For Malick Gakou:"))
#Get Total Valid Votes For  Habib Sy
Totalvalidvotesfor_Habib_Sy=int(input("Enter Total Valid Votes For Habib Sy:"))
percent=100

if Totalvalidvotesfor_Bassirous_Diomaye_Faye>Totalvalidvotes/2+1:
   print("Congratulations Bassirous Diomaye Faye  you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Amadou_Ba>Totalvalidvotes/2+1:
   print("Congratulations Amadou Ba  you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Aliou_Mamadou_Dia>Totalvalidvotes/2+1:
   print("Congratulations  Aliou Mamadou Dia you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Khalifa_Sall>Totalvalidvotes/2+1:
       print("Congratulations Atupele Muluzi you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Idrissa_Seck>Totalvalidvotes/2+1:
   print("Congratulations Idrissa Seck you're the winner of 2014 presidential Election")

elif Totalvalidvotesfor_Thierno_Alassane_Sall>Totalvalidvotes/2+1:
       print("Congratulations Thierno Alassane Sall you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Boubacar_Camara>Totalvalidvotes/2+1:
   print("Congratulations Boubacar Camara you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Aly_Ngouille_Ndiaye>Totalvalidvotes/2+1:
       print("Congratulations Aly Ngouille Ndiaye you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Papa_Djibril_Fall>Totalvalidvotes/2+1:
   print("Congratulations Papa Djibril Fall you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Serigne_Mboup>Totalvalidvotes/2+1:
   print("Congratulations Serigne Mboup you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Dethie_Fall>Totalvalidvotes/2+1:
       print("Congratulations Dethie Fall you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Daouda_Ndiaye>Totalvalidvotes/2+1:
   print("Congratulations Daouda Ndiaye you're the winner of 2024 presidential Election")


elif Totalvalidvotesfor_Anta_Babocar_Ngom>Totalvalidvotes/2+1:
       print("Congratulations Anta Babocar Ngom you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Cheikh_Tidians_Dieye>Totalvalidvotes/2+1:
   print("Congratulations Cheikh Tidians Dieye  you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Momadou_Diao>Totalvalidvotes/2+1:
       print("Congratulations Momadou Diao you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Mamadou_Lamine_Diallo>Totalvalidvotes/2+1:
   print("Congratulations Mamadou Lamine Diallo you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Mahammed_Dionne>Totalvalidvotes/2+1:
   print("Congratulations Mahammed Dionne you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Malick_Gakou>Totalvalidvotes/2+1:
       print("Congratulations Malick Gakou   you're the winner of 2024 presidential Election")

elif Totalvalidvotesfor_Habib_Sy>Totalvalidvotes/2+1:
   print("Congratulations Habib Sy you're the winner of 2024 presidential Election")

else:
    print("No majority winner was found RUNOF may be required Thank you.\n\n")


print("_________________________________ELECTION STATISTICS_____________________________________\n\n")
#Calculating percentage
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout 
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void in percentage=",Percentage)
#Calculating percentage for Bassirous Diomaye Faye 
Percentage=round(Totalvalidvotesfor_Bassirous_Diomaye_Faye*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Bassirous Diomaye Faye in percentage=",Percentage)
#Calculating percentage for Amadou Ba
Percentage=round(Totalvalidvotesfor_Amadou_Ba*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Amadou Ba in percentage=",Percentage)
#Calculating percentage for Aliou Mamadou Dia
Percentage=round(Totalvalidvotesfor_Aliou_Mamadou_Dia*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Aliou Mamadou Dia in percentage=",Percentage)
#Calculating percentage for Khalifa Sall
Percentage=round(Totalvalidvotesfor_Khalifa_Sall*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Khalifa Sall in percentage=",Percentage)
#Calculating percentage for Idrissa Seck
Percentage=round(Totalvalidvotesfor_Idrissa_Seck*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Idrissa Seck in percentage=",Percentage)
#Calculating percentage for Thierno Alassane Sall
Percentage=round(Totalvalidvotesfor_Thierno_Alassane_Sall*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Thierno Alassane Sall percentage=",Percentage)
#Calculating percentage for Boubacar Camara
Percentage=round(Totalvalidvotesfor_Boubacar_Camara*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Boubacar Camara in percentage=",Percentage)
#Calculating percentage for Aly Ngouille Ndiaye
Percentage=round(Totalvalidvotesfor_Aly_Ngouille_Ndiaye*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Aly Ngouille Ndiaye in percentage=",Percentage)
#Calculating percentage for Papa Djibril Fall
Percentage=round(Totalvalidvotesfor_Papa_Djibril_Fall*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Papa Djibril Fall in percentage=",Percentage)
#Calculating percentage for Serigne Mboup
Percentage=round(Totalvalidvotesfor_Serigne_Mboup*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Serigne Mboup in percentage=",Percentage)
#Calculating percentage for Dethie Fall
Percentage=round(Totalvalidvotesfor_Dethie_Fall*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Dethie Fall in percentage=",Percentage)
#Calculating percentage for  Daouda_Ndiaye
Percentage=round(Totalvalidvotesfor_Daouda_Ndiaye*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Daouda Ndiaye in percentage=",Percentage)
#Calculating percentage for Anta_Babocar_Ngom
Percentage=round(Totalvalidvotesfor_Anta_Babocar_Ngom*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Anta Babocar Ngom percentage=",Percentage)
#Calculating percentage for Cheikh_Tidians_Dieye
Percentage=round(Totalvalidvotesfor_Cheikh_Tidians_Dieye*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Cheikh Tidians Dieye in percentage=",Percentage)
#Calculating percentage for Momadou Diao
Percentage=round(Totalvalidvotesfor_Momadou_Diao*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Momadou Diao in percentage=",Percentage)
#Calculating percentage for Mamadou Lamine Diallo
Percentage=round(Totalvalidvotesfor_Mamadou_Lamine_Diallo*percent/Totalvalidvotes, 2);
print("Total Valid Votes Mamadou Lamine Diallo in percentage=",Percentage)
#Calculating percentage for Mahammed Dionne
Percentage=round(Totalvalidvotesfor_Mahammed_Dionne*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Mahammed Dionne in percentage=",Percentage)
#Calculating percentage for Malick Gakou
Percentage=round(Totalvalidvotesfor_Malick_Gakou*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Malick Gakou in percentage=",Percentage)
#Calculating percentage for Habib Sy
Percentage=round(Totalvalidvotesfor_Habib_Sy*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Habib Sy in percentage=",Percentage)


print("==========================================================================================\n\n") 































