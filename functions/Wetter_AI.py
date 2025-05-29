#function that put an promt into an prompt for an AI and outputs the Response of the AI

import cohere


def cohere_prompt( prompt):
    """
    Sendet einen Prompt an die Cohere API und gibt die Antwort zurück.

    :param api_key: Dein Cohere API-Key
    :param prompt: Der Text, den du generieren möchtest
    :param model: Das Modell, das verwendet werden soll (Standard: "command-xlarge-nightly")
    :return: Die generierte Antwort
    """

    try:
        # Cohere-Client initialisieren
        co = cohere.Client("2hgobMGpg7rtxIcLDGsLLDaR1CgflJfrhyZ3fxWx")

        # API-Aufruf durchführen
        response = co.generate(
            model="command-xlarge-nightly",
            prompt=prompt,
            max_tokens=300,  # Maximale Länge der Antwort
            temperature=0.7,  # Kreativität der Antwort (niedrig = präziser, hoch = kreativer)
            k=0,
            p=1.0,
            stop_sequences=None,
            return_likelihoods='NONE'
        )

        # Generierten Text zurückgeben
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Fehler bei der Anfrage: {e}"




