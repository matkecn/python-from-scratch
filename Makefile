.PHONY: help install test lesson verify scaffold report notebook lint clean

SLICE ?= 1-50

help:  ## Show this help
	@grep -E '^[a-z-]+:.*?##' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

install:  ## Install the tools you need
	python3 -m pip install -r requirements-dev.txt

test:  ## Run every test and every docstring example
	python3 -m pytest

lesson:  ## Run the tests for one slice of the course, for example make lesson SLICE=101-120
	python3 -m pytest -- $(SLICE)

verify:  ## Check that every lesson is complete and runnable
	python3 tools/verify.py

scaffold:  ## Create any lesson files that do not exist yet
	python3 tools/scaffold.py

report:  ## Show how many lessons are hand written and how many are drafts
	python3 tools/scaffold.py --report

notebook:  ## List the notebooks you can open
	@ls */lesson.ipynb | head -20
	@echo "... and many more"

lint:  ## Check style, when ruff is installed
	ruff check .

clean:  ## Remove caches
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache
