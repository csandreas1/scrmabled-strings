## Scrambled Strings assignment

[Github](https://github.com/csandreas1/scrmabled-strings)



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
