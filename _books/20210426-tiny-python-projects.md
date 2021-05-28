---
title: "Tiny Python Projects"
description: "Book of the Week. Tiny Python Projects by Ken Youens-Clark"
cover: "images/books/20210426-tiny-python-projects/cover.jpg"
image: "images/books/20210426-tiny-python-projects/preview.jpg"
start: 2021-04-26 00:00:00
end: 2021-04-30 22:59:58
authors: [kenyouens-clark]
links: 
  - text: Book's page
    link: https://www.manning.com/books/tiny-python-projects
  - text: Book's GitHub repository
    link: https://github.com/kyclark/tiny_python_projects

archive:
- name: Dustin Coates
  text: Hi Ken Youens-Clark, great to see a fellow Manning author! Would you say your
    book is a good fit for someone coming from other languages? I've a lot of experience
    with JS and Ruby, for example, but most of my Python is written with a JS accent.
    Would your book be good to learn the Python way of doing things?
  replies:
  - name: Ken Youens-Clark
    text: 'Hey, Dustin. Yes, I specifically hope that someone is coming from a previous
      language, but I also try to cover everything just in case this is a person''s
      first Python book. I try to show Pythonic ways to do things you might know from
      other languages, but I also try to show that Python is quite flexible and often
      has many ways to accomplish the same task. For instance, the list comprehension
      is very Pythonic (it''s similar to Haskell in this way). C-type languages such
      as JavaScript might initialize an empty list and use a `for` loop to build it
      up

      ```
      >>> powers_of_two = []
      >>> for i in range(4):
      ...     powers_of_two.append(2**i)
      ...
      >>> powers_of_two
      [1, 2, 4, 8]
      ```

      But a list comprehension can do this in one step:

      ```>>> powers_of_two = [2**i for i in range(4)]
      >>> powers_of_two
      [1, 2, 4, 8]```

      I think these kinds of idioms make Python easier to read and share.'
  - name: Ken Youens-Clark
    text: 'I should say that I quite flagrantly violate the Python Zen of "there should
      be one obvious way to do something." I specifically show many ways to accomplish
      the same ideas, and I really like to get the reader used to purely functional
      ideas. So, if you can see how a `for` loop (which is a _statement_ that produces
      no result) can be written as a list comprehension (which is an _expression_
      that returns a value), then you might be comfortable writing this with `map`:

      ```>>> list(map(lambda i: 2**i, range(4)))
      [1, 2, 4, 8]```

      Similarly, if you are comfortable using a list comprehension with a guard to
      conditionally accept some values:

      ```>>> evens = [n for n in range(10) if n % 2 == 0]
      >>> evens
      [0, 2, 4, 6, 8]```

      Then you might be good with learning to use `filter`:

      ```>>> list(filter(lambda n: n % 2 == 0, range(10)))
      [0, 2, 4, 6, 8]```

      JavaScript really uses functions in a similar way, in my experience. That is,
      functions are first-class objects that can be passed as values and overwritten,
      used as callbacks, etc. I think teaching these kinds of ideas to novice programmers
      will make it easier for them to launch into other languages, too.'
  - name: Eric Sims
    text: Wow, those examples are really helpful. I am getting better at using list
      comprehensions, but that `filter` with the `lambda` function to do the same
      thing is cool!
  - name: Ken Youens-Clark
    text: When you start thinking in terms of functions and how they fit together,
      you can see how to fit code together like Lego pieces. Working in a strongly/statically
      typed, purely functional language (e.g., Haskell or Elm) is one way to burn
      your boats and force yourself to think this way. My experience in Elm totally
      changed my approach to using imperative, dynamically typed languages.
  - name: Ken Youens-Clark
    text: 'Note that you don''t have to write `lambda` defs. You can also use regular
      functions:

      ```>>> def p2(n): return 2**n
      ...
      >>> list(map(p2, range(4)))
      [1, 2, 4, 8]```'
- name: Brian Fleming
  text: 'Hi Ken Youens-Clark

    Can you recommend whether you think a Marketing Analyst (GA/SQL based) that''s
    looking to upgrade their skills would be better starting with something like your
    book and Python or concentrate on a new platform and deprioritise coding/Python?'
  replies:
  - name: Ken Youens-Clark
    text: 'SQL databases have been an integral part of everything I''ve written over
      the last 25 years. For the longest time, I relied on Perl for this, but Python''s
      integration with SQL platforms is really great. For instance, I now mostly use
      Postgres and rely on the `peewee` module to create an object-relational module
      (ORM) that minimizes the amount of raw SQL I write. When I combine that with
      something like FastAPI and type hints, I can bang out a web back-end API in
      relatively.

      For instance, I''m currently working on [ct.c-path.org](http://ct.c-path.org)
      for my employer (The Critical Path Institute). This a mirror of [clinicaltrials.gov](http://clinicaltrials.gov)
      with a custom query interface. All my code is in [https://github.com/criticalpathinstitute/ctweb](https://github.com/criticalpathinstitute/ctweb),
      and you can look in the "fastapi" directory to see how I leverage these technologies
      to create what is, IMHO, a readable codebase for interacting with Postgres.

      So, TL;DR: Yes, I would definitely recommend learning Python and how to integrate
      with databases. If you combine types and tests, then I think you''ll get even
      more out of this, and I discuss these at length in my book(s).'
  - name: Brian Fleming
    text: "Thanks Ken, I'll have a look at the repo \U0001F642"
  - name: Ken Youens-Clark
    text: I have plans to pitch a book about Python + ORMs + SQL databases (SQLite,
      Postgres) one day. My current project is _Hands-on Systems Programming with
      Rust_ for O'Reilly, and I might pitch a book on purely functional programming
      with Elm next. Not sure when I'll get to Python/SQL.
- name: Matthew Emerick
  text: "Hey, Ken Youens-Clark! Thanks for doing this. \nDo your tiny projects make\
    \ for a great portfolio strictly as they are in the book? Are there recommendations\
    \ to expand them?"
  replies:
  - name: Ken Youens-Clark
    text: If I were a potential employer and saw that someone had managed to create
      a repository of programs that included documentation, sample data, and tested
      code, I'd be fairly impressed. If a person did nothing other than type out the
      code I present and run the tests, I think that would be a fairly impressive
      first step in learning how to organize, run, and test Python. If they had managed
      to write their own solutions before consulting my versions, that would be even
      more impressive. If they went on to expand the programs by adding features and
      tests, that would be &lt;chef's kiss&gt;. Each chapter has a "Going Further"
      list of suggested expansions, but one's imagination is the limit.
- name: Matthew Emerick
  text: Do the projects put together teach a wide enough variety of skills to give
    a deeper understanding of what Python is capable of?
  replies:
  - name: Ken Youens-Clark
    text: Python can do an incredible amount, but I can only move the user a couple
      clicks along. That is, when I first started talking with Manning, they suggested
      I imagine a scale 1-10 where 1 is a beginner and 10 is an expert. I can only
      hope to move, say, a 2-3 level user to maybe a 5-6. Trying to move someone from
      a 2 to a 9 in one book makes for material that moves too quickly. So I try very
      hard to make a novice programmer feel comfortable with testing which in and
      of itself is usually considered some sort of super-skill. Testing is not actually
      all that difficult, but I hardly find anyone trying to teach this vitally important
      skill. While I try to show just how flexible Python is as a language, I would
      say my secret goal is to get people to think about how to write small, testable,
      composable functions. I want my readers to be able to take these skills and
      apply them to learning and writing any other languages they encounter.
- name: Matthew Emerick
  text: Is there a project in your book that shows you how to call C code?
  replies:
  - name: Ken Youens-Clark
    text: No, I would consider that a very advanced skill. To be honest, I've never
      written a C program beyond "Hello, world!" I never have need for C, and I have
      no idea how to call it from Python. My next book is a similar beginner's guide
      to Rust, which I would consider a much better language for trying to interface
      with external libraries.
- name: Sara Garcia
  text: 'Hi Ken Youens-Clark

    I''m reading the list of the Python projects of your book  and I wonder if the
    reader should have a previous knowledge of python, or any other programming language
    or concepts. I also want to know what concepts do you recommend to expand, and
    if you have another book to recommend for that.'
  replies:
  - name: Ken Youens-Clark
    text: 'Hi, Sara. I honestly think _Tiny Python Projects_ is a great 2nd or 3rd
      Python book. If you don''t know the language at all, you might find _The Quick
      Python Book_ or something like that a good introduction. If you know any other
      language at all, my book is probably a fast way to get familiar with the language.
      Just reading about concepts is not at all the same as trying to write your own
      programs. Writing forces you to really interact with the language, and learning
      how to test your programs will really focus your attention.

      I think my book explains a lot of basic programming concepts reasonably well,
      things like loops and variables and functions. I completely avoid object-oriented
      programming for various reasons I could explain if you care. If you don''t known
      OOP, then you definitely don''t need that concept. I subtly push my own biases
      that include a penchant for purely functional program, immutable data structures
      (e.g., tuples), the use of testing, and the introduction of type hints which
      comes in the last chapter. If you like these ideas, you might be interested
      in my second book, _Mastering Python for Bioinformatics_ (O''Reilly) which will
      be in print next month. That book goes much deeper into testing, types, and
      functions, even if you are necessarily interested in biology + computer science.
      The material is actually fascinating, and the solutions can get quite complex.'
- name: Anna Parfenova
  text: 'Hi Ken Youens-Clark!

    Despite I don''t belong to Z-generation, it''s hard for me to start learning (programming)
    from books, when there are plenty of video-courses and other web-resources available.

    I see one big *pro* of book:

    - it will make me re-type things instead of copy-pasting.

    What are other pros (and maybe cons)?'
  replies:
  - name: Alexey Grigorev
    text: Actually, you can copy-paste from pdf...
  - name: Ken Youens-Clark
    text: The reader will gain the biggest benefit by writing the programs. Even if
      you do copy-and-paste from the PDF, the act of getting the code, altering the
      programs, and running the tests will give you a categorically different experience
      from simply reading the book. I strongly encourage the reader to type in all
      the examples, both the examples in the REPL and the actual programs. In the
      language of pedagogy, this is an "active learning" approach where the student
      *does* stuff rather than just listens or reads. I really enjoyed my times in
      the classroom using these kinds of exercises to get people writing and testing
      programs. Those classes were so different from times when I would just lecture
      about Python lists and blah blah blah. If you want to learn to write programs,
      you have to write programs!
  - name: Ken Youens-Clark
    text: Oh, also all the code/tests/solutions are directly available from my GitHub
      repo at [https://github.com/kyclark/tiny_python_projects](https://github.com/kyclark/tiny_python_projects).
  - name: Ken Youens-Clark
    text: And I've also created videos to walk a person through the solutions, step-by-step.
      You can find them all from [http://tinypythonprojects.com/](http://tinypythonprojects.com/).
      This is another important skill I'm trying to teach--that is, how should one
      start a program, what's the next logical step. For instance, I suggest using
      the `bin/new.py` program in the repo, then defining the parameters using `argparse`
      and testing the interface with the first couple tests. Then move to maybe printing
      something, maybe reading a file, etc. The process of writing and testing is
      much more important than just learning Python syntax.
  - name: Vladimir Finkelshtein
    text: In my personal experience, online videos tend to be on the shorter side,
      so they will usually cover each topic in much less detail than a corresponding
      chapter in a decent book. Many of these videos are made by reading a chapter
      from a good book and trying to squeeze it into a determined time interval.
  - name: Anna Parfenova
    text: "Thank you, Ken Youens-Clark \U0001F64F\nGood point, Vladimir Finkelshtein\
      \ \U0001F914"
- name: Eric Sims
  text: "Not so much a question at the moment, but a comment from the GitHub repo:\
    \ I really like your philosophy of \"test-driven development\" and writing tests\
    \ before writing code. Taking the time to define success before jumping into a\
    \ project would probably save me a fair bit of time and certainly help manage\
    \ scope creep! \U0001F604"
  replies:
  - name: Ken Youens-Clark
    text: '"Weeks of coding can save you hours of planning." -- Anonymous'
  - name: Ken Youens-Clark
    text: I really feel that TDD is an under-appreciated teaching tool. I found that
      giving my students a test suite makes it crystal clear what the expectations
      are for a program. I would actually see students get excited when they would
      go from all failing tests to passing one or two tests and finally passing all
      tests. The motivation of see all those passes should not be dismissed.
  - name: Eric Sims
    text: I hadn't thought of it that way, but you are definitely right. It feels
      so rewarding to solve lots of small problems along the way and celebrate the
      small wins.
  - name: Ken Youens-Clark
    text: Tests really prove their value when you try to add a new feature to your
      program and find you've accidentally broken something that used to work.
- name: Simon Steinkamp
  text: "I had a quick look over the projects and the Github Repro and it sure looks\
    \ interesting \U0001F642\nAs someone who has done quite some coding in Python\
    \ so far (including a little package with tests) but never took the time to get\
    \ a  formal / solid Python foundation - I was wondering what someone like me could\
    \ get out of your book and whether it could help to get more structure in the\
    \ hacky coding style?  ( I hope the phrasing isn't to confusing)"
  replies:
  - name: Ken Youens-Clark
    text: If you are a more experienced developer, the first few chapters may feel
      a little simple for you. I'd still encourage you to work through even the most
      basic programs to get a feel for using tests to verify your programs. TDD encourages
      us to first write tests and *watch them fail*. Then fix the code until the tests
      pass. If you've never done this before, you may be surprised at just how easy
      testing with a framework like `pytest` can be. I really feel like "testing"
      is made out to be some really advanced topic, beyond the comprehension of students
      and novices, and is something you'll learn about on the job. My experience is
      that testing is easier than not, and that not enough people on the job use testing
      or ever teach it. I may also surprise you with how differently Python can be
      written when you rely mostly on functions and tests. For instance, if you've
      mostly done OO-style programming with Python, you'll see much simpler code in
      my examples. So, yes, I think you'd get a good bit from going through my examples.
  - name: Simon Steinkamp
    text: "Great! Thanks \U0001F642"
- name: Gant
  text: Hi Ken Youens-Clark what is the most fun project in the book?
  replies:
  - name: Ken Youens-Clark
    text: T'ehres stenhoimg aoubt The Srebalcmr taht I find rellay fun. I'ts amnizag
      taht your biarn can raed this text, and I ejnoy wtrinig pgmraros taht eplmoy
      rodnamsnes. ([https://github.com/kyclark/tiny_python_projects/tree/master/16_scrambler](https://github.com/kyclark/tiny_python_projects/tree/master/16_scrambler))
  - name: Ken Youens-Clark
    text: I also love ideas about encryption, and [Gematria](https://github.com/kyclark/tiny_python_projects/tree/master/18_gematria)
      is interesting to me. I got that idea while reading _The Chosen_ by Chaim Potok.
  - name: Ken Youens-Clark
    text: Although this is not a reversible encryption. My latest book using Rust
      will likely include a simple ROT13 (rotate 13 characters) encryptor.
  - name: Ken Youens-Clark
    text: Each chapter is intended to teach some few skills. Even though they are
      playful, trivial programs like "Apples and Bananas" can lead you to explore
      many interesting ways to write the same idea ([https://github.com/kyclark/tiny_python_projects/tree/master/08_apples_and_bananas](https://github.com/kyclark/tiny_python_projects/tree/master/08_apples_and_bananas))
      while testing helps you learn how to *refactor* programs while still ensuring
      they work.
- name: Glenn
  text: Hi Ken, what's something about Python that you learned while writing this
    book that you didn't know about beforehand? And possibly the most important question,
    in terms of "RegEx", are you of the camp that it's pronounced with a hard g (like
    garden) or soft g (like generator)?
  replies:
  - name: Ken Youens-Clark
    text: 'Hi, Glenn. Your first question is really interesting. I actually find it
      remarkable that I got a chance to write a book on Python when I''d only been
      working in the language a couple of years. I spent most of my career using Perl,
      which I find to be extremely similar in all the important ways (dynamically
      typed, c-like syntax, modules, variables). Still, there were lots of nuances
      to learn, and I''d say that I got much more familiar with testing/`pytest` and
      the use of randomness which I''d never really used much before. E.g., while
      writing one of the exercises I discovered that the reader might make some random
      choices in a different order than I did and so would end up with a different
      answer. Not a *wrong* answer, just different because the RNG (random number
      generator) would be called differently. I learned much more about testing writing
      this second book (_Mastering Python for Bioinformatics_, O''Reilly, 2021) such
      as how to better organize tests and data as well as how to integrate linting
      and type checking.

      As to your second question, I guess I''m completely inconsistent because I pronounce
      "regex" with a soft _g_ like "rej-ex" but "regular" has a hard _g_. Completely
      random anecdote: A couple of years ago I was walking across the Univ of AZ campus
      to get a coffee with a friend and we bumped into Noam Chomsky (who''s done tons
      of work in linguistics and "regular" languages and such). We were star-struck.'
  - name: Glenn
    text: Thanks for the response, and a very cool story about Noam Chomsky! I remember
      seeing Perl listed on a Stack Overflow survey as the "most hated language" by
      programmers. What are your thoughts on that?
  - name: Ken Youens-Clark
    text: 'It''s easy to write bad code in any language. Perl''s penchant for sigils
      like `@{ $hash{ $key }}` can be really hard to read. I understand that fine,
      but I also appreciate that it''s hard to read. Perl was ascendent in the late
      90s and early aughts when I became a web developer and fell into bioinformatics.
      Perl was king of text processing and regular expressions, and it worked really
      well in those domains. I loved it very much and only used Perl for about 15
      years. I released a few modules ([https://metacpan.org/author/KCLARK](https://metacpan.org/author/KCLARK)),
      SQL::Translator was perhaps one of my best works, and I built and maintained
      a cool genomic map viewer ([https://pubmed.ncbi.nlm.nih.gov/19648141/](https://pubmed.ncbi.nlm.nih.gov/19648141/)).

      Sometime in the last 10 year, Python simply took over scientific computing.
      Modules like Numpy, Pandas, and Scikit-learn are just too good and important
      to ignore. In web development, I found Perl modules I''d used for so long couldn''t
      compare with the features I found in JavaScript and Python. It was teaching
      that pushed me over the edge, though. I asked my boss at UA to move our intro
      programming from Perl to Python because I thought it was much easier to teach
      and we were doing a disservice by teaching students an older language when Python
      was clearly more in demand. Perl still has a special place in my heart, but
      I''ve moved on. I thought Perl 6/Raku was interesting, but I''m not sure it''s
      ever going to draw me in. My biggest push lately has been into using Elm for
      web front-ends and Rust for systems programs, and, in fact, my next book with
      O''Reilly is an intro to Rust.'
  - name: Glenn
    text: Thanks for the detailed response, Ken! My first language was JavaScript
      and have worked on teams that have used Go, Swift, and Python. I found that
      Python was the quickest to learn and be productive in (but could also be because
      I started working with it after years of programming experience). I'm still
      fairly new to it, but blown away by pandas and scikit-learn. Sounds like you're
      busy writing a lot of books!!
- name: Jeffrey Jex
  text: "Hi Ken, with the idea of working on fun projects and puzzles, what minimum\
    \ age range would this book be appropriate for?  I saw you mentioned it\u2019\
    s a great 2nd or 3rd python book in an earlier comment. In other words, would\
    \ this work for early teenagers still learning to code?"
  replies:
  - name: Ken Youens-Clark
    text: I wrote this material when I was teaching college-aged beginners while I
      was working at the Univ of AZ, but I had in mind at least high-school aged readers
      and perhaps even younger. I illustrated it with my crude cartoons and tried
      to interject enough levity so it doesn't feel like a textbook. The material
      is drawn from simple games that kids would likely know like "Telephone" and
      "Mad Libs" so I can focus on learning syntax and *testing* more than anything
      else. I would love to think that teenagers would find this approachable, but
      I don't have direct experience with students younger than 18 or so.
  - name: Jeffrey Jex
    text: "\U0001F44D thanks for the info!"
- name: Tatyjana Ankudo
  text: Hi Ken! Thanks for your work. How is this book different from another Python
    books? What particular did you pay the most attention to writing the book?
  replies:
  - name: Ken Youens-Clark
    text: I think it took me writing the book to finally realize that the biggest
      difference is that I'm trying to teach people how and why to test their code.
      There are so many beginner Python books that just snippets of code like how
      to implement something like a Caesar cipher, which is cool, but they don't show
      how to integrate this into a _complete program_ that, for instance, takes a
      text file as an argument, validates said file, reads it, encrypts it, and writes
      the output perhaps to STDOUT or maybe to another file. Along the way, how do
      you test the program to ensure it does all those things correctly? And how does
      one go about writing such a complicated program? I think it's not actually too
      difficult to teach all these concepts to novice programmers. It's actually better
      to set the bar a little higher and let new programmers know that we're expected
      to write programs that have documentation and tests, that it's incumbent on
      the author to provide good code to users. But I try to make all this subtext.
      The foreground is solving little puzzles and these other things are techniques
      that help one do that. When the reader has finished the book, though, they've
      seen dozens of unit and integration tests and have used their own interfaces
      to run their programs. I think this is the most important thing my readers could
      learn and definitely these are skills I don't see other authors attempting to
      teach.
  - name: Ken Youens-Clark
    text: "Sorry to go on and on, but I love this quote about testing:\nMore than\
      \ the act of testing, the act of designing tests is one of the best bug preventers\n\
      known. The thinking that must be done to create a useful test can discover and\
      \ eliminate\nbugs before they are coded\u2014indeed, test-design thinking can\
      \ discover and eliminate\nbugs at every stage in the creation of software, from\
      \ conception to specification, to\ndesign, coding, and the rest.\n\u2014Boris\
      \ Beizer, Software Testing Techniques"
  - name: Tatyjana Ankudo
    text: "I am glad you wrote this book, because I absolutely agree to your point\
      \ of view. I was lucky to get very good mentor who make me love testing. Your\
      \ book is in my list \u201Cmust read\u201D"
- name: Alexey Grigorev
  text: Were there some tiny projects that you wanted to include, but couldn't?
  replies:
  - name: Ken Youens-Clark
    text: I was only able to include about 1/3-1/2 of the exercises I originally sketched
      out. That being my first book, I had no idea of the exposition I would end up
      writing. For some reason, I originally thought I would spend just a few pages
      per exercise and let the code speak for itself. I came to realize this wasn't
      really teaching, and so I had to create much more prose. I put a bunch of other
      ideas into [https://github.com/kyclark/more_tiny_python_projects](https://github.com/kyclark/more_tiny_python_projects)
      some of which might one day find their way into a more advanced Python programming
      book, one that would advocate more for the use of types which I do in my bioinformatics
      book. I'm surprised that types seem to be rejected by a lot of very accomplished
      Python programmers, so this might be a somewhat controversial stance. I'm also
      very interested to see how the latest language features of 3.10 and beyond evolve,
      e.g., pattern matching (which is not the same as regexes) and switch/case statements
      could really improve Python code. If I write another Python book, I will definitely
      push to show how these features would look.
  - name: Alexey Grigorev
    text: That's a very familiar story. thanks for sharing!
- name: Alexey Grigorev
  text: Also, for someone who's learning some other programming language (say Rust),
    would you recommend the same set of tiny projects or something else?
  replies:
  - name: Ken Youens-Clark
    text: Absolutely! In fact, to become a better programmer in general I would strongly
      advocate to try writing these ideas in any other language you know. Try JavaScript
      or C. Then go make yourself learn something completely different like Haskell
      or Lisp. Certainly Rust is an interesting choice, too. My next book project
      is "beginner" programs in Rust, but the level of that beginner is expected to
      be a bit further along in their career than for TPP, so the programs are more
      complex.
  - name: Ken Youens-Clark
    text: For example, the first Rust project in my book is an implementation of `echo`
      which repeats back anything it is given. This is essentially "Hello, world"
      and is very close to the Crow's Nest exercise in TPP. I have Tic-Tac-Toe in
      TPP, and I might include Hangman in my Rust book (depending on space). Both
      are simple games that iterate through play and maintain state. TPP has text
      transformations like The Scrambler, Gematria, and Jump The Five, and my Rust
      book will likely include encoders for ROT13 (rotate characters 13 so A becomes
      M, etc.) and a Pig Latin ("ig-pay atlin-lay"). The TPP Workout-of-the-Day (WOD)
      shows how to read a CSV file, and in Rust I'm writing a version of `cut` that
      also handles delimited text.
  - name: Ken Youens-Clark
    text: The goal is to get the reader to see patterns. I mostly see the world now
      in terms of primitives like strings and numbers and then data structures like
      lists, sets, and dictionaries. Functions transform these in various ways, so
      it's mostly a matter of hooking up the plumbing correctly, no matter the language.
      Some languages are stricter in the compile phase so they help you find places
      where you didn't get it right. Rust won't even budge until it's satisfied that
      everything is perfect, whereas Python will just blow up at runtime so it's important
      to include types and tests.
  - name: Alexey Grigorev
    text: "Thanks! \nJust curious, why would you recommend learning lisp or haskell?\
      \ Just because they are quite different from the mainsteam imperative languages?"
- name: Alexey Grigorev
  text: I also know that you're quite a prolific author. How do you manage to finish
    one book and find the energy to jump on another one immediately?
  replies:
  - name: Ken Youens-Clark
    text: I'm not sure I'd call myself prolific just yet. My second book, _Mastering
      Python for Bioinformatics_ (O'Reilly) is heading to press next week, and I have
      started my third on Rust. Maybe if I get to five books I'll accept that description!
      I've been programming for about 25 years and spent a good bit of time teaching
      and mentoring and reviewing code. I finally found enough to say, and now I feel
      like I just need to write and write to get all these ideas down on paper.
  - name: Ken Youens-Clark
    text: I recall when I started my undergraduate degree at the Univ of North Texas
      back in 1990. I signed on to be a Jazz Studies major because I wanted to study
      the drum set. I'd be playing since age 9, and the choices were either to study
      music ed to become an instructor, music performance to become an orchestral
      player, or Jazz to study the kit. Anyway, it seems ridiculous now that I was
      studying Jazz because I'd never listened to it in my life.
  - name: Ken Youens-Clark
    text: I could barely read music, couldn't hear the difference b/w a major and
      minor scale, couldn't vocalize, didn't know jack about music history or theory.
      Mostly I could bang out some rock beats on a kit, and yet I was going to study
      music! Anyway, I come to quickly realize that I'm in way over my head. I'm trying
      to learn how to play swing on the kit when I've mostly just listened to hard
      rock. It was a radical change. I had no vocabulary.
  - name: Ken Youens-Clark
    text: Every member of a jazz group is expected to be a virtuoso and take a solo.
      You have to know the form of a tune, play in the correct style, interact in
      real time with other players. When it came time to take a solo, I would just
      freeze. I had no idea what to "say" on my instrument.
  - name: Ken Youens-Clark
    text: One of the instructors patiently said one day that jazz is something of
      an old person's music. That it takes a really long time, lots of studying and
      playing and listening, to find something to say on your instrument, particularly
      something new.
  - name: Ken Youens-Clark
    text: Until then, we should just study what others have said, mimic them, write
      down ideas, synthesize until we found our own voices. This would ultimately
      take decades, so don't be in too much of a hurry.
  - name: Ken Youens-Clark
    text: After a couple of years, I switched majors (a few times), but I kept studying
      music on my own. I got deeper into literature and reading and thought about
      writing fiction, but, again, this was so beyond me. I still harbor delusions
      of writing stories. The words of my jazz prof stuck with me, though. It would
      take a really long time for me to find something to say, so I've just kept trying
      over the years to work out what I have to bring.
  - name: Ken Youens-Clark
    text: I also really thought about teaching as a career, but obviously programming
      pays way better. While working at the Univ of AZ, I finally got a chance to
      teach in a classroom by helping my boss, Dr. Bonnie Hurwitz. At first we split
      classes, her teaching science (metagenomics) and me programming so our student
      could learn how to do computational research.
  - name: Ken Youens-Clark
    text: Teaching was a huge challenge, and I really sucked at it at first. I would
      type out my lectures entirely long-hand, that is, as a prose document to work
      out what I wanted to say in an hour. That's pretty much the length of a decent
      chapter. I would devise examples and sequence things to show, for instance,
      what is a list, why it's useful, how to manipulate it, where you'll find one
      in the wild.
  - name: Ken Youens-Clark
    text: After a couple of years, I finally designed an entire course just on the
      programming material and got to teach for entire semesters. That was really
      life-changing. I enjoyed working with students and seeing their struggles. Since
      I learned to program so long ago, it was easy to forget what was hard to learn.
      I kept refining my examples and prose and lectures and moved entirely towards
      live-coding in class.
  - name: Ken Youens-Clark
    text: '"Active learning" is a great way to keep people from falling asleep in
      class and really helps people retain information. So I have adopted this active
      approach to writing. I describe a challenge, give the reader some information
      and hints on how to solve it along with the data and tests to know when things
      are correct, and push the reader to work it out. Then I present some different
      ways to solve the problem.'
  - name: Ken Youens-Clark
    text: I don't know if it's just a formula I'm following for now. I'm not trying
      to be derivative, but this is the format for TPP, the bioinformatics book, and
      now the Rust book. There are plenty of other books that describe everything
      you want to know about a list or a dictionary for a given language, but not
      enough that show you when and how to use one in an actual program.
  - name: Ken Youens-Clark
    text: As for the energy, I've got issues. I feel really OCD about writing at this
      point in my life. Like I've been trying to learn to speak and finally figured
      it out. My father died young, and I think I'm haunted by ideas of mortality.
      I recently watched (and rewatched and rewatched many times) "Hamilton" with
      my daughter, so I guess "I am not throwing away my shot."
  - name: Ken Youens-Clark
    text: Sorry if that took a weird turn, but you hit a button, I guess.
  - name: Alexey Grigorev
    text: "What I can see is you definitely love writing \U0001F605"
  - name: Alexey Grigorev
    text: I was really curious where the jazz story is leading!
  - name: Alexey Grigorev
    text: So, if I can attempt to summarize it, you did a lot of work prior to writing
      the book, and already had experience with structuring your thoughts on paper.
      Am I close?
  - name: Alexey Grigorev
    text: I also like the idea of active learning! That's really great! I haven't
      heard this term (in this context) previously
  - name: Ken Youens-Clark
    text: Yes, you summarized it fine. I started to scratch the surface of learning
      formal pedagogy when I was working on my MS at UA. I may have an opportunity
      to teach there this fall, and I'd love to continue learning more about the science
      and art of teaching. As interesting as I think my own lectures are, I've literally
      seen my students struggling to stay awake. That doesn't happen when everyone
      is trying to write code together. Sometime I have them do pair programming in
      class, too. Another great teaching tool.
- name: Alexey Grigorev
  text: 'Okay, I have a few more questions!

    You just finished a book about bioinformatics. Can you tell us a bit what bioinformatics
    is and what kind of problems it solves?'
  replies:
  - name: Ken Youens-Clark
    text: Yes, my latest book is with O'Reilly and is called _Mastering Python for
      Bioinformatics_ ([https://learning.oreilly.com/library/view/mastering-python-for/9781098100872/](https://learning.oreilly.com/library/view/mastering-python-for/9781098100872/)).
      Bioinformatics is the application of computer science to biology. There was
      a time up until the 1990s when most biological data sets would easily fit into
      small Excel files. With the advent of genome sequencing, that is no longer the
      case. Sequencers have been able to create more and more data for cheaper and
      cheaper prices at a rate that outpaces Moore's law. Biology is swimming in data,
      and so it's imperative to use computer science to find patterns.
  - name: Ken Youens-Clark
    text: In French, "informatics" is computer science, so it makes a little more
      sense. Anyway, I've been working in and around bioinformatics since 2001 when
      I got a job as a web developer in the lab of Dr. Lincoln Stein at Cold Spring
      Harbor Labs. He was a big Perl name, author of core modules and several books.
      Hanging around him at conferences was like being around a rock star back then.
      It was weird.
  - name: Ken Youens-Clark
    text: I knew basically nothing about biology. My undergrad degree was English
      lit (minor in music) I was hired to build databases and code Perl web interfaces.
      I also wrote a comparative map viewer that many people used for a while ([https://pubmed.ncbi.nlm.nih.gov/19648141/](https://pubmed.ncbi.nlm.nih.gov/19648141/))
      but I never felt I had my _bona fides_ in the field. I jumped at the chance
      to work at the Univ of AZ as I wanted to earn my MS which I finished in 2019.
      That gave the me chance to fill in a lot of missing knowledge esp in stats and
      machine learning.
  - name: Ken Youens-Clark
    text: When I was writing material to teach basic programming at UA, I started
      with the ideas in Tiny Python Projects, and then showed how those simple ideas
      had cognates in biology. I had dozens of ideas for chapters for a book on bioinformatics,
      but I realized that the [Rosalind.info](http://Rosalind.info) problems just
      couldn't be topped.
  - name: Ken Youens-Clark
    text: So I chose 14 of those challenges and showed how to solve them in Python,
      ordering them in such a way to build on the ideas as in TPP. Then I threw in
      5 more of my own ideas to show some more advanced programs.
  - name: Ken Youens-Clark
    text: I haven't quite answered your question -- What does bioinformatics solve?
      Well, pretty much all the big advances in biology including things like the
      COVID vaccine are due to using computational approaches to solving data problems.
      For instance, protein folding is a wicked hard problem, but all the information
      to figure out the 3D structure of a protein is necessarily contained in the
      raw DNA sequence. We just have to figure out how to go from one to the other.
  - name: Ken Youens-Clark
    text: I worked for 13 years on a plant genomics project where we looked at things
      like orthologous genes, that is genes that basically encode the same proteins/function
      in different plants. For instance, some species of rice are more drought tolerant
      than others. Why? Is it one gene or a set of genes? Can those be transferred
      to another species? Humans have been doing gene transfers for centuries in plants
      and animals through selective breeding. Now we are able to select individual
      genes.
  - name: Ken Youens-Clark
    text: Then I worked in metagenomics at UA which is the study of uncultured genomes
      found in the wild. Think about taking a sample of ocean water and trying to
      figure out all the microbial species living in it by extracting the DNA and
      sequencing everything. We only know a fraction of the species existing on earth,
      so a lot of the DNA you find will be unidentifiable. Still, you can find genic
      regions and compare them to known genes/structures to infer what's going on
      the organisms that are present. Extend that to a sample from a person with an
      unknown infection. Take a sample maybe from the gut. Do they have C. difficile
      or something else like a virus? Antibiotics don't work on viruses, so antibiotics
      could actually make the patient sicker. If someone is septic, you give the worst
      antibiotic possible but you need to de-escalate quickly so you need to identify
      what organisms are present to choose the right antibiotic (or something else
      entirely).
  - name: Ken Youens-Clark
    text: The field of bioinformatics is huge and growing, e.g., biotech. It's an
      exciting field.
- name: Alexey Grigorev
  text: And why did you decide to write a book about it?
  replies:
  - name: Alexey Grigorev
    text: Is it something you do at work?
  - name: Ken Youens-Clark
    text: Oh, I should have answered that here, but yes, most of what I've done over
      the last 20 years.
- name: Wendy Mak
  text: to add to the above questions above bioinformatics-- I find it quite an interesting
    topic, but as someone who has no biology background beyond high school, what's
    a good way to learn about it/get involved in projects etc? would you say your
    new book a good starting point?
  replies:
  - name: Ken Youens-Clark
    text: I had no formal training when I started, but I was also not hired to do
      bioinformatics per se but web development. If you are truly interested, a formal
      training would be pretty necessary. Many people in the field have PhDs or at
      least an MS. There are some degree programs in bioinformatics, but usually people
      train in something like molecular biology or biochemistry and do lots of coding.
      Some people formally train in both biology and CS, and those people usually
      have it really going on.
  - name: Ken Youens-Clark
    text: If you wanted to test the waters, you might try working through the exercises
      in my new book ([Rosalind.info](https://learning.oreilly.com/library/view/mastering-python-for/9781098100872/>)
      and then continue on with others from <http://Rosalind.info). The book _Bioinformatics
      Algorithms_ is also great. Compeau wrote that and Rosalind!
  - name: Ken Youens-Clark
    text: Most people in the field are biologist who learn to code or coders who learn
      biology. If you know one really well, it might be possible to get in with a
      lab. That's how I started, as a coder who learned biology, but wow does the
      biology get HEAVY really quickly.
  - name: Ken Youens-Clark
    text: There are a few rare people like Lincoln Stein who really get both the CS
      and the biology. FWIW, he's at the Ontario Inst for Cancer Research now. He's
      just killing it. A lot of PIs (principal investigators, the people who run the
      labs, write the grants, spend the money) in my experience are mostly very good
      biologists who have research questions but don't have the time to write all
      the code. I think a hotshot programmer who's willing to really learn a lot of
      biology could get hired.
  - name: Ken Youens-Clark
    text: Someone with a deep background in biology who's also a good coder might
      choose to go to work for a biotech firm like 10X Genomics or they might start
      their own lab.
  - name: Ken Youens-Clark
    text: But look over the job postings at 10X and you'll see they aren't exclusively
      looking for biology people. They also need QA/testers and front-end devs and
      cloud computing specialists and workflow developers.
  - name: Ken Youens-Clark
    text: It's a big field, and often you'll find there are projects that are really
      contributing to the good of mankind. Even though Big Pharma can do bad things,
      where would we be without the COVID vaccines?!
  - name: Saulius Lukauskas
    text: 'I currently work in the field so can add a bit as well if the author doesn''t
      mind me hijacking this thread. Bioinformatics in the classical sense is slowly
      disappearing as a field of its own as it is getting absorbed by data science:
      [https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001165](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001165)
      . If you come from data science background  I strongly suggest going through  Manolis
      Kellis (MIT) deep learning for biology course which is public - you will see
      that a lot of the knowledge you have already is directly transferrable. Having
      said that, entry is easy (you can follow the advice from the authors book for
      instance), but  to quote Ken, biology gets heavy real fast. What this means
      there are two learning curves: one relatively small but technical, needed to
      enter, and one relatively steep, biological, which is needed to be successful.
      But if you''re interested you won''t mind that as it''s a very fun field.'
  - name: Wendy Mak
    text: "\U0001F44D thanks for your perspectives :))"

---

A long journey is really a lot of little steps. The same is true when you're learning Python,
so you may as well have some fun along the way! Written in a lighthearted style with entertaining
exercises that build powerful skills, Tiny Python Projects takes you from amateur to Pythonista as
you create 22 bitesize programs. Each tiny project teaches you a new programming concept, from the
basics of lists and strings right through to regular expressions and randomness. Along the way you'll
also discover how testing can make you a better programmer in any language.