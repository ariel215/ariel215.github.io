What do you do when you have a function that needs to be called in a certain context? 

The miniquad framework has two initialization functions, sort of. 

`miniquad::start` serves as the entry point for the framework. You write a struct that implements
the `miniquad::EventHandler` trait, and then pass a constructor for that struct into 
`miniquad::start()`, which will call its trait methods in a loop forever and ever.

One thing the framework tries to do is to provide platform-independant abstractions for 
many things you might need to do in order to display graphics. The trait that does this is 
`miniquad::RenderingBackend`, and you the user get a struct implementing it by calling 
`miniquad::window::new_rendering_backend()`, which you can then use to load shaders etc.

Quiz time: you call `new_rendering_backend()` before you call `miniquad::start()`. What will happen?

...

It panics! Because `new_rendering_backend()` assumes that you've already loaded the graphics library you're going to use (either OpenGL or Metal), and tries to initialize the `RenderingBackend` with 
function pointers from that library. Minor credit to the author: these functions are represented as  Options that then get unwrapped, which is why you get a panic and not something less pleasant.

Why might you think you could do this? Well, for other design reasons, you may have written your code
so that the event loop is entered from a method on your `EventHandler`, and so you want to do something
like
```
fn run(self){
    miniquad::start(move||Box::new(self))
}
```
This looks like it should work; it typechecks, it compiles, and it runs afoul of this dependency we just described. 

The *intent* is that you only call `new_rendering_backend()` from within the callback that you pass into `miniquad::start()`. Now, sometimes libraries end up with dependencies like this, and you just have to document them and hope that the user reads them, but it feels like in this case we should be 
able to find a design that does better.

One possibility, of course, is that this is just separation of concerns gone awry. The code that loads
OpenGL should go in the constructor for miniquad's GlContext, not in the code that launches the 
event loop. I haven't looked closely enough to see if there's anything blocking that.

Assuming that the OpenGL loading code really does belong in `miniquad::start` -- or at least, that it would be a great deal of work to refactor everything so this is no longer the case -- one could change the signature of `miniquad::start()`. Right now it takes a closure of type `FnOnce() -> Box<dyn EventHandler>`. It could instead take a closure of type `FnOnce(Box<dyn RenderingContext>) -> Box<dyn EventHandler>`; user code would in turn have to change to accept a `RenderingContext` instead of constructing one itself. The nice part of this is it expresses the dependency through Miniquad is a relatively old framework, with ... some number of users; it would be rude to hand them a breaking change to 

