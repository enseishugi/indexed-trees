# indexed-trees

It's a python3 script to print Emacs org-mode trees sharing the same structure, except for some variables, by traversing all the possible values.

For example, say we want to print trees of the form
```
* Exercise I.2.X
  #+start_exercise
  #+end_exercise
  
  file:~/a/path/to/a/file-X
```
where X denotes an integer, and we want it to vary from 1 to 150. Well, this script does the job.

## How this idea started
When I study a (usually math) book, I create an .org file and create a trees for chapters, sections, etc. Each section has exercises, and usually there are tons. Quite immediately, I got tired of creating subtrees over subtrees.

Most of them share the same structure, along the lines of
```
* Exercise I.2.3
  #+start_exercise
  #+end_exercise
  
* Exercise I.2.4
  #+start_exercise
  #+end_exercise
```
and sometimes I add hypertext to files

so it's quite natural to delegate some of the work to a script.

## Future goals
Well, I wrote this in python3 because I'm not fluent enough with elisp; this script was thought to be temporary. I'd eventually turn it into an Emacs org-mode function as soon as I'll be able to do it.
