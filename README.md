DSC 10 Course Notes
===================

These are the course notes for DSC 10 @ UCSD.

DSC 10 is an introductory data science course which develops the core ideas of
statistics via programming and simulation instead of the manipulation of
mathematical formulae. At the same time, the course does not assume that the
reader has any experience in programming; instead, we learn "just enough"
programming to do data science. 

These course notes are based on the textbook [*Computational and Inferential
Thinking: The Foundations of Data
Science*](https://inferentialthinking.com/chapters/intro.html) by Ani Adhikari,
John DeNero, and David Wagner. However, while the textbook uses the
[`datascience`](https://github.com/data-8/datascience) module to introduce
programming with tabular data, these course notes instead use
[`babypandas`](https://github.com/babypandas-dev/babypandas).
`babypandas` is an
opinionated proper subset of the popular `pandas` package designed with the
novice data scientist in mind.


#### Table of Contents

- [Building](#building)
- [Making Changes](#making-changes)
- [Publishing](#publishing)
- [Project Structure](#project-structure)
- [Extensions](#extensions)
- [Reader-Friendly Jupyter Notebooks](#reader-friendly-jupyter-notebooks)


Building
--------

### With Poetry

This project's dependencies are managed with
[poetry](https://python-poetry.org/). First, make sure that you have *poetry*
installed. Before building the project for the first time, run `poetry install`
in the repository root to install the dependencies. Then, to build the project,
run `poetry run make`. The contents will be placed in the `src/_build/html`
directory, and opening `src/_build/html/index.html` in a browser will display
the front page of the notes.

### With Nix

> ⚠️ Nix is used to ensure reproducibility of the build, but it is more difficult
> to set up. Using Poetry is recommended for most use cases.

For a more reproducible build, the Python and Poetry dependencies are also
specified using [Nix](https://nixos.org/). The below assumes that you have
installed a recent version of Nix that has the "flake" feature enabled. For
instructions, see the [Nix Wiki](https://nixos.wiki/wiki/Flakes).

To build the notes, run `nix develop` in the current directory to enter the
development environment; this will install both python and poetry and will
download the needed python dependencies using poetry. Next, run `make` to build
the project. The results will again appear in `src/_build/html`.


Making Changes
--------------

0. Before working on the notes for the first time, run `make init` in the
   project's root. This will install git pre-commit hooks which clean the
   notebook pages of output.
1. Create a new branch to hold your changes with `git checkout -b
   <branch_name>`.
2. Make your changes by editing the appropriate file (usually in the `src/`
   directory).
3. Build and preview the updated notes using the instructions [above](#building).
4. Push your branch to the `dsc-courses/dsc10-notes` repository and submit a
   pull request.


Publishing
----------

Notes are automatically built and published when changes are pushed to the
`main` branch on GitHub. The build and publication is managed by [this GitHub
workflow](https://github.com/dsc-courses/dsc10-notes/blob/main/.github/workflows/deploy.yaml).

The workflow builds the `main` branch with Nix and copies the HTML output to the
`gh-pages` branch published to GitHub Pages.

It also builds "clean" versions of the Jupyter Notebooks that are used as pages
by removing directive cells. These notebooks are what students will see when
they click the "Launch in JupyterHub" link at the top of a page. These cleaned
notebooks are kept in the `notebooks` branch of the repository. This branch
should not be manually edited, as all changes will be overwritten by the
workflow. For more information, see [Reader-Friendly
Notebooks](#reader-friendly-notebooks) below.


Project Structure
-----------------

These notes are written using [JupyterBook](jupyterbook.org) along with
several custom extensions and scripts. Pages are either Jupyter notebooks or
MyST markdown files.

The `src/` directory contains the pages. `src/_config.yml` contains
important configuration variables, such as the URL of the JupyterHub that will
be used to launch notebooks interactively.

`extensions/` contains the extensions which define custom directives. See
[Extensions](#extensions) below.

`scripts/` contains various scripts used in the development and building of the
textbook, such as the script which generates the "cleaned" version of textbook
pages that appear in the `notebooks/book_pages` directory. These scripts should
generally not be invoked manually.


Extensions
----------

Several extensions of MyST markdown are used in this textbook. These extensions
are defined by the files in `extensions/`. Their usage is described below.

### The "hiddenanswer" directive

This directive provides a way of quickly "quizzing" readers for understanding.
It is invoked as follows:

    ```{hiddenanswer}
    ---
    question: This is the question.
    answer: This is the answer.
    ```

This will create a "tabbed" container. The first tab will show the question.
Clicking on the second tab shows the answer.

Long answers or code can be included using the standard 
[YAML syntax](https://yaml-multiline.info/) for multi-line strings. For example:

    ````{hiddenanswer}
    ---
    question: |
        This is the question,
        which will be
        1. Parsed *as* [MyST](#)
        2. With paragraph breaks preserved

        Like this.
    answer: |
        ```
        def func(arg):
            return 42
        ```
    ````
(note that an additional backtick has been used in the directive code fence to
allow us to nest a code block in the answer)

### The "jupytertip" and "jupytertiplist" directives

The `jupytertip` directive creates an admonition box intended to display a tip
related to Jupyter notebooks. The `jupytertiplist` directive creates list of
all of the tips.

Example:

    ```{jupytertip}

    Select `Kernel -> Restart and Run All` to restart the kernel and run all of
    the notebook's cells from top to bottom.
    ```

### The "jupyterhublink" directive

Sometimes it is useful to place a link to open a notebook in JupyterHub within
the text. This can be done with the "jupyterhublink" directive:

    ```{jupyterhublink} path/to/notebook/relative/to/repo/root.ipynb
    ```

The URL used for the links is configured in `book/_config.yml`.


Reader-Friendly Notebooks
-------------------------

Many textbook pages are written as Jupyter Notebooks which are then converted to
HTML by the build process. Readers can click the rocket icon on the HTML page to
launch the notebook version in a JupyterHub session. However, the Jupyter
notebooks used as source documents may include directives and other content that
might confuse readers. Therefore, as part of the build process, the source
notebooks are transformed by a GitHub workflow into "reader-friendly" notebooks
and stored in the `notebooks` branch (these are the notebooks that are launched
when the user clicks the rocket link to interact with a page). The notebooks are
made "reader-friendly" by several mechanisms described below.


### Admonition Cells

Cells containing an admonition, such as

    ```{warning}

    This is a warning.
    ```

are automatically-identified and converted to Markdown:

    **Warning**

    This is a warning.


**Note**: This conversion occurs only if the directive is the only content of
the cell. See `./scripts/make_reader_friendly_notebooks.py` for more
information.


### Hiddenanswer Cells

Cells containing a hidden answer directive, such as

    ```{Hiddenanswer}
    ---
    question: This is the question
    answer: This is the answer
    ```

are automatically-identified and converted to Markdown:

    **Question**: This is the question

    **Answer**: This is the answer

This conversion occurs only if the directive is the only content of the cell.
See `./scripts/make_reader_friendly_notebooks.py` for more information.


### Hiding Cells

Cells can be hidden in the reader-friendly version by adding a
`hide-from-reader` tag to the cell.
