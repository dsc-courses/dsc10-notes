Dive into Data Science
======================

*Dive into Data Science* is an introductory textbook which develops the core
ideas of statistics via programming and simulation instead of the manipulation
of mathematical formulae. At the same time, the textbook does not assume that the
reader has any experience in programming; instead, we learn "just enough"
programming to do data science. The textbook is written around the
[`babypandas`](https://github.com/babypandas-dev/babypandas) package; an
opinionated proper subset of the popular `pandas` package designed with the
novice data scientist in mind.


#### Table of Contents

- [Building](#building)
- [Developing](#developing)
    - [Getting Started](#getting-started)
    - [Project Structure](#project-structure)
    - [Extensions](#extensions)
    - [Reader-Friendly Jupyter Notebooks](#reader-friendly-jupyter-notebooks)
    - [Git Hooks](git-hooks)


Building
--------

The textbook is developed using [Jupyter Book](https://jupyterbook.org/intro.html).
Pages are written as either Jupyter notebooks or MyST markdown. The development
and build dependencies are managed using [Nix](https://nixos.org/). The below
assumes that you have installed a recent version of Nix that has the "flake"
feature enabled. For instructions, see the [Nix
Wiki](https://nixos.wiki/wiki/Flakes).

To build the HTML version of the textbook, first enter the development shell by
invoking `nix develop` at the repository's root. Then run `make html` (or
simply `make`) to compile the book. The results will be placed in the
`book/_build` directory.

Developing
----------

### Getting Started

Before working on the book, run `make init` in the project's root. Among other
things, this will install git pre-commit hooks.

### Project Structure

This textbook is written using [JupyterBook](jupyterbook.org) along with
several custom extensions and scripts.

The `book/` directory contains the book's contents. `book/_config.yml` contains
important configuration variables, such as the URL of the JupyterHub that will
be used to launch notebooks interactively.

`extensions/` contains the extensions which define custom directives. See
"Extensions" below.

`notebooks/book_pages` contains the Jupyter notebooks that students will see if
they open the interactive version of the textbook page. These notebooks are
automatically generated from the textbook pages by cleaning them of directive
cells. Generating these notebooks is done by running `make notebooks` in the
project root. This target is also run whenever the HTML version of the textbook
is built (using `make html`). For more information on how these notebooks are
generated, see "Reader-Friendly Jupyter Notebooks" below.

Notebooks in the `notebooks/out_of_tree` directory are "out-of-tree" notebooks
that should not appear in the table of contents and are not textbook pages as
such, but should still be published. They are *not* automatically generated. An
example of an "out-of-tree" notebook is one demonstrating features of Jupyter
notebooks, such as markdown cells and syntax highlighting. This is not a
textbook page, but it should be published so that students can interact with the
notebook on JupyterHub.

`scripts/` contains various scripts used in the development and building of the
textbook, such as the script which generates the "cleaned" version of textbook
pages that appear in the `notebooks/book_pages` directory. These scripts should
generally not be invoked manually.

### Extensions

Several extensions of MyST are used in this textbook. These extensions are
defined by the files in `extensions/`. Their usage is described below.

#### The "hiddenanswer" directive

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

#### The "jupytertip" and "jupytertiplist" directives

The `jupytertip` directive creates an admonition box intended to display a tip
related to Jupyter notebooks. The `jupytertiplist` directive creates list of
all of the tips.

Example:

    ```{jupytertip}

    Select `Kernel -> Restart and Run All` to restart the kernel and run all of
    the notebook's cells from top to bottom.
    ```

#### The "jupyterhublink" directive

Sometimes it is useful to place a link to open a notebook in JupyterHub within
the text. This can be done with the "jupyterhublink" directive:

    ```{jupyterhublink} path/to/notebook/relative/to/repo/root.ipynb
    ```

The URL used for the links is configured in `book/_config.yml`.

### Reader-Friendly Jupyter Notebooks

This `notebooks` directory contains the reader-friendly Jupyter notebooks
displayed to the user when they click the link to launch the current page in
JupyterHub.

Many textbook pages are written as Jupyter Notebooks which are then converted to
HTML by the build process. Readers can click the rocket icon on the HTML page to
launch the notebook version in a JupyterHub session. However, the Jupyter
notebooks used as source documents may include directives and other content that
might confuse readers. Therefore, as part of the build process, the source
notebooks are transformed into "reader-friendly" notebooks and stored in the
`notebooks/book_pages` directory (these are the notebooks that are launched when
the user clicks the rocket link to interact with a page). The notebooks are made
"reader-friendly" by several mechanisms described below.

`notebooks/out_of_tree/` contains various other Jupyter notebooks that should be
available for interaction, but which are not themselves pages in the textbook.
They are not automatically generated.

Below, several mechanisms are described for creating "friendly" Jupyter
notebooks from book page source notebooks.


#### Admonition Cells

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


#### Hiddenanswer Cells

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


#### Hiding Cells

Cells can be hidden in the reader-friendly version by adding a
`hide-from-reader` tag to the cell.

### Git Hooks

To install the Git hooks, run `make init` in the repository root.

The pre-commit hook removes the output of every cell in every notebook in
`book/`. This makes for more meaningful diffs.
