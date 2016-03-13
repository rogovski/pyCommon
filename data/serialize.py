import zlib, cPickle as pickle

# receive pickled object from zmq
def recv_zipped_pickle(blob, protocol=-1):
    p = zlib.decompress(blob)
    return pickle.loads(p)

# send pickled object, zip before sending
def send_zipped_pickle(obj, protocol=-1):
    p = pickle.dumps(obj, protocol)
    return zlib.compress(p)

# receive pickled object from zmq
def zmq_recv_zipped_pickle(socket, flags=0, protocol=-1):
    z = socket.recv(flags)
    p = zlib.decompress(z)
    return pickle.loads(p)

# send pickled object through zmq socket, zip before sending
def zmq_send_zipped_pickle(socket, obj, flags=0, protocol=-1):
    p = pickle.dumps(obj, protocol)
    z = zlib.compress(p)
    return socket.send(z, flags=flags)