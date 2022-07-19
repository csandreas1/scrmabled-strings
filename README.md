## Scrambled Strings assignment

[Github](https://github.com/csandreas1/scrmabled-strings)

## Problem

This code challenge is based on [this problem ](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004) from Google Code Competitions.

Count how many of the words from a dictionary appear as substrings in a long string of
characters either in their original form or in their scrambled form. The scrambled form of the
dictionary word must adhere to the following rule: the first and last letter must be maintained
while the middle characters can be reorganised.

The scrambled or original form of the dictionary word may appear multiple times but we only
count it once since we only need to know whether it shows up at least once.
For example, if we had the word this in the dictionary, the possible valid words which would be
counted are this (original version) and tihs (scrambled version). tsih , siht and other variations
are not valid since they do not start with t and end with s . Also, tis , tiss , and thiss are not
scrambled forms, because they are not reorderings of the original set of letters.



## Environment setup

Install Python inside a docker container.

Within the project root directory, run the following commands
```sh
docker build --pull --rm -f "Dockerfile" -t scrmabledstrings:latest "."
```

This will build the scrmabledstrings image from the Dockerfile and pull in the necessary dependencies.


Next, you need to create a writeable container layer over the specified image and run it using the command.

```sh
docker run -it --rm --name my-running-app  scrmabledstrings
```


Verify the installation by checking the output, you should see the latest Python 3 version.

E.g.

Python 3.10.5 (main, Jul 12 2022, 11:32:11) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.


## Running the module
Inside the scramble folder run python3 main.py.
Notice that a log file will be generated. Also you can check the console for the output
```
cd project_directory/scramble
python3 main.py
```

## Sample output
    Case #1: 18

## Sample logging
```
2022-07-17 18:36:08,658 Execution started...
2022-07-17 18:36:08,659 Dictionary List:
2022-07-17 18:36:08,659 ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd']
2022-07-17 18:36:08,659 4 matches found for input 'aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt'
2022-07-17 18:36:08,659 ['axpaj', 'apxaj', 'dnrbt', 'pjxdn']
2022-07-17 18:36:08,659 Execution ended succesfully...
```

## Running Tests

You can either run tests manually or configure your IDE/ editor

[Read more](https://docs.python.org/3/library/unittest.html#test-discovery) on Python Unittest Test Discovery

```cd project_directory
python -m unittest discover
```

## Limits
- No two words in the dictionary are the same.
- Each word in the dictionary is between 2 and 105 letters long, inclusive.
- The sum of lengths of all words in the dictionary does not exceed 105.

## Future works
- Python build in lists can be optimized by using Deque (Doubly Ended Queue) from the collections module. Deque is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.