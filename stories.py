"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text, img):
        """Create story with title, words, and template text."""

        self.title = title
        self.prompts = words
        self.template = text
        self.img = img

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    "TEST", ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""", '<p>NO PICTURE</p>'
)

trex = Story(
"Tyrannosaurus Rex", ["Plural Noun 1","Adjective 1","Plural Noun 2","Noun 1","Plural Noun 3","Plural Noun 4","Adjective 2", "Plural Noun 5","Plural Noun 6","Adjective 3","Noun 2","Adjective 4","Plural Noun 7","Plural Noun 8","City"],
"""Dinosaur bones and {Plural Noun 1} have been discovered from a period knowm as the {Adjective 1} Age."""
""" Fromthese fossils, scientists learned that dinosaurs were the largest {Plural Noun 2} who ever inhabited the {Noun 1}."""
""" The fiercest by far was Tyrannosaurus Rex, who ruled the land at the same time that the flying {Plural Noun 3} ruled the skies, and the swimming {Plural Noun 4} ruled the oceans."""
""" These {Adjective 2} reptiles had serrated {Plural Noun 5} for devouring {Plural Noun 6}."""
""" With their {Adjective 3} jaws, they could tear an animal limb from {Noun 2} with just one {Adjective 4} bite."""
""" The world has never been populated with such ferocious {Plural Noun 7}, with the possible exception of the members of the House of {Plural Noun 8}, who live and work in {City}.""", 
'/static/img/trex.jpg'
)

threemusketeers = Story("The Three Musketeers", ["Country Adjective","Plural Noun 1","Adjective 1","Noun 1","Adjective 2","Noun 2","Noun 3","Plural Noun 2", "Noun 4","Person in the Room","Plural Noun 3","Adjective 3","Noun 5","Noun 6","Plural Noun 4","Noun 7"],
"""There is no more rousing story in {Country Adjective} literature than The Three {Plural Noun 1}."""
""" This {Adjective 1} romance by the great French {Noun 1}, Alexander Dumas, tells the story of D'Artagnan,"""
""" a/an {Adjective 2} young {Noun 2} who arrives in 17th-century Paris riding a/an {Noun 3} with only three"""
""" {Plural Noun 2} in his pocket. Determined to be in the service of the {Noun 4} who rules all of France, """
"""he duels with Athos, Pathos, and {Person in the Room}, three of the king's best {Plural Noun 3}. Eventually, """
"""these swordsmen and D'Artagnan save their {Adjective 3} king from being overthrown and losing his {Noun 5}. """
"""Over the years, The Three Musketeers has been made into a stage {Noun 6}, two motion {Plural Noun 4}, and, """
"""most recently, into a Broadway {Noun 7}.""", '/static/img/3musketeers.jpg')

skunks = Story("Why Do Skunks Smell?", ["Noun 1","Adjective 1","Plural Noun 1","Place","Plural Noun 2","Adjective 2","Noun 2","Verb Ending in -ing", "Part of the Body 1","Part of the Body 2 (Plural)","Part of the Body 3 (Plural)","Adverb","Color","Part of the Body 4","Part of he Body 5"],
"""Surprisingly, a skunk is a friendly {Noun 1} who can make a/an {Adjective 1} household pet. """
"""But what makes these {Plural Noun 1} smell to high {Place}? The skunk has scent {Plural Noun2} that conatains """
"""a/an {Adjective 2}-smelling fluid. When attacked, the skunk aims this smelly {Noun 2} at its enemies. """
"""But the skunk does give warning before {Verb Ending in -ing}. It raises its {Part of the Body 1} first, """
"""or stamps its {Part of the Body 2 (Plural)} so that you can run away as fast as your """
"""{Part of the Body 3 (Plural)} can carry you. The most {Adverb} recognizable skunk is the one with a {Color} """
"""line on its {Part of the Body 4} and another one between its {Part of the Body 5} and its ears.""", 
'/static/img/skunk.jpg')

aliens = Story("Aliens Are Our Friends", ["Noun","Adjective 1","Something Round","Adjective 2","Occupation","Exclaimation","Plural Noun 1", "Adjective 3", "Plural Noun 2", "Place", "Type of Food (Plural)","Adjective 4","Type of Vehicle (Plural)","Adverb"],
"""If you run into an alien {Noun} who comes from some other {Adjective 1} planet which revolves around a distant """
"""{Something Round} in another galaxy, do not be {Adjective 2}. Id it says, "Take me to your {Occupation}," """
"""you must act friendly and say, "{Exclaimation}!" Remember, extra-terrestrial {Plural Noun 1} are not necessarily """
"""hostile. Many of them are {Adjective 3} and all they want is to put you in one of their {Plural Noun 2} and """
"""fly off for a vacation in {Place}. So offer them a few {Type of Food (Plural)} or take them out to a movie. """
"""If you do, maybe they will tell you the secret of {Adjective 4} telepathy or how they power their rocket """
"""{Type of Vehicle (Plural)}. If you treat an extra-terrestrial {Adverb} you may make a new friend.""",
'/static/img/alien.jpg')

story_dict = {"trex": trex,"threemusketeers": threemusketeers, "skunks": skunks, "aliens": aliens}


