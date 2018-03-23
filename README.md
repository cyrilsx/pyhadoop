Hadoop and Python
===

How hadoop communicate with our python script? Pipes
---
A pipe is a form a redirection used in Unix-like systems. Pipes allows us to transfer standard output
to some other destination such as program, file, printer, display...

In linux, the pipe is represent with the symbol `|`.

So our python program will need to read data from the standard input and write result to
standard output.

Let's write a small python program to do that.

Exercise 1:
---
Write a simple program that count the number of word in the standard input `stdin`.

```
$ echo "A lot of information" | python count_word.py 
4
```

Hint:
```
import sys

for line in sys.stdin:
    print(line) 

```
in this example, we just print information! Replace it with the correct code.

Question: How do you send data to the standard output?

Exercise 2:
---
Let's do our mapper.
The result should be:
```
$ echo "foo bar beer linux output bar" | python mapper.py
foo	1
bar	1
beer	1
linux	1
output	1
bar	1

```

Exercise 3:
---
Let's do the reducer
To test it:
```
$ echo "foo bar bar beer linux output bar" | python mapper.py | sort -k1,1 | python reducer.py
bar	3
beer	1
foo	1
linux	1
output	1

```

Exercise 4:
---
Let's try it on hadoop
```
$ bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file /home/hduser/mapper.py    -mapper /home/hduser/mapper.py \
-file /home/hduser/reducer.py   -reducer /home/hduser/reducer.py \
-input /user/hduser/input/* -output /user/hduser/output
```

