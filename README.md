EC2 Visualizer
========================

This small app provides an easy way to visualize your EC2 Instances and group them by different criteria.
It shows just Instances for now, but more will come :)

Dependencies
------------

Python (I use 2.7, might work on older)
web.py (0.36, same disclaimer)

Other that this, it uses the [GraphDracula](http://www.graphdracula.net/) library, and jQuery.

Usage
-----

You need to put your AWS key and AWS secret in a text file called settings.conf in this format
[Credentials]
key=<key>
secret=<secret>

and place the file either in your Linux home directory or in the current directory from where you're running this.

After this, go to your ec2viz directory and type

python code.py 8080

Point your browser to http://<your ip>:8080/static/view.html

(Takes a little while to load)

