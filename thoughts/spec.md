## Elements

- NB. The web server will be seperate from the API for marking
- Web GUI for uploading work
- Web GUI for creating the test data for each function name
	- Method for generating the questions / test data
- Database for storing user data
- Python scripts for marking and producing the report
	- Fuzzy string matching algorithm for finding functions with the same name
	- Method of extracting relevant functions from the source code
	- Method of securely running the python script
		- Maybe via spinning up Docker containers
	- Php (?) for taking the code snippets for peer review / marking

(I quite like the idea of a command line tool for running the testing)


## Who is it for?

This project aims to solve this difficulty faced by programming teachers when marking an entire class' work. Currently, pupils will all submit a single .py file. The teacher will then go through each file, looking at the coding and writing another Python script to test the given Python scripts with test data. This poses multiple problems, ranging from security issues of running potentially unverified code, to sheer inefficiency and repetitiveness.


## What will this project do?

This project consists of several components. There is the testing aspect. This will be a program that runs the testing on the given script and gives the marked output. There are two inputs: the function names to test and the test data and expected output from the test data; the path to the folder containing the student submissions. The program will then run the test data and output a file for each pupil with their results. As part of this feedback, there is the potential for style recommendation (e.g changes to conform to the PEP 8).

## How is the data handed to the program?

There are several options. The program itself could be run entirely locally on the user's computer. However, this project will also develop a web app that allows for pupils to easily submit work, and for teachers to easily submit the function names, test data, and expected output.

## Other aspects

- Security, the python scripts will be run in a docker container to provide some form of sandboxing
- Client / server model, the testing functionality will be provided over an API.
- Seperate web server, this means that the webserver will be hosted seperately from the API
- If there's too much to do, the first step would be to get the API working, then expand to the web server
- Once the webserver is up, a method of peer-reviewing the code would be devised. This could be done by showing samples of code and allowing people to give a mark out of 5 and provide comments on it. This could be mandatory or gamified in some way or form

---
## The actual spec
### What the teacher uses
- Web GUI to upload test data, expected results and names of functions to test
- There will be the option to programatically generate a template .py file to send to students
- Some form of dashboard to review students' work, with access to the percentage of questions answered
- If desired, the ability to just manually upload files, rather than getting pupils to upload by themselves

### What the pupils get
- A authenticated simple-to-use web gui to upload their work
- Feedback about how their work performed on the test cases (won't actually show the test data)
	- This will be in the form of either a webpage or a downloadable report (haven't decided which is easiest)
- An optional extension would be feedback on the coding style which would include the following:
	- Conformance to PEP 8 (whether function names have underscores, whether variable names are descriptive)
	- "Quiet" functions, whether the functions are printing or directly taking input
	- Runtime, this would provide the average time taken per test case
		- One thing to possibly implement would be runtime comparison with a teacher provided sample

### Other areas that may/may not be implemented based on time
- A method of peer marking scripts which would work as follows
	- The first to submit doesn't review anyone's work
	- The second to submit reviews the first persons
	- The third reviews some portion of first/second

- The reviewing process would work as follows
	- The pupil would submit a general comment about the code they're shown
	- They would then have to provide a mark out of 5 (its out of 5 rather than 10 to reduce the spread and interpretation)
	- The teacher would be able to view the individual comments and ratings of each pupil

