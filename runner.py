from ComposerCorpus import ComposerCorpus ;
from MelodyMarkov import MelodyMarkov;
import midiWriter;
import pygame;

def play_music(music_file):
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

corpus = ComposerCorpus('bach');
print('loaded all the bach')
markov = MelodyMarkov(corpus.notes,2);
print('made the markov')
melody = markov.generateMelody();
print('generated the melody');
midiWriter.generateMidiFile(melody,'bach');

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.set_volume(0.8)
try:
    play_music('bach.mid');
except KeyboardInterrupt:
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit