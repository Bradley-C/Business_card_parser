import time
from Card_Parser import BusinessCardParser #Allows use of class and any of its functions 

start_time = time.time() #Start timer to test run time

#Different tests to pass to parser (more tests can be added)
test1 = \
"""ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com"""

test2 = \
"""Foobar Technologies
Analytic Developer
Lisa Haung
1234 Sentry Road
Columbia, MD 12345
Phone: 410-555-1234
Fax: 410-535-4321
lisa.haung@foobartech.com"""

test3 = \
"""Arthur Wilson
Software Engineer
Decision & Security Technologies
ABC Technologies
123 North 11th Street
Suite 229
Arlington, VA 22209
Fax: +1 (703) 555-1259
Tel: +1 (703) 555-1200
awilson@abctech.com"""

test4 = \
"""Mr. Matthew Hyde
Railway Corp.
556 Pecan Street
Marlboro, NJ, 07746
Fax: +1 522-124-8126
Tel: +1 522-146-0013
Pager: (421)-492-5512
Hyde.JMatthew@Rails.net"""

test5 = \
""" Senior Investor
Mrs. Betty Klosky
1203 Washington Street
Hoboken, NJ, 05124
Tel: 522-146-0013
Pager: (612)1115128
Klosk.B32@Inves.org"""

testBench = [test1, test2, test3, test4, test5] #List of tests created above (new tests must be added here as well) 
for i in range(0,len(testBench)): #Loop for amount of tests in testBench
    t=testBench[i] #Set t equal to next test string
    Output = BusinessCardParser.getContactInfo(t) #Pass test string to parsing file to create string of name, phone number, and email

    #Print the input string as well as the results
    print ("INPUT #",i+1)
    print (t)
    print ("")
    print ("OUTPUT #",i+1)
    print (Output) 
    print ("")

print ("Time to complete",len(testBench),"tests", round (time.time() - start_time,5), 'sec') #Display runtime for all tests completed
x = input ("Press Enter to exit program")
