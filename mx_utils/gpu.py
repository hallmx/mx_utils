# AUTOGENERATED! DO NOT EDIT! File to edit: 04_device.ipynb (unless otherwise specified).

__all__ = ['versions']

# Cell
def versions():
  "Checks if GPU enabled and if so displays device details with cuda, pytorch, fastai versions"
  print("GPU: ", torch.cuda.is_available())
  if torch.cuda.is_available() == True:
    print("Device = ", torch.device(torch.cuda.current_device()))
    print("Cuda version - ", torch.version.cuda)
    print("cuDNN version - ", torch.backends.cudnn.version())
    print("PyTorch version - ", torch.__version__)
    print("fastai version", fastai.__version__)