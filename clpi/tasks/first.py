from inspect import currentframe, getframeinfo
from pathlib import Path
from time import sleep

from clpi.settings.base import *


class generate_samTask():

    def __init__(self, inp_files=[], out_files=[], gl_vars=None):
        self.inp_files = inp_files
        self.out_files = out_files

    def execute(self):
        """
        generate_sam
        >  input_read1
        >  input_read2

        <  bwa_pl.sam
        """
        inp_args = self.inp_files[:]
        out_args = self.out_files[:]

        sleep(1)
        for ele in out_args:
            Path(ele).touch()



class generate_bamTask():

    def __init__(self, inp_files=[], out_files=[], gl_vars=None):
        self.inp_files = inp_files
        self.out_files = out_files

    def execute(self):
        """
        generate_bam
        >  bwa_pl.sam

        <  bwa_pl.bam
        """
        inp_args = self.inp_files[:]
        out_args = self.out_files[:]

        sleep(1)
        for ele in out_args:
            Path(ele).touch()



class add_or_replace_read_groupsTask():

    def __init__(self, inp_files=[], out_files=[], gl_vars=None):
        self.inp_files = inp_files
        self.out_files = out_files

    def execute(self):
        """
        add_or_replace_read_groups
        >   bwa_pl.bam

        <   bwa_pl_sorted_RG.bam
        """
        inp_args = self.inp_files[:]
        out_args = self.out_files[:]

        sleep(1)
        for ele in out_args:
            Path(ele).touch()


class mark_duplicatesTask():

    def __init__(self, inp_files=[], out_files=[], gl_vars=None):
        self.inp_files = inp_files
        self.out_files = out_files


    def execute(self):
        """
mark_duplicates
>   bwa_pl_sorted_RG.bam

<   bwa_pl_sorted_RG_dupMarked.bam
<   aligned_sorted_RG_dupMarked_metrics.txt
<   aligned_sorted_RG_dupRemoved.bam
<   aligned_sorted_RG_dupRemoved_metrics.txt

        """

        inp_args = self.inp_files[:]
        out_args = self.out_files[:]

        sleep(1)
        for ele in out_args:
            Path(ele).touch()


class collect_hs_metricsTask():

    def __init__(self, inp_files=[], out_files=[], gl_vars=None):
        self.inp_files = inp_files
        self.out_files = out_files


    def execute(self):
        """
collect_hs_metrics
>   bwa_pl_sorted_RG_dupMarked.bam

<   aligned_sorted_RG_picard_collect_metrics.txt
<   aligned_sorted_RG_picard_collect_metrics_with_qc_roi_bed.txt

        """
        inp_args = self.inp_files[:]
        out_args = self.out_files[:]

        sleep(1)
        for ele in out_args:
            Path(ele).touch()


class collect_alignment_summary_metricsTask():

    def __init__(self, inp_files=[], out_files=[], gl_vars=None):
        self.inp_files = inp_files
        self.out_files = out_files


    def execute(self):
        """
collect_alignment_summary_metrics
>   bwa_pl_sorted_RG_dupMarked.bam

<   aligned_sorted_RG_picard_alignment_metrics.txt

        """

        inp_args = self.inp_files[:]
        out_args = self.out_files[:]

        sleep(1)
        for ele in out_args:
            Path(ele).touch()

