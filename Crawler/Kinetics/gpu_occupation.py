import torch


def main():
    _device = torch.device('cuda')
    _tensor_a = torch.randn(10000).to_device(_device)
    _tensor_b = torch.randn(4096, 10000).to_device(_device)
    while True:
        torch.matmul(_tensor_b, _tensor_a)


if __name__ == '__main__':
    main()