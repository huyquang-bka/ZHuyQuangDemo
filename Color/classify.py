# Copyright © 2020 by Spectrico
# Licensed under the MIT License

import numpy as np
import MNN
import cv2


def load_labels(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


class Classifier():
    def __init__(self, model, labels):
        self.interpreter = MNN.Interpreter(model)
        self.session = self.interpreter.createSession()
        self.input_tensor = self.interpreter.getSessionInput(self.session)
        self.labels = load_labels(labels)

    def predict(self, image):
        # change to rgb format
        image = image[..., ::-1]
        # change to rgb format
        image = cv2.resize(image, (224, 224))
        # resize to mobile_net tensor size
        image = image - (103.94, 116.78, 123.68)
        image = image * (0.017, 0.017, 0.017)
        # preprocess it
        image = image.transpose((2, 0, 1))
        # change numpy data type as np.float32 to match tensor's format
        image = image.astype(np.float32)
        # cv2 read shape is NHWC, Tensor's need is NCHW,transpose it
        tmp_input = MNN.Tensor((1, 3, 224, 224), MNN.Halide_Type_Float, image, MNN.Tensor_DimensionType_Caffe)
        self.input_tensor.copyFrom(tmp_input)
        self.interpreter.runSession(self.session)
        output_tensor = self.interpreter.getSessionOutput(self.session)
        preds = output_tensor.getData()

        top = 1
        top_indices = np.array(preds).argsort()[-top:][::-1]
        ix = top_indices[0]
        return (self.labels[ix], str(float(np.array(preds)[ix])))
