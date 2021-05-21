from array import array
from decimal import FloatOperation
import re # Regular expression word 
import os #Operating system onboard 
import glob
import subprocess
import typing_extensions
from PyPDF2.generic import FloatObject
from numpy import left_shift #Subprocess for processing the command and extract string from the terminal
import camelot # Extract the data table from the pdf file
from PyPDF2 import PdfFileWriter, PdfFileReader
import wordninja
import json
import pandas as pd
os.system("echo 'Rkj3548123' | sudo -S mkdir ComponentDoc") # Get the documentation of the components 
os.system("echo 'Rkj3548123' | sudo -S mkdir tempolarydocextract") #Get the data extract from the table of the pdf part specification
os.system("echo 'Rkj3548123' | sudo -S mkdir Configuresearch") #Create the configure file for the search in json 
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 ComponentDoc") # Activate the permission 
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 tempolarydocextract") # Activate the permission
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 Configuresearch") # Activate the permission
username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
PATHMAIN = "/home/"+str(Getusername)+"/Automaticsoftware/ComponentDoc"
HOME = "/home/"+str(Getusername)+"/Automaticsoftware/"
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# List file in the path directory on each 
listMainpath = os.listdir(PATHMAIN)  #Get the main path of the directory 
listExtract = os.listdir(EXTRACT)    #Get the extraction of the data tables in the component information pins configurection 
listConfig = os.listdir(CONFIG) #Get the list config file from the system 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
output = PdfFileWriter()
input1 = PdfFileReader(open(PATHMAIN+"/"+"drv8320.pdf", "rb"))  #using oslist dir readding the file and extract all the value in the loop 
inputcomp = "drv8320" # Get the component input data 
Pathdata = EXTRACT+"/"+str(inputcomp)
# Pins search continued function for long range pins configurection 
searchpinsconfiguretion = "Pin Configuration and Functions"
searchConfigcontinued = "Pin Functions (continued)"
searchSpecification = "Absolute Maximum Ratings"  # Get the specifications page and break from the pins configuretion and functions
specificationExtract = ""
# print how many pages input1 has:
print("document1.pdf has %d pages." % input1.getNumPages())
#for page in input1.pages:
         
#            print(page,page.extractText())
#first_page = input1.getPage(3)
#print(first_page.extractText())
#print(wordninja.split(str(first_page.extractText())))
listConfig = os.listdir(CONFIG) #Get the config file 
Pageclassification = [] # Save the page classification for predeict the next page output from the boundary configuretion on the json file
Packagecheck = []  # Checking the len of the list package 
Pinsquantity = []  # Get the quantity of the pins on the ic 
reforder =  []  #Save the reference breakpage order  
predictorder = [] #Save the 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        #list devices bugget and combine for the table data type page processing
Devicesname = [] #Getting the devices name paring
Devicelist = {} #Get the list dictionary of paring group device package name 
Deviceodd = [] #Getting the device odd 
Deviceeven = [] #Getting the device even 
Devicesbucket = [] # Device bucket for the page processing 
Packagetypebucket = [] #Package type for the page processing 
Pinsbucket = [] # Getting the pins bucket data for the value of each package type data combination dictionary
reftabledetect = [] # Get the table detector referent inside the array 
refpins = [] #Get the reference pins 
refpagecal = [] # Get the referent page from the page classification algorithm
nextpage = [] #Get the prediction page 
Specpage = [] #Get the spec page data 
combinedictdata = {}  # Get the dictionarylist of the data output for page processingfunction 
Predictbreak = {} # Get the reference page and prediction page for 
Pinsextract = {} # Generate the dictionary for the page reference and the next page prediction 
csvmergepare = {} #Generate the paring csv for merging page data 
Paringlist = [] #Getting the list inside the key of the csv merge page 
Dataodd = [] #Getting the data odd 
Dataeven = [] #Getting the data even
Drifgroup = {} #Get the drif group from the table to recombine with the other directory 
Normalgroup = [] #Get the the normal group list for regrouping with the drif group
Regrouping = {} #The last grouping for the path copy renew directory for merching new order csv file
Basedir = [] #Get the base dir for modify the new directory for new group order 
Newdir = [] #Get the new directory list for putting the fileinto the group 
memdat = [] #Getting the memory of 
Packageslist  = open(CONFIG+"/"+listConfig[0],'r')# Reading the configfile 
Packagedatalist = Packageslist.readline()
PackagesLoad = json.loads(Packagedatalist)

print(PackagesLoad.get('package').get('packagesdrawing')) #Get the package of the ic for adding into the list detected 
def Pagecalculation(outputinterger): 
   if int(outputinterger) <= 144:
          print("In the range of package pins=",outputinterger)
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Put the page calculation here for the 
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")
def Modeextractnotable(datapins,df,listdata,q): 

                  if str(listdata[q]).split(" ")[0] in datapins:
                          print("Found the header",listdata[q],"Begin extraction....") # Activate actraction begin 
                          for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])

                  if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Pinsquantity.append(str(df[listdata[q]].values[i])))
def Modeextracttion(datapins,transfer,df,listdata,q):
               # TI pattern pinconfigureation table 
               # Pins configure 

                 
                  devicename = transfer.get("Device").get("devices") #Extracting the pins name from the TI 
                  packagedevice = transfer.get("Device").get("packagedata") # Get the Description text 
                  pinsnumber = transfer.get("Device").get("pins") #Get the pins number from the device package from the pdf file
                  Devices = ['Device']
                  Package = ['Package\nType']
                  Pinsnumber = ['Pins']
                  if datapins[0] == "Device":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Devicesbucket.append(str(df[listdata[q]].values[i])))
                  if datapins[0] == "Package\nType":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Packagetypebucket.append(str(df[listdata[q]].values[i]))) 
                  if datapins[0] == "Pins":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Pinsbucket.append(str(df[listdata[q]].values[i]))) 
#Bit bucket for the combine                                                      
def Bucketcombinefunc(devicesinput,Packagetypebucket,Pinsbucket): # Get the list from each package input  
       print("Combine each package datainto the dict") # The function to combine the dictionary file into the dictionary 
       for qw in range(0,len(devicesinput)):  # using qw to get the value in the list array 
                   print("Begin creating the dictionary data function") 
                   combinedictdata[str(devicesinput[qw])] = str(Packagetypebucket[qw])+","+str(Pinsbucket[qw])  #Get the list variable to generate the json and dictionary data structure                  
                   
def extractionalgorithm(df,listdata,configfile):
          # In the case not detected table running this function 
          try: 
              print(configfile)
              data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
              datas = data.readline()
              transfer = json.loads(datas)
              print(transfer)
          except:
              print("Not found the configure file please check again")

          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # TI pattern for the extraction

          datapins = transfer.get("Unnamed").get("Unnamed") #Extracting the pins name from the TI 
          description = transfer.get("Description").get("description") # Get the Description text 
          inputoutput = transfer.get("IO").get("io") #IO get the input output pins function matching pins
          print(inputoutput)
          print(description)
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Pins configure 
          for q in range(0,len(listdata)): 
                  
                  Modeextractnotable(datapins, df, listdata, q),Modeextractnotable(description, df, listdata, q),Modeextractnotable(datapins, df, listdata, q) 
def extractpinspackage(df,listdata,configfile): 
           print("Begin extraction the pins and package from the package information page")
           try: 
              print(configfile)
              data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
              datas = data.readline()
              transfer = json.loads(datas)
              print(transfer)
           except:
              print("Not found the configure file please check again")

          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # TI pattern for the extraction

           devicename = transfer.get("Device").get("devices") #Extracting the pins name from the TI 
           packagedevice = transfer.get("Device").get("packagedata") # Get the Description text 
           pinsnumber = transfer.get("Device").get("pins") #Get the pins number from the device package from the pdf file
           print(devicename)  # Using the first one as the key 
           print(packagedevice) # First value 
           print(pinsnumber) # Second value 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Pins configure 
           listMode = [['Device'],['Package\nType'],['Pins']]            
           for q in range(0,len(listdata)):     
                  print(Modeextracttion(listMode[0],transfer,df,listdata,q))
           for q in range(0,len(listdata)): 
                  print(Modeextracttion(listMode[1], transfer, df, listdata, q))
           for q in range(0,len(listdata)): 
                  print(Modeextracttion(listMode[2], transfer, df, listdata, q))
def Tabledetector(intput1,inputcomp,Pinsquantity): 
        for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
         first_page = input1.getPage(i)
         print(first_page.extractText())
         print(wordninja.split(str(first_page.extractText())))
         outputdat = str(first_page.extractText())
         Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
         if 'PACKAGING'in Extracteddata: 
                   print("Found package")
                   if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 1")  
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              print(Pinsquantity.append(str(outputinterger)))
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)

                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  if len(tables) >= 1:
                                         #Data table found then classify and extract the pins and packages 
                                         print("Found the data table",len(tables)) 
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractpinspackage(df,listdata,listConfig[0])
                                  break
         if 'PACKAGE'in Extracteddata: 
                   print("Found package")
                   if 'MATERIALS' in Extracteddata: 
                           print("Found Material")
                           if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 2")
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   print(outputinterger)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(wordninja.split(str(outputinterger)))
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")

                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         print(wordninja.split(str(outputinterger)))
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                              if outputinterger <=144: 
                                                                     print("In the ranage of the package pins",outputinterger) 
                                                                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                                    #Get the page calculation here  
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                              if outputinterger <= 144:
                                                                      print("In the range of package pins",outputinterger)
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                   break                                       
                                          except:
                                             print("This part is not found in the list package")  
                                  if len(tables) >= 1:
                                         print("Found the data table",len(tables))
                                         reftabledetect.append(str(len(tables))) # checking the len after fererence if found then equal 1 
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractpinspackage(df,listdata,listConfig[0])
                                  break
def CheckingPins(input1):
       for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
         first_page = input1.getPage(i)
         print(first_page.extractText())
         print(wordninja.split(str(first_page.extractText())))
         outputdat = str(first_page.extractText())
         Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
         if 'PACKAGING'in Extracteddata: 
                   print("Found package")
                   if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 1")
                                  for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)
                                                                      Packagecheck.append(outputinterger)
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  break
         if 'PACKAGE'in Extracteddata: 
                   print("Found package")
                   if 'MATERIALS' in Extracteddata: 
                           print("Found Material")
                           if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 2")
                                  for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   print(outputinterger)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(wordninja.split(str(outputinterger)))
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")

                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         print(wordninja.split(str(outputinterger)))
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              if outputinterger <=144: 
                                                                     print("In the ranage of the package pins",outputinterger) 
                                                                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                                    #Get the page calculation here  
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              if outputinterger <= 144:
                                                                      print("In the range of package pins",outputinterger)
                                                                      Packagecheck.append(outputinterger) #Get the output integer of the pins and save into the package check list to classify the pins 
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                   break                                       
                                          except:
                                             print("This part is not found in the list package")         
                                  break
def Pinsearchfunction(input1,inputcomp,searchpinsconfiguretion):   
               print("Searching pin configuretion page.....")
               for i in range(0,input1.getNumPages()):  # Running the page for the back checking 
                  first_page = input1.getPage(i)
                  print(first_page.extractText())
                  print(wordninja.split(str(first_page.extractText())))
                  outputdat = str(first_page.extractText())
                  Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
                  datasearch = str(searchpinsconfiguretion).split(" ") 
                  check2 = any(item in datasearch for item in Extracteddata)
                  packlist = PackagesLoad.get('package').get('rootpackages')
                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                  boundary = ['0','1','2']
                  check0 = any(item in list(str(i)) for item in boundary) # Setting default check bundary 
                  if check0 == False:
                      print("Check false page")
                      if check2 == True:
                                  print("Found the Pins configuretion","page",str(i))
                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                       #This is the starter page only ignite the starter loop 
                                  Packagecheck.append(str(i)) # Get the current page and detecting the other page in the search 
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)

                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  if len(tables) >= 1:
                                         print("Found the data table",len(tables))
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractionalgorithm(df,listdata,listConfig[0]) #running the function of the configuretion file function 

                                  break


                      break  
# Search specification function 
def SpecificationExtract(input1,inputcomp,searchSpecification): 
       print("Start the specification extraction....") #Specification page extraction 
       for i in range(3,input1.getNumPages()):  # Running the page for the back checking 
                  first_page = input1.getPage(i)
                  #print(first_page.extractText())
                  print(wordninja.split(str(first_page.extractText())))
                  outputdat = str(first_page.extractText())
                  Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
                  print(Extracteddata)
                  datasearch = str(searchSpecification).split(" ")
                  #check2 = any(item in datasearch for item in Extracteddata)
                  #print(check2)
                  #packlist = PackagesLoad.get('package').get('rootpackages')
                  #packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                  boundary = ['0','1','2']
                  check0 = any(item in list(str(i)) for item in boundary) # Setting default check bundary
                  print(check0)
                  if datasearch[0] in Extracteddata: 
                            print(str(i),Extracteddata)
                            Specpage.append(str(i)) #Toget the number of real page you need to +1 beacause it's started from 0
                            first_page = input1.getPage(i)
                            print(first_page.extractText()) 
                            break         
                                               

def Classifypagematch(input1,inputcomp,Pinsquantity,Packagecheck):
             print("Begin predict the next page")
             pageclassifylist = PackagesLoad.get("Pageclassify")
             #print(pageclassifylist)
             print(Packagecheck,Pinsquantity) # Show the input page variable and the pins quantity 
             val_list = list(pageclassifylist.values())  # Get the page classify list 
             print(val_list)
             for i in range(0,len(val_list)):
                    try: 
                        if int(val_list[i][0]) <= int(Pinsquantity[0]) <= int(val_list[i][1]): 
                           try:
                                 position = val_list.index(val_list[i])
                                 print("Array position",position)
                                 print(list(pageclassifylist)[position])
                                 if int(list(pageclassifylist)[position]) == 1:
                                         savenextpage = int(Packagecheck[0])+int(list(pageclassifylist)[position])-1
                                         Packagecheck.append(str(savenextpage))
                                         print(Packagecheck[0])      
                                         refpagecal.append(Packagecheck[0]) #Get the reference of the page  
                                 if int(list(pageclassifylist)[position]) >= 2:
                                         
                                         refpage =  int(Packagecheck[0])+int(list(pageclassifylist)[position])-1 # ref starter page 
                                         savenextpage = int(Packagecheck[0])+int(list(pageclassifylist)[position]) #Real page in the document 
                                         Packagecheck.clear() # Clear the recent page before append the new page 
                                         Packagecheck.append(str(savenextpage)) # Real page classification 
                                         print(refpage) # Get the reference starter page 
                                         print(Packagecheck[0])      
                                         refpagecal.append(refpage) #Get the reference of the page in array mode 
                                         #Pageclassification.append(refpagecal[0]) # replace the refernce page into the starter page
                                         nextpage.append(Packagecheck[0]) # Next page append  in array mode    
                                                                 
                                 break
                           except:
                               print("Not in the list",str(i))
                    except: 
                        print("Not in the list",str(i))       
def Classifyselectionfunction(input1,inputcomp,Pinsquantity,Packagecheck,reftabledetect,combinedictdata): #Get the reftable for setting the condition function and the combination dictionary data for get the key and value of the ic  
                    print("Classify the reference detection",str(reftabledetect))
                    if str(reftabledetect) == '1':
                           print("Detected table in the page")
                           for w in range(0,len(list(combinedictdata))):
                                     print("#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                     print(str(w),list(combinedictdata)[w])
                                     Devicesname.append(list(combinedictdata)[w]) #Getting the combine dictionary 
                                     pinsoutput = combinedictdata.get(str(list(combinedictdata)[w])).split(",")[1] # Get the pins out from the string to add the array value into the classification base 
                                     #Reference 
                                     refpins.append(pinsoutput)# add the reference pins and clear after running the new process 
                                     print("Pins number",refpins[0])
                                     Classifypagematch(input1,inputcomp,refpins,Packagecheck) #Get the refpins into the loop and calculate the page from the input estimation 
                                     #after add the estimation page delete the refpins to be ready for adding the new one
                                     refpins.clear() # Clear the refferent pins 
                                     print(refpagecal) # Adding the reference page int the array 
                                     #Getting the refpage and the predictpage 
                                     print("#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                     
                    if str(reftabledetect) == '0': 
                           print("Not detected table in the page") 
                           Classifypagematch(input1,inputcomp,Pinsquantity,Packagecheck) #Get the refpins into the loop and calculate the page from the input estimation 
def Devicenameparing(combinedictdata): #Device name paring function 
      print("Start paring devices name")
      Devicelist = list(combinedictdata)
      for i in range(0,len(Devicelist)):
                     if i%2 == 0: 
                          Deviceeven.append(Devicelist[i])
                          print("Device even:",Deviceeven)
                     if i%2 == 1: 
                          Deviceodd.append(Devicelist[i])
                          print("Device odd",Deviceodd)
def Groupingdevicelist(Deviceeven,Deviceodd):
      try:                
          for kr in range(0,len(Deviceeven)):
                  Devicelist[str(kr)] = str(Deviceeven[kr]) +","+str(Deviceodd[kr])
      except:
            print("Out of range")
            if len(Deviceeven) > len(Deviceodd): 
                   print("Paring add new order in group....")
                   print(str(Deviceeven[len(Deviceeven)-1]))
                   Devicelist[str(len(Deviceodd))] = str(Deviceeven[len(Deviceeven)-1])
                   print(Devicelist)
                   
            if len(Deviceeven) < len(Deviceodd): 
                   print("Paring add new order in group....")     
                   Devicelist[str(len(Deviceeven))] = str(Deviceodd[len(Deviceodd)-1])
                   print(Deviceodd)

def SavebreakPinsconfigtable(referencepage,predictnextpage,Specpage): # Getting the page reference and predict page specpage input 
       print("Start save breaking pinsconfig......")  # Breaking end configuretion page 
       for s in range(0,len(referencepage)):
                  print("Starting.....") #Getting the page comparation into the loop 
                  try:
                     reforder.append(str(referencepage[s]))     
                     predictorder.append(str(predictnextpage[s]))     #Running until found the break order 
                  
                     if int(referencepage[s]) == int(Specpage[0]): 
                              print(referencepage[s]) #reference page compare specpage number 
                              reforder.remove(reforder[s])
                              break 
                     if int(predictnextpage[s]) == int(Specpage[0]): 
                              print(predictnextpage[s])
                              predictorder.remove(predictnextpage[s])
                              break
                  except: 
                       print("No need table paring !")          

def Retrivepage(reforder,predictorder):
           print("Retrieving page order")
           for r in range(0,len(reforder)): 
                     print("Create the dictionary....")
                     try: 
                         Predictbreak[str(r)] = str(reforder[r])+","+ str(predictorder[r])  #Make the dictionary porder prediction list for textracting the certain devices 
                         print(Predictbreak) # Show the predict page dictionary
                     except: 
                           print("Out of range list...") # Find the outrange dictionary and add the value into the dictionary list
                           if len(reforder) < len(predictorder):
                              Predictbreak[str(len(predictorder)-1)] = str(predictorder[len(predictorder)-1])
                              print(Predictbreak)
                           if len(reforder) > len(predictorder): 
                              Predictbreak[str(len(reforder)-1)] = str(reforder[len(reforder)-1])
                              print(Predictbreak)    

def Groupingpinextractor(Pathway,pagevalue,tables,varm,megaposition): 
         tables[int(len(tables))-int(varm)].df
         print("Found the data table",len(tables))
         print(tables[int(len(tables))-int(varm)].df)
         print(tables[int(len(tables))-int(varm)].parsing_report)
         tables[int(len(tables))-int(varm)].to_csv(Pathway +"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(megaposition)+'.csv') 
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         print("Reading pandas....")
         df = pd.read_csv (r''+Pathway+"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(megaposition)+'.csv')
         print(df)
         print(Configure(listConfig[0])) # Get the data from the json file
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         # Algorithm for classify the extraction of the text 
         index = df.index
         number_of_rows = len(index)
         print(number_of_rows)
         listdata = list(df.columns.values)
         print(listdata)
def Grouploopanalysis(Pathway,pagevalue,tables):
   for i in range(0,len(tables)): 
         tables[i].df
         print("Found the data table",len(tables))
         print(tables[i].df)
         print(tables[i].parsing_report)
         tables[i].to_csv(Pathway +"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(i)+'.csv') 
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         print("Reading pandas....")
         df = pd.read_csv (r''+Pathway+"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(i)+'.csv')
         print(df)
         print(Configure(listConfig[0])) # Get the data from the json file
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         # Algorithm for classify the extraction of the text 
         index = df.index
         number_of_rows = len(index)
         print(number_of_rows)
         listdata = list(df.columns.values)
         print(listdata)
def Cutheader(Pathdata): 
       print("Removing header data") #Removing the header data
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt]) 
               if len(listfile) >= 2: 
                        for ik in range(0,len(listfile)):
                                 
                                 if ik%2 == 1:
                                         
                                        print("Getting the file name to cut header",listfile[ik]) # Getting the list of the file name from the odd numner after grouping the file
                                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                              #Getting the file name for extracting 
                                        df = pd.read_csv(Pathdata+"/"+listcut[rt]+"/"+listfile[ik]) #Getting the filename and running the head custter and replace the old file before merging data
                                        print(df) #Getting the data frame of the original csv header mark 
                                        print(df.values.tolist()) #Getting the data in list 
                                        #Getting the function of the header cutter
                                        memdat.clear() #Clear the memdat before adding the new list of the dataset 
                                        for ir in range(0,len(df.values.tolist())):
                                                extractdat = df.values.tolist()[ir]
                                                print(extractdat)
                                                memdat.append(extractdat)  #Getting the extract data from the dataset 
                                        memdataextract(Pathdata)
                                       #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
def memdataextract(Pathdata): 
       print("Removing header beginn") #Removing the header data
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt]) 
               if len(listfile) == 2: 
                        for ik in range(0,len(listfile)):  
                                 if ik%2 == 1:
                                    for rl in range(0,1):
                                       memdat.remove(memdat[rl]) 
                                        
                        da = pd.DataFrame(memdat)
                        da.to_csv(r""+Pathdata+"/"+listcut[rt]+"/"+listfile[ik]) #Getting the file header cut off to convert into the csv file
def precisecuthead(Pathdata): 
       print("Removing header data") #Removing the header data
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt])
               sorting  = sorted(listfile,reverse=False) 
               if len(sorting) >= 2: 
                        for ik in range(0,len(sorting)):
                                 if ik%2 == 1:               
                                        print("Getting the file name to cut header",sorting[ik]) # Getting the list of the file name from the odd numner after grouping the file
                                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                              #Getting the file name for extracting 
                                        df = pd.read_csv(Pathdata+"/"+listcut[rt]+"/"+sorting[ik]) #Getting the filename and running the head custter and replace the old file before merging data
                                        datatrans = df.values.tolist() #Getting the data transformation 
                                        for r in range(0,2):
                                              datatrans.remove(datatrans[0]) #remove the header out from the list 
                                        da = pd.DataFrame(datatrans)
                                        print(da)
                                        da.to_csv(Pathdata+"/"+listcut[rt]+"/"+sorting[ik],index=False)
                                         
def Removeunname(Pathdata):
       print("Start remove unnamed from table")
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt]) 
               if len(listfile) >= 2: 
                        for ik in range(0,len(listfile)):  
                                 if ik%2 == 1:
                                     df = pd.read_csv(Pathdata+"/"+listcut[rt]+"/"+listfile[ik])
                                     try:
                                        df.drop(['Unnamed: 0','0','0','1'],axis=1)
                                     except:
                                        df.drop(['PIN','Unnamed: 1','Unnamed: 2','TYPE (1)'],axis=1) 
                                     df.to_csv(r""+Pathdata+"/"+listcut[rt]+"/"+listfile[ik])
                                     print(df)
def Mergecsvalgorithm(Pathdata):
       print("Starting merging the csv file....") # Merging the csv file for the devices pins function
       listreadymerge = os.listdir(Pathdata) #Getting the directory in the path 
       print("Running the directory for merging data:",listreadymerge) #Getting the ready merge list for running the merging data
       for ir in range(0,len(listreadymerge)): 
                   os.chdir(Pathdata+"/"+listreadymerge[ir]) #Getting the list directory to merge the data on each directory
                   extension = 'csv'
                   all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                   print(all_filenames)
                   all_filesort = sorted(all_filenames, reverse=False)
                   print(all_filesort)
                   """
                   if len(all_filesort) == 2:
                        df = pd.read_csv(all_filesort[0], header=None) 
                        df.reset_index(inplace=True, drop=True)
                        df1 = pd.read_csv(all_filesort[1],header=None)
                        df1.reset_index(inplace=True, drop=True) 
                        combined_csv = pd.concat([df,df1],axis=0) # Concatinate the file
                   """     
                   for f in all_filesort:
                         df = pd.read_csv(f,header=1) 
                         df.reset_index(inplace=True, drop=True) #reset index 
                         combined_csv = pd.concat([df],axis=0) # Concatinate the file
                         getfilename = listreadymerge[ir].split("_")[0]
                         print("Filename in directory",getfilename)
                         combined_csv.to_csv(str(getfilename)+".csv",index=False, encoding='utf-8-sig')
                         print(combined_csv) # Getting the csv merged display on the terminal 

def Cutoutgroup(devicenamedata,Pathway,megapositon):
       print("Starting grouping cut ....")
       seekingovergroup  = os.listdir(Pathway)   #Get the list of the file and seek the over groupping 
       print(sorted(seekingovergroup, reverse=False))
       splitfile =  sorted(seekingovergroup, reverse=False)
       for i in range(0,len(splitfile)): 
               print(splitfile[i])
               getfilename = splitfile[i].split(".csv")[0]
               Getclassfile = getfilename.split("_")
               print(Getclassfile)
               if len(Getclassfile) == 3: 
                       print("Detected file name pattern")
                       if int(Getclassfile[2]) >=1:
                               print("Diff group of data tables:",splitfile[i]) #Get the file name for regrouping the table with the new upcoming file in directory
                               # append process here  
                               Drifgroup[str(devicenamedata) + "_"+str(megapositon)] = str(splitfile[i]) #Get the file append in the list  
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3                            
def Processingregroup(Pathdata,Normalgroup,Drifgroup): 
          print("Processing the group of the ") #Getting the data from the directory management processing
          datapath = os.listdir(Pathdata) #Get the directory from the list to extract the file name from the next directory to copy int the new group 
          sortedpath = sorted(datapath,reverse=False) #Get the path of the directory 
          print(sortedpath,len(sortedpath)) #Get sorted path
          for i in range(0,len(list(Drifgroup))):
                PositionPath = sortedpath.index(str(list(Drifgroup)[i])) 
                print("Getting the position of sorted path:",PositionPath) #Getting the position of the path 
                for ri in range(int(PositionPath)+1,int(len(sortedpath))): #Getting the prediction of the next directory
                          print("Copy loop to the new path",sortedpath[ri]) #Getting the the function from the sorted list
                          Basedir.append(sortedpath[ri]) #getting the reorder directory name
                          copyPath = os.listdir(Pathdata +"/"+sortedpath[ri])
                          print('Copy file path',copyPath) #Getting the list of the file inner directory 
                          for rk in range(0,len(copyPath)): 
                                    Normalgroup.append(copyPath[rk]) #Getting the append of the file from the next path into the list to combine with the function 
def Reoderprocessinggroup(Pathdata): #Getting the path data for processing the size of the path file re-ordering
          print("Reorder group of the file in the path directory...")
          Drifdata = list(Drifgroup.values())
         
          if len(Drifdata) < len(Normalgroup):
                     print("Drif group is bigger than Normal group")
                     try: 
                        for ij in range(0,len(Normalgroup)):

                              Regrouping[str(ij)] =str(Normalgroup[ij]) +","+ str(Drifdata[ij]) #
                     except:
                           Regrouping[str(ij)] = str(Normalgroup[ij])#                       
                        

          if len(Drifdata) > len(Normalgroup):
                        print("Normal group is bigger than Drif group")
                        try: 
                            for ij in range(0,len(Drifdata)):
                                 Regrouping[str(ij)] =str(Normalgroup[ij]) +","+ str(Drifdata[ij]) #
                        except:
                             Regrouping[str(ij)] = str(Drifdata[ij])# 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Make new directory in the pathdata
          print("Showing the current list of directory for new group:",Basedir)
          for r in range(0,len(Basedir)): 
                     print("Current base dir:",Basedir[r])
                     newdir = str(Basedir[r]) +"_"+"new"  #new file name reorder
                     Newdir.append(newdir) #Getting the new directory list          
                     os.system("echo 'Rkj3548123' | sudo -S mkdir"+"\t"+EXTRACT+"/"+str(inputcomp)+"/"+str(newdir))
                     os.system("echo 'Rkj3548123' | sudo -S chmod -R 777"+"\t"+EXTRACT+"/"+str(inputcomp)+"/"+str(newdir)) 
          print("Created the directory",os.listdir(Pathdata)) #Show the list directory to see new directory created
          Newdirectorycreator(Pathdata)
          
def Newdirectorycreator(Pathdata): 
        print("Create new directory.....") #Getting the list of the reorder to create the new directory 
        #Fiding the directory for copying into the new file 
        findnewdir = os.listdir(Pathdata) #Finding the new data of the list file 
        for il in range(0,len(findnewdir)): 
                  splitfile = str(findnewdir[il]).split("_")
                  if "new" in splitfile: 
                          print("Found new",str(splitfile))
                          print("Here is the target directory",findnewdir[il]) #get the new dir
                          #Getting the base dir for copy the file to new directory
                          Newpathdir = Pathdata+"/"+findnewdir[il] #Getting the new file directory
                          Getoverlistdata = list(Drifgroup)
                          Regroupdata = list(Regrouping)   #Getting the data from the regrouping by seaching the value of the data 
                          print(Regrouping)
                          for ij in range(0,len(Getoverlistdata)):
                                  print("Getting the file to copy",Getoverlistdata) #  
                                  Readingdir = Pathdata+"/"+Getoverlistdata[ij]
                                  readingdir = os.listdir(Pathdata+"/"+Getoverlistdata[ij])
                                  print("Check seeking file",str(readingdir))
                                  for ikl in range(0,len(Regroupdata)): 
                                             listcheck = Regrouping.get(Regroupdata[ikl]).split(",") #Getting the list
                                             print("Data from list check",listcheck) 
                                             if len(listcheck) != 1:
                                                  intersecfile = intersection(readingdir,listcheck) #Getting the file same file from the list  
                                                  if intersecfile != []:
                                                     for ih in range(0,len(intersecfile)):
                                                           os.system("echo 'Rkj3548123' | sudo -S mv"+"\t"+Readingdir+"/"+intersecfile[ih]+"\t"+"-t"+"\t"+Pathdata+"/"+findnewdir[il]) # Get the documentation of the components 
                                  #Checking the loop of the base dir and the regrouping list compattibility

                                  for ikh in range(0,len(Regroupdata)): 
                                             listcheck = Regrouping.get(Regroupdata[ikh]).split(",") #Getting the list
                                             print("Data from list check",listcheck)
                                             if len(listcheck) != 1:        
                                                for ihl in range(0,len(Basedir)): 
                                                      checkbasedir = os.listdir(Pathdata+"/"+Basedir[ihl]) 
                                                      print("Base directory file checklist:",checkbasedir) #Getting the list from the base directory to find the fintersection and remove the file
                                                      Readingdir2 = Pathdata+"/"+Basedir[ihl] #Checking base dir for path file copy instruction 
                                                      intersecfile = intersection(checkbasedir,listcheck) #Getting the file same file from the list                                                        
                                                      print("Second intersection:",intersecfile) 
                                                      if intersecfile != []:
                                                            for ih in range(0,len(intersecfile)):
                                                                 print("Position",ih)
                                                                 os.system("echo 'Rkj3548123' | sudo -S mv"+"\t"+Readingdir2+"/"+intersecfile[ih]+"\t"+"-t"+"\t"+Pathdata+"/"+findnewdir[il]) # Get the documentation of the components 
                                                  
                                  #check if the file inside is equal regrouping dictionary  data if yes then copy into the new directory 
                                  
#Finding the merging position                                                           
def Paringtables(inputcomp,Predictbreak):  #Bredict the breaking data 
        Pathdata = EXTRACT+"/"+str(inputcomp) #Create the path from the input 
        print("Begin paring tables data......")
        #Extracting the tables page from the  
        Getpagevalue = list(Predictbreak) #Get the list of the predictbreak key
        print("Predictbrake list",Getpagevalue) 
        for i in range(0,len(Getpagevalue)): 
                print(Getpagevalue[i]) #Get the page value from the list 
                pagevalue = Predictbreak.get(Getpagevalue[i]).split(",") #Get the list of the page for checking table len extraction and paring the page data 
                print(pagevalue) #Get the page paring value for the table data extraction
                Paringlist.append(pagevalue) #Getting the page value to make the list 
                #print("Paringlist",Paringlist)
        #Created the main directory system 
        os.system("echo 'Rkj3548123' | sudo -S mkdir"+"\t"+EXTRACT+"/"+str(inputcomp))
        os.system("echo 'Rkj3548123' | sudo -S chmod -R 777"+"\t"+EXTRACT+"/"+str(inputcomp))
        for qw in range(0,len(Getpagevalue)):        
                       pagevalue = Predictbreak.get(Getpagevalue[qw]).split(",")  
                       for a in range(0,len(pagevalue)): 
                               print("Page array data:",pagevalue[a])#get the prediction of each value in the page
                               for kc in range(0,len(Paringlist)):
                                        if str(pagevalue[a]) in Paringlist[kc]:
                                              megapositon = Paringlist.index(Paringlist[kc]) #Getting the mega position of the array for the page meging group 
                                              print("Array position:",pagevalue,megapositon)
                                              if int(megapositon) == int(Getpagevalue[qw]): #Always check the type of the variable in this case using integer to define the array position
                                                                   devicenamedata = list(Devicelist.values())[megapositon].split(",")[0] 
                                                                   os.system("echo 'Rkj3548123' | sudo -S mkdir"+"\t"+EXTRACT+"/"+str(inputcomp)+"/"+str(devicenamedata)+"_"+str(megapositon)) #Getting the number of the pins on the package data    
                                                                   os.system("echo 'Rkj3548123' | sudo -S chmod -R 777"+"\t"+EXTRACT+"/"+str(inputcomp)+"/"+str(devicenamedata)+"_"+str(megapositon))
                                                                   Pathway = EXTRACT+"/"+str(inputcomp)+"/"+str(devicenamedata)+"_"+str(megapositon) #Getting the path for the directory and file grouping input
                                                                   print("Getting the mega positon page",megapositon) # Find the way to put the megaposition back into the 
                                                                   tables = camelot.read_pdf(PATHMAIN + "/"+str(inputcomp)+".pdf",pages=str(pagevalue[a]))
                                                                   Cutoutgroup(devicenamedata,Pathway,megapositon)                     
                                                                   if megapositon == 0:
                                                                           Groupingpinextractor(Pathway,pagevalue[a],tables,1,megapositon) # Starter directory 
                                                                   if megapositon >= 1:
                                                                           Grouploopanalysis(Pathway,pagevalue[a],tables) #Looping analysis 
                                                                                   
                   
        # Merge the CSV file frim the table and access key of the devices 
        Processingregroup(Pathdata,Normalgroup,Drifgroup) 
        Reoderprocessinggroup(Pathdata) #Getting the reorder processing 
        #Cutheader(Pathdata) #Cut the header before start merging the file processing  
        #Removeunname(Pathdata) 
        #Mergecsvalgorithm(Pathdata) #Getting the path data for merging 
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                      #Get the data sopecification function for the 
Tabledetector(input1,inputcomp,Pinsquantity) #Get the pins and quantity of the package specificatoin 
Pinsearchfunction(input1,inputcomp,searchpinsconfiguretion) #Get the pins function of the input pdf file 
print(list(Packagecheck))
print(list(Pinsquantity))
print(list(Devicesbucket))
print(list(Packagetypebucket))
print(list(Pinsbucket))
Bucketcombinefunc(Devicesbucket,Packagetypebucket,Pinsbucket) #Processing the json type data 
print(combinedictdata) #Get the combine data from the json file generated function 
print(reftabledetect,len(reftabledetect)) # Get the reference of the data table on the function 
SpecificationExtract(input1, inputcomp, searchSpecification) #Specification page extraction
print("spec page number:",Specpage) # Reference for the specpage  
Classifyselectionfunction(input1,inputcomp,Pinsquantity,Packagecheck,len(reftabledetect),combinedictdata)
Devicenameparing(combinedictdata)#Device paring function 
Groupingdevicelist(Deviceeven,Deviceodd)
print("Reference starter page",refpagecal) # Get the reference page
print("Nextpage prediction",nextpage) #Get the next page prediction 
print("Device even:",Deviceeven)
print("Device odd:",Deviceodd)
print("Device list grouping",Devicelist)
#Get the reference page and next page prediction 
print("Clear Predict",Pageclassification)
SavebreakPinsconfigtable(refpagecal,nextpage,Specpage) 
print("Reference re-order:",reforder)
print("Predict order:",predictorder)
Retrivepage(reforder, predictorder)  #Retriving the page from the existing list and paring the data of the page to classify tables
print("Rethrived page:",Predictbreak) 
   #Looping to recheck and make directory from the grooup up
for i in range(0,2):
    Paringtables(inputcomp,Predictbreak) #Get the paring table to extract the page data 
#Cutheader(Pathdata)
#Removeunname(Pathdata) 
precisecuthead(Pathdata)
Mergecsvalgorithm(Pathdata)
#print("Drif group:",Drifgroup) #Get the data from the drif group to processing the new directory management
#print("Normal group:",Normalgroup) #Get the normal group
#print(list(Drifgroup.values()))
#print("Reoder dictionary:",Regrouping) #Getting the regrouping order function 