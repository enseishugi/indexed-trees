# 

# How this idea started
When I study a (usually math) book, I create an .org file and create a trees for chapters, sections, etc. Each section has exercises, and usually there are tons. Quite immediately, I got tired of creating subtrees over subtrees.

Most of them share the same structure, along the lines of
```org-mode
* Exercise I.2.3
  #+start_exercise
  #+end_exercise
  
* Exercise I.2.4
  #+start_exercise
  #+end_exercise
```



for each numbered nodes in Org sharing the same structure. So I wrote this messy code.
