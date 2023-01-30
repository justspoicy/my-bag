# %matplotlib inline
import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l

d2l.use_svg_display()

batch_size = 256

# 通过ToTensor实例将图像数据从PIL类型变换成32位浮点数格式，
# 并除以255使得所有像素的数值均在0～1之间
trans = transforms.ToTensor()
mnist_train = torchvision.datasets.FashionMNIST(
    root="./data", train=True, transform=trans, download=True)
mnist_test = torchvision.datasets.FashionMNIST(
    root="./data", train=False, transform=trans, download=True)

print(len(mnist_train), len(mnist_test))
print("*************")
print(mnist_train[0][0].shape)
# def get_dataloader_workers():  #@save
#     """使用4个进程来读取数据"""
#     return 4

# train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True,
#                              num_workers=get_dataloader_workers())

# timer = d2l.Timer()
# for X, y in train_iter:
#     continue
# f'{timer.stop():.2f} sec'

# def load_data_fashion_mnist(batch_size, resize=None):  #@save
#     """下载Fashion-MNIST数据集，然后将其加载到内存中"""
#     trans = [transforms.ToTensor()]
#     if resize:
#         trans.insert(0, transforms.Resize(resize))
#     trans = transforms.Compose(trans)
#     mnist_train = torchvision.datasets.FashionMNIST(
#         root="../data", train=True, transform=trans, download=True)
#     mnist_test = torchvision.datasets.FashionMNIST(
#         root="../data", train=False, transform=trans, download=True)
#     return (data.DataLoader(mnist_train, batch_size, shuffle=True,
#                             num_workers=get_dataloader_workers()),
#             data.DataLoader(mnist_test, batch_size, shuffle=False,
#                             num_workers=get_dataloader_workers()))

# train_iter, test_iter = load_data_fashion_mnist(32, resize=64)
# for X, y in train_iter:
#     print(X.shape, X.dtype, y.shape, y.dtype)
#     break