import ctypes

class EstimatorCS:
    def __init__(self):
        self.f = ctypes.cdll.LoadLibrary('.\\c_module\\checksum.dll')
        self.f.calculateChecksum.restype = ctypes.c_char
        self.f.calculateChecksum.argtypes = [ctypes.POINTER(ctypes.c_char), ]

    def get_CS(self, cmd):
        return ord(self.f.calculateChecksum(cmd.encode('utf-8')))