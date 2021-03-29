import torch


def main():
    _device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('Using device:', _device)

    _tensor_a = torch.randn(10000).to_device(_device)
    _tensor_b = torch.randn(4096, 10000).to_device(_device)

    print(_tensor_a.get_device())
    print(_tensor_b.get_device())

    c = torch.matmul(_tensor_b, _tensor_a)
    print(c.get_device())
    while True:
        c = torch.matmul(_tensor_b, _tensor_a)


if __name__ == '__main__':
    main()