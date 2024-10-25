import json
import logging
import pyttsx3

# Configure logging to output to a file with UTF-8 encoding
logging.basicConfig(filename='tts_log.txt', level=logging.INFO, encoding='utf-8')

def generate_audio_from_dataset(json_file):
    # Load dataset from JSON file with UTF-8 encoding
    with open(json_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Iterate through each entry in the dataset
    for entry in dataset:
        term = entry['Term']
        definition = entry['Definition']
        example_sentence = entry['ExampleSentence']
        phonetic_representation = entry['PhoneticRepresentation']
        
        # Construct text to synthesize
        text = (
            f"Term: {term}. "
            f"Definition: {definition}. "
            f"Example: {example_sentence}. "
            f"Phonetic representation: {phonetic_representation}."
        )
        
        # Create a file path for the audio file
        file_name = term.replace(" ", "_") + ".wav"  # Using .wav for pyttsx3
        
        try:
            # Log the action instead of printing to the console
            logging.info(f"Generating audio for: {text.encode('utf-8', 'replace').decode('utf-8')}")
            
            # Generate audio file for the term
            engine.save_to_file(text, file_name)
            engine.runAndWait()
            logging.info(f"Audio saved to {file_name}")
        
        except Exception as e:
            logging.error(f"Error while generating audio for '{term}': {e}")

if __name__ == "__main__":
    try:
        # Start the TTS process
        generate_audio_from_dataset('dataset.json')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
