import torch

def load_model():
    model = torch.load("models/asd_model.pth")
    model.eval()
    return model

def predict(model, data):
    output = model(data)
    return output