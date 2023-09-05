
import sys
from pydub import AudioSegment

def convert_dat_to_wav(dat_file_path):
    # Load the .dat file (assuming it's in 3GP format)
    audio = AudioSegment.from_file(dat_file_path, format="3gp")
    
    # Define the output file name
    wav_file_path = dat_file_path.replace('.dat', '.wav')
    
    # Export the audio in WAV format
    audio.export(wav_file_path, format="wav")
    print(f"File converted and saved as: {wav_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dat2wav.py <path_to_dat_file>")
        sys.exit(1)

    dat_file_path = sys.argv[1]
    convert_dat_to_wav(dat_file_path)
