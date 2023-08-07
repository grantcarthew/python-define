# define

An OpenAI-powered command-line linguistics assistant.

If you're like me, you often feel unsure about the spelling of words, and sometimes even the definition of a word. Perhaps you're a programmer trying to come up with a name for that variable, function, data, or whatever else.

The 'define' command is a godsend. It's one of the best things to come out of Large Language Models.

It uses the OpenAI API to query definitions of words, correct spelling mistakes, and provide synonyms as well as antonyms.

The 'define' command solely utilizes ChatGPT v3.5 and will cost you around $1 USD per month for typical use.

## define IS NOT

- A general purpose OpenAI client
- A free tool to use, you will need an [OpenAI API Key](https://platform.openai.com/account/api-keys)
- Always perfect in its response

## Installation

First install [pipx](https://pypa.github.io/pipx/)

```shell
export OPENAI_API_KEY="<your-openai-api-key>"
# echo 'export OPENAI_API_KEY="<your-openai-api-key>"' >> "${HOME}/.bashrc"
pipx install python-define
```

Package Address: https://pypi.org/project/python-define/

## Examples

```markdown
> $ define oss

Spelling: Oss
Correction: It seems that there is a spelling mistake. Could you please provide more context or clarify the word you are referring to?

> $ define "oss as in software"

Spelling: OSS (Open Source Software)
Definition: Software that is freely available and can be modified and distributed by anyone.

Synonyms:
1. Open source
2. Free software
3. Libre software
4. FOSS (Free and Open Source Software)
5. FLOSS (Free/Libre and Open Source Software)
6. Community-driven software
7. Collaborative software
8. Transparent software
9. Unrestricted software
10. Public software

Antonyms:
1. Proprietary software
2. Closed source software
3. Commercial software
4. Restricted software
5. Private software
6. Non-open source software
7. Paid software
8. Exclusive software
9. Confidential software
10. Restricted-access software

> $ define "A variable that holds key/value data"

Spelling: Dictionary
Definition: A variable that holds key/value pairs of data.

Synonyms:
1. Map
2. Hash
3. Associative array
4. Keyed array
5. Lookup table
6. Symbol table
7. Hash table
8. Index
9. Directory
10. Container

Antonyms: N/A

> $ define orsom

Spelling: Awesome
Definition: Extremely impressive or daunting; inspiring awe.

Synonyms:
1. Amazing
2. Incredible
3. Fantastic
4. Wonderful
5. Spectacular
6. Breathtaking
7. Remarkable
8. Astonishing
9. Extraordinary
10. Magnificent

Antonyms:
1. Terrible
2. Awful
3. Mediocre
4. Unimpressive
5. Ordinary
6. Dull
7. Boring
8. Mundane
9. Average
10. Subpar

> $ define "god send"

Spelling: Godsend
Definition: Something or someone that is unexpectedly helpful or beneficial.

Synonyms:
1. Blessing
2. Boon
3. Gift
4. Windfall
5. Stroke of luck
6. Miracle
7. Lifesaver
8. Relief
9. Advantage
10. Bonanza

Antonyms:
1. Curse
2. Misfortune
3. Calamity
4. Disaster
5. Setback
6. Problem
7. Hindrance
8. Obstacle
9. Difficulty
10. Burden

> $ define horseduvers

Spelling: Hors d\'oeuvres
Definition: Small savory dishes served as an appetizer before a meal.

Synonyms:
1. Appetizers
2. Starters
3. Canapés
4. Finger foods
5. Snacks
6. Tapas
7. Antipasti
8. Mezze
9. Amuse-bouches
10. Nibbles

Antonyms: N/A (Hors d'oeuvres are a specific type of food and do not have direct antonyms)

> $ define cricky

Spelling: Cricket
Definition: A game played with a ball and bat by two teams of eleven players on a large field.

Synonyms:
1. Bat-and-ball game
2. Gentleman's game
3. Test match
4. T20
5. ODI
6. Wicket
7. Innings
8. Bowler
9. Batsman
10. Fielder

Antonyms: N/A

> $ define "cricky as in aussie slang"

Spelling: Crikey
Definition: An exclamation used to express surprise or astonishment, often associated with Australian slang.

Synonyms:
1. Wow
2. Gee
3. Gosh
4. Golly
5. Blimey
6. Jeez
7. Holy cow
8. Goodness gracious
9. My word
10. Well, I'll be

Antonyms: N/A

> $ define "I don't know what it's called, but when you are scared of crouds?"

Spelling: Crowds
Definition: A large number of people gathered closely together in a confined space.

The fear of crowds is called:

Phobia: Agoraphobia

Agoraphobia is an anxiety disorder characterized by a fear of being in situations where escape might be difficult or help might not be available, often resulting in avoidance of crowded places or public spaces.

```
