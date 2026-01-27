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

#trying to add output file to see if it works with any file not just 
def matching(n, hospitalList, studentList, outputfile):
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
    
    # trying to use output file to see if it works with every file
    with open(outputfile, "w") as f:
        for i in range(n):
            print(f"{i + 1} {hospital_matches[i] + 1}", file=f)

    
def read_output(filename, n):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("INVALID: output file not found")
        return None
    
    if len(lines) != n:
        print("INVALID: output file has incorrect number of lines")
        return None
    
    hospital_matches = [None] * n
    seen_hospitals = set()
    seen_students = set()

    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            print("INVALID: line format is incorrect")
            return None
        try:
            i = int(parts[0])
            j = int(parts[1])
        except ValueError:
            print("INVALID: non-integer values are in output")
            return None
        
        if not (1 <= i <= n):
            print("INVALID: hospital's index out of range")
            return None
        if not (1 <= j <= n):
            print("INVALID: student's index out of range")
            return None
        
        if i in seen_hospitals:
            print("INVALID: hospital is matched more than once")
            return None
        seen_hospitals.add(i)

        if j in seen_students:
            print("INVALID: student is matched more than once")
            return None
        seen_students.add(j)

        hospital_matches[i - 1] = j - 1

    if any(x is None for x in hospital_matches):
        print("INVALID: some hospitals are unmatched")
        return None
    
    return hospital_matches
        
# helper function to build an array to easily check all matches to keep shorter runtime
def array_from_matches(hospital_matches, n):
    student_matches = [None] * n
    for h in range(n):
        s = hospital_matches[h]
        student_matches[s] = h
    return student_matches

'''
blocking if
hospital h prefers student more than student its currently assigned to
AND student prefers hospital more than hospital its currently assigned to
'''
# creating a function to find the position of the hospital in the students preference list
# if its lower then preferred
def student_rank(studentList):
    n = len(studentList)
    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for position, hospital_label in enumerate(studentList[s]):
            hospital_index = hospital_label - 1
            student_rank[s][hospital_index] = position
    return student_rank

# this is the position of student in the hospitals preference list
def hospital_rank(hospitalList):
    n = len(hospitalList)
    hospital_rank = [[0] * n for _ in range(n)]
    for h in range(n):
        for position, student_label in enumerate(hospitalList[h]):
            student_index = student_label - 1
            hospital_rank[h][student_index] = position
    return hospital_rank

def check_blocking_pairs(n, hospitalList, studentList, hospital_matches):
    student_matches = array_from_matches(hospital_matches, n)
    student_position = student_rank(studentList)
    hospital_position = hospital_rank(hospitalList)

    for h in range(n):
        assigned_student = hospital_matches[h]
        for student_label in hospitalList[h]:
            s = student_label - 1
            if s == assigned_student:
                continue

            if hospital_position[h][s] < hospital_position[h][assigned_student]:
                assigned_hospital = student_matches[s]
                if student_position[s][h] < student_position[s][assigned_hospital]:
                    return (h, s)
    return None

def final_check(inputfile, outputfile):
    n, hospitalList, studentList = parsefile(inputfile)
    if n is None:
        print("INVALID: input file is bad")
        return
    hospital_matches = read_output(outputfile, n)
    if hospital_matches is None:
        return
    bp = check_blocking_pairs(n, hospitalList, studentList, hospital_matches)
    if bp is None:
        print("VALID STABLE")
    else:
        h, s = bp
        print(f"UNSTABLE: blocking pair ({h+1}, {s+1})")


def main():
    '''
    n, hospitalList, studentList = parsefile("data/example.in")
    matching(n, hospitalList, studentList)

    test = read_output("data/example.out", n)
    print("Parsed hospital matches from output:", test)
    '''
    inputfile = "data/unstable_example.in"
    outputfile = "data/unstable_example.out"
    # n, hospitalList, studentList = parsefile(inputfile)
    # matching(n, hospitalList, studentList, outputfile)
    final_check(inputfile, outputfile)
    
    
if __name__ == "__main__":
    main()        
        

    