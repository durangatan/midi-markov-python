import re;
import midi;

def formatFilename(filename):
  regex = re.compile("\.mid");
  return filename if regex.match(filename) else filename + ".mid";

def generateMidiNotes(pitches,track):
  for idx in range(len(pitches)):
    velocity = 0 if (pitches[idx] == pitches[idx-1]) else 100;
    on = midi.NoteOnEvent(tick=0, velocity=velocity, pitch=pitches[idx])
    track.append(on)
    off = midi.NoteOffEvent(tick=100, pitch=pitches[idx])
    track.append(off)

def generateMidiFile(pitches, filename):
  pattern = midi.Pattern();
  track = midi.Track();
  pattern.append(track);
  generateMidiNotes(pitches,track);
  eot = midi.EndOfTrackEvent(tick=1)
  track.append(eot)
  formattedFilename = formatFilename(filename);
  midi.write_midifile(formattedFilename, pattern)