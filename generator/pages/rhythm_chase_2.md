"stylesheets": ["../css/style.css"]
"template": "text-page.htm.tpl"
"path": "html/game_idea.html" 
"name": "Rhythm Chase: pt 2"
"index": true
=======================

Let's Add a Beat
-----------------

Previously, we put a checkerboard grid on screen! An excellent start. Our goal now 
is to have the black and red squares blink back and forth in time,
in a way that is useful for the future.

Currently, we have a `Tile` struct that right now just holds a single color. 
Let's add some rythmic information to our `Tile`s: a time signature, and 
the beats that we want it to be on for: 

``` rust
pub struct TileRhythm {
    // Number of beats in a measure
    length: usize,
    // Length of a beat, in milliseconds
    duration: Ms,
    // which beats to play; zero-indexed
    beats: HashSet<usize>,
    // time elapsed in the measure
    time: Ms,
}
```

We add a method on Tiles to have them keep track of time passing, and to 
only show a color on the appropriate beats, and...

Nothing happens.

Our draw loop is too fast, and so `std::time::Duration::as_millis()` never reaches a full millisecond.
We need to track time more finely; using a 64-bit float to count fractional seconds will do for now.
We might need to worry about floating-point error eventually, but not until it's physically perceptible.

After that update, it's kind of ugly, but it does what we wanted it to. 

Truly painful to look at though.



