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
3. Choose input and output file inside of main()
    For example -> inputfile = "data/example.in"
                   outputfile = "data/example.out"
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


Runtime Graph for Gale-Shapley
<img width="789" height="404" alt="image" src="https://github.com/user-attachments/assets/e45b3a7e-42eb-4630-b67b-ad88e8123ba1" />
