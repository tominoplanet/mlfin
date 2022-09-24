"""
Labeling techniques used in financial machine learning.
"""

from mlfin.labeling.labeling import (add_vertical_barrier, apply_pt_sl_on_t1, barrier_touched, drop_labels,
                                        get_bins, get_events)
from mlfin.labeling.trend_scanning import trend_scanning_labels
from mlfin.labeling.tail_sets import TailSetLabels
from mlfin.labeling.fixed_time_horizon import fixed_time_horizon