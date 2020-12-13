from familyTree import familyTreeNode


class usableFunctions:
    # ----------------------------------------------------------
    #         CREATING  NODES
    # ----------------------------------------------------------
    def makeFamilyTree(self):

        # generating king Shan family
        kingShan = familyTreeNode("King Shan", "Male", "Queen Anga", "Female")
        # children of King Shan and Queen Anga ---- level_1
        chit = familyTreeNode("Chit", "Male", "Amba", "Female")
        ish = familyTreeNode("Ish", "Male")
        vich = familyTreeNode("Vich", "Male", "Lika", "Female")
        aras = familyTreeNode("Aras", "Male", "Chitra", "Female")
        satya = familyTreeNode("Satya", "Female", "Vyan", "Male")

        # children of Chit and Amba ---- level_2
        dritha = familyTreeNode("Dritha", "Female", "Jaya", "Male")
        tritha = familyTreeNode("Tritha", "Female")
        vritha = familyTreeNode("Vritha", "Male")

        # chldren of Vich and Lika ---- level_2
        vila = familyTreeNode("Vila", "Female")
        chika = familyTreeNode("Chika", "Female")

        # children of Aras and Chitra ---- level_2
        janki = familyTreeNode("Jnki", "Female", "Arit", "Male")
        ahit = familyTreeNode("Ahit", "Male")

        # children of Satya and Vyan ---- level_2
        asva = familyTreeNode("Asva", "Male", "Satvy", "Female")
        vyas = familyTreeNode("Vyas", "Male", "Krpi", "Female")
        atya = familyTreeNode("Atya", "Female")

        # children of Dritha and Jaya ---- level_3
        yodhan = familyTreeNode("Yodhan", "Male")

        # children of Janki and Arit ---- level_3
        laki = familyTreeNode("Laki", "Male")
        lavnya = familyTreeNode("Lavnya", "Female")

        # children of Asva and Satvy ---- level_3
        vasa = familyTreeNode("Vasa", "Male")

        # children of Vyas and Krpi ---- level_3
        kriya = familyTreeNode("Kriya", "Male")
        krithi = familyTreeNode("Krithi", "Female")

        # ----------------------------------------------------------
        #         ADDING CHILDREN TO ITS PARENTS
        # ----------------------------------------------------------
        # adding level_3 child to Vyas and Krpi
        vyas.addChildNode(kriya)
        vyas.addChildNode(krithi)

        # adding level_3 child to Asva and Satvy
        asva.addChildNode(vasa)

        # adding level_3 child to Janki and Arit
        janki.addChildNode(laki)
        janki.addChildNode(lavnya)

        # adding level_3 child to Dritha and Jaya
        dritha.addChildNode(yodhan)

        # adding level_2 child to Chit and Amba
        chit.addChildNode(dritha)
        chit.addChildNode(tritha)
        chit.addChildNode(vritha)

        # adding level_2 child to Vich and Lika
        vich.addChildNode(vila)
        vich.addChildNode(chika)

        # adding level_2 child to Aras and Chitra
        aras.addChildNode(janki)
        aras.addChildNode(ahit)

        # adding level_2 child to Satya and Vyan
        satya.addChildNode(asva)
        satya.addChildNode(vyas)
        satya.addChildNode(atya)
        # ---------------------------------------------------------

        # adding level_1 child to King Shan and Queen Anga
        kingShan.addChildNode(chit)
        kingShan.addChildNode(ish)
        kingShan.addChildNode(vich)
        kingShan.addChildNode(aras)
        kingShan.addChildNode(satya)

        # print the tree from root to bottom --> king Shan.print_family_tree()

        return kingShan

    # ------------------------  *** --------------------------#

    # --# ----- search member in the family
    # --# ----- for get_relationship function and returns it -------# --#

    def searchMemberInTheTreeGet(self, familyHead, name):

        if familyHead.name == name or familyHead.partnerName == name:
            member = familyHead
            return member

        else:
            for child in familyHead.children:
                test_child = self.searchMemberInTheTreeGet(child, name)
                if test_child:
                    return test_child

    # ------------------------  *** --------------------------#

    # --# ----- search member in the family
    # --# ----- for add_input_child function and returns it

    def searchMemberInTheTree(self, familyHead, name):

        if familyHead.partnerGender is not None:
            if familyHead.name == name or familyHead.partnerName == name:
                member = familyHead
                return member
            else:
                for child in familyHead.children:
                    test_child = self.searchMemberInTheTree(child, name)
                    if test_child:
                        return test_child

    # ------------------------  *** --------------------------#

    # --# ------- add child fuction ---------# --#

    def addInputChild(self, familyHead, motherName, childName, childGender):

        parent = self.searchMemberInTheTree(familyHead, motherName)

        if parent:

            if (parent.name == motherName and parent.gender == 'Female') or \
                (parent.partnerName == motherName and
                 parent.partnerGender == 'Female'):
                    newChild = familyTreeNode(childName, childGender)
                    parent.addChildNode(newChild)
                    print("CHILD_ADDITION_SUCCEEDED")
            else:
                print("CHILD_ADDITION_FAILED")

        else:
            print("PERSON_NOT_FOUND")

    # ------------------------  *** --------------------------#

    # --# ----- get relationship fuction --------# --#

    def getRelationshipOfMember(self, familyHead, name, relation):

        member = self.searchMemberInTheTreeGet(familyHead, name)

        if member:
            if relation == "Son":
                list = member.getRelationshipSon()
            elif relation == "Daughter":
                list = member.getRelationshipDaugther()
            elif relation == "Siblings":
                list = member.getRelationshipSiblings()
            elif relation == "Paternal-Uncle":
                list = member.getRelationshipPaternalUncle()
            elif relation == "Paternal-Aunt":
                list = member.getRelationshipPaternalAunt()
            elif relation == "Maternal-Uncle":
                list = member.getRelationshipMaternalUncle()
            elif relation == "Maternal-Aunt":
                list = member.getRelationshipMaternalAunt()
            elif relation == "Brother-In-Law":
                list = member.getRelationshipBrotherInLaws(name)
            elif relation == "Sister-In-Law":
                list = member.getRelationshipSisterInLaws(name)
            else:
                list = []
            if list:
                print(" ".join(list))
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")


# ------------------------  *** --------------------------#
