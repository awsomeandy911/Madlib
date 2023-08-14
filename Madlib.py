# Program that prints out a madlib based on users input
# string concatenation (how to put strings together)
adj = input("Enter a Adjective: ")
noun1 = input("Enter a Noun: ")
noun2 = input("Enter a Noun: ")
pluraln = input("Enter a Plural Noun: ")
verbing = input("Enter a verb ending in -ing: ")


madlib1 = f"\nTitle: The Wacky Adventure\
    \nOnce upon a time in a town far, far away, there lived a {adj} {noun1}. \
    \nThis {noun1} was known for their love of {pluraln} and their peculiar habit of {verbing} at the moon. \
    \nOne fine [day of the week], the {noun1} stumbled upon a mysterious {noun2}, shimmering with [color] lights. \
    \nFilled with [emotion], the [noun] couldn't resist the temptation and decided to [verb] into the unknown. Little did they know, \
    \nthis would be the beginning of an extraordinary journey. As soon as the [noun] stepped inside, they were greeted by a [adjective] \
    \n[noun] who introduced themselves as [name]. [name] had an unusual request for the adventurous [noun]. They needed help retrieving the \
    \nlegendary [noun] of [mythical creature]. It was said to possess the power of [verb ending in -ing] and could grant any [noun] one wish. \
    \nEager for excitement, the [noun] agreed to embark on the quest. Together, they traversed through [adjective] forests, crossed treacherous \
    \n[plural noun], and encountered mischievous [plural noun]. Along the way, they collected [plural noun] and solved perplexing riddles to \
    \nunlock the path forward. The journey was filled with laughter, [adjective] surprises, and countless [noun] to tell. Finally, after facing \
    \nmany challenges, the duo reached the fabled [noun]. As they stood before it, the [noun] couldn't help but feel a mix of anticipation and \
    \n[emotion]. With a deep breath, they touched the artifact and made their wish. What did they wish for, you may ask? That's a secret only \
    \nthe [noun] and the [noun] know. Satisfied and filled with newfound [emotion], the [noun] and [name] bid farewell to the enchanted [noun] and returned home. \
    \nThey would forever cherish the memories of their wacky adventure, reminding them that sometimes, the greatest stories come from embracing the unknown"

print(madlib1) 