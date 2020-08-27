import array
import urllib.request as urllib

def firstChoice():
    global string2
    string2 = input("Enter a chemical name: ")

def choices():
    print(40 * "_")
    print(3 * " " + "Select the value below to retrieve")
    print(40 * "_")
    print('{:>23}'.format("InChi[0]"))
    print('{:>23}'.format("InChiKey[1]"))
    print('{:>23}'.format("Molecular Formula[2]"))
    print('{:>23}'.format("Smiles[3]"))
    print('{:>23}'.format("Molecular Weight[4]"))
    print('{:>23}'.format("IUPAC Name[5]"))
    print('{:>23}'.format("Charge[6]"))
    print('{:>23}'.format("Mass for Mass Spec[7]"))
    print(40 * "_")
    global idChoice
    idChoice = int(input("Enter a number choice? "))
    if 0 <= idChoice <=7:
        choiceID()
    elif idChoice != range(0,7):
        print(2 * '\n' + 38 * '*')
        print("* Incorrect Number Choice, Try Again *")
        print(38 * '*' + 2 * '\n')
        choices()

def choiceID():
    inputList = ['INCHI', 'INCHIKEY', 'MolecularFormula','CanonicalSMILES', 'MolecularWeight', 'IUPACName', 'Charge', 'ExactMass']
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
