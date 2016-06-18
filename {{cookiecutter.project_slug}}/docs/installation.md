# Installation


## Stable release

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```bash
$ pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install {{ cookiecutter.project_name }}, as it
will always install the most recent stable release. 

If you don't have [`pip`][0] installed, this [`Python installation guide`][1]
can guide you through the process.


## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [`Github repo`][2].

You can either clone the public repository:

```bash
$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
```

Or download the [`tarball`][3]:

```bash
$ curl  -OL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
$ python setup.py install
```


[0]: https://pip.pypa.io 
[1]: http://docs.python-guide.org/en/latest/starting/installation/
[2]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
[3]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
