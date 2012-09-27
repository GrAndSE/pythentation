pythentation
============

What is Pythentation?
---------------------

Tool to build a pretty presetations in html format from single markdown file.

Writting using [python](http://python.org/) and [reveal.js](https://github.com/hakimel/reveal.js)

Small and simple.

How can I create a presentation?
--------------------------------

Just write a markdown in file:

	Presentation title
	==================

	Slide title
	-----------

	Some slide taxt

And call the pythentation with this file name as argument.

How to try?
-----------

[Download from github](https://github.com/GrAndSE/pythentation/zipball/master)

Unpack.

Write some markdown (ex. my-markdown.md)

Generate html:

	python pythentation/__init__.py my-markdown.md
