import spacy
from spacy.pipeline.textcat import Config
from spacy.training import Example
import random
from spacy.util import minibatch, compounding
from training_data import TRAINING_DATA, TEST_DATA


# create a blank Dutch model ('nl' for Dutch)
nlp = spacy.blank("nl")

# Add the textcat component to the pipeline
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
nlp.to_disk("path_to_save_model")  # Specify the path where you want to save the model


# Test the trained model
correct = 0
total = len(TEST_DATA)

for text, expected in TEST_DATA:
    # Make prediction
    doc = nlp(text)
    predicted = doc.cats  # This gives the predicted categories

    # Find the category with the highest score
    predicted_label = max(predicted, key=predicted.get)
    expected_label = max(expected['cats'], key=expected['cats'].get)

    # Compare the predicted label to the expected label
    if predicted_label == expected_label:
        correct += 1

accuracy = correct / total
print(f"Accuracy: {accuracy * 100:.2f}%")
