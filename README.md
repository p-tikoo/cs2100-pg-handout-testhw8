> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# Homework 8

## Overview

In this assignment, students will interactively download and parse webpages from Wikipedia.org.

Students will get practice with:
- Comparable
- Equality and hashing
- Recursion on Trees (DFS)
- Scraping websites

## Part 1: Download and parse a single webpage using `requests` and `BeautifulSoup`

You may need to `pip install requests beautifulsoup4` to install both. Because we are limited in the packages we can install on the Pawtograder servers, you must use these two libraries to download the webpage. You may use Claude or a similar LLM to learn about the syntax needed to do this.

Once you have found how to download a webpage in a few lines of code, encapsulate it in a class called `WikipediaPage`. The constructor should take a keyword as the argument, and if there exists a Wikipedia page with that title, it should request and save as attributes:
1. The keyword
2. The text of the webpage
3. A list of all the Wikipedia links found on the webpage

For example, if the keyword is `"effervescence"`, it should:
1. Check and make sure there is a webpage at `https://en.wikipedia.org/wiki/Effervescence`. (Note the case insensitivity.) If there is not, raise an appropriate error.
3. Store the keyword `"effervescence"` as an appropritately named attribute.
4. Store the text of the webpage as an appropritately named attribute.
5. From the list of all links on the webpage, store the ones for Wikipedia pages as an appropriately named attribute (as a list).

Overwrite the `__eq__()` and `__hash__()` methods so that two `WikipediaPage`s are equal if they have the same keyword (title in the URL).

Overwrite the `__str__()` and `__repr__()` methods to return the keyword (title in the URL).

## Part 2: Make `WikipediaPage` `Comparable`

Choose a word, such as "effervescence". Make a class attribute that stores this word as a `target_word`.
When two `WikipediaPage`s are compared, the one with more instances of the `target_word` is considered "bigger".

## Part 3: Add the ability to interactively traverse the Wikipedia webpage graph

We will now treat the `WikipediaPage` class as a node in a graph (or tree). It has a list of options for what
its children could be (the Wikipedia links available on the page), but they are not children, because they are
of type `str` and not `WikipediaPage`. Add another attribute to `WikipediaPage` called `children` which starts
as an empty list of `WikipediaPage`. We will add pages to it as we interactively surf Wikipedia.org.

In `main.py`, implement the `WikipediaSurfer` constructor and methods as described in the comments.
You will need to add documentation. You may remove the "TODO" comments after implementing them.

It may be useful to `pip3 install sortedcontainers sortedcontainers-stubs`.

## Part 4: Try it out

In `main.py`, create an instance of `WikipediaSurfer` and interact with your application. After quitting, copy
the list of keywords outputted into the appropriate question in `Summary.md`.

Anwer the other questions in `Summary.md`.