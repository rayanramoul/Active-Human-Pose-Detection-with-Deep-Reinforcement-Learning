import torch.nn as nn
import torchvision


class FeatureExtractor(nn.Module):
    def __init__(self):
        super(FeatureExtractor, self).__init__() 
        vgg16 = torchvision.models.vgg16(pretrained=True)
        vgg16.eval() 
        self.features = list(vgg16.children())[0] 
        self.classifier = nn.Sequential(*list(vgg16.classifier.children())[:-2])
    def forward(self, x):
        x = self.features(x)
        return x