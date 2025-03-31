makefile = """
# Makefile for Sphinx documentation
.PHONY: clean html

clean:
	rm -rf _build/

html:
	sphinx-build -b html . _build/html
"""
