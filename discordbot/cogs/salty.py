"""
Salty commands, require the bot to have the role "Salty"
"""

import discord
from discord.ext import commands
import random
import urbandictionary as ud

from discordbot.bot import DiscordBot
from discordbot.cogs.utils import checks


class Salty:
    def __init__(self, bot: DiscordBot):
        self.bot = bot

    @commands.command()
    @checks.role("salty")
    async def insult(self, ctx, user: discord.Member = None):
        """Insults a user."""
        name = "{0}".format(user.mention + ": " if user else "")
        insult_words = {
            'A': ['a confoundedly', 'a conspicuously', 'a cruelly', 'a deucedly', 'a devilishly', 'a dreadfully',
                  'a frightfully', 'a grievously', 'a lamentably', 'a miserably', 'a monstrously', 'a piteously',
                  'a precociously', 'a preposterously', 'a shockingly', 'a sickly', 'a wickedly', 'a woefully',
                  'an abominably', 'an egregiously', 'an incalculably', 'an indescribably', 'an ineffably',
                  'an irredeemably', 'an outrageously', 'an unconscionably', 'an unequivocally', 'an unutterably'],
            'B': ['appalling', 'babbling', 'backward', 'bantering', 'blabbering', 'blighted', 'boorish',
                  'contemptible', 'corpulent', 'cretinous', 'debauched', 'decadent', 'demented', 'depraved',
                  'detestable', 'dissolute', 'execrable', 'fiendish', 'foolish', 'foul', 'gluttonous', 'grotesque',
                  'gruesome', 'hermaphroditic', 'hideous', 'ignominious', 'ignorant', 'ill-bred', 'ill-mannered',
                  'incompetent', 'incorrigible', 'indecent', 'inept', 'insignificant', 'insufferable',
                  'insufferable', 'lascivious', 'lecherous', 'licentious', 'loathsome', 'maladjusted', 'malignant',
                  'minuscule', 'miserable', 'myopic', 'naive', 'narcissistic', 'nonintuitive', 'obese', 'obtuse',
                  'offensive', 'parasitic', 'pedestrian', 'perverted', 'petty', 'primitive', 'promiscuous',
                  'reprehensible', 'repugnant', 'repulsive', 'revolting', 'salacious', 'subliterate', 'sybaritic',
                  'uncivilized', 'uncouth', 'unseemly', 'unsightly', 'vile', 'vulgar', 'witless'],
            'C': ['barbarian', 'cannibal', 'coccydynia', 'cretin', 'degenerate', 'delinquent', 'derelict',
                  'dingleberry', 'dolt', 'dullard', 'dunce', 'fiend', 'filcher', 'glutton', 'half-wit', 'heathen',
                  'hemorrhoid', 'idiot', 'ignoramus', 'imbecile', 'lackey', 'lecher', 'libertine', 'loafer', 'lout',
                  'malefactor', 'menace', 'microphallus', 'miscreant', 'misdemeanant', 'moron', 'narcissist',
                  'neanderthal', 'nincompoop', 'ninny', 'nose picker', 'oaf', 'onanist', 'parasite', 'peon',
                  'pervert', 'pick pocket', 'plebeian', 'polisson', 'prostitute', 'rapscallion', 'reprobate',
                  'reprobate', 'reptile', 'rogue', 'ruffian', 'scoundrel', 'simpleton', 'slattern', 'sphincter',
                  'subhuman', 'swine', 'sycophant', 'sycophant', 'troglodyte', 'trollop', 'twit', 'varmint',
                  'vermin', 'wretch'],
            'D': ['belligerent', 'catatonic', 'corrupt', 'dastardly', 'debased', 'debauched', 'decadent',
                  'decrepit', 'degenerate', 'demented', 'deplorable', 'depraved', 'disgusting', 'fecal', 'feculent',
                  'fiendish', 'flaccid', 'flagitious', 'flagrant', 'frightful', 'gaudy', 'glaring', 'gluttonous',
                  'gross', 'grotesque', 'heinous', 'hopeless', 'horribly atrocious', 'infamous', 'loathsome',
                  'ludicrous', 'maladjusted', 'malingering', 'malingering', 'malodorous', 'maniacal', 'maniacal',
                  'masturbatory', 'miscreant', 'miserable', 'monstrous', 'myopic', 'myopic', 'naive',
                  'narcissistic', 'narcissistic', 'nefarious', 'nefarious', 'outrageous', 'perverse', 'perverted',
                  'petty', 'preposterous', 'preposterous', 'primitive', 'primitive', 'putrid', 'putrid', 'rank',
                  'reprehensible', 'repugnant', 'revolting', 'rotten', 'vacuous', 'vapid', 'villainous',
                  'wearisome'],
            'E': ['acidly acrimonious', 'air-polluting', 'all-befouling', 'all-defiling', 'armpit-licking',
                  'blood-curdling', 'blood-freezing', 'bug-eyed', 'buttock-rimming', 'cantankerously-caterwauling',
                  'chromosome deficient', 'chronically flatulent', 'cold-hearted', 'coma-inducing',
                  'congenitally clueless', 'dandruff-eating', 'disease-ridden', 'dull-witted', 'enema-addicted',
                  'feces-collecting', 'feeble-minded', 'flea-infested', 'flesh-creeping', 'foul-smelling',
                  'gossip-mongering', 'grudge-festering', 'halitosis-infested', 'heart-sickening',
                  'Internet-addicted', 'irredeemably boring', 'maliciously malodorous', 'mattress-soiling',
                  'monotonous solitaire playing', 'mucous-eating', 'nose-picking', 'nostril-offending',
                  'odiously suffocating', 'one dimensional', 'orgasm faking', 'scruffy-looking', 'sheep-molesting',
                  'simple-minded', 'small-minded', 'snake-eyed', 'sock-sucking', 'soul-destroying',
                  'stench-emitting', 'thick-headed', 'toe-sucking', 'urine-reeking'],
            'F': ['aberration of nature', 'abomination of humanity', 'abomination to all the senses',
                  'abomination to all the senses', 'acrid smog of oppressively caustic oral effluvium',
                  'amalgamation of loathsome repulsiveness', 'arbitrary dereliction of genetics',
                  'assault on the ocular senses', 'blight upon society', 'buggering buttock bandit',
                  'cacophonous catastrophe', 'cesspool of putrid effluvium', 'cesspool of sub-human filth',
                  'cheap Internet loiterer', 'chromosome-deficient test tube experiment',
                  'conglomerate of intellectual constipation', 'conglomerate of intellectual constipation',
                  'delinquent who has delusions of adequacy', 'deplorable calamity of birth',
                  'depraved orgy of subhuman indecency', 'depravity of genetics', 'display of indecency',
                  'dreg of the Internet', 'derelict whose birth certificate is an apology from the condom factory',
                  'derelict whose birth certificate is an apology from the condom factory',
                  'evangelical crusader of sub-mediocrity', 'evangelical crusader of sub-mediocrity',
                  'excrement stain on a Sumo Wrestler\'s underpants', 'glob of grease',
                  'grotesque visual experience', 'grudge-festering haggard',
                  'gruesome vista to all eyes assaulted by the sight of you', 'hysterical mass of warbling inanity',
                  'lamentable mistake by your parent\'s reckless exchange of genetic material', 'leach on humanity',
                  'malfunctioning little twerp', 'malodorous heathen', 'malodorous marinade of sweat and fear',
                  'manifestation of contraceptive personality', 'mass of existential impotence',
                  'mass of loathsome repulsiveness', 'mass of neuroses and complexes',
                  'mass of neuroses and pathologies', 'mass of neuroses and pathologies', 'mean-spirited poltroon',
                  'mediocrity afflicted with mental retardation',
                  'menace to, not only society, but all living creatures',
                  'mental midget with the natural grace of an intoxicated beluga whale',
                  'molester of small furry animals', 'molester of small old men', 'moving stench of leprosy',
                  'mutilation of decency', 'nauseating assault on the senses', 'nauseating assault on the senses',
                  'nefarious vermin', 'obfuscation of all that is good', 'object of execration',
                  'ocular depravity to all of discrimination', 'odious leach-covered blob of quivering slime',
                  'odious leach-covered glob of quivering slime', 'offense to all of good taste and decency',
                  'oppressive orgy of perversion', 'orgy of indecency', 'orgy of indignity',
                  'parasite on the states resources', 'personification of vulgarity',
                  'piece of excrement attached to a dogs posterior', 'pitiful sideshow freak',
                  'plague of sighing and grief', 'plague upon humanity', 'plot-less melodrama of uneventful life',
                  'plot-less melodrama of uneventful life', 'practitioner of bestiality',
                  'proof that evolution can go in reverse',
                  'proof that test tube experiments can go horribly wrong', 'pulp of stultifying inanity',
                  'putrid waste of flesh', 'repulsive polisson', 'sadistic hippophilic necrophile',
                  'scourge of decency', 'sexual assaulter of barnyard animals',
                  'shameless exhibition of genetic deficiency', 'shameless exhibition of genetic deficiency',
                  'sideshow freak whose word is as valuable as an aging cow paddy', 'spawn from a lunatics rectum',
                  'spawn of a mad scientist and a disastrous test tube experiment',
                  'sub-literate simple minded mental midget', 'tainted spawn of a syphilitic swamp rat',
                  'tainted spawn of a syphilitic swamp hog', 'tasteless amalgam of dross',
                  'toll on the nerves of those with good taste and decency',
                  'unfortunate occurrence of unprotected intercourse', 'unspeakably offensive barbarian',
                  'vulgarity to all and sundry', 'wretched horror to all who encounter you']
        }

        a = random.choice(insult_words['A'])
        b = random.choice(insult_words['B'])
        c = random.choice(insult_words['C'])
        d = random.choice(insult_words['D'])
        e = random.choice(insult_words['E'])
        f = random.choice(insult_words['F'])

        await ctx.send("{} You are {} {} {} and a {} {} {}.".format(name, a, b, c, d, e, f))

    @commands.command()
    async def urband(self, ctx, query: str, page: int = None):
        """
        Finds a phrase in the Urban Dictionary.
        """
        resp = await ud.define(query)
        if resp:
            if page:
                term = resp[page-1]
            else:
                term = resp[0]
            em = discord.Embed(color=0x2EAE48)
            em.title = term.word
            em.url = term.permalink
            em.description = term.definition
            em.add_field(name="Example", value=term.example)
            em.set_footer(text="Author: {}".format(term.author))
            em.timestamp = ctx.message.created_at
            await ctx.send(embed=em)
        else:
            em = discord.Embed(color=discord.Color.red())
            em.title = "\N{CROSS MARK} Error"
            em.description = "Either the page doesn't exist, or you typed it in wrong. Either way, please try again."
            await ctx.send(embed=em)


def setup(bot: DiscordBot):
    bot.add_cog(Salty(bot))
