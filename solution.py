#marks sample data
marks = [[-1, 20, 38, 40, 40, 40],[40, 40, -1, 40, 40, 40],[40, 40, -1, 40, 40, 40]]

#Question 1.1
def STaverages(MARKS):
    students_avg_scores = [] #hold all avg scores
    for student in MARKS:
        module_total = 0
        for module in student: #if the student didn't take the module
            if module != -1:
                module_total += module
        modules_taken = len(student) - student.count(-1)
        if modules_taken == 0:
            students_avg_scores.append(-1)
        else:
            student_average = module_total/modules_taken
            students_avg_scores.append(student_average) #append the average score to the students_avg_scores list
        
    return students_avg_scores
    
#Question 1.2
def MODAverages(MARKS):
    module_avg_scores = [] #hold averages for all modules
    for index in range(len(MARKS[0])):
        module_scores = [x[index] for x in MARKS] #all scores for a particular module

        filtered_scores = list(filter((-1).__ne__, module_scores)) #remove all occurences of -1
        if len(filtered_scores) == 0:
            module_avg_scores.append(-1) #append -1 if no one took the module
        else:
            total = 0 #hold the total
            for x in filtered_scores:
                total += x
            avg = total/len(filtered_scores) #divide the total by the number of students to get the average
            module_avg_scores.append(avg) #append to module_avg_scores
    return(module_avg_scores)

#Question 1.3
def CanGraduate(MARKS, COMPULSORY, s):
    student_scores = MARKS[s] #get scores for the specified student
    all_modules = [x for x in range(len(MARKS[s]))] #get all the modules taken by the student
    optional = list(set(all_modules) - set(COMPULSORY)) #get optional modules
    for index in COMPULSORY:
        if student_scores[index] == -1: #return false if student got less than 40 or didn't take a compulsory module
            return False
        if student_scores[index] < 40:
            return False
    count = 0 #hold the number of optional modules the student has passed
    #check scores for optional modules
    for index in optional:
        if student_scores[index] >= 40: 
            count += 1 
    if count < 3:
        return False
    else:
        return True
        
# result = CanGraduate(marks, [0, 1], 1)
# print(result)


# Question 1.4
def GraduatesList(MARKS, COMPULSORY, NAMES):
    average_scores = STaverages(MARKS) #use STaverages function to get all avg scores
    graduates_list = []                 #hold the list of all graduates
    for student_id in range(len(marks)):
        if CanGraduate(MARKS, COMPULSORY, student_id) == True: #check if student can graduate using the CanGraduate function
            graduates_list.append(f"{NAMES[student_id]} {average_scores[student_id]}") #append to the list of graduates
    return graduates_list

# names = ['mungai hosea', 'gladys aloo','elvis moraa']
# result = GraduatesList(marks, [0,1], names)
# print(result)


#Question 2.1
def FirstInSecond(A, B):
    for item in A:
        if B.__contains__(item): #check if B contains every item of a
            pass
        else:
            return False
    return True

#Question 2.2
def FirstInSecondRec(A, b):
    if len(A) > 0: #repeat until the list is empty
        if not b.__contains__(A[0]): #check the first row 
            return False
        else:
            A.remove(A[0]) #remove the checked row and
            return FirstInSecondRec(A, b)   # recursion till False or True is returned
    else:
        return True

# print(FirstInSecondRec([1,2,3], [1, 2, 3, 4]))

#Question 3.1
def IsNonrepeatedRow(A):
    for row in A:
        if len(list(set(row))) == len(row): #use set to filter list and leave it with unique values
            return True
    return False

#Question 3.2
def IsNonrepeatedRowRec(A):
    if len(A) > 0:    
        if len(A[0]) == len(list(set(A[0]))): #check the first row
            return True
        else:
            A.remove(A[0]) #remove the checked row
            return IsNonrepeatedRowRec(A) #use recursion until the row has a length of 0
    else:
        return False

# print(IsNonrepeatedRowRec([[1,2,2],[2,2,2]]))


#Question 4.1
def IsDominated(A,S,v):
    if len(A) != 0:    
        vert=S[-1] #get the last item in the list
        if(A[vert][v]==1):
            return True
        else:
            A = A.pop() #remove the tested item and recurse
            return IsDominated(A,S,v)
    else:
        return False #return false if all elements have been tested


#Question 4.2
def IsDominatingSet(A,s): #A is the gram and s is the subset
    edges = [] #holds all edges in the graph
    filtered_edges = [] #holds unique edges
    for row in range(len(A)):
        for column in range(len(A[0])):
            if A[row][column] is not None: #check if the space is None
                edges.append([column, row])
    #arrage it in such a manner that the smaller number comes first
    for x in [[min(edge[0], edge[1]),max(edge[0], edge[1])] for edge in edges]: 
        if not filtered_edges.__contains__(x):
            filtered_edges.append(x) #remove duplicate edges and append to edges list
    #Check if s is a dominating subset
    for point in s: 
        if filtered_edges.__contains__(point) == False:
            return False #return false if not
    return True #return True if all points in s are contained in the graph


#Question 5
def ListEdges(G): #use None to represent an empty space in the matrix
    edges = [] #hold all edges ..This list could contain repeated edges e.g (1,2) and (2,1)
    filtered_edges = [] #hold unique edges (1,2) and (2,1) are replaced by (1,2) only
    for row in range(len(G)):
        for column in range(len(G[0])):
            if G[row][column] is not None:
                edges.append([column, row])
    #arrage it in such a manner that the smaller number comes first
    for x in [[min(edge[0], edge[1]),max(edge[0], edge[1])] for edge in edges]:
        if not filtered_edges.__contains__(x):
            filtered_edges.append(x) #remove duplicate edges and append to edges list
    return filtered_edges

# test the ListEdges function using a matrix of this form
# matrix = [
#     [None, 1, 1, None, None],
#     [1, None, 1, 1, None],
#     [None, None, None, None, 1],
#     [None, None, None, None, 1],
#     [None, None, None, None, None]]

# result = ListEdges(matrix)
# print(result)