class familyTreeNode:
    def __init__(self, name, gender, partnerName=None, partnerGender=None):
        self.name = name
        self.gender = gender
        self.partnerName = partnerName
        self.partnerGender = partnerGender
        self.children = []
        self.parent = None

    def getNodeLevel(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent

        return level

    def addChildNode(self, child):
        child.parent = self
        self.children.append(child)

    def getRelationshipSon(self):

        listSon = []
        for child in self.children:
            if child.gender == "Male":
                listSon.append(child.name)

        return listSon

    def getRelationshipDaugther(self):

        listDaughter = []
        for child in self.children:
            if child.gender == "Female":
                listDaughter.append(child.name)

        return listDaughter

    def getRelationshipBrother(self):

        listBrother = []
        currParent = self.parent
        for child in currParent.children:
            if child.name != self.name and child.gender == "Male":
                listBrother.append(child.name)

        return listBrother

    def getRelationshipSister(self):

        listSister = []
        currParent = self.parent
        for child in currParent.children:
            if child.name != self.name and child.gender == "Female":
                listSister.append(child.name)

        return listSister

    def getRelationshipSiblings(self):

        sister = self.getRelationshipSister()
        brother = self.getRelationshipBrother()
        listSiblings = sister + brother
        return listSiblings

    def getRelationshipPaternalUncle(self):

        listPaternalUncle = []
        currParent = self.parent
        suprParent = currParent.parent

        if currParent.gender == "Male":
            for child in suprParent.children:
                if child.gender == "Male" and child.name != currParent.name:
                    listPaternalUncle.append(child.name)

            return listPaternalUncle

        else:

            return None

    def getRelationshipPaternalAunt(self):

        listPaternalAunt = []
        currParent = self.parent
        suprParent = currParent.parent

        if currParent.gender == "Male":
            for child in suprParent.children:
                if child.gender == "Female" and child.name != currParent.name:
                    listPaternalAunt.append(child.name)

            return listPaternalAunt

        else:

            return None

    def getRelationshipMaternalUncle(self):

        listMaternalUncle = []
        currParent = self.parent
        suprParent = currParent.parent

        if currParent.gender == "Female":
            for child in suprParent.children:
                if child.gender == "Male" and child.name != currParent.name:
                    listMaternalUncle.append(child.name)

            return listMaternalUncle

        else:

            return None

    def getRelationshipMaternalAunt(self):

        listMaternalAunt = []
        currParent = self.parent
        suprParent = currParent.parent

        if currParent.gender == "Female":
            for child in suprParent.children:
                if child.gender == "Female" and child.name != currParent.name:
                    listMaternalAunt.append(child.name)

            return listMaternalAunt

        else:

            return None

    def getRelationshipSisterInLaws(self, name):

        listSisterInLaw = []
        sisters = []
        wives = []
        currParent = self.parent

        if self.partnerName == name:
            for child in currParent.children:
                if child.name != self.name and child.gender == "Female":
                    sisters.append(child.name)

        else:
            for child in currParent.children:
                if child.name != self.name and child.gender == "Male":
                    wives.append(child.partnerName)

        listSisterInLaw = sisters + wives
        return listSisterInLaw

    def getRelationshipBrotherInLaws(self, name):

        listBrotherInLaw = []
        husbands = []
        brothers = []
        currParent = self.parent

        if self.partnerName == name:
            for child in currParent.children:
                if child.name != self.name and child.gender == "Female":
                    brothers.append(child.name)

        else:
            for child in currParent.children:
                if child.name != self.name and child.gender == "Female":
                    husbands.append(child.partnerName)

        listBrotherInLaw = brothers + husbands
        return listBrotherInLaw

# ---------use to print the tree ---------#

    def printFamilyTree(self):
        spaces = ' ' * self.getNodeLevel() * 3
        prefix = spaces + ">________" if self.parent else " "
        if self.partnerName is None:
            print(prefix + self.name + ' ' + self.gender + "\n")
        else:
            print(prefix + self.name + ' ' + self.gender + ' + ' +
                  self.partnerName + ' ' + self.partnerGender + "\n")

        if self.children:
            for child in self.children:
                child.printFamilyTree()

# --------------------  ***  -----------------#
