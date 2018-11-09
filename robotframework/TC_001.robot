*** Settings ***
Library  Selenium2Library

*** Variables ***
#To declare a variable always need ${Variable Name}  Argument
${Browser}  Chrome
#${URL}  http://www.thetestingworld.com/testings
${URL}  https://www.salesforce.com/mx/form/signup/sales-cloud/freetrial-sales-essentials/
*** Test Cases ***
#Test Name
TC_001 Browser Start and Close
    #Steps:
    Open Browser  ${URL}  ${Browser}
    #Maximize Browser Window Currently not working
    Input Text  name:UserFirstName  Fernando
    Input Text  name:UserLastName   Dìaz
    Input Text  name:UserTitle  Manager
    Input Text  name:UserEmail  fer@mail.com
    Input Text  name:UserPhone  98656789
    Input Text  name:CompanyName  Salesforce
    Select From List  xpath://a[text()='Menos de 8 empleados']  Menos de 8 empleados
#    Clear ELement Text  name:fld_username
#    Select Radio Button  add_type  office
#    Select Checkbox  name: terms
#    Click Link  xpath://a[text()='Read Detail']
    #Close Browser
