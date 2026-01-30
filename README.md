# COP4533-Matching-and-Verifying
Programming Assignment 1

Paige Vanover UFID : 22473613
Victoria Villasana UFID: 86143370

## To get started:
- Clone the repository into your desired Python supported IDE.
- No external dependencies

## To run the matcher:
The matcher will take the input from inputfile, generate a matching and then write the output to its corresponding outputfile

### Steps:
1. Open 'src/matching.py'
2. Scroll down to main and set the "TEST = matcher"
3. Choose input and output file inside of main(). For example:
-  **inputfile = "data/example.in"**
- **outputfile = "data/example.out"**
4. Run src/matching.py
- Once this is run, it will write out the matching pairs to a .out file. The verifier will then check that the matchings made are stable/unstable/invalid

## To run the verifier
The verifier will check exisiting .out files including edge cases

### Steps:
1. Open 'src/matching.py'
2. Scroll down to main and set the "TEST = verifier"
3. run src/matching.py
- If want to test another .out file, add file to data and then add line like this to the bottom of verifier
        **final_check(inputfile, "data/NAME_OF_FILE_HERE.out")**
- Once this is run, the verifier will report if the matching is VALID STABLE, UNSTABLE: blocking pair (h,s), or INVALID with a reason

## Runtime's with Graphs

### Runtime Graph for Gale-Shapley matching()
<img width="789" height="404" alt="image" src="https://github.com/user-attachments/assets/e45b3a7e-42eb-4630-b67b-ad88e8123ba1" />

### Runtime Graph for verifier + stability checking
<img width="468" height="249" alt="image" src="https://github.com/user-attachments/assets/c8170438-3269-4a9d-a636-b3e6d442e64f" />

- After running the inputs on the verifier function, a graph was made to see the pattern with an increasing size n. From the graph, it can be seen that for inputs size n = 1 to n = 16, the verifier had an extremely low runtime and appears on the graph as almost flat. As n increases, the runtime begins to increase a little bit more noticeably, especially when we reach around input size n = 64. The runtime increases the most with larger inputs like n = 128, 256, 512. When run, the verifier builds the matrices using functions student_rank and hospital_rank, then it checks for blocking pairs using the blocking pairs function. After that, it performs the final check tying everything together. Since the steps are executed together, the verifiers time complexity can be seen as O(n^2). 
