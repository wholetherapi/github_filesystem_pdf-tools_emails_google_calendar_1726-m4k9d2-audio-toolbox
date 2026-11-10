"""Polyphase sample-rate conversion."""

import math


def resample(signal, source_rate, target_rate):
    if source_rate == target_rate:
        return list(signal)
    ratio = target_rate / float(source_rate)
    out_len = int(math.floor(len(signal) * ratio))
    return [signal[min(len(signal) - 1, int(i / ratio))] for i in range(out_len)]
