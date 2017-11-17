import random;
class MelodyMarkov:

  def __init__(self,notes,steps=2):
    self.steps = steps;
    self.phrases = [];
    self.markovChain = {};
    self.generateMarkovChain(notes);

  #takes an array of midi values
  def generateMarkovChain(self,notes):
    for idx in range(len(notes)):
      listToTuple = [];
      for stepIdx in range(self.steps,0, -1):
        listToTuple.append(notes[idx - stepIdx]);

      key = tuple(listToTuple);
      pitchObject = notes[idx];
      if self.markovChain.get(key,False):
          self.markovChain[key].append(pitchObject)
      else:
          self.markovChain[key] = [pitchObject]
    
    return self.markovChain;


  def generateTupleKey(self,phrase,currentIndex,repeat=False):
      listToTuple = [];
      for j in range(self.steps, 0, -1):
        offset = 1 if repeat else j;
        listToTuple.append(phrase[currentIndex-offset]);

      return tuple(listToTuple);

  def appendToPhrase(self,tupleKey,phrase):
    if self.markovChain.get(tupleKey,False):
      randomNote = random.choice(self.markovChain[tupleKey]);
      phrase.append(randomNote);
      return True;

    return False;

  def generateMelody(self, phraseLength=1000, endless=False):
    randomStartingTuple = self.getStartingTuple();
    phrase = list(randomStartingTuple);

    for i in range(1, phraseLength):
      tupleKey = self.generateTupleKey(phrase,i);
      if self.appendToPhrase(tupleKey,phrase):
        continue;
      
      repeatedNote = self.generateTupleKey(phrase,i,True);
      if self.appendToPhrase(repeatedNote,phrase):
        continue;
      else:
        if (endless):
          if (not self.appendToPhrase(randomStartingTuple,phrase)):
            break;
    
    self.phrases.append(phrase);
    return phrase;

  def getStartingTuple(self):
    randomStartingTuple = random.choice(self.markovChain.keys());
    length = len(self.markovChain[randomStartingTuple]);
    return randomStartingTuple;

  def getPitchDuration(notes, idx):
    if idx:
      return notes[idx].offset - notes[idx-1].offset
    else:
      return notes[idx].offset
