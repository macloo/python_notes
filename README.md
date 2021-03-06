Python Notes (Python 2.7)
=========================

In trying to learn Python, I have used several resources. I have produced a lot of files, some of which I probably will never need again.

In this repo, I am saving my files to which I expect to return, for reference.

The tests/ directory contains trivial small files, referenced in some of my notes.

## The Files

* [alien_while_loop.py](alien_while_loop.py)

  Use of random number to make a simple fight scene; if-elif-else; while-loop

* [builtin_functions.py](builtin_functions.py)

  10 useful built-in functions, used in examples.

* [classes_objects.py](classes_objects.py)

  Demo of how to create classes, with their attributes and internal functions. How the functions are called. How to pass one class into another class — in this case, making all "customers" also "people."

* [format_strings.py](format_strings.py)

  Demo of how using a different formatter produces different output.

* [lambda_and_map.py](lambda_and_map.py)

  How to use lambda (Python's anonymous function construct) and `map()`, a built-in function that's kind of like a for-loop in that it runs a function on each item in a list or a range. Handy!

* [lists_practice.py](lists_practice.py)

  Things we can do with lists.

* [modulo_test.py](modulo_test.py)

  Demo showing how modulo (modulus) works: Test a number to see if it is prime.

* [options_for_function_args.py](options_for_function_args.py)

  These options can make the arguments more flexible. One option is to set a default value. Another is to say the number of arguments might vary.

* [print_python_keywords.py](print_python_keywords.py)

  Short program that prints all Python keywords.

* [read_write_easy.py](read_write_easy.py)

  Very basic read and write for files: `open()`, `read()`, `write()`, `close()`.

* [split_string_make_dict.py](split_string_make_dict.py)

  Split a string on a char (e.g. ",") to make a list. If the resulting list
  items are splittable pairs, you can use a for-loop to build a dictionary
  from the list.

* [string_searches.py](string_searches.py)

  Run various tests on a string to find out whether it would be okay
  to use it as a filename.

* [try_except.py](try_except.py)

  Some simple examples of error handling. Students sometimes want to use an if-statement instead, but this is better because you can catch specific types of errors. Also, use of `finally:`

* [tuples.py](tuples.py)

  Examples of tuples. Unlike a list, a tuple is immutable.

* [turtle_tests.py](turtle_tests.py)

  Learning to use Python's turtle module.

* [useful_modules.py](useful_modules.py)

  Tests with copy, random, time, pickle (for saving binary data out, as from a game, and then reading it back in).

* [wrapping_02_notes.py](wrapping_02_notes.py)

  Examples based on a Python intro. Using for-loops to get keys, values from a dictionary is useful. Good for a fast review of basics. Also `if x in y:`

* [write_read_file.py](write_read_file.py)

  Writing non-text data into a file as text and (awesomely) reconstituting
  the data back into Python objects as you read it out of the text file.

## Files in /tests

Very trivial small files to show me how something is done.

## Files in /texts

* [firstamendment.txt](texts/firstamendment.txt) - dummy text file

* [p_data_types.txt](texts/p_data_types.txt)
* [p_escapes.txt](texts/p_escapes.txt)
* [p_keywords.txt](texts/p_keywords.txt)
* [p_operators.txt](texts/p_operators.txt)
* [p_string_formatters.txt](texts/p_string_formatters.txt)

  My notes about these, following LPTHW ex. 37.

* [p_style_guide.txt](texts/p_style_guide.txt)

  My notes about Python style (from PEP 8).
