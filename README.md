# Little Uglies

A Pet Directory on Neopets for Mutants, Snots, Swamp Gases, and Zombies at [/~fef](https://www.neopets.com/~fef) run by [candy_fizz](https://www.neopets.com/userlookup.phtml?user=candy_fizz). This is candy_fizz's Github account.

The code to automate grabbing neomail listings and updating the code for the side is contained here, eventually to be hosted on Azure?!?!

All Neopets trademarks belong to Neopets, I do not own Neopets.

## Requirements

* Python 3.11.7  (A lower version may also be fine)

## Design Choices

This does not automatically push updates to /~fef - this is manually done to avoid being frozen by Neopets and avoid load on Neopets servers.

Automatically grabbing neomails is similar enough to what a person normally does (open neomail in new tab, close neomail tab), so I'm able to avoid a lot of manual work that way.

Please note there will be no automated response if your listing wasn't formatted properly - this is not automated to avoid being frozen by Neopets and avoid load on Neopets servers.