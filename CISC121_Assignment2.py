"""
ASSIGNMENT 2 SKELETON CODE
Assumes all lists contain numeric data.
This file contains skeleton versions of the required functions
for Assignment 2, as well as a few functions to help you test
your functions.

This program was created by Margaret Lamb and is licensed under
Creative Commons Attribution-NonCommercial (CC BY-NC).
"""
def nthNode(LL, index): #finds the value of the requested node index
    if index == 0: #if asked for the first node
        return LL
    current = LL
    count = 0
    while count < index:
        count += 1
        current = current['next']
    return current

def nthNodeData(LL, index): #finds the value of the requested node index, returns its data
    if index == 0: #if asked for the first node
        return LL['data']
    current = LL
    count = 0
    while count < index:
        count += 1
        current = current['next']
    return (current['data'])

def nodeCounter(LL): #counts the number of nodes in a linked list
    count= 0
    while LL != None: #increments a counter by 1 until it reaches the end of the list
        count += 1
        LL = LL['next']
    return count
    
def isSorted(nums): 
    """
    Assumes nums is a linked list of numbers.  
    Returns True if the values in nums are sorted in non-decreasing order,
    False otherwise.  An empty or one-element list is considered sorted.
    
    """
    nodes = nodeCounter(nums)

    if nodes == 0 or nodes == 1: #checking if list is 0 or 1 elements
        return True

    for i in range (0,nodes-1): 
        if nthNodeData(nums, i) > nthNodeData(nums, i+1): #comparing if every node in nums is greater than the next node
            return False        
    return True

def noDups(nums):
    """
    Assumes nums is a linked list of numbers sorted in non-decreasing order.
    Modifies nums to get rid of all duplicate elements.
    Returns a pointer to the first element of the modified version
    of nums
    """
    if nums == None: #checking if list is empty
        return nums
    
    nodes = nodeCounter(nums) #counting the number of nodes in linked list

    newList = None #creating duplicate-free list

    for i in range (nodes-1,-1,-1):#counting down through number of node in linked list
        if nthNodeData(nums, i) != nthNodeData(nums, i-1): #if the data of the linked list node equal to i is different from the node before it:
            newList = {'data':nthNodeData(nums, i), 'next':newList} #filling in the new linked list with all non-duplicate elements from the original linked list
    newList = {'data':nthNodeData(nums,0), 'next':newList} #regardless of whether your list is [1,2,3] or [1,1,1,2,3] the 1 won't be included in newList, so this step is necessary
    return newList

def insertInOrder(linkedList, value):
    """
    Inserts a value into a sorted linked list.  Assumes the linkedList
    parameter is sorted in non-decreasing order.
    """
    nodes = nodeCounter(linkedList)
    before = nthNode(linkedList, nodes-1)
    
    if linkedList == None or linkedList['data'] > value: #if value is less than all list elements or there are no elements        
        linkedList = {'data':value, 'next':linkedList}        
        return linkedList
    if before['data'] < value: #if value is greater than all list elements
        newNode = {'data':value, 'next':None}
        before ['next'] = newNode
        return linkedList

    for i in range (0,nodes): #iterating through all pairs of elements
        before = nthNode(linkedList, i)
        after = nthNode(linkedList, i+1)
        if before['data'] <= value and after['data'] >= value: #inserting value into correct location
            newNode = {'data':value, 'next':after}
            before['next'] = newNode      
            return linkedList


def sort(nums):
    """
    Assumes nums is a list of numbers but does NOT assume nums is sorted.
    Returns a sorted copy of nums.
    """
    sortedList = {'next':None}
    nodes = nodeCounter(nums)

    for i in range (0, nodes):
        sortedList = {'next':insertInOrder(sortedList['next'], nthNodeData(nums, i))}
    return (sortedList['next'])



#########################################################################################################
# The following functions are included for testing purposes, so that you can easily create and print
# linked lists.  You may not call these functions from any of your required functions.
#########################################################################################################

def listString(linkedList):
    """
    Returns a string describing the list, suitable for printing.
    """
    result = '['
    current = linkedList
    while current != None:
        result += str(current['data'])
        current = current['next']
        if current != None:
            result += ","
    return result + ']'


def printList(linkedList):
    """
    Prints a representation of a list
    """
    print(listString(linkedList))
    

def createList(plist):
    """
    Creates and returns a linked list containing all of the elements
    of the Python-style list parameter.  A useful shortcut for testing.
    """
    result = None # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist)-1,-1,-1):
        result = {'data':plist[index], 'next':result}
    return result

