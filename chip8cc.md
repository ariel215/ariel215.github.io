# Chip8CC: A C Compiler for the Chip8

C is a language which can be, and has been, used to program all sorts of devices,
some of them very small indeed. The Chip8 virtual architecture specifies a *very*
small device, with only 4 KB of memory and a limited instruction set. Why not write a C compiler for it? 

Or, well, something resembling a C compiler. The Chip8 instruction set has only 36 instructions, so floating-point math is out, as is the standard library. It uses a 16-bit 
architecture, so our implementation will have `char` and `short` both be 1 byte long, while 
`int` and `long` are both 2 bytes. Signed arithmetic is possible but discouraged, since 
they take more than a single instruction. There's no filesystem and no terminal, so while 
`char` is a type we probably won't bother with implementing the string functions, at least not just yet. 

Also there's no heap, only static data and stack data, only one thread of execution,
and we probably won't implement debug info, variadics, or the preprocesser.

So what's left? 

- signed and unsigned integers
- pointers and arrays
- string constants (although their usage is discouraged)
- structs
- functions
- the IO functions that the Chip8 actually gives you: a 16-key keyboard
  and a 32x64 screen.
- (some) type conversions

It's more about writing code for the chip8 in a kind of c-like syntax, rather than actually 
porting C as specified.


# Front-to-back or Back-to-front?

When writing a compiler from scratch, there's two ways to go about it. Either you can start from the frontend, parsing the language you're targeting and then writing lowerings and transformations until you have machine code. Or you can start from the back, adding features
and transformations to the machine code (in this case the chip-8 instruction set) until you 
can get there from the high-level language. 

Both approach has its advantages. Starting from the end means that at every stage you have programs you can run, which lets you develop functional tests and observe the behavior of the code you produce from the very beginning. In contrast, starting from the frontend means that 
it can take a long time before you arrive at a compiled program you can actually run. On the 
other hand, effectively going back-to-front means parsing not just our C dialect and chip-8 assembly, but everything implemented in between. 

On the balance, with my own proclivities and preferences, it seems better to start at the backend and work backwards; I already have a parser for assembly, and reworking it step by step seems more managable than parsing C and then lowering it. 