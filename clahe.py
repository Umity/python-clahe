{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "#img = cv2.imread('Desktop/IMG_1382.jpg',0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [],
   "source": [
    "#clahe = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(1,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [],
   "source": [
    "#cl1 = clahe.apply(img)\n",
    "#cv2.imwrite('Desktop/clahe_2.jpg',cl1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [],
   "source": [
    "bgr = cv2.imread('Desktop/IMG_1382.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [],
   "source": [
    "lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)\n",
    "lab_planes = cv2.split(lab)\n",
    "\n",
    "clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))\n",
    "\n",
    "lab_planes[0] = clahe.apply(lab_planes[0])\n",
    "\n",
    "lab = cv2.merge(lab_planes)\n",
    "\n",
    "bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "lab_planes = cv2.split(lab)\n",
    "\n",
    "clahe = cv2.createCLAHE(clipLimit=1.0,tileGridSize=(8,8))\n",
    "\n",
    "lab_planes[0] = clahe.apply(lab_planes[0])\n",
    "\n",
    "lab = cv2.merge(lab_planes)\n",
    "\n",
    "bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv2.imwrite('Desktop/clahe_2b.jpg',bgr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-154-5c644eb67425>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-154-5c644eb67425>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    cv2.\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
