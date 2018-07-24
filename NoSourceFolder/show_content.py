from pkg_resources import resource_filename


def run():
    with open(resource_filename(__name__, 'file.txt')) as f:
        print(f.read())


if __name__ == '__main__':
    run()
