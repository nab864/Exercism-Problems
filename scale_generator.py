'''Scales in Western music are based on the chromatic (12-note) scale. This scale can be expressed as the following group of pitches:

    A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯

A given sharp note (indicated by a ♯) can also be expressed as the flat of the note above it (indicated by a ♭) so the chromatic scale can also be written like this:

    A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭

The major and minor scale and modes are subsets of this twelve-pitch collection. They have seven pitches, and are called diatonic scales. The collection of notes in these scales is written with either sharps or flats, depending on the tonic (starting note). Here is a table indicating whether the flat expression or sharp expression of the scale would be used for a given tonic:
Key Signature 	Major 	Minor
Natural 	C 	a
Sharp 	G, D, A, E, B, F♯ 	e, b, f♯, c♯, g♯, d♯
Flat 	F, B♭, E♭, A♭, D♭, G♭ 	d, g, c, f, b♭, e♭

Note that by common music theory convention the natural notes "C" and "a" follow the sharps scale when ascending and the flats scale when descending. For the scope of this exercise the scale is only ascending.
Task

Given a tonic, generate the 12 note chromatic scale starting with the tonic.

    Shift the base scale appropriately so that all 12 notes are returned starting with the given tonic.
    For the given tonic, determine if the scale is to be returned with flats or sharps.
    Return all notes in uppercase letters (except for the b for flats) irrespective of the casing of the given tonic.'''

sharp_chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
flat_chromatic_scale = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
sharp_tonic = ['G', 'D', 'A', 'E', 'B', 'F#', 'B', 'C#', 'G#', 'D#']
flat_tonic = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'D', 'G', 'C', 'Bb']

#My Solution
class Scale:
    def __init__(self):
        self.sharp_chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.flat_chromatic_scale = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        self.sharp_tonic = ['G', 'D', 'A', 'E', 'B', 'F#', 'B', 'C#', 'G#', 'D#']
        self.flat_tonic = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'D', 'G', 'C', 'Bb']

    def scale_generator(self, tonic):
        tonic = tonic.title()
        sharp_scale = tonic in self.sharp_tonic
        if sharp_scale:
            new_scale = self.sharp_chromatic_scale[self.sharp_chromatic_scale.index(tonic):]
            for key in self.sharp_chromatic_scale[:self.sharp_chromatic_scale.index(tonic)]:
                new_scale.append(key)
        else:
            new_scale = self.flat_chromatic_scale[self.flat_chromatic_scale.index(tonic):]
            for key in self.flat_chromatic_scale[:self.flat_chromatic_scale.index(tonic)]:
                new_scale.append(key)

        return print(new_scale)


    def diatonic_scale(self, tonic, interval):
        interval_dict = {'A': 3,
                         'M': 2,
                         'm': 1}
        tonic = tonic.title()
        sharp_scale = tonic in self.sharp_tonic
        if sharp_scale:
            temp_scale = self.sharp_chromatic_scale[self.sharp_chromatic_scale.index(tonic):]
            for key in self.sharp_chromatic_scale[:self.sharp_chromatic_scale.index(tonic)]:
                temp_scale.append(key)
        else:
            temp_scale = self.flat_chromatic_scale[self.flat_chromatic_scale.index(tonic):]
            for key in self.flat_chromatic_scale[:self.flat_chromatic_scale.index(tonic)]:
                temp_scale.append(key)

        current_index = 0
        new_scale = []
        for letter in interval:
                new_scale.append(temp_scale[current_index])
                current_index += interval_dict[letter]
        new_scale.append(temp_scale[0])

        return print(new_scale)


object = Scale()
object.scale_generator('G')
object.diatonic_scale('G', 'MMmMMMm')

#Community Solution
class Scale2:

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        sharps_scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        flats_scale = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
        self.sharp_base = ["C", "G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#"]
        self.flat_base = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
        if tonic in self.sharp_base:
            self.scale = sharps_scale
        if tonic in self.flat_base:
            self.scale = flats_scale

    def chromatic(self):
        result = []
        start_index = self.scale.index(self.tonic)
        for i in range(12):
            result.append(self.scale[start_index])
            start_index = (start_index + 1) % 12
        return result

    def interval(self, intervals):
        result = []
        result.append(self.tonic)
        index = self.scale.index(self.tonic)
        for interval in intervals:
            i = 1
            if interval == "M":
                i = 2
            elif interval == "A":
                i = 3
            index = (index + i) % 12
            result.append(self.scale[index])
        return result

community = Scale2('G')
print(community.chromatic())
print(community.interval('MMmMMMm'))
