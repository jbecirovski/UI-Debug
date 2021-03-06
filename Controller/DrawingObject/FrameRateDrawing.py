# Under MIT License, see LICENSE.txt

from Controller.DrawingObject.BaseDrawingObject import BaseDrawingObject
from Controller.QtToolBox import QtToolBox

__author__ = 'RoboCupULaval'


class FrameRateDrawing(BaseDrawingObject):
    def __init__(self):
        super().__init__()

    def draw(self, painter, frame_rate=0):
        if self.isVisible():
            painter.setPen(QtToolBox.create_pen(color=(255, 255, 0), width=3))
            painter.setBrush(QtToolBox.create_brush(color=(0, 255, 255)))
            painter.setFont(QtToolBox.create_font(width=20,
                                                  is_bold=True))
            painter.drawText(5, 50, str(frame_rate))

    @staticmethod
    def get_datain_associated():
        return 'frame-rate'
