"stylesheets": ["../css/style.css"]
"template": "text-page.htm.tpl"
"path": "html/rhythm_chase_1.html" 
"name": "Game Idea"
"index": true
=======================

Don't Let Your Dreams Be Dreams
-----------

Not that the game discussed previously came to me in a dream, exactly, but you know.
Late night epiphanies might as well be dreams. 

I'm going to make it in Rust because Rust is everything, its the future,
it has reached maturity and is hotter than buttered toast and I haven't *really* 
had a major project to let me really learn how it works until now. Furthermore, 
I want to solve some of the lower-level problems of implementing something like this.

Step One: Copy the `miniquad` example code into the project
---------
---------

I did say *some* of the low-level problems. I've forgotten everything I 
ever knew about how graphics actually works, so that's where we're going to start;
getting some tiles onto the screen. 

...it works! Now to take this and refactor it into something I understand.

...oh. oh no. This is not what I want to use at all.

Step Two: Remove the `miniquad` example code, add the `raylib` example code
---------------------
---------------------

[raylib](https://www.raylib.com/) is a small games-like library written in C. It has 
a crate with Rust bindings. It doesn't assume I want to write shader code, and thus 
seems like it will probably be a better choice. Its example is "hello world", but 
we can pretty get it to make a checkerboard pretty quickly!

[red and black checkerboard](/images/checkerboard.png)

Next up: Let's add some rhythm!


