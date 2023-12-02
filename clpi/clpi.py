import argparse
import os

from clpi.pipes.dna import dna_pipe


from clpi.version import version
__version__ = version



def perform_analysis(list_of_tasks_to_execute):
    for task_iter, pipe_task in enumerate(list_of_tasks_to_execute):
        pipe_task.execute()



def main():

    parser = argparse.ArgumentParser(description='DNA pipeline.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    args = parser.parse_args()

    os.chdir(r"K:\for_backup_tch\tch_proj\clpi1\out")
    perform_analysis(dna_pipe)


if __name__ == '__main__':
    main()
