import os
import time
from datetime import datetime

import numpy as np
import sounddevice as sd
#import torch
#import torchaudio
i = 0


def parse_audio_device(device):
    if device is None:
        return device
    try:
        return int(device)
    except ValueError:
        return device


def process():
    # input stream
    device_in = parse_audio_device(args.in_)
    stream_in = sd.InputStream(
        device=device_in,
        samplerate=args.sample_rate,
        channels=1)

    # denoised output stream
    device_out = parse_audio_device(args.out)
    stream_out = sd.OutputStream(
        device=device_out,
        samplerate=args.sample_rate,
        channels=1)

    stream_in.start()
    stream_out.start()

    length = 16000

    #input_frames = np.zeros((1, length), dtype=np.float32)
    #output_frames = np.zeros((1, length), dtype=np.float32)

    """while True:
        try:
            # Reading audio frames for input to denoiser
            frame, overflow = stream_in.read(length)
            frame = torch.from_numpy(frame).to(args.device)
            frame = frame.view(1, length)

            # writing input frames to sanity check the claim of input imputation
            input_frames = np.append(input_frames, frame.cpu().numpy(), axis=1)
            print('noisy frame written ---> input buffer')

            with torch.no_grad():
                # denoiser inference
                out = enhance_model.enhance_batch(frame, lengths=torch.tensor([1.]))

                # writing denoised frame to output stream
                output_frames = np.append(output_frames, out.cpu().numpy(), axis=1)
                print('enhanced frame written ---> out buffer')

                out = out.view(length)

            underflow = stream_out.write(out)

        except KeyboardInterrupt:
            print("Stopping")

            # Saving files
            _inp = torch.from_numpy(input_frames)
            _out = torch.from_numpy(output_frames)

            date_time = datetime.now().strftime("%d%m%Y_%H%M%S")
            in_file = 'in_mgan_frame_sliced_' + date_time + '.wav'
            out_file = 'out_mgan_frame_sliced_' + date_time + '.wav'

            torchaudio.save(os.path.join('results', in_file), _inp, 16000)
            torchaudio.save(os.path.join('results', out_file), _out, 16000)

            break"""

    while i==0:
        val = input("Enter a number")
        if val == 1:
            i = 1


    #stream_out.stop()
    #stream_in.stop()
