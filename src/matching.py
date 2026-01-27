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
    
    with open("data/example.out", "w") as f:
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
        


def main():
    n, hospitalList, studentList = parsefile("data/example.in")
    matching(n, hospitalList, studentList)

    test = read_output("data/example.out", n)
    print("Parsed hospital matches from output:", test)

    ''''
    dup_test = read_output("data/duplicate_student.out", n)
    print("Testing duplicate student match:", dup_test)

    dup_hosp_test = read_output("data/duplicate_hospital.out", n)
    print("Testing duplicate hospital match:", dup_hosp_test)

    bad_lines = read_output("data/wrong_num_lines.out", n)
    print("Testing wrong number of lines:", bad_lines)

    bad_range = read_output("data/bad_range.out", n)
    print("Testing out of range indices:", bad_range)
    '''
    
if __name__ == "__main__":
    main()        
        

    