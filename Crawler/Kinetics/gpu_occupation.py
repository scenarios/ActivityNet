import torch


def main():

    while True:
        _tensor_a = torch.randn(10000)
        _tensor_b = torch.randn(4096, 10000)
        torch.matmul(_tensor_b, _tensor_a)


if __name__ == '__main__':
    main()