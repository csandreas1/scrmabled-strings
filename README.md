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

## Loger example output
```
2022-07-17 09:34:05,490 Execution started...
2022-07-17 09:34:05,490 Dictionary List:
2022-07-17 09:34:05,491 ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd']
2022-07-17 09:34:05,491 Generated scrambles:
2022-07-17 09:34:05,491 ['axapj', 'apaxj', 'aaxpj', 'aapxj', 'aaxpj', 'aapxj', 'axapj', 'apaxj', 'apaxj', 'axapj', 'aapxj', 'aaxpj', 'aapxj', 'aaxpj', 'apaxj', 'axapj', 'dnbrt', 'drnbt', 'drbnt', 'dbnrt', 'dbrnt', 'pjdxn', 'pxjdn', 'pxdjn', 'pdjxn', 'pdxjn']
2022-07-17 09:34:05,491 Dictionary list with scrambles:
2022-07-17 09:34:05,491 ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd', 'axapj', 'apaxj', 'aaxpj', 'aapxj', 'dnbrt', 'drnbt', 'drbnt', 'dbnrt', 'dbrnt', 'pjdxn', 'pxjdn', 'pxdjn', 'pdjxn', 'pdxjn']
2022-07-17 09:34:05,491 18 matches found for input 'aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt'
2022-07-17 09:34:05,491 ['dnrbt', 'dnbrt', 'drnbt', 'drbnt', 'dbnrt', 'dbrnt', 'aapxj', 'axpaj', 'apxaj', 'axapj', 'apaxj', 'aaxpj', 'pxjdn', 'pjxdn', 'pjdxn', 'pxdjn', 'pdjxn', 'pdxjn']
2022-07-17 09:34:05,491 Execution ended succesfully...

```

## Docker

Install Python inside docker container.

Within the project root directory, run the following commands:
```sh
docker build --pull --rm -f "Dockerfile" -t scrmabledstrings:latest "."
```

This will build the scrmabledstrings image from the Dockerfile and pull in the necessary dependencies.


Next, you need to create a writeable container layer over the specified image and run it using the command.

```sh
docker run -it --rm --name my-running-app  scrmabledstrings
```


Verify the installation by checking the output, you should see the Python version.

E.g.
```
Python 3.10.5 (main, Jul 12 2022, 11:32:11) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

## Running module
Inside the scramble folder run python3 main.py.
Notice that a log file will be generated. Also you can check the console for the output
```
cd project_directory/scramble
python3 main.py
```

## Running tests
You can either run tests manually or configure your IDE.

[Read more](https://docs.python.org/3/library/unittest.html#test-discovery) on python unittest

```
cd project_directory
python -m unittest discover
```