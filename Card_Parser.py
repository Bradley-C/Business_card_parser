import re
import csv

#Class used to parse the name, phone and, email from a buisness card
class BusinessCardParser:

    #Calls seprate functions to get the name, phone and, email then combines them
    #Returns that combined string to be outputted on console
    def getContactInfo(document):
        strName = "Name: " + str(ContactInfo.getName(document)) #New string that combines the label and calls getName to find the name in the passed string
        strPhone = "Phone: " + str(ContactInfo.getPhoneNumber(document)) #Does same as above for phone numbers
        strEmail = "Email: " + str(ContactInfo.getEmailAddress(document)) #Does same as above for emails
        fullInfo = '\n'.join([strName, strPhone, strEmail]) #Take the three strings above putting each in its own line
        return fullInfo

#Class containing set of functions used to individually find the name, phone, and email in different ways
class ContactInfo:

    #Function to find the name in the string
    @staticmethod
    def getName(CardInfo):
        #CSV files used as repositories for first, middle, and last names
        Filename = "CSV_Database_of_First&Middle_Names.csv"
        Filename2 = "CSV_Database_of_Last_Names.csv"

        #Regular experssions used to identify 3 or 2 words with only letters each seperated by a space
        NameKey = "[a-zA-Z\-.]{2,} [a-zA-Z\-.]{2,} [a-zA-ZA\-.]{2,}"
        NameKey2 = "[a-zA-Z\-.]{2,} [a-zA-ZA\-.]{2,}"
        
        for name in re.findall(NameKey, str(CardInfo)): #Search passed string for pattern matching NameKey and set it equal to 'name' 
            if name != "": #Contiune if somethign found
                First, Middle, Last = name.split(" ") #Split name string into three seperate strings
                with open(Filename,'r') as csv_firstName: #Open first/middle name CSV file
                    csv_reader = csv.reader(csv_firstName) #Read the file and set equal to another string
                    with open(Filename2,'r') as csv_lastName: #Open last name CSV file
                        csv_reader2 = csv.reader(csv_lastName) #Read the file and set equal to another string

                        #compare if first, middle, and last name are in the repositories and if so return it as name
                        for line in csv_reader:
                            if First and Middle in line:
                                for line3 in csv_reader2:
                                    if Last in line3:
                                        return name

        #Performs same task as above but only if a name with two words is found
        for name2 in re.findall(NameKey2, str(CardInfo)):
            if name2 != "":
                First, Last = name2.split(" ")
                with open(Filename,'r') as csv_firstName:
                    csv_reader = csv.reader(csv_firstName)
                    with open(Filename2,'r') as csv_lastName:
                        csv_reader2 = csv.reader(csv_lastName)
                        for line in csv_reader:
                            if First in line:
                                for line2 in csv_reader2:
                                    if Last in line2:
                                        return name2            
        return "No name was found" #If no name at all was found

    #Function to find the phone number in the string
    @staticmethod
    def getPhoneNumber(CardInfo):
        PhoneKey = "(?:\+\d{1,3})?\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}" #Regular experssions that describes the characteristics of a phone number
        notPhones = ("FAX", "PAGER") #Disqualifiers for a possible phone number
        for line in CardInfo.splitlines(): #Split each line to be search individually
            for phoneMess in re.findall(PhoneKey, line): #Search passed string for pattern matching PhoneKey and set it equal to 'phoneMess' 
                if not any(s in line.upper() for s in notPhones): #Reject any number where its line contains a disqualifiers
                    phone = re.sub("[^0-9]", "", str(phoneMess)) #Removes all charcters execpt numbers 
                    return phone
                
        return "No phone was found" #If no phone number at all was found
    
    #Function to find the email in the string
    @staticmethod
    def getEmailAddress(CardInfo):
        EmailKey = "[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+" #Regular experssions that describes the characteristics of an email
        for email in re.findall(EmailKey, str(CardInfo)): #Search passed string for pattern matching EmailKey and set it equal to 'email' 
            return email
        return "No email was found" #If no email at all was found
