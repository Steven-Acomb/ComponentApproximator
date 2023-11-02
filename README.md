# ComponentApproximator
A python script I created for identifying the optimal way to approximate an equivalent resistance/capacitance using a given set of standard components. Free and open source.

This is a quick & dirty script that I wrote more for the purpose of hastening work on my own projects and not necessarily for the use of others. As such, the method I used when I originally wrote this was brute-force with some very minor optimizations to reduce redundancy. 

My implementation is generalized such that it can work for any arbitrary type of component where multiple of them can be compounded to form an equivalent component having a parameter value that is a function of those for the parts comprise it. I am working on a fork of this which abandons that feature in order to allow better optimization for the equations governing resistors and capacitors in series and parallel.

You can create your own component by creating an instance of the Component class with operations that define the ways two of them can be combined and the functions that return the resulting equivalent parameter values.  Refer to the resistor and capacitor components as examples.
