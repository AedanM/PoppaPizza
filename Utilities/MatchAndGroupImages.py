"""Puts matching images in Folders"""

import argparse
import glob
import os
from dataclasses import dataclass

import cv2
import numpy as np
from skimage.metrics import structural_similarity


@dataclass
class Image:
    """Image Object"""

    FilePath: str
    FileName: str
    CvObj: np.array
    DstPath: str = ""
    HasParent: bool = False
    HasChild: bool = False

    def __repr__(self) -> str:
        return f"{self.FilePath} to {self.DstPath}, Parent Status is {self.HasChild}"


def GetAllImages(filePath) -> list:
    """Collects all images in folders into list of Image objects

    Args-
        filePath (str): Path to parent folder

    Returns-
        list: List of Image Objects
    """
    pathList = glob.glob(root_dir=filePath, pathname="*.jpg")
    pathList.extend(glob.glob(root_dir=filePath, pathname="*.png"))
    pathList.extend(glob.glob(root_dir=filePath, pathname="*.jpeg"))
    outputList = []
    for image in pathList:
        fullPath = os.path.join(filePath, image)
        outputList.append(
            Image(FilePath=fullPath, FileName=image, CvObj=cv2.imread(fullPath))
        )
    return outputList


def AreSimilar(image1, image2, tolerance=0.75) -> bool:
    """Determines if 2 images are similar

    Args-
        image1 (Image): 1st Image
        image2 (Image): 2nd Image
        tolerance (float, optional): Closeness required for match. Defaults to 0.75.

    Returns-
        bool: Are They Similar?
    """
    firstGray = cv2.cvtColor(image1.CvObj, cv2.COLOR_BGR2GRAY)
    secondGray = cv2.cvtColor(image2.CvObj, cv2.COLOR_BGR2GRAY)

    score = structural_similarity(firstGray, secondGray, full=True)
    score = score[0]
    return score > tolerance


def MatchImages(fileList) -> list:
    """Creates Parent and Child Relationship for Images

    Args-
        fileList (list[Image]): List of Images

    Returns-
        list: list of Images with Relationships applied
    """
    unMatched = [x for x in fileList if x.hasParent is False]
    matched = [x for x in fileList if x.hasParent is True]
    for image in unMatched:
        foundPartner = False
        for parentImage in matched:
            if image.cvObj.shape == parentImage.cvObj.shape:
                if AreSimilar(image1=image, image2=parentImage):
                    foundPartner = True
                    image.dstPath = parentImage.dstPath
                    parentImage.hasChild = True
                    image.hasParent = True
        if not foundPartner:
            image.hasParent = False
            image.dstPath = image.fileName.split(".")[0]
        matched.append(image)
    return fileList


def MoveImagesToDest(fileList) -> None:
    """Moves Images to directory of parent image

    Args-
        fileList (list[Image]): List of Images
    """
    numMatched = 0
    foldersCreated = 0
    for image in fileList:
        if image.hasParent or image.hasChild:
            destFolder = os.path.join(os.path.dirname(image.filePath), image.dstPath)
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
                foldersCreated += 1
            os.rename(image.filePath, os.path.join(destFolder, image.fileName))
            numMatched += 1
    print(f"{numMatched}/{len(fileList)} images moved in {foldersCreated} folders")


def Main(filePath) -> None:
    """Find all images which are similar and place them in a folder togethers

    Args-
        filePath (str): Path to parent dir
    """
    fileList = GetAllImages(filePath=filePath)
    fileList = MatchImages(fileList=fileList)
    MoveImagesToDest(fileList=fileList)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Matching and Grouping Images")
    parser.add_argument("-d", "--directory", default=os.getcwd())
    args = parser.parse_args()
    Main(filePath=args.directory)
