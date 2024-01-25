"""Class for Altering Colors"""
from dataclasses import dataclass
import colorsys
import numpy as np


@dataclass
class Color:
    H: int
    S: int
    V: int

    def GetNumPy(self) -> "np.NDArray[np.uint8]":
        return np.array([self.H, self.S, self.V], dtype=np.uint8)

    @property
    def HSV(self) -> tuple[int, int, int]:
        return (self.H, self.S, self.V)

    @property
    def RGB(self) -> tuple[int, ...]:
        return tuple(
            round(i * 255)
            for i in colorsys.hsv_to_rgb(
                float(
                    self.H,
                )
                / 255,
                float(self.S) / 255,
                float(self.V) / 255,
            )
        )

    @property
    def BGR(self) -> tuple[int, int, int]:
        rgb = self.RGB
        return (rgb[2], rgb[1], rgb[0])


White = Color(H=0, S=0, V=255)
black = Color(H=0, S=0, V=0)
Blue = Color(H=128, S=200, V=128)
Green = Color(H=70, S=200, V=128)
Grey = Color(H=0, S=0, V=128)
Pink = Color(H=220, S=200, V=128)
Yellow = Color(H=25, S=200, V=180)

"""

def OpenCVToPygame(opencv_image):
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
    orginalColor = Color(h=orginalHue, s=255, v=128)
    newColor = Color(h=newHue, s=255, v=128)
    hueshifted = shift_hue(openCVimage, orginalColor.getNumPy(), newColor.getNumPy())
    return opencv_to_pygame(hueshifted)


def pygame_to_opencv(pygame_image):
    # Convert Pygame image to string
    pygame_str = pygame.image.tostring(pygame_image, "RGB")

    # Create a NumPy array from the string
    pygame_array = np.frombuffer(pygame_str, dtype=np.uint8)

    # Reshape the array to match the Pygame image dimensions
    pygame_array = pygame_array.reshape(
        (pygame_image.get_height(), pygame_image.get_width(), 3)
    )

    # Convert the NumPy array to an OpenCV image
    opencv_image = cv2.cvtColor(pygame_array, cv2.COLOR_RGB2BGR)

    return opencv_image


def ToOpenCV(image):
    image_array = pygame.surfarray.array3d(image)
    opencv_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)
    return opencv_image

"""
