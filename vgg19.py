from torchvision.models import vgg19 
from torch import nn
from torchvision.models.feature_extraction import create_feature_extractor 
import torch

# VGG19 Model Defination 

class VGG19(nn.Module):
    def __init__(self):
        super().__init__()
        
        # Loading the pre-trained VGG19 model from the torchvision models
        self.vgg19 = vgg19(weights='IMAGENET1K_V1').features
        self.max_pool_layers = [4, 9, 18, 27]

        for param in self.vgg19.parameters():
            param.requires_grad_(False)

        for idx, module in enumerate(self.vgg19):
            if hasattr(module, 'inplace'):
                self.vgg19[idx].inplace = False
            if idx in self.max_pool_layers:
                self.vgg19[idx] = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)

        # Extracting the intermediate features from the model
        self.model = create_feature_extractor(self.vgg19, {
            '1': 'conv1_1',
            '6': 'conv2_1',
            '11': 'conv3_1',
            '20': 'conv4_1',
            '29': 'conv5_1',
        })

    def forward(self, x):
        output = self.model(x)
        return output
