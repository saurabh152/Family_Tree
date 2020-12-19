#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


class family_Tree_Node:

    def __init__(
        self,
        name,
        gender,
        partner_name=None,
        partner_gender=None,
        ):
        self.name = name
        self.gender = gender
        self.partner_name = partner_name
        self.partner_gender = partner_gender
        self.children = []
        self.parent = None

    def get_node_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent

        return level

    def add_child_node(self, child):
        child.parent = self
        self.children.append(child)

    def get_relationship_son(self):

        list_son = []

        for child in self.children:
            if child.gender == 'Male':
                list_son.append(child.name)

        return list_son

    def get_relationship_daugther(self):

        list_daughter = []

        for child in self.children:
            if child.gender == 'Female':
                list_daughter.append(child.name)

        return list_daughter

    def get_relationship_brother(self):

        list_brother = []
        curr_parent = self.parent
        for child in curr_parent.children:
            if child.name != self.name and child.gender == 'Male':
                list_brother.append(child.name)

        return list_brother

    def get_relationship_sister(self):

        list_sister = []
        curr_parent = self.parent
        for child in curr_parent.children:
            if child.name != self.name and child.gender == 'Female':
                list_sister.append(child.name)

        return list_sister

    def get_relationship_siblings(self):

        sister = self.get_relationship_sister()
        brother = self.get_relationship_brother()
        list_siblings = sister + brother

        # print( list_siblings)

        return list_siblings

    def get_relationship_paternal_uncle(self):

        list_paternal_uncle = []
        curr_parent = self.parent
        supr_parent = curr_parent.parent

        if curr_parent.gender == 'Male':
            for child in supr_parent.children:
                if child.gender == 'Male' and child.name \
                    != curr_parent.name:
                    list_paternal_uncle.append(child.name)

            return list_paternal_uncle
        else:

            return None

    def get_relationship_paternal_aunt(self):

        list_paternal_aunt = []
        curr_parent = self.parent
        supr_parent = curr_parent.parent

        if curr_parent.gender == 'Male':
            for child in supr_parent.children:
                if child.gender == 'Female' and child.name \
                    != curr_parent.name:
                    list_paternal_aunt.append(child.name)

            return list_paternal_aunt
        else:

            return None

    def get_relationship_maternal_uncle(self):

        list_maternal_uncle = []
        curr_parent = self.parent
        supr_parent = curr_parent.parent

        if curr_parent.gender == 'Female':
            for child in supr_parent.children:
                if child.gender == 'Male' and child.name \
                    != curr_parent.name:
                    list_maternal_uncle.append(child.name)

            return list_maternal_uncle
        else:

            return None

    def get_relationship_maternal_aunt(self):

        list_maternal_aunt = []
        curr_parent = self.parent
        supr_parent = curr_parent.parent

        if curr_parent.gender == 'Female':
            for child in supr_parent.children:
                if child.gender == 'Female' and child.name \
                    != curr_parent.name:
                    list_maternal_aunt.append(child.name)

            return list_maternal_aunt
        else:

            return None

    def get_relationship_sister_in_law(self):

        list_sister_in_law = []
        parent = self.parent

        for child in parent.children:

            if child.partner_gender:

                if child.gender == 'Female':
                    list_sister_in_law.append(child.name)
                elif child.partner_gender == 'Female':
                    list_sister_in_law.append(child.partner_name)
            else:

                if child.gender == 'Female':
                    list_sister_in_law.append(child.name)

        if self.name in list_sister_in_law:
            list_sister_in_law.remove(self.name)
        elif self.partner_name in list_sister_in_law:
            list_sister_in_law.remove(self.partner_name)

        return list_sister_in_law

    def get_relationship_sister_in_laws(self, name):

        list_sister_in_law = []
        sisters = []
        wives = []
        curr_parent = self.parent

        if self.partner_name == name:
            for child in curr_parent.children:
                if child.name != self.name and child.gender == 'Female':
                    sisters.append(child.name)
        else:

            for child in curr_parent.children:
                if child.name != self.name and child.gender == 'Male':
                    wives.append(child.partner_name)

        list_sister_in_law = sisters + wives
        return list_sister_in_law

    def get_relationship_brother_in_law(self):

        list_brother_in_law = []
        parent = self.parent

        for child in parent.children:

            if child.partner_gender:

                if child.gender == 'Male':
                    list_brother_in_law.append(child.name)
                elif child.partner_gender == 'Male':
                    list_brother_in_law.append(child.partner_name)
            else:

                if child.gender == 'Male':
                    list_brother_in_law.append(child.name)

        if self.name in list_brother_in_law:
            list_brother_in_law.remove(self.name)
        elif self.partner_name in list_brother_in_law:
            list_brother_in_law.remove(self.partner_name)

        return list_brother_in_law

    def get_relationship_brother_in_laws(self, name):

        list_brother_in_law = []
        husbands = []
        brothers = []
        curr_parent = self.parent

        if self.partner_name == name:
            for child in curr_parent.children:
                if child.name != self.name and child.gender == 'Female':
                    brothers.append(child.name)
        else:

            for child in curr_parent.children:
                if child.name != self.name and child.gender == 'Female':
                    husbands.append(child.partner_name)

        list_brother_in_law = brothers + husbands
        return list_brother_in_law

# ---------use to print the tree ---------#

    def print_family_tree(self):
        spaces = ' ' * self.get_node_level() * 3
        prefix = (spaces + '>________' if self.parent else ' ')
        if self.partner_name == None:
            print(prefix + self.name + ' ' + self.gender + '\n')
        else:
            print(prefix + self.name + ' ' + self.gender \
                + ' ++++++++++++++++++ ' + self.partner_name + ' ' \
                + self.partner_gender + '\n')

        if self.children:
            for child in self.children:
                child.print_family_tree()


# --------------------  ***  -----------------#

# ----------------------------------------------------------
#         CREATING  NODES
# ----------------------------------------------------------

def make_family_tree():

    # generating king Shan family

    king_Shan = family_Tree_Node('King_Shan', 'Male', 'Queen_Anga',
                                 'Female')

    # children of King Shan and Queen Anga ---- level_1

    chit = family_Tree_Node('Chit', 'Male', 'Amba', 'Female')
    ish = family_Tree_Node('Ish', 'Male')
    vich = family_Tree_Node('Vich', 'Male', 'Lika', 'Female')
    aras = family_Tree_Node('Aras', 'Male', 'Chitra', 'Female')
    satya = family_Tree_Node('Satya', 'Female', 'Vyan', 'Male')

    # children of Chit and Amba ---- level_2

    dritha = family_Tree_Node('Dritha', 'Female', 'Jaya', 'Male')
    tritha = family_Tree_Node('Tritha', 'Female')
    vritha = family_Tree_Node('Vritha', 'Male')

    # chldren of Vich and Lika ---- level_2

    vila = family_Tree_Node('Vila', 'Female')
    chika = family_Tree_Node('Chika', 'Female')

    # children of Aras and Chitra ---- level_2

    janki = family_Tree_Node('Jnki', 'Female', 'Arit', 'Male')
    ahit = family_Tree_Node('Ahit', 'Male')

    # children of Satya and Vyan ---- level_2

    asva = family_Tree_Node('Asva', 'Male', 'Satvy', 'Female')
    vyas = family_Tree_Node('Vyas', 'Male', 'Krpi', 'Female')
    atya = family_Tree_Node('Atya', 'Female')

    # children of Dritha and Jaya ---- level_3

    yodhan = family_Tree_Node('Yodhan', 'Male')

    # children of Janki and Arit ---- level_3

    laki = family_Tree_Node('Laki', 'Male')
    lavnya = family_Tree_Node('Lavnya', 'Female')

    # children of Asva and Satvy ---- level_3

    vasa = family_Tree_Node('Vasa', 'Male')

    # children of Vyas and Krpi ---- level_3

    kriya = family_Tree_Node('Kriya', 'Male')
    krithi = family_Tree_Node('Krithi', 'Female')

# ----------------------------------------------------------
#         ADDING CHILDREN TO ITS PARENTS
# ----------------------------------------------------------
    # adding level_3 child to Vyas and Krpi

    vyas.add_child_node(kriya)
    vyas.add_child_node(krithi)

    # adding level_3 child to Asva and Satvy

    asva.add_child_node(vasa)

    # adding level_3 child to Janki and Arit

    janki.add_child_node(laki)
    janki.add_child_node(lavnya)

    # adding level_3 child to Dritha and Jaya

    dritha.add_child_node(yodhan)

    # adding level_2 child to Chit and Amba

    chit.add_child_node(dritha)
    chit.add_child_node(tritha)
    chit.add_child_node(vritha)

    # adding level_2 child to Vich and Lika

    vich.add_child_node(vila)
    vich.add_child_node(chika)

    # adding level_2 child to Aras and Chitra

    aras.add_child_node(janki)
    aras.add_child_node(ahit)

    # adding level_2 child to Satya and Vyan

    satya.add_child_node(asva)
    satya.add_child_node(vyas)
    satya.add_child_node(atya)

# ---------------------------------------------------------

    # adding level_1 child to King Shan and Queen Anga

    king_Shan.add_child_node(chit)
    king_Shan.add_child_node(ish)
    king_Shan.add_child_node(vich)
    king_Shan.add_child_node(aras)
    king_Shan.add_child_node(satya)

    # king_Shan.print_family_tree()

    return king_Shan


# --#------ search member in the family and returns it

def search_member_in_the_tree_get(family_head, name):

    if family_head.name == name or family_head.partner_name == name:
        member = family_head
        return member
    else:

        for child in family_head.children:
            test_child = search_member_in_the_tree_get(child, name)
            if test_child:
                return test_child


def search_member_in_the_tree(family_head, name):

    if family_head.partner_gender != None:

        if family_head.name == name or family_head.partner_name == name:
            member = family_head
            return member
        else:

            for child in family_head.children:
                test_child = search_member_in_the_tree(child, name)
                if test_child:
                    return test_child


# --#------ add child fuction

def add_input_child(
    family_head,
    mother_name,
    child_name,
    child_gender,
    ):

    parent = search_member_in_the_tree(family_head, mother_name)

    if parent:

        if parent.name == mother_name and parent.gender == 'Female' \
            or parent.partner_name == mother_name \
            and parent.partner_gender == 'Female':
            new_child = family_Tree_Node(child_name, child_gender)
            parent.add_child_node(new_child)
            print('CHILD_ADDITION_SUCCEEDED') 
        else:
            print('CHILD_ADDITION_FAILED') 
    
    else:
        print('PERSON_NOT_FOUND') 


# --#------ get relationship fuction

def get_relationship_of_member(family_head, name, relation):

    member = search_member_in_the_tree_get(family_head, name)

    if member:
        if relation == 'Son':
            list = member.get_relationship_son()
        elif relation == 'Daughter':
            list = member.get_relationship_daugther()
        elif relation == 'Siblings':
            list = member.get_relationship_siblings()
        elif relation == 'Paternal-Uncle':
            list = member.get_relationship_paternal_uncle()
        elif relation == 'Paternal-Aunt':
            list = member.get_relationship_paternal_aunt()
        elif relation == 'Maternal-Uncle':
            list = member.get_relationship_maternal_uncle()
        elif relation == 'Maternal-Aunt':
            list = member.get_relationship_maternal_aunt()
        elif relation == 'Brother-In-Law':
            list = member.get_relationship_brother_in_laws(name)
        elif relation == 'Sister-In-Law':
            list = member.get_relationship_sister_in_laws(name)
        else:
            list = []
        if list:
            print(' '.join(list))
        else:
            print('NONE')
    else:
        print('PERSON_NOT_FOUND')


if __name__ == '__main__':

    family_head = make_family_tree()

    f = open(sys.argv[1], 'r+')

# --#------ Below block adds_child and gets_relation ------#--#

    for input_string in f.readlines():

        inp = input_string.split()[0]

        if inp == 'ADD_CHILD':

            mother_name = input_string.split()[1]
            child_name = input_string.split()[2]
            child_gender = input_string.split()[3]
            add_input_child(family_head, mother_name, child_name,
                            child_gender)
        elif inp == 'GET_RELATIONSHIP':

            name = input_string.split()[1]
            relation = input_string.split()[2]
            get_relationship_of_member(family_head, name, relation)

    f.close()
