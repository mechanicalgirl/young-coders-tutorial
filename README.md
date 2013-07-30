Young Coder class materials
=====================

Slides and resources from the Young Coder tutorials at PyCon 2013

https://us.pycon.org/2013/events/letslearnpython/

At PyCon 2013, we taught two 1-day workshops for young and aspiring programmers.  The material we used was the same on both days; on the first day, we taught it to younger programmers, aged approximately 10-12, and on the second day we had a group of 13-16 year olds.

The students worked on Raspberry Pis (which they were allowed to keep after the class).  We also sent them home with two books -  "Python For Kids" and "Hello World! Computer Programming for Kids and Other Beginners".

Notes about the curriculum
=======

This one-day class curriculum starts simple and gradually adds more complex terms and concepts along the way.

You'll see that this is a beginner level class and not a complete overview.  There is a limit to the amount that we felt we could teach in a day, so we had to make deliberate choices about what to include and what to leave out, trusting that the students will learn about those concepts later as they continue their self-education.

So I won't be accepting pull requests to add additional content to this original set of slides, but feel free to fork and remix them yourself if you want to.

The class is deliberately open-ended - if you cover the material in less than whatever time you have allotted, you can review the included game code samples (the state capitals quiz and the number guessing game).

With the group of younger students (ages 10-12), we got through the full set of slides and reviewed the Raspberry Rogue code in eight hours.  With the older group (ages 13-16), it only took about four hours to get through the slides, and then we took the last four hours to cover Raspberry Rogue, the other game examples, and then added some off the cuff discussion of open source, and pointed them at a few additional learning resources that they could follow up with (LPTHW and Coding Bat).

The same material was comprehensible for students of different ages and experience levels - the only notable difference was the amount of time it took for each age group.

Raspberry Rogue game code can be found here:

https://github.com/kcunning/Katie-s-Rougish-PyGame


Teaching tools
=======

We used Idle instead of the standard Python shell, so there wasn't much emphasis on indentation in our presentation - your mileage may vary.

Our students were working on Raspberry Pis, so we discovered that we had to keep examples simple and warn them about processes that could cause memory errors (such as multiplying a string by a large number).  On the plus side, when an unrecoverable error occurred, it was simple enough to unplug the RPi and reboot.

Pacing
=======

Wherever there are examples displayed with prompts in the slides:
- first give the students some time to try typing and running the examples themselves
- then switch over to Idle and demonstrate the examples for them

Be sure and give the students time to catch up - they won't be able to type as quickly as you do, and we saw a lot of students struggle and then give up if we moved too quickly.  After each new exercise, do something like getting a show of hands to confirm that everyone's getting it before you move on to the next topic.

Classroom volunteers
=======

Volunteers are crucial - each student has unique needs and levels of understanding, so with both age groups, we relied heavily on one-on-one help to get the students through some of the tougher concepts.

The one thing that we asked was that volunteers wait until break times to make remarks about the content.  We felt that it was important to avoid derailing the class with interruptions, and that any errors or missed content could be taken care of later.  We wanted to keep the focus on the students, rather than on the slides.

Breaks
=======

Build in plenty of breaks and give students some hack time to experiment with their new skills.

Without any bult-in testing, this break time is also a great opportunity to observe students and see what they're hacking on as a comprehension check.

Release form
============

A sample release form has been included in this repository. It's a good idea to send these out beforehand, so the parents know what is expected of them and their child. Make sure to have a stack of blank ones on hand, though, for people that forget theirs.
