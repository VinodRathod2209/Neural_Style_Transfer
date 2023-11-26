# Neural Style Transfer

## Introduction
This is an implementation of the paper "Image Style Transfer Using Convolutional Neural Networks"[1]. In this project, I use the VGG19[2] as the backbone for image feature extraction. The VGG19 extracts the content representation of the content image and the intermediate style representation of the style image. The final style representation is derived from the result of second order polynomial kernel of the intermediate style representation[3].

While generating the output image, the neural style transfer algorithm tries to minimize both the style loss and the content loss. However, the style loss and the content loss contradicts to each other in most cases(if the output image is "closer" to the content image, then it should be "farther" from the style image, and vice versa). Therefore, the final output image is at a balance point that possess both the content information from the content image and the texture from the style image.

## Setup
To perform style transfer, you need to save the image that you want to modify in the content folder inside the image folder, and the image that you want to use as a reference in the style folder inside the image folder. Then, you need to edit the main.py file and specify the names of the content image and the style image that you have chosen.

## Limitations
Synthesized images often have low-level noise, which is less noticeable in artistic style transfer but affects photorealism when both content and style images are photographs. This noise, resembling network filters, could potentially be removed with efficient post-optimization de-noising techniques.
The resolution of synthesized images is a significant constraint, as both the optimization problem’s dimensionality and the Convolutional Neural Network’s unit count increase linearly with pixel count. This affects the synthesis speed, which is heavily dependent on image resolution.


## References
[1] L. A. Gatys, A. S. Ecker and M. Bethge, Image Style Transfer Using Convolutional Neural Networks, 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, USA, 2016, pp. 2414-2423, doi: 10.1109/CVPR.2016.265.

[2] K. Simonyan and A. Zisserman, Very Deep Convolutional Networks for Large-Scale Image Recognition. arXiv, 2014. doi: 10.48550ARXIV.1409.1556.

[3] Y. Li, N. Wang, J. Liu, and X. Hou, Demystifying Neural Style Transfer. arXiv, 2017. doi: 10.48550/ARXIV.1701.01036.

[4]	D. Ulyanov, V. Lebedev, A. Vedaldi, and V. Lempitsky, Texture Networks: Feed-forward Synthesis of Textures and Stylized Images. arXiv, 2016. doi: 10.48550/ARXIV.1603.03417
