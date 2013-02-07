Nude
====

Nude - removes your window dressings.


Nude is a simple python/gtk app which runs in the background and strips all
but a very small border from every window you open. Primarily designed to 
work with the Metacity/Mutter/Muffin family of WMs but will work with most WMs.

Why?
----

I've tried multiple times to use a tiling window manager but they tend to 
destroy apps which need to manage their own window placement (gimp, my custom
vim extensions etc). 

Metacity/Muffin/Mutter have some really nice shortcuts for moving windows 
(ALT-mouse) and snapping them together (SHIFT-ALT-mouse) so you can replicate
tiling fairly quickly _when you need it_, all that is left is to remove those
annoying window decorations.

installing nude
---------------

Nude is a single python file, it requires python-gtk and python-wnck which you
can probably manage installing yourself with apt or something. Then simply run
./nude.py&, perhaps from your ~/.xsession, or perhaps some other way. 

