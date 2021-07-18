/* Silicon Valley s03e06 12:44
   
   Sources:
      -  (fictional)    https://github.com/Stitchpunk/atari-ai/blob/master/src/lib/common.cc 
      -  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/stream_executor/stream.cc
*/

namespace {
// Code to turn parameters to functions on stream into strings that
// will be VLOG'ed. We need overloads, instead of
// e.g. BatchDescriptorToVlogString(), as the code that calls these
// functions does not know what the type of the parameter is.
string ToVlogString(const dnn::BatchDescriptor &descriptor) {
    return descriptor.ToShortString();
}

string ToVlogString(const dnn::FilterDescriptor &descriptor) {
    return descriptor.ToShortString();
}

string ToVlogString(const dnn::ConvolutionDescriptor &descriptor) {
    return descriptor.ToShortString();
}

string ToVlogString(const dnn::PoolingDescriptor &descriptor) {
    return descriptor.ToShortString();
}

string ToVlogString(const dnn::NormalizeDescriptor &descriptor) {
    return descriptor.ToShortString();
}
