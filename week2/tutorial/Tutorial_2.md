## Stuff from the tutorial

* If you think you are not too comfortable with Python in general, consider doing a basic Python class. You can either do the one offered at our university, or take an online class, as for example https://www.codecademy.com/learn/learn-python


* In the homework, you're asked to check if the numbers you pass to your Matrix-Class are `ints` or `floats`. To do so, you need the python-inbuild-function `isinstance`. The syntax to check if `var` is actually an int or float is: `isinstance(var, (int, float))`.


* The question how to use assertions came up quite a few times in the tutorial. The syntax for assertions is: `assert TRUTHVALUE`, or `assert TRUTHVALUE, "message if TRUTHVALUE is false"`.   

    Assertions are used when some behaviour is supposed to only work if TRUTHVALUE is True -- the program will simply crash (and throw an `AssertionError`) if TRUTHVALUE is False.

    You use assertions the other way round than you'd use if-constructs! You want the TRUTHVALUE to be True, not False! To check if all numbers of a one-dimensional list are ints, you do this:

    ```
    for element in your_list:
        assert isinstance(element, (int, float)), "An element is not an int or float!"
    ```

* There were many questions how to do the homework in the first place. Unfortunately, the homework requires much of the knowledge from the last parts of last monday's lecture, over which I skipped really fast. (Classes, Dunder-methods and decorators) To make up for that, I created an Ipython-Notebook file *Classes_Dunders_Decorators.ipynb*


* If (and only if!) your homework is still too hard for you, I provided the frame for the Matrix-class. This frame contains all the names of the functions, such that you only need to fill these methods to make the pytest pass. Look at this only if you're really unsure on how to solve the task.
