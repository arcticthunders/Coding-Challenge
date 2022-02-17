import numpy as np


class Box():
    def __init__(self, center, size) -> None:
        self.center = np.array(center)
        self.size = size
        self.edges = {
            0: [1, 2, 4],
            1: [3, 5],
            2: [3, 6],
            3: [7],
            4: [5, 6],
            5: [7],
            6: [7]
        }
        self.faces = {
            1: [0, 1, 2, 3],
            2: [0, 2, 4, 6],
            3: [0, 1, 4, 5],
            4: [2, 3, 6, 7],
            5: [4, 5, 6, 7],
            6: [1, 3, 5, 7]
        }

    def getCorners(self):
        corners = []
        sign = np.array([1, -1])
        for i in sign:
            for j in sign:
                for k in sign:
                    displacement = self.size*np.array([i/2, j/2, k/2])
                    newarr = self.center.__add__(displacement)
                    corners.append(newarr)
        return corners

    def getEdges(self):
        x, y, z = [], [], []
        corners = self.getCorners()
        for corner1, cornerList in self.edges.items():
            for i in range(len(cornerList)):
                start = corners[corner1]
                end = corners[cornerList[i]]
                x.append([start[0], end[0]])
                y.append([start[1], end[1]])
                z.append([start[2], end[2]])
        return x, y, z

    def getSurfaces(self):
        corners = self.getCorners()
        faceList = []
        for face, cornerList in self.faces.items():
            X, Y, Z = [], [], []
            for corn in cornerList:
                X.append(corners[corn][0])
                Y.append(corners[corn][1])
                Z.append(corners[corn][2])
            faceList.append([X, Y, Z])
        return faceList
