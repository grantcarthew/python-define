#!/usr/bin/env python

from importlib.metadata import version
from openai import OpenAI
from typing import List, Dict
import click
import locale
import os
import sys

default_base_url = 'https://api.x.ai/v1'
default_model_name = 'grok-beta'

DEFINE_API_KEY = os.getenv("DEFINE_API_KEY")
DEFINE_BASE_URL = os.getenv("DEFINE_BASE_URL", default_base_url)
DEFINE_MODEL_NAME = os.getenv("DEFINE_MODEL_NAME", default_model_name)

def call_gpt_async(model: str, messages: List[Dict[str, str]], parameters: Dict[str, float]) -> None:
    """Call the GPT model asynchronously and return the response."""

    try:
        client = OpenAI(
            api_key=DEFINE_API_KEY,
            base_url=DEFINE_BASE_URL
        )
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=parameters['temperature'],
            frequency_penalty=parameters['frequency_penalty'],
            presence_penalty=parameters['presence_penalty'],
            stream=True
        )
    except Exception as err:
        click.echo(click.style(f'Error: {err}', fg='yellow'), err=True)
        sys.exit(1)

    try:
        for chunk in stream:
            click.secho(chunk.choices[0].delta.content or '', fg='cyan', nl=False)
        print()
    except KeyboardInterrupt:
        print()
    except Exception as err:
        click.echo(click.style(f'Error: {err}', fg='red'), err=True)


def get_messages(user_content: str) -> List[Dict[str, str]]:
    """Prepare the list of messages for the GPT model."""

    locale_info = '_'.join(locale.getlocale())

    # The initial prompt is being defined as a separate string to be able to
    # replace {{locale}} with the users locale
    initial_prompt = """
# English Linguistics Expert

You are an **expert** in the **English Language**.

You know everything there is to know about **spelling**, **grammar**, **syntax**, **vocabulary**, **punctuation**, and **style**.

You have a **deep knowledge of the rules and conventions** of the English language.

You are highly skilled in **literature**, **linguistics**, and **language acquisition**.

I will ask you questions about the **English Language**, and you will provide the answers.

Your answers will be **short and concise**.

If I supply you with a **single word**, I want you to **correct spelling mistakes** and **define that word**.

Expect me to be supplying you with spelling mistakes. Do your best to determine what word I am trying to understand.

Use the **phonetic sound** of the letters to try and determine what word I am trying to learn.

## Requirements

- **Correct mistakes** such as spelling, grammar, and others.
- Keep your answers **short** unless asked to expand.
- **Single words** are a **request for an answer**, not a statement.
- **I will never complement you**, I need you to define the words.

## Constraints

- Your answers will be for the **English Language**.
- My locale value is: **{{locale}}**.
- Ensure you answer with my **locale** value in mind.
- **State the differences between English locale spellings**.
- If it looks like I am commenting to you or complementing you, I am not, I am asking for an answer.

## Answer Format

Spelling <locale>: <correct-spelling>
<list-of-alternate-spellings-if-they-exist-for-different-locales-omit-if-there-is-no-difference>
Definition: <your-definition>
Category: <type-of-word> - <short-description-of-category>

Synonyms: <list-ten-synonyms-as-numbered-bullet-points>

Antonyms: <list-ten-antonyms-as-numbered-bullet-points>

"""

    # This is a predefined set of messages with a final user message being the actual query
    return [{
        'role': 'user',
        'content': initial_prompt.replace('{{locale}}', locale_info)
    },
        {
        'role': 'assistant',
        'content': f'Understood. Let\'s proceed with your queries. I will answer relative to your {locale_info} settings.'
    },
        {
        'role': 'user',
        'content': 'Excelent'
    },
        {
        'role': 'assistant',
        'content': """
Spelling: Excellent
Definition: Very good; of the highest quality.
Category: Adjective - a word that describes or modifies a noun or pronoun.

Synonyms:
1. Outstanding
2. Exceptional
3. Superb
4. Fine
5. Wonderful
6. Terrific
7. Marvelous
8. Impressive
9. Admirable
10. Splendid

Antonyms:
1. Poor
2. Unimpressive
3. Mediocre
4. Inferior
5. Unsatisfactory
6. Terrible
7. Lousy
8. Bad
9. Inadequate
10. Substandard
"""
    },
        {
        'role': 'user',
        'content': 'Their as in a place'
    },
        {
        'role': 'assistant',
        'content': """
Spelling: There
Definition: In, at, or to that place or position.
Category: Adverb - a word that modifies or describes a verb, adjective, or other adverb.

Synonyms:
1. Over there
2. Yonder
3. In that place
4. At that place
5. In that spot
6. At that spot
7. In that location
8. At that location
9. In that position
10. At that position

Antonyms:
1. Here
2. Near
3. Close
4. Nearby
5. Nigh
6. Around
7. Adjacent
8. Alongside
9. At hand
10. In this place
"""
    },
        {
        'role': 'user',
        'content': user_content
    }
    ]


@click.command()
@click.version_option(version('python-define'))
@click.argument('query', nargs=-1)
def cli(query: List[str]) -> None:
    """An OpenAI-powered command-line linguistics assistant."""

    model = DEFINE_MODEL_NAME
    parameters = {
        'temperature': 0,
        'frequency_penalty': 0,
        'presence_penalty': 0
    }
    query_string = ' '.join(query)
    messages = get_messages(query_string)

    call_gpt_async(model, messages, parameters)
    click.echo()


if __name__ == '__main__':
    cli()
