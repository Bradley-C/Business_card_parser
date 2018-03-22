import re
import csv
#from ContactInfo import ContactInfo

class BusinessCardParser:
        
    @staticmethod
    def FindName(document):
        Filename = "CSV_Database_of_First&Middle_Names.csv"
        Filename2 = "CSV_Database_of_Last_Names.csv"
        NameKey = "[a-zA-Z\-.]{2,} [a-zA-Z\-.]{2,} [a-zA-ZA\-.]{2,}"
        NameKey2 = "[a-zA-Z\-.]{2,} [a-zA-ZA\-.]{2,}"
        for name in re.findall(NameKey, document):
            if name != "":
                First, Middle, Last = name.split(" ")
                with open(Filename,'r') as csv_firstName:
                    csv_reader = csv.reader(csv_firstName)
                    with open(Filename2,'r') as csv_lastName:
                        csv_reader2 = csv.reader(csv_lastName)
                        for line in csv_reader:
                            if First and Middle in line:
                                for line3 in csv_reader2:
                                    if Last in line3:
                                        print (name)
                                        return name
                    
        for name2 in re.findall(NameKey2, document):
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
                                        print (name2)
                                        return name2
    @staticmethod
    def FindPhone(document):
        PhoneKey = "(?:\+\d{1,3})?\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}"
        NotPhones = ("FAX", "PAGER")
        for line in document.splitlines():
            for PhoneMess in re.findall(PhoneKey, document):
                if not any(s in line.upper() for s in NotPhones):
                    phone = re.sub("[^0-9]", "", PhoneMess)
                    print(phone)
                    return phone
    @staticmethod
    def FindEmail(document):
        EmailKey = "[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        for email in re.findall(EmailKey, document):
            print (email)
            return email
