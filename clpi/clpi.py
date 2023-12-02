import argparse

from clpi.pipes.dna import dna_pipe


from clpi.version import version
__version__ = version

def main():

    parser = argparse.ArgumentParser(description='DNA pipeline.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    args = parser.parse_args()

if __name__ == '__main__':
    main()
