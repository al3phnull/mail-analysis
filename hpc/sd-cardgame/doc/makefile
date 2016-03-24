B076963-SD-IR.pdf:

%.pdf: %.tex
	pdflatex $*.tex && \
	pdflatex $*.tex && \
	pdflatex $*.tex

.PHONY: clean
clean:
	@echo rm *.aux *.log *.toc *.pdf *.lot *.lof *.out
	@rm *.aux *.log *.toc *.pdf *.lot *.lof *.out; true

