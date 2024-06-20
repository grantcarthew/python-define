# define

An OpenAI-powered command-line linguistics assistant.

If you're like me, you often feel unsure about the spelling of words, and sometimes even the definition of a word. Perhaps you're a programmer trying to come up with a name for that variable, function, data, or whatever else.

The 'define' command is a godsend. It's one of the best things to come out of Large Language Models.

It uses the OpenAI API to query definitions of words, correct spelling mistakes, and provide synonyms as well as antonyms.

The 'define' command solely utilizes ChatGPT v4o and will cost you around $2 USD per month for typical use.

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
> $ define acomodate

Spelling: Accommodate
Definition: To provide lodging or sufficient space for; to fit in with the wishes or needs of.
Category: Verb - a word that describes an action, state, or occurrence.

Synonyms:
1. House
2. Lodge
3. Shelter
4. Fit
5. Hold
6. Contain
7. Adapt
8. Adjust
9. Conform
10. Serve

Antonyms:
1. Displace
2. Evict
3. Reject
4. Refuse
5. Turn away
6. Inconvenience
7. Disorganize
8. Misfit
9. Disturb
10. Upset


> $ define A variable that holds key/value data

Spelling: Dictionary
Definition: A data structure that holds key/value pairs, allowing for efficient retrieval of values based on their associated keys.
Category: Noun - a word that represents a person, place, thing, or idea.

Synonyms:
1. Hashmap
2. Hashtable
3. Map
4. Associative array
5. Key-value store
6. Lookup table
7. Symbol table
8. Index
9. Registry
10. Catalog

Antonyms:
1. List
2. Array
3. Sequence
4. Stack
5. Queue
6. Set
7. Collection
8. Series
9. Chain
10. Line


> $ define orsom

Spelling: Awesome
Definition: Extremely impressive or daunting; inspiring great admiration, apprehension, or fear.
Category: Adjective - a word that describes or modifies a noun or pronoun.

Synonyms:
1. Amazing
2. Astonishing
3. Astounding
4. Breathtaking
5. Impressive
6. Magnificent
7. Marvelous
8. Stunning
9. Wonderful
10. Spectacular

Antonyms:
1. Unimpressive
2. Ordinary
3. Mediocre
4. Common
5. Dull
6. Boring
7. Unremarkable
8. Uninspiring
9. Mundane
10. Plain


> $ define god send

Spelling: Godsend
Definition: A very helpful or valuable event, person, or thing.
Category: Noun - a word that functions as the name of a specific object or set of objects.

Synonyms:
1. Blessing
2. Boon
3. Windfall
4. Benefit
5. Advantage
6. Gift
7. Aid
8. Help
9. Miracle
10. Treasure

Antonyms:
1. Curse
2. Misfortune
3. Disaster
4. Calamity
5. Hindrance
6. Burden
7. Drawback
8. Obstacle
9. Problem
10. Nuisance


> $ define horseduvers

Spelling: Hors d'oeuvres
Definition: Small dishes served before a meal or at a party.
Category: Noun - a word that functions as the name of a specific object or set of objects.

Synonyms:
1. Appetizers
2. Starters
3. Canapés
4. Nibbles
5. Snacks
6. Finger food
7. Tapas
8. Antipasti
9. Amuse-bouches
10. Tidbits

Antonyms:
1. Main courses
2. Entrées
3. Main dishes
4. Principal dishes
5. Main meals
6. Main servings
7. Main plates
8. Main courses
9. Main fare
10. Main entrees


> $ define cricky

Spelling: Crikey
Definition: An exclamation of surprise or astonishment.
Category: Interjection - a word or phrase that expresses a sudden emotion or reaction.

Synonyms:
1. Blimey
2. Gosh
3. Wow
4. Jeez
5. Goodness
6. Holy cow
7. My word
8. Oh my
9. Heavens
10. Yikes

Antonyms: (Note: Interjections typically do not have direct antonyms, but here are some expressions of calm or indifference)
1. Meh
2. Whatever
3. No big deal
4. So what
5. Who cares
6. Fine
7. Okay
8. Alright
9. Sure
10. Alright then


> $ define I don't know what it's called, but when you are scared of crouds?

Spelling: Crowds
Definition: Large groups of people gathered together.
Category: Noun - a word that represents a person, place, thing, or idea.

Spelling: Agoraphobia
Definition: An anxiety disorder characterized by an intense fear of places or situations where escape might be difficult or help unavailable, often leading to avoidance of crowds or open spaces.
Category: Noun - a word that represents a person, place, thing, or idea.

Synonyms:
1. Fear of open spaces
2. Social anxiety
3. Panic disorder
4. Claustrophobia (related but different)
5. Anxiety disorder
6. Fear of public places
7. Fear of leaving home
8. Fear of being trapped
9. Fear of being helpless
10. Fear of being embarrassed

Antonyms:
1. Sociability
2. Extroversion
3. Confidence
4. Calmness
5. Composure
6. Ease
7. Assurance
8. Boldness
9. Fearlessness
10. Tranquility

```
