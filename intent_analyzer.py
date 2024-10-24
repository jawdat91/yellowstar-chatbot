import spacy


# Laad het getrainde model vanaf de schijf
nlp = spacy.load("path_to_save_model") 


class IntentAnalyzer:
    def analyze_intent(text):
        doc = nlp(text.lower())  # Use the loaded trained model
        
        # Check if the model has performed the classifications
        if not doc.cats:
            print("Geen intentie gedetecteerd. Het model heeft geen classificaties gegeven.")
            return "onbekend"

        # Determine the intent based on the category with the highest probability
        intent = max(doc.cats, key=doc.cats.get)
        confidence = doc.cats[intent]

        # Set a threshold for the accuracy of intent recognition
        if confidence < 0.99:
            print(f"Intent niet herkend: te lage waarschijnlijkheid ({confidence}). Gedetecteerde intentie: {intent}")
            return "unknown"  # Indicates that the intent has not been recognized with certainty

        print(f"Gedetecteerde intentie: {intent} met vertrouwen {confidence}")
        return intent

