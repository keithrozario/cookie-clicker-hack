# Background

## What is cookie clicker?

Cookie clicker is an online browser-based game my daughter introduced me to. The objective of the game is to get as many cookies as you can. You can use cookies as currency to buy buildings and upgrades that will give you more cookies. In other words you spend cookies to make cookies and fun continues!

## Why do you want to hack it?

I want to hack it -- for the fun of it. And to learn Gemini-CLI.

## What are you hacking?

The game has an `export` function, where you can save your current progress to a long string of characers. Similarly it has an `import` function that enables you to resume your game from anywhere by loading in this string. 

Hence the string must contain all details about your current state. Which means we can modify this state -- and give yourself billions of cookies, without earning a single legitimate cookie :).

All this diabolical-ness is getting too exciting. Let's begin.

# Approach

I went to [cookieclicker.com](https://cookieclicker.com) and found a `main.js` file, which was conveniently the entire game in a single ~16,000 line file.

Luckily, `main.js` wasn't minified, and all human readable with comments.

I then bootstrapped a simple directory on my local mac with:

* A JJ repository to track changes
* Initialized a uv environment for my python code
* Add `black` and `pytest` to the my environment
* Drafted a small `GEMINI.md` file to instruct the agent
* Created two folders, `/src` and `/docs`. For code and docs.
* Copied `main.js` into the root directory.

Then I started up Gemini-CLI and starting working.

## Did it work?

It finally worked. The full conversation between the agent and me is [here](/conversation.md), with some annotated notes from me.

## Did you manage to get all the cookies?

Yes, the final python code allowed me to modify any field, to get as many cookies,buildings, and upgrades/achievements I wanted. The agent also generated documentation about the program for me.

## Did the agent do all the work?

No. I had to jump in occassionally to solve some problems the agent was stuck on. And I refactored and rewrote some of the code.

## Did the agent solve it in one prompt?

I don't believe any amount of prompting would have succeeded in a single prompt. 

There were 3 points in the conversation where the agent was caught in loop, and I had to manually escape it. It also encountered plenty problems that needed my expertise to solve.

#  Lessons

## Research before doing

Because this took real code from the real-world. I had to first analyze the 16,000 lines of Javascript. I asked Gemini to write documentation, starting at a high level and then drilling deeper into areas I knew I wanted to cover. One `.md` file per document in my `/docs` folder.

I read every bit of documentation, so that my knowledge of the running program was also growing over time. This allowed me to guide the agent better.

## Plan before doing

Asking the agent for a plan before it begins executing works well.

Twice in the conversation I had to stop the agent from executing, and instead asked it for a plan of how to resolve the issue. Success rates are better if the agent writes a plan, especially for a large change. Occassionally you'll have to tweak the plan as well.

## Dual screen terminals for the win

I asked the agent to output documentation to `.md` files in markdown. On a split screen terminal I have Gemini-CLI on one terminal, and another for other things. I used `glow` to view `.md` files and `nvim` to modify if needed. But when I needed to really debug, I dropped into VSCode, I still prefer debugging in a visual editor. This split terminal allowed to read the documents the agent produced and then continue prompting it by referencing specific areas of the document (e.g. section 2.1 of file a)

## JJ

I'm also learning `jj` at the same time. JJ works a little better than git as it forced me to think about stuff **before** the commit rather than after. It also has a nicer log. The best part is that I would create a new commit in JJ, and then save the corresponding chat in gemini-cli via `/chat save commit-name` to allow to restore everything back in case the agent went hay-wire. 

Fortunately, the agent didn't go hay-wire and I never had to go back revisions. But knowing that I would be one `jj abandon` away from restoring everything was nice.

## Small is better than Big

Everyone knows at least one Agile practioner who took agile a bit too seriously than necessary. But, at the core of Agile lies an important truth -- small changes over time are better than big changes all at once.

Asking the agent to perform big changes increases the chances of the agent looping forever. Big changes also mean more lines for me to read, which reduces the probability of me actually reading everything (or anything!)

I'm definitely in the small-changes camp. I know some folks prefer spending time writing up the detail specification for the AI to write -- but if you wouldn't like to merge a 10,000 line PR, why ask the agent to generate 10,000 lines of code in one go.

## Guide the Agent

I've learnt over the years that there is one (maybe two) ways of doing things right -- but a million ways to do things wrong.

Everyone gets things wrong in their own unique way. Which means when an AI agent (trained on pattern recognition) sees a new 'hack' of an application, it probably doesn't have a clear understanding of what's going on, or how to address it. 

In this case, the agent hung trying to decode the encoded file because the original author of `main.js` did a 'hacky' encoding of the string. It's only after you guide the agent was it able to resolve the issue. It's also the reason why I believe it's impossible to one-shot the solution to this problem.

## Refactoring is harder when code isn't yours

[Chesterton's fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence) states that you shouldn't remove something until you know why it was there in the first place.

It was hard for me to refactor the code, because I didn't write it -- and hence didn't fully understand it. Refactoring involves re-writing and removing, but if you didn't write the code, you need to fully understand before re-writing it. At one point the code stopped working after what I thought was a simple refactor.

This is why I had to write the test before refactoring. Maybe I should have asked the agent to write the test as well, and execute if before begining my refactoring.

## Vibe-coding can be addictive

At one point, I was resistant to actually make code changes. I noticed that I would rather ask the agent to do something than do it myself, even though it was a one liner change. I know people who can't drive 15 minutes from their home without a GPS map guiding them -- I'm afraid of the brain athrophy I would get if I vibe-code and no longer code-code.

