import sys
from usableFunction import usableFunctions

if __name__ == '__main__':
    usables = usableFunctions()
    familyHead = usables.makeFamilyTree()
    file = open('myfile.txt', 'r+')
    # file = open(sys.argv[1], 'r+')
    # -------- Below block adds_child and gets_relation ------- #
    for inputString in file.readlines():

        action = inputString.split()[0]
        if (action == "ADD_CHILD"):
            motherName = inputString.split()[1]
            childName = inputString.split()[2]
            childGender = inputString.split()[3]
            usables.addInputChild(familyHead, motherName, childName,
                                  childGender)

        elif (action == "GET_RELATIONSHIP"):
            name = inputString.split()[1]
            relation = inputString.split()[2]
            usables.getRelationshipOfMember(familyHead, name, relation)

    file.close()
