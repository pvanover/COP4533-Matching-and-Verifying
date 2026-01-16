def parsefile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    n = int(lines[0].strip())
    hospitalList = []
    studentList = []
    
    for i in range(1, n + 1):
        ranks = list(map(int, lines[i].strip().split()))
        hospitalList.append(ranks)
    
    for i in range(n + 1, 2 * n + 1):
        prefs = list(map(int, lines[i].strip().split()))
        studentList.append(ranks)
    
    return n, hospitalList, studentList


print(parsefile("data/example.in"))



# def matching(n, hospitalList, studentList):
#     #
        

        
        

    