# Define the training data
TRAINING_DATA = [

        # Vacation Overview Intent
    ("wat is mijn vakantieoverzicht?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel vakantiedagen heb ik nog?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("geef mij een overzicht van mijn vakantiedagen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wat zijn mijn vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("ik wil mijn vakantiedagen bekijken", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel vrije dagen heb ik?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wat is het saldo van mijn vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel vakantiedagen zijn er nog over?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wanneer verstrijken mijn vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("ik wil weten hoeveel vakantiedagen ik heb", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("geef mij een lijst van mijn vakantiedagen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wat is de status van mijn verlofaanvraag?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("ik wil een overzicht van mijn verlofdagen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoe kan ik mijn vakantieoverzicht krijgen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wanneer is het overzicht van mijn vakantiedagen beschikbaar?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("heb ik recht op extra vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoe vraag ik een vakantieoverzicht aan?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kan ik een overzicht krijgen van mijn vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel verlofdagen heb ik nog beschikbaar?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kan ik mijn verlofsaldo inzien?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wat is mijn resterend aantal vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel dagen vakantie heb ik al opgenomen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kun je een overzicht geven van mijn vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("wat is mijn huidige aantal vakantiedagen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kan ik een overzicht van mijn verlofdagen krijgen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel verlofdagen heb ik nog over?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kan ik zien hoeveel vakantiedagen ik nog heb?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel dagen vakantie staan er nog open?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kan ik mijn vakantieoverzicht inzien?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel dagen heb ik nog vrij?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel vakantie staat er nog open voor mij?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("kan ik mijn verlofsaldo bekijken?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("hoeveel vakantiedagen heb ik nog beschikbaar?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("ik wil een overzicht van mijn vakantie", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("ik wil een overzicht van mijn vakantiedagen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),
    ("ik wil mijn verlofsaldo bekijken?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 1.0}}),

    
    # Greeting Intent
    ("hallo", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hi", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hoi", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goedemorgen", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goedenavond", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("dag", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("mijn dag is goed", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),

    # ("dag", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),

    ("goeiedag", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goedemiddag", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hey", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hallo daar", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hey daar", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goeiemorgen", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goedenacht", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("welkom", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goed om je te zien", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("fijn je te ontmoeten", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goeieavond", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goede morgen", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hoi daar", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goed je te zien", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hoe gaat het?", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goede dag", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hallo iedereen", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("fijn je weer te zien", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goedemorgen allemaal", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hey, hoe gaat het?", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("goedendag", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("hoi, wat leuk je te zien", {"cats": {"greeting": 1.0, "sick": 0.0, "vacation": 0.0, "vacation_overview": 0.0}}),



    # Sick Intent
    ("ik ben ziek", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik voel me niet lekker", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb griep", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb koorts", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb buikpijn", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik ben verkouden", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik voel me moe", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik ben misselijk", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb hoofdpijn", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik voel me slecht", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb pijn", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik ben ziek geweest", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik voel me niet goed", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik ben niet lekker", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik moet naar de dokter", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb een afspraak met de dokter", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik voel me niet oké", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb geen energie", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik ben niet in orde", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik voel me gebroken", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb geen zin", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),
    ("ik heb koorts gehad", {"cats": {"greeting": 0.0, "sick": 1.0, "vacation": 0.0, "vacation_overview": 0.0}}),



    # Vacation Intent
    ("ik wil verlof aanvragen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik wil mijn verlof aanvragen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),

    ("kan ik vakantie aanvragen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik wil op vakantie", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe vraag ik verlof aan?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik heb vakantie nodig", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik wil mijn vakantiedagen plannen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik wil een verlofaanvraag indienen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("wat zijn de regels voor vakantie aanvragen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe kan ik mijn vakantie plannen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("kan ik vrij nemen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("kan ik op vakantie als ik ziek ben?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik heb verlof nodig", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe kan ik vakantie reserveren?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe kan ik vakantie indienen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoeveel dagen kan ik vakantie nemen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("wat is de procedure voor vakantie aanvragen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe kan ik verlof opnemen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik wil verlof plannen", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("kan ik mijn vakantie nu aanvragen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik moet mijn vakantie boeken", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe kan ik verlof plannen voor volgende maand?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("wat zijn de stappen voor het indienen van een vakantie?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("kan ik nu verlof opnemen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoeveel dagen kan ik deze zomer vrij nemen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("kan ik verlof aanvragen voor deze zomer?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe kan ik mijn vakantie boeken?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoeveel dagen vakantie kan ik opnemen?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("hoe vraag ik vakantie aan voor volgende week?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("verlof aanvragen voor augustus", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("kan ik een verlofaanvraag indienen voor twee weken vakantie?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("ik moet mijn vakantie reserveren voor volgende maand", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("wat zijn de voorwaarden voor het aanvragen van verlof?", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),
    ("mijn vakantiedagen reserveren", {"cats": {"greeting": 0.0, "sick": 0.0, "vacation": 1.0, "vacation_overview": 0.0}}),

]



import spacy
from spacy.pipeline.textcat import Config
from spacy.training import Example
import random
from spacy.util import minibatch, compounding


# Load or create a blank dutch model
nlp = spacy.blank("nl") 

# Add the textcat component to the pipeline without specifying a model
text_cat = nlp.add_pipe("textcat", last=True)

# Add labels to the text classifier
text_cat.add_label("greeting")
text_cat.add_label("sick")
text_cat.add_label("vacation")
text_cat.add_label("vacation_overview")

# Convert the training data into the right format for spaCy
train_examples = []
for text, annotations in TRAINING_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    train_examples.append(example)

# Train the model
nlp.begin_training()
for epoch in range(70):  # Adjust the number of epochs as needed
    losses = {}
    # Create minibatches
    random.shuffle(train_examples)  # Shuffle examples before creating minibatches
    for batch in minibatch(train_examples, size=compounding(8.0, 128.0, 0.7)):  # Use compounding to define batch sizes
        nlp.update(batch, drop= 0.3, losses=losses)  # Update the model with the batch

    print(f"Epoch {epoch}: Losses {losses}")

# Save the trained model
nlp.to_disk("path_to_save_model")  # the path of the model 