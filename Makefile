export PYTHONPATH := ./extensions:${PYTHONPATH}


.PHONY: html
html: notebooks
	# build the HTML version of the textbook
	jupyter-book build --builder html src/


.PHONY: notebooks
notebooks:
	# take the notebooks used as source documents and remove tagged cells,
	# placing them in the notebooks/ directory.
	mkdir -p notebooks/book_pages
	cd notebooks/book_pages && \
		python ../../scripts/make_reader_friendly_notebooks.py ../../src


.PHONY: init
init:
	# intialize the repository for development
	git config --local core.hooksPath .githooks/


.PHONY: clean
clean:
	rm -rf src/_build
	rm -rf notebooks/book_pages
