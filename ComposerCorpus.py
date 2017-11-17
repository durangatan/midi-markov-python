from music21 import *;

class ComposerCorpus:

  def __init__(self, composers=[]):
    self.composers = composers if isinstance(composers,list) else [composers];
    self.notes = [];
    self.getNotes();

  def getNotes(self):
    for composer in self.composers:
      self.getNotesFromSearchTerm(composer);

  def getNotesFromSearchTerm(self,searchTerm):
    allWorks = corpus.search(searchTerm);
    for idx in range(len(allWorks)):
      self.notes += self.getNotesFromScore(allWorks[idx]);

  def getNotesFromScore(self,score):
    return map(lambda x: x.midi, score.parse().flat.getElementsByClass("Note"));
