from clpi.pipes.build import build_pipe


dna_pipe = build_pipe(list(map(str.strip, """
________________________________________
generate_sam
>  input_read1.fastq.gz
>  input_read2.fastq.gz

<  bwa_pl.sam
________________________________________
generate_bam
>  bwa_pl.sam

<  bwa_pl.bam
________________________________________
add_or_replace_read_groups
>   bwa_pl.bam

<   bwa_pl_sorted_RG.bam
________________________________________
add_or_replace_read_groups
>   bwa_pl.bam

<   bwa_pl_sorted_RG.bam
________________________________________
mark_duplicates
>   bwa_pl_sorted_RG.bam

<   bwa_pl_sorted_RG_dupMarked.bam
<   aligned_sorted_RG_dupMarked_metrics.txt
<   aligned_sorted_RG_dupRemoved.bam
<   aligned_sorted_RG_dupRemoved_metrics.txt
________________________________________
collect_hs_metrics
>   bwa_pl_sorted_RG_dupMarked.bam

<   aligned_sorted_RG_picard_collect_metrics.txt
<   aligned_sorted_RG_picard_collect_metrics_with_qc_roi_bed.txt
________________________________________
collect_alignment_summary_metrics
>   bwa_pl_sorted_RG_dupMarked.bam

<   aligned_sorted_RG_picard_alignment_metrics.txt
_______________________________________
""".split("\n")[1:-1])))
