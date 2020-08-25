import array
import urllib.request as urllib

def firstChoice():
    global string2
    string2 = input("Enter a chemical name: ")

def choices():
    print(40 * "_")
    print(3 * " " + "Select the value below to retrieve")
    print(40 * "_")
    print('{:>23}'.format("INCHI[0]"))
    print('{:>23}'.format("INCHIKEY[1]"))
    print('{:>23}'.format("MOLECULAR FORMULA[2]"))
    print('{:>23}'.format("SMILES[3]"))
    print('{:>23}'.format("MOLECULAR WEIGHT[4]"))
    print(40 * "_")
    global idChoice
    idChoice = int(input("Enter a number choice? "))
    if 0 <= idChoice <= 4:
        choiceID()
    elif idChoice != range(0,4):
        print(2 * '\n' + 38 * '*')
        print("* Incorrect Number Choice, Try Again *")
        print(38 * '*' + 2 * '\n')
        choices()

def choiceID():
    inputList = ['INCHI', 'INCHIKEY', 'MolecularFormula','CanonicalSMILES', 'MolecularWeight']
    selChoice = inputList[idChoice]

    string1 = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
    string3 = "/property/"
    string4 = "/TXT"
    html = urllib.urlopen(string1 + string2 + string3 + selChoice + string4).read()
    html2 = html.decode('UTF-8')
    print(2 * '\n')
    print(html2)
    print(2 * '\n')
    redoProg = input("Would you like to check another compound, yes or no? ")
    if redoProg == "yes":
        print ("\n" * 2)
        main()
    else:
        print("Done!")

def main():
    firstChoice()
    choices()
## Program Assignments ##
main()
