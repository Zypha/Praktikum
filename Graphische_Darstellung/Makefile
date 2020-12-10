all: build/GraphDarst.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot1.py header-matplotlib.tex matplotlibrc python/tabel.txt| build
		TEXINPUTS=$$(pwd): python python/plot1.py

build/plot2.pdf: python/plot2.py header-matplotlib.tex matplotlibrc python/tabel2.txt| build
		TEXINPUTS=$$(pwd): python python/plot2.py

build/plot3.pdf: python/plot2.py header-matplotlib.tex matplotlibrc python/tabel3.txt| build
		TEXINPUTS=$$(pwd): python python/plot3.py




# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/GraphDarst.pdf: build/plot1.pdf \
						build/plot2.pdf \
						 build/plot3.pdf 

build/GraphDarst.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	Abgabe.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
