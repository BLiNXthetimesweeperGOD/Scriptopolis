# Scriptopolis
Requirements:
- PyGame
- Python 3 or newer

The source code for this game is VERY messy. Feel free to modify it in any way you'd like and make your own versions of the game (as long as you at least link the original page for it somewhere anyways).

The original versions were based on a tutorial I found back in 2019. The tutorial lacked scrolling and had a bug where jumping while moving would teleport you to the left side of the platform you're standing on. I eventually kind of fixed the bug, but it required a nearly complete rewrite of the physics code.

My goal with this was to make a 2D platformer with a ton of object types, a world generation mode with infinite levels, special tile types (pushable ones, falling ones, timed ones, gravity ones), some enemies (never got implemented) and a story (also never really got implemented).

List of current features:
- Several tile types (there's a list of them at the start of the first level's script in the latest version)
- Sprites (they all kind of fall under "programmer art" though)
- (Kind of) functional physics (they still need work...)
- (Kind of) functional collision detection (needs a lot of work to make the physics/controls feel better)
- Several debug features that can be accessed with a number pad (and the end key if you want to skip a level)
- A few test maps (also one of the easier things to add more of to the game)
- Particles (kind of, it's really just an overlay around the player that moves a bit as they run around and changes color based on the player state)
- The game "ends" when you reach the final programmed in level (the screen stops scrolling to the right anyways. No real ending has been implemented yet.)

List of missing/unimplemented features and tools:
- Enemies (and bosses)
- Hazards (tiles that "hurt" the player)
- Real particles (sprites or auto-generated graphics that get sent out of an object or area of the screen and can have their own physics)
- World generation
- A frame count and playback speed system for sprites instead of just using object states to set sprites
- A health system (or power up system)
- A ton of tile/floor types (A lot are listed but are just the default platform with no properties)
- A level editor/maker
- A "liquid" object type (should have the player pass through it or die on contact depending on the mode it's in)
- A goal object (to remove the kind of unexpected level endings)
- A title screen (should be fairly easy to implement though)
- A genuine ending
