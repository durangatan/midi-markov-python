# WORK IN PROGRESS

## Python Midi Markov
  
  Uses the music21 Python library to generate semi-improvised melodies. 

If you run  `runner.py`, right now it will

- Read all the compositions of JS Bach into a Markov chain data structure (implemented in Python)
- Start on a random note and write a midi file approximately 1000 notes in length
- Play the generated midi file

Future feature ideas include a command-line interface for choosing a different composer, phrase length, and making optimizations on the data structure (it's very slow). 
