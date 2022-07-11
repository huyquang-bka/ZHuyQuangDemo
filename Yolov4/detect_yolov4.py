import os

import cv2
import numpy as np


class Detection:
    def __init__(self):
        self.size = (224, 224)
        self.scale = 1 / 255.
        self.conf_threshold = 0.5
        self.nms_threshold = 0.4
        self.weight_path = "Yolov4/lp.weights"
        self.cfg_path = "Yolov4/base_data_tiny.cfg"
        self.class_path = "Yolov4/obj.names"
        self.net = cv2.dnn.readNet(self.weight_path, self.cfg_path)
        self.classes = self.get_classes()
        self.output_layers = self.get_output_layers(self.net)

    def get_classes(self):
        with open(self.class_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        return self.classes

    def get_output_layers(self, net):
        layer_names = net.getLayerNames()

        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        return output_layers

    def detect(self, image):
        Width = image.shape[1]
        Height = image.shape[0]
        blob = cv2.dnn.blobFromImage(image, 1 / 255., (224, 224), (0, 0, 0), True, crop=False)

        self.net.setInput(blob)

        outs = self.net.forward(self.get_output_layers(self.net))

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.conf_threshold:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)

        bboxes = []

        for i in indices:
            i = i[0]
            box = list(map(int, boxes[i]))
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            id = class_ids[i]
            bboxes.append([x, y, w, h, self.classes[id], confidences[i]])

        return bboxes


if __name__ == "__main__":
    detection = Detection()

    for imageName in os.listdir("Crop"):
        # image = cv2.imread("download.jpg")
        image = cv2.imread("Crop/" + imageName)
        bboxes = detection.detect(image)
        lp_text = ""
        for bbox in sorted(bboxes, key=lambda x: x[0]):
            x, y, w, h = bbox[0], bbox[1], bbox[2], bbox[3]
            cls = bbox[4]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, cls, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            lp_text += cls
        print(lp_text)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
