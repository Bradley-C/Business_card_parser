# Business Card Reader

We’ve created a new smartphone app that enables users to snap a photo of a business card and have the information from the card automatically extracted and added to their contact list.
We need you to write the component that parses the results of the optical character recognition (OCR) component in order to extract the name, phone number, and email address from the processed business card image.
We have provided you with a basic specification [1] and a series of example inputs [2] and would like you to provide the implementation.


## Getting Started
This project was written in Python version 3.6.5 on a Windows machine. If Python is not installed please follow the steps below

### Prerequisites

To run the Business Card Reader first an IDLE of Python must be installed, see the following links below for your OS

Windows: https://www.python.org/downloads/windows/ 
Linux/UNIX: https://www.python.org/downloads/source/
MAC OS X: https://www.python.org/downloads/mac-osx/

For Windows click the download link named, 'Download Windows x86-64 executable installer' run the executable file and follow prompts to install.
For Mac OS clicl the download link named, 'Download macOS 64-bit installer' run the executable file and follow prompts to install.

### Installing

Once your IDLE is finished installing download the ZIP file located at: https://github.com/Bradley-C/Business_card_parser

Unzip the files to where you wish, ensure all files all have the same path to ensure the program works


## Running Tests

By double clicking 'Test_Cards.py' you can run five premade tests to ensure accuracy of the code as well as see how long it to to complete the task

### Adding new tests
To add or delete tests right click on 'Test_Cards.py' and select 'Edit with IDLE'. This will allow you to enter new tests to validate the functionality of the code further.

The five premade tests should be labled test1 through test5, these can be named anything you wish, just ensure the same convection is used for all new tests, this convection is as follows
'
Test Name = \ """ Your test string here """
'

Also add the name of your test to the testBench below the defined tests by simply typing its name into the square brackets with a common
