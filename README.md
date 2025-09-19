# About Puffin
***Simple, playful, and vicious***

## What?
Puffin is my own programming language, built from scratch. It's simple, consistent, concise, and somewhat logical. Puffin has almost no overloading, and everything is easy to get once you understand it. In the creation of Puffin, I made the decision to abandon almost all of the typical programming conventions, meaning Puffin is truly one of a kind.

To program in Puffin, keep an eye on this repo. It's not currently usable, but I'm currently working on it.

## Why?
In truth, I'm only making Puffin because I can. To say I did. "I made a language, and you're using it. What do you think of that?"<br>
Puffin doesn't fill a niche, it's not the best tool for any scenario, and it really serves no purpose. It's not an esolang, either. It's just here. And that's enough for me.

## When?
Development on Puffin started in September of 2025. I was in math class, and I wondered if there was a language called Puffin. There wasn't, and I started designing the syntax, taking inspiration from JavaScript, Python, and my beloved AXE Basic, a modified version of TI-Basic for the TI-83+ and TI-84+ calculators. That very evening, I wrote the lexer, and Puffin was born.

## How?
I'm currently using Python to make the interpreter for Puffin, but once it's in a stable state I'm going to upgrade to Rust. My final goal is to have the language be self-hosting, meaning the Puffin interpreter will run in Puffin itself. To figure out exactly how a language is made, I've read a lovely article by William W Wold, who made his own language called Pinecone. I'm also referring to the Pinecone source code to see exactly how these things function, and I couldn't have found a better resource.

# Using Puffin
***For fun, practicality, or torture***

## What?
In order to use Puffin, you'll need to write code in the Puffin interpreter, which I've named Puffin Rock because of a little show I used to watch when I was young.<br>
As of right now, there is no Puffin interpreter, but that will change when Puffin is in a stable state.

## Why?
If you want to use Puffin, you surely have a reason. You could be using it just because you think it'd be fun to learn a new little language, you could be using it to support me, or you could be using it just because you're bored. Whatever the reason, I'm glad you chose Puffin!

## When?
I don't really know when Puffin will be available for public use, as I tend to take breaks from projects a lot. If you want to keep up with the progress, consider watching the repo!

## How?
Despite how incomplete it is, the syntax for Puffin is basically set in stone. Here's a simple "Hello, world!" program written in Puffin.
```puffin
.Hullo world
output('Hullo, world!');
```
`> Hullo, world!`
Admittedly, that is quite simple. Here's the classic FizzBuzz program. It cycles through numbers 1 to 20, returning "fizz" if it's a multiple of 3, "buzz" if a multiple of 5, and "fizzbuzz" if both.
```puffin
.FizzBuzz

.Calls the function
fizzBuzz(1, 20);

.Defines the function
def fizzBuzz(int start, int finish):
  for i, start, finish:
    if i % 3 = 0 and i % 5 = 0:
      output('fizzbuzz');
    elif i % 3 = 0:
      output('fizz');
    elif i % 5 = 0:
      output('buzz');
    else:
      output(i);
    end;
  end;
end;
```
The syntax may seem a little weird, but remember: I'm focusing on simplicity while still keeping functionality. Veteran programmers may take some time to get used to it, but beginners should learn it pretty fast. If you want to see more of how Puffin looks, check the *example.txt* file.

# Final Words
***You made it this far***

That's really all I have to say. You can see what Puffin is, why it is, how it is, and I hope that you'll keep up with this project and make wonderful creations.

## Contributing
One more thing:<br>
I'm not great at programming. You might be! If you want to contribute to Puffin, I'm always open to suggestions, and don't be afraid to make a pull request! And don't worry- you'll be credited for anything you do.