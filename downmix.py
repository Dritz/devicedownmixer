import pyaudio
import audioop
import time

p = pyaudio.PyAudio()

CHUNK = 1024
RATE = 44100
FORMAT = pyaudio.paInt16
smpSize = p.get_sample_size(FORMAT)

def callback(in_data, frame_count, time_info, status):
    outstream.write(audioop.tomono(in_data, smpSize, .66, .66))
    return (in_data, pyaudio.paContinue)

deviceindex = None

for i in range(0, p.get_device_count()):
    print "%i: %s" % (i, p.get_device_info_by_index(i)['name'])

indeviceindex = int(raw_input("\nEnter input device number: "))
outdeviceindex = int(raw_input("Enter output device number: "))

instream = p.open(format=FORMAT,
                channels=2,
                rate=RATE,
                input=True,
                output=False,
                frames_per_buffer=CHUNK,
                input_device_index=indeviceindex,
                stream_callback=callback)

outstream = p.open(format=FORMAT,
                channels=1,
                rate=RATE,
                input=False,
                output=True,
                frames_per_buffer=CHUNK,
                output_device_index=outdeviceindex,)

instream.start_stream()

print "\nNow downmixing... (ctrl+c to close)"

while instream.is_active():
    time.sleep(0.1)

instream.close()
outstream2.close()

p.terminate()
