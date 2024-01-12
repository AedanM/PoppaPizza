import pygame
import cv2
import numpy as np
from dataclasses import dataclass
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

@dataclass
class Color:
    h: int
    s: int
    v: int

    def getNumPy(self):
        return np.array([self.h, self.s, self.v],dtype=np.uint8)

    def to_rgb(self):
        """
        Convert HSV color to RGB.
        """
        hi = int(self.h / 60) % 6
        f = self.h / 60 - hi
        p = self.v * (1 - self.s)
        q = self.v * (1 - f * self.s)
        t = self.v * (1 - (1 - f) * self.s)

        if hi == 0:
            return int(self.v * 255), int(t * 255), int(p * 255)
        elif hi == 1:
            return int(q * 255), int(self.v * 255), int(p * 255)
        elif hi == 2:
            return int(p * 255), int(self.v * 255), int(t * 255)
        elif hi == 3:
            return int(p * 255), int(q * 255), int(self.v * 255)
        elif hi == 4:
            return int(t * 255), int(p * 255), int(self.v * 255)
        else:
            return int(self.v * 255), int(p * 255), int(q * 255)

    def to_bgr(self):
        """
        Convert HSV color to BGR.
        """
        rgb = self.to_rgb()
        return rgb[2], rgb[1], rgb[0]

def opencv_to_pygame(opencv_image):
    # Convert the OpenCV image to RGB
    opencv_image_rgb = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

    # Convert NumPy array to Pygame surface
    pygame_surface = pygame.surfarray.make_surface(opencv_image_rgb)

    return pygame_surface


def shift_hue(img, color_from, color_to):
    # Convert the image to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define a mask for the color range to be replaced
    mask = cv2.inRange(hsv_img, color_from, color_from)
    print(color_from, color_to)
    # Calculat  e the hue difference between the two colors
    hue_diff = (
        int(color_from[0]) - int(color_to[0])
    ) % 180  # Ensure the difference is within the valid range

    # Shift the hue values
    hsv_img[:, :, 0] = (hsv_img[:, :, 0] + hue_diff) % 180

    # Apply the mask to the image
    img_masked = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

    # Convert the image back to BGR
    result_img = cv2.cvtColor(img_masked, cv2.COLOR_HSV2BGR)

    return result_img


def ChangeColorToColor(image, orginalHue, newHue):
    openCVimage = pygame_to_opencv(image.image)
    orginalColor = Color(h=orginalHue, s=255,v=128)
    newColor = Color(h=newHue, s=255,v=128)
    hueshifted = shift_hue(openCVimage, orginalColor.getNumPy(), newColor.getNumPy())
    return opencv_to_pygame(hueshifted)


def pygame_to_opencv(pygame_image):
    # Convert Pygame image to string
    pygame_str = pygame.image.tostring(pygame_image, 'RGB')

    # Create a NumPy array from the string
    pygame_array = np.frombuffer(pygame_str, dtype=np.uint8)

    # Reshape the array to match the Pygame image dimensions
    pygame_array = pygame_array.reshape((pygame_image.get_height(), pygame_image.get_width(), 3))

    # Convert the NumPy array to an OpenCV image
    opencv_image = cv2.cvtColor(pygame_array, cv2.COLOR_RGB2BGR)

    return opencv_image

def ToOpenCV(image):
    image_array = pygame.surfarray.array3d(image)
    opencv_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)
    return opencv_image



