export PYTHONPATH := ./extensions:${PYTHONPATH}


.PHONY: html
html:
	# build the HTML version of the notes
	jupyter-book build --builder html src/


.PHONY: notebooks
notebooks:
	# take the notebooks used as source documents and remove tagged cells,
	# placing them in the notebooks/ directory.
	rm -rf _notebooks
	mkdir -p _notebooks
	cd _notebooks && \
		python ../scripts/make_reader_friendly_notebooks.py ../src


.PHONY: init
init:
	# intialize the repository for development
	git config --local core.hooksPath .githooks/


.PHONY: clean
clean:
	rm -rf src/_build
	rm -rf notebooks/book_pages
