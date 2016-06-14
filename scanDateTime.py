# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:32:50 2016

@author: Libby
"""

import numpy as np
import datetime as dt

def get_start_end_times(experiment_name):
    """
    Start and end times of experiment run segments, bounded by laser scans,
    meetings, sleep, etc.
    """
    
    if experiment_name == '151124_MC_DW_IW_01':
        
        scan_start_times = np.array([    dt.datetime(2015, 11, 24,  8, 59, 37),
                                         dt.datetime(2015, 11, 24,  9, 28,  3),
                                         dt.datetime(2015, 11, 24, 10,  8, 25),
                                         dt.datetime(2015, 11, 24, 10, 48, 16),
                                         dt.datetime(2015, 11, 24, 11, 24, 51),
                                         dt.datetime(2015, 11, 24, 12,  3, 24),
                                         dt.datetime(2015, 11, 24, 12, 40, 42),
                                         dt.datetime(2015, 11, 24, 13, 55, 34),
                                         dt.datetime(2015, 11, 24, 14, 38,  0),
                                         dt.datetime(2015, 11, 24, 15, 19,  5),
                                         dt.datetime(2015, 11, 24, 15, 57, 17),
                                         dt.datetime(2015, 11, 24, 16, 31,  1),
                                         dt.datetime(2015, 11, 24, 17,  8, 44),
                                         dt.datetime(2015, 11, 24, 17, 44, 55),
                                         dt.datetime(2015, 11, 24, 18, 22,  1),
                                         dt.datetime(2015, 11, 25, 10, 11, 19),
                                         dt.datetime(2015, 11, 25, 10, 47, 41),
                                         dt.datetime(2015, 11, 25, 11, 29,  6),
                                         dt.datetime(2015, 11, 25, 12,  5, 24),
                                         dt.datetime(2015, 11, 25, 13, 27, 51),
                                         dt.datetime(2015, 11, 25, 14,  4, 23),
                                         dt.datetime(2015, 11, 25, 14, 41, 58),
                                         dt.datetime(2015, 11, 25, 15, 18, 42)])
        
        #array of "scan end times", which are the photo start times
        scan_end_times = np.array([      dt.datetime(2015, 11, 24,  9,  6, 23),
                                         dt.datetime(2015, 11, 24,  9, 38, 25),
                                         dt.datetime(2015, 11, 24, 10, 18, 16),
                                         dt.datetime(2015, 11, 24, 11,  0, 11),
                                         dt.datetime(2015, 11, 24, 11, 33, 23),
                                         dt.datetime(2015, 11, 24, 12, 10, 43),
                                         dt.datetime(2015, 11, 24, 13, 25, 32),
                                         dt.datetime(2015, 11, 24, 14,  1, 51),
                                         dt.datetime(2015, 11, 24, 14, 47, 47),
                                         dt.datetime(2015, 11, 24, 15, 25, 17),
                                         dt.datetime(2015, 11, 24, 16,  3, 21),
                                         dt.datetime(2015, 11, 24, 16, 38, 43),
                                         dt.datetime(2015, 11, 24, 17, 14, 55),
                                         dt.datetime(2015, 11, 24, 17, 51, 59),
                                         dt.datetime(2015, 11, 25,  9, 41, 40),
                                         dt.datetime(2015, 11, 25, 10, 17, 40),
                                         dt.datetime(2015, 11, 25, 10, 58, 11),
                                         dt.datetime(2015, 11, 25, 11, 35, 23),
                                         dt.datetime(2015, 11, 25, 12, 57, 50),
                                         dt.datetime(2015, 11, 25, 13, 34, 23),
                                         dt.datetime(2015, 11, 25, 14, 11, 57),
                                         dt.datetime(2015, 11, 25, 14, 48, 41),
                                         dt.datetime(2015, 11, 25, 15, 25, 58)])
    
    elif experiment_name == '151127_MC_IW_IW_01':
        
        scan_start_times = np.array([    dt.datetime(2015, 11, 27, 12, 10, 23),
                                         dt.datetime(2015, 11, 27, 12, 47, 50),
                                         dt.datetime(2015, 11, 27, 13, 25, 38),
                                         dt.datetime(2015, 11, 27, 14, 36, 36),
                                         dt.datetime(2015, 11, 27, 15, 14, 27),
                                         dt.datetime(2015, 11, 27, 15, 50, 41),
                                         dt.datetime(2015, 11, 27, 16, 26, 50),
                                         dt.datetime(2015, 11, 27, 17, 51, 40),
                                         dt.datetime(2015, 11, 28, 15, 17, 06),
                                         dt.datetime(2015, 11, 28, 15, 54, 10),
                                         dt.datetime(2015, 11, 28, 16, 31, 34),
                                         dt.datetime(2015, 11, 28, 17,  9, 17),
                                         dt.datetime(2015, 11, 28, 17, 45, 55),
                                         dt.datetime(2015, 11, 29,  9, 51, 44),
                                         dt.datetime(2015, 11, 29, 10, 28, 49),
                                         dt.datetime(2015, 11, 29, 11,  6, 15),
                                         dt.datetime(2015, 11, 29, 11, 42, 52),
                                         dt.datetime(2015, 11, 29, 12, 19, 23)])
        
        #array of "scan end times", which are the photo start times
        scan_end_times = np.array([      dt.datetime(2015, 11, 27, 12, 17, 30),
                                         dt.datetime(2015, 11, 27, 12, 55, 38),
                                         dt.datetime(2015, 11, 27, 14,  6, 36),
                                         dt.datetime(2015, 11, 27, 14, 44, 27),
                                         dt.datetime(2015, 11, 27, 15, 20, 41),
                                         dt.datetime(2015, 11, 27, 15, 56, 50),
                                         dt.datetime(2015, 11, 27, 16, 34, 35),
                                         dt.datetime(2015, 11, 28, 14, 47, 24),
                                         dt.datetime(2015, 11, 28, 15, 24,  9),
                                         dt.datetime(2015, 11, 28, 16, 01, 33),
                                         dt.datetime(2015, 11, 28, 16, 39, 17),
                                         dt.datetime(2015, 11, 28, 17, 15, 56),
                                         dt.datetime(2015, 11, 29,  9, 20, 26),
                                         dt.datetime(2015, 11, 29,  9, 59, 29),
                                         dt.datetime(2015, 11, 29, 10, 36, 15),
                                         dt.datetime(2015, 11, 29, 11, 12, 52),
                                         dt.datetime(2015, 11, 29, 11, 49, 44),
                                         dt.datetime(2015, 11, 29, 12, 25, 53)])
    
    elif experiment_name == '151130':
        
        scan_start_times = np.array([   dt.datetime(2015, 11, 30, 14, 35, 25),
                                        dt.datetime(2015, 11, 30, 17, 29, 39),
                                        dt.datetime(2015, 11, 30, 17, 56, 13),
                                        dt.datetime(2015, 12,  1,  9, 43, 54),
                                        dt.datetime(2015, 12,  1, 10, 21, 51),
                                        dt.datetime(2015, 12,  1, 10, 59, 27),
                                        dt.datetime(2015, 12,  1, 11, 39, 21),
                                        dt.datetime(2015, 12,  1, 12, 17, 34),
                                        dt.datetime(2015, 12,  1, 13, 45, 51),
                                        dt.datetime(2015, 12,  1, 14, 31, 22),
                                        dt.datetime(2015, 12,  1, 15,  9, 51),
                                        dt.datetime(2015, 12,  1, 15, 47, 35),
                                        dt.datetime(2015, 12,  1, 16, 25, 21),
                                        dt.datetime(2015, 12,  1, 17,  6, 25),
                                        dt.datetime(2015, 12,  1, 17, 44, 10),
                                        dt.datetime(2015, 12,  2, 10,  0, 53),
                                        dt.datetime(2015, 12,  2, 10, 52, 12),
                                        dt.datetime(2015, 12,  2, 11, 33,  1),
                                        dt.datetime(2015, 12,  2, 12,  9, 33),
                                        dt.datetime(2015, 12,  2, 12, 48,  2),
                                        dt.datetime(2015, 12,  2, 13, 26,  6)])
        
        #array of "scan end times", which are the photo start times
        scan_end_times = np.array([      dt.datetime(2015, 11, 30, 17, 20, 39),
                                         dt.datetime(2015, 11, 30, 17, 34, 53),
                                         dt.datetime(2015, 12,  1,  9, 13, 35),
                                         dt.datetime(2015, 12,  1,  9, 52, 11),
                                         dt.datetime(2015, 12,  1, 10, 29, 27),
                                         dt.datetime(2015, 12,  1, 11,  9, 20),
                                         dt.datetime(2015, 12,  1, 11, 47, 33),
                                         dt.datetime(2015, 12,  1, 13, 15, 51),
                                         dt.datetime(2015, 12,  1, 14,  0,  9),
                                         dt.datetime(2015, 12,  1, 14, 39, 51),
                                         dt.datetime(2015, 12,  1, 15, 17, 34),
                                         dt.datetime(2015, 12,  1, 15, 55, 20),
                                         dt.datetime(2015, 12,  1, 16, 35, 22),
                                         dt.datetime(2015, 12,  1, 17, 14, 18),
                                         dt.datetime(2015, 12,  2,  9, 17, 48),
                                         dt.datetime(2015, 12,  2, 10, 22, 12),
                                         dt.datetime(2015, 12,  2, 11,  2, 41),
                                         dt.datetime(2015, 12,  2, 11, 40, 12),
                                         dt.datetime(2015, 12,  2, 12, 18,  1),
                                         dt.datetime(2015, 12,  2, 12, 56,  5),
                                         dt.datetime(2015, 12,  2, 14,  7, 33)])
        
    elif experiment_name == '':
        scan_start_times = None
        scan_end_times = None
        pass
    
    elif experiment_name == '':
        scan_start_times = None
        scan_end_times = None
        pass
    
    elif experiment_name == '':
        scan_start_times = None
        scan_end_times = None
        pass
    
    else:
        scan_start_times = None
        scan_end_times = None
        print "Can't find time stamps for this experiment!"
        
    return scan_start_times, scan_end_times