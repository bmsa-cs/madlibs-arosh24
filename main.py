"""
MadLibs
Author: Andrew Roshong
Period/Core: 7


"""
"""
[name] went to the store to get some [noun1] .
When [name] stepped inside of the [adjective1] store, they notice a [adjective2] [noun2] standing in their way.
They,[adverb1][verb1] past the [adjective2] [noun2] getting into the store.
[name][adverb2][verb2 plural] down the aisle, rushing to find the spot where [noun1] is located...
Finally you locate the [noun1] on the shelf next to some [adjective3][noun3].
[name] [adverb3] [verb3 plural] out of the store, finally ready to go home.

"""

print("Let's" + " " "play" + " " + "Silly" + " " + "Sentences!")
name = input("Enter a name: ")
noun1 = input("Enter a noun: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
noun2 = input("Enter a noun: ")
adverb1 = input("Enter a adverb: ")
verb1 = input("Enter a verb: ")
adverb2 = input("Enter an adverb: ")
verb2 = input("Enter a plural verb: ")
adj3 = input("Enter an adjective: ")
noun3 = input("Enter a plural noun: ")
adverb3 = input("Enter an adverb: ")
verb3 = input("Enter a plural verb: ")

print(f"{name} went to the store to get some {noun1}.\nWhen {name} stepped inside of the {adj1} store they notice a {adj2} {noun2} standing in their way.\nThey {adverb1} {verb1} past the {adj2} {noun2} barely managing to get into the store.\n{name} {adverb2} {verb2} down the aisle, rushing to find the spot where {noun1} is located...\nFinally {name} notices the {noun1} they were looking for on the shelf next to some {adj3} {noun3}\n{name} {adverb3} {verb3} out of the store, finally ready to go home. ")

