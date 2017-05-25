from music21 import *;
import midi;
import random;

def getPitchDuration(notes, idx):
  if idx:
    return notes[idx].offset - notes[idx-1].offset
  else:
    return notes[idx].offset

def getNotesFromScore(score):
  return score.parse().flat.getElementsByClass("Note");

def generateMarkovChain(notes,markovChain={}):
  for idx in range(len(notes)):
    key = (notes[idx-2].midi,notes[idx-1].midi);
    pitchObject = notes[idx].midi;
    if markovChain.get(key,False):
        markovChain[key].append(pitchObject)
    else:
        markovChain[key] = [pitchObject]

  return markovChain;

def generateMidiFile(pitches):
  pattern = midi.Pattern();
  track = midi.Track();
  pattern.append(track);
  for idx in range(len(pitches)):
    velocity = 0 if (pitches[idx] == pitches[idx-1]) else 100;
    on = midi.NoteOnEvent(tick=0, velocity=velocity, pitch=pitches[idx])
    track.append(on)
    off = midi.NoteOffEvent(tick=100, pitch=pitches[idx])
    track.append(off)

  eot = midi.EndOfTrackEvent(tick=1)
  track.append(eot)
  midi.write_midifile("example.mid", pattern)

def getStartingTuple(markovChain):
  length = 0;
  while(length < 10):
    randomStartingTuple = random.choice(markovChain.keys());
    length = len(markovChain[randomStartingTuple]);

  return randomStartingTuple;

def addComposerToMarkov(searchTerm, markovChain):
  allWorks = corpus.search(searchTerm);
  for idx in range(len(allWorks)):
    print allWorks[idx];
    notes = getNotesFromScore(allWorks[idx]);
    markovChain = generateMarkovChain(notes, markovChain);

  return markovChain

def generateMarkovPhrase(markovChain, phraseLength=1000, endless=False):
  randomStartingTuple = getStartingTuple(markovChain);
  phrase = [randomStartingTuple[0],randomStartingTuple[1]];
  for i in range(1, phraseLength):
    tupleKey = (phrase[i-2], phrase[i-1]);
    if markovChain.get(tupleKey,False):
      randomNote = random.choice(markovChain[tupleKey])
      phrase.append(randomNote)
    else:
      repeatedNote = (phrase[i-1],phrase[i-1]);
      if markovChain.get(repeatedNote,False):
        randomNote = random.choice(markovChain[repeatedNote]);
        phrase.append(randomNote);
      else:
        if (endless):
          randomNote = random.choice(markovChain[randomStartingTuple]);
          phrase.append(randomNote);
        else:
          break;

  print phrase;
  return phrase;

markovChain = {};
composers = ['bach','mozart']

for composer in composers:
  print 'importing ' + composer;
  markovChain = addComposerToMarkov(composer, markovChain);

print 'generated markov chain';
print markovChain;

phrase = generateMarkovPhrase(markovChain);
print 'ok made a phrase';
generateMidiFile(phrase);


