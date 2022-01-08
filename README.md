# Project 1
Building a FAST[AQ] Parser + Building a DNA -> RNA Transcriber

# Assignment Overview
The purpose of this assignment is to bring everybody up to speed on using python and highlight some of the elements of the language and of OOP that will be _inherited_ by downstream course content. We also hope to use this as an opportunity to learn some of the useful tools within github for software development that will be useful to you in your research experiences down the road. 

The learning goals of this project are:

	1. object oriented programming
	2. python language skills
	3. modular programming / predetermined APIs
	4. best practices for reproducible code development

# Assignment Tasks

## Coding Assessment
* Write a Fasta Parser (Write this code in the parse.py file)
* Write a Fastq Parser (Write this code in the parse.py file)
* Write a Transcription Function (Write this code in the seq.py file)
* Write a Reverse Transcription Function (Write this code in the seq.py file)

## Software Development Assessment
* Create a pip installable tool (only locally, do not submit to PyPI)
	* Edit the `pyproject.toml` file to reflect author information
	* Update the dependencies to include those that you use in your code

* Write a unit test (in the test.py file) for
	* Fasta Parser
	* Fastq Parser
	* Transcription
	* Reverse Transcription

* Automate Testing with a [Github Actions](https://docs.github.com/en/actions)

	See blogposts below on helping set up github actions with pytest:
	
	* [post 1](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions)
	* [post 2](https://mattsegal.dev/pytest-on-github-actions.html)

	Ensure that the github actions complete the following:
	* pip installs tool
	* runs pytest

# Getting Started
To get started you will need to fork this repository onto your own github. You will then work on the code base from your own repo and make changes to it in the form of commits. 

## Git Basics

### Overview
Git is a version control tool originally built to keep track of the linux kernel. We will expect you to become familiar with it mainly up to the point of forking, adding, committing, and pushing. There are more things you can do with it, but we will leave that up to you to learn if you are interested. 

### Forking
Forking is a means of copying the existing code base to another "branch" which you can then work on. This leaves the original upstream branch unchanged. This is useful when you are modifying an existing code base for an extra purpose which goes beyond the scope of the original authors. It is also the de facto way to contribute to open source repositories (by forking the existing repo, making your changes, and then merging back into the upstream branch via a pull request). We will not go over pull requests here, but there are plenty of resources online about them if you are interested. 

### General Pipeline
The general overview of git actions is as follows. 
```bash
# staging changed files 
git add changed_file.txt changed_file_2.txt

# commiting changed files
git commit -m "this is a message describing my changes"

# pushing to the repository (upstream branch)
git push
```

# Reference Information
## Test Data
The data we will be testing with will be single-line FASTA files and single-line FASTQ files. This means that the entire sequence will be on one line and you don't need to implement a multi-line FASTA/FASTQ parser. 
We've included some test data under `data/test.f[qa]` which can be used to validate your code as you are writing it. 
If you don't like these test data though you can make your own by changing the seed on the tool `data/make_seq.py` and rerunning the code.

## FASTA File Format
I am sure you have seen this before, but for those who have not, the FASTA file format is a plaintext representation of sequencing data. Some FASTA representations include multiple lines / sequence, but more often than not you will find the format only with 1 sequence per line so that is the format we will use. Here is an example of 3 sequencing records. 

### FASTA Representation
```
>Header
Sequence
```

### Example FASTA 
```
>sequence_1
ACGGACCACCATGAA
>sequence_2
ACGGACCTGAA
>sequence_3
ACGGACCGGATTAACCATGAA
```

## FASTQ File Format
The FASTQ file format is very similar to the FASTA records, but it includes 2 extra lines per record. The only added information is the quality score, which will look like a computer's stream of consciousness but is in fact the confidence that a base is the base called. If you are interested in that process, take a look at PHRED scoring, if you are not that is ok too

### FASTQ Representation
```
@Header
Sequence
+
Quality
```

### Example FASTQ
```
@seq0
TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCG
+
*540($=*,=.062565,2>'487')!:&&6=,6,*7>:
@seq1
CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGG
+
'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,
@seq2
GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTT
+
1,758$,:7654/7<0%5/12%-3>-2.>$$443-,'9,
```

## Transcription

### Transcription 
This process is returning the complement strand to the provided sequence. You can think of this as a mapping of complement bases, except that the `T`s are replaced with `U`s

```
input  : A C T G A A C C C
         | | | | | | | | |
output : U G A C U U G G G
```

### Reverse - Transcription
This process is used to return the reverse of the complement strand. It is equivalent to a `reverse(transcribe(seq))`

```
input       : A C T G A A C C C
              | | | | | | | | |
transcribe  : U G A C U U G G G 

output : G G G U U C A G U
```

# Github Actions
These are really useful tools for software development and are a good way to test if you are adding breaking changes to a code base. They are a must for open source projects, but even in my own moonshine-esque bioinformatic exploits they have proven invaluable. 

The idea behind them is that you can set up github to do something when you do something. If that sounds vague please know that it is merely abstracted; and for good reason! You can set these up to do quite a bit of things and test quite a bit of things in response to multiple conditions being met (i.e. merging branches, publishing packages, alerting failures, etc.). You can get into the weeds with metaprogramming and DevOps nightmares with this, but knowing a little can be really useful in distributing your code to other lab members or collaborators and is something that is useful to learn. 

For the purposes of this assignment we are interested in responding to git `push` commands. We will be writing a github action that will test the installation of our package and then run our unit tests to make sure they pass.

Github already offers some boilerplate actions that can be found under the `Actions` tab on the webpage of your repo. It'll recognize the `*.py` files in the repository and offer you some python related options. There isn't one prebuilt for what we're asking for the assignment, but either of the 4 options provided as defaults could be easily modified to run the installation and the tests - but the PyLint one is the most similar.

You will need to run the following commands in your `YAML` file, but the implementation details are up to you

```bash
pip install . 
pytest -v
```

# Python Modules
`pip` is the go to installer for python packages. You may have heard of `conda` before, which is an environment manager and a package installer, and it is very useful for defining specific environments that don't break as years go by. `conda` is a useful tool, but is beyond the scope of this class. Frankly, `pip` is beyond the scope also in a 10 week course, but writing shareable code is important and learning how to write a standalone module makes that process much easier. 

There are a lot of details and documentation behind making a python module, but the skinny is that at minimum you need to tell pip (the installer) what your packages is, the minimum requirements, and the module dependencies. You put this information into a file: `pyproject.toml` or `setup.py` and then you can install the tool into an existing environment (whethers its conda managed or not). 

The original means of installing was by using the `setup.py` file and specifying information that way, but this is no longer the best practice and it has moved to using a `pyproject.toml` framework. However, both are supported, and it is not a requirement to use one or the other for this class. 

## `setup.py`
You can read more about this [here](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)
Here is an example `setup.py`
```python3
from setuptools import setup

setup(
    name= #NAME_OF_PACKAGE,
    version= #VERSION_OF_PACKAGE,
    author= #WHO_ARE_YOU,
    author_email= #HOW_DO_I_YELL_AT_YOU,
    packages= [
		#WHAT_DO_I_CALL_THIS_THING
		],
    description= #WHAT_IS_THIS_THING,
	install_requires= [
		#WHAT_DOES_THIS_NEED_TO_WORK
		]
)
```

## `pyproject.toml`
you can read more about creating packages easily with [flit](https://flit.readthedocs.io/en/latest/index.html)

here is an example `pyproject.toml`
```toml
[build-system]
requires = [
	"flit_core >=3.2,<4",
	"python_version >= '3.7'"
	]
build-backend = "flit_core.buildapi"

[project]
name = #NAME_OF_PACKAGE
authors = [{
	name = #WHO_ARE_YOU,
	email = #HOW_DO_I_YELL_AT_YOU
	}]
readme = "README.md"
license = {file = "LICENSE"}
classifiers = ["License :: OSI Approved :: MIT License"]
dynamic = ["version", "description"]
dependencies = [
	#WHAT_DOES_THIS_NEED_TO_WORK
]
```

## Installation
If everything works as its supposed to you will now have a python module you can use!

The following code is how you would install it:
```
pip install NAME_OF_PACKAGE
```

# Unit Testing
The testing framework we are going to use in grading is pytest. We recommend you also learn how to use pytest when making your unit tests, but you can use whatever testing framework you want. pytest is easy to use though and can be setup pretty quickly. You can read the documentation for pytest [here](https://docs.pytest.org/en/6.2.x/)

The main idea is that you want to test your code with assertions. These assertions must always be true! If they are broken, then your code is not doing what it's supposed to be doing. 

Here is an example of a unit test:

```python
def add_numbers(x, y):
    return x + y

assert add_numbers(2,3) == 5
assert add_numbers(2,3) != 0
```

pytest will by default recursively search for functions to test in all `tests/test*.py` files that meet the regex `test*`.

Here is an example of a testing script that will test two functions once pytest is run:

```python
from module import add_numbers

def test_module_correct():
    assert add_numbers(2,3) == 5

def test_module_incorrect():
    assert add_numbers(2,3) != 0
```
