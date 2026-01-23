def parsefile(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("file not found")
        return None, None, None
    
    if not lines or len(lines) == 0:
        print("empty file")
        return None, None, None
    
    try:
        n = int(lines[0].strip())
    except (ValueError, IndexError):
        print("Error: Invalid or missing number of hospitals/students.")
        return None, None, None
    
    if len(lines) < 2 * n + 1:
        print("not enough lines")
        return None, None, None
    
    hospitalList = []
    studentList = []
    
    for i in range(1, n + 1):
        ranks = list(map(int, lines[i].strip().split()))
        if len(ranks) != n:
            print("hospital ranks have incorrect amount of students")
            return None, None, None
        hospitalList.append(ranks)
    
    for i in range(n + 1, 2 * n + 1):
        ranks = list(map(int, lines[i].strip().split()))
        if len(ranks) != n:
            print("student ranks have incorrect amount of hospitals")
            return None, None, None
        studentList.append(ranks)

    return n, hospitalList, studentList


def matching(n, hospitalList, studentList):
    if n is None or hospitalList is None or studentList is None:
        print("invalid input")
        return
    free_hospitals = list(range(n))
    hospital_matches = [None] * n
    student_matches = [None] * n
    next_sproposal = [0] * n 

    while free_hospitals:
        h = free_hospitals[0]
        
        if next_sproposal[h] >= n:
            free_hospitals.remove(h)
            continue
        
        a = hospitalList[h][next_sproposal[h]] - 1
        next_sproposal[h] += 1
        
        if student_matches[a] is None:
            hospital_matches[h] = a
            student_matches[a] = h
            free_hospitals.remove(h)
        elif studentList[a].index(h + 1) < studentList[a].index(student_matches[a] + 1): 
            hprime = student_matches[a]
            hospital_matches[hprime] = None
            free_hospitals.append(hprime)
            hospital_matches[h] = a
            student_matches[a] = h
            free_hospitals.remove(h)
        else:  
           pass
    
    for i in range(n):
        print(f"{i + 1} {hospital_matches[i] + 1}")
             
        
def main():
    n, hospitalList, studentList = parsefile("data/example.in")
    matching(n, hospitalList, studentList)


if __name__ == "__main__":
    main()        
        

    