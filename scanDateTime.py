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
    
    elif experiment_name == '151130_IW_and_SMC_DSMC_01':
        
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
        
    elif experiment_name == '151203_MC_BLF_01':
        
        scan_start_times = np.array([    dt.datetime(2015, 12,  3, 14, 19, 26),
                                         dt.datetime(2015, 12,  3, 14, 41, 54),
                                         dt.datetime(2015, 12,  3, 15,  4, 28),
                                         dt.datetime(2015, 12,  3, 15, 27, 11),
                                         dt.datetime(2015, 12,  3, 15, 49, 12),
                                         dt.datetime(2015, 12,  4,  9, 55, 58),
                                         dt.datetime(2015, 12,  4, 10, 19, 11),
                                         dt.datetime(2015, 12,  4, 10, 38, 25),
                                         dt.datetime(2015, 12,  4, 10, 59, 57),
                                         dt.datetime(2015, 12,  4, 11, 20,  9),
                                         dt.datetime(2015, 12,  4, 11, 43, 50),
                                         dt.datetime(2015, 12,  4, 12,  4, 25),
                                         dt.datetime(2015, 12,  4, 12, 26, 19),
                                         dt.datetime(2015, 12,  4, 12, 47, 15),
                                         dt.datetime(2015, 12,  4, 14, 46, 46),
                                         dt.datetime(2015, 12,  4, 15,  7, 49),
                                         dt.datetime(2015, 12,  4, 15, 50, 45),
                                         dt.datetime(2015, 12,  4, 16, 11, 55),
                                         dt.datetime(2015, 12,  4, 16, 54, 29),
                                         dt.datetime(2015, 12,  4, 17, 30, 57),
                                         dt.datetime(2015, 12,  4, 18,  7, 20),
                                         dt.datetime(2015, 12,  5,  9, 56, 37),
                                         dt.datetime(2015, 12,  5, 10, 32, 51),
                                         dt.datetime(2015, 12,  5, 11,  9, 44)])
        
        #array of "scan end times", which are the photo start times
        scan_end_times = np.array([      dt.datetime(2015, 12,  3, 14, 26, 32),
                                         dt.datetime(2015, 12,  3, 14, 48, 48),
                                         dt.datetime(2015, 12,  3, 15, 12, 11),
                                         dt.datetime(2015, 12,  3, 15, 33, 52),
                                         dt.datetime(2015, 12,  4,  9, 40, 58),
                                         dt.datetime(2015, 12,  4, 10,  1, 10),
                                         dt.datetime(2015, 12,  4, 10, 26, 21),
                                         dt.datetime(2015, 12,  4, 10, 44, 37),
                                         dt.datetime(2015, 12,  4, 11,  5, 29),
                                         dt.datetime(2015, 12,  4, 11, 28, 49),
                                         dt.datetime(2015, 12,  4, 11, 49, 25),
                                         dt.datetime(2015, 12,  4, 12, 11, 19),
                                         dt.datetime(2015, 12,  4, 12, 32, 15),
                                         dt.datetime(2015, 12,  4, 14, 31, 45),
                                         dt.datetime(2015, 12,  4, 14, 52, 49),
                                         dt.datetime(2015, 12,  4, 15, 22, 18),
                                         dt.datetime(2015, 12,  4, 16,  1, 35),
                                         dt.datetime(2015, 12,  4, 16, 23, 50),
                                         dt.datetime(2015, 12,  4, 17,  1, 37),
                                         dt.datetime(2015, 12,  4, 17, 37, 19),
                                         dt.datetime(2015, 12,  5,  9, 26, 37),
                                         dt.datetime(2015, 12,  5, 10,  2, 51),
                                         dt.datetime(2015, 12,  5, 10, 39, 25),
                                         dt.datetime(2015, 12,  5, 11, 16, 50)])    
    
    elif experiment_name == '151207_MC_IS_DS_01':
        
        scan_start_times = np.array([  dt.datetime(2015, 12,  7,  9, 43, 35),
                                         dt.datetime(2015, 12,  7, 10, 21, 58),
                                         dt.datetime(2015, 12,  7, 11,  8, 35),
                                         dt.datetime(2015, 12,  7, 11, 46, 33),
                                         dt.datetime(2015, 12,  7, 12, 23,  8),
                                         dt.datetime(2015, 12,  7, 12, 59, 25),
                                         dt.datetime(2015, 12,  7, 14, 32, 38),
                                         dt.datetime(2015, 12,  7, 15,  9,  5),
                                         dt.datetime(2015, 12,  8, 10, 47, 19),
                                         dt.datetime(2015, 12,  8, 12,  0,  1),
                                         dt.datetime(2015, 12,  8, 13, 22, 23),
                                         dt.datetime(2015, 12,  8, 14,  1, 42),
                                         dt.datetime(2015, 12,  8, 14, 38,  6),
                                         dt.datetime(2015, 12,  8, 15, 14,  2),
                                         dt.datetime(2015, 12,  8, 15, 57, 19),
                                         dt.datetime(2015, 12,  8, 16, 33, 56),
                                         dt.datetime(2015, 12,  8, 17, 10, 56),
                                         dt.datetime(2015, 12,  9,  9, 36, 40),
                                         dt.datetime(2015, 12,  9, 10, 12, 49),
                                         dt.datetime(2015, 12,  9, 10, 50,  2),
                                         dt.datetime(2015, 12,  9, 11, 26, 26)])
        
        #array of "scan end times", which are the photo start times
        scan_end_times = np.array([      dt.datetime(2015, 12,  7,  9, 51, 57),
                                         dt.datetime(2015, 12,  7, 10, 38, 34),
                                         dt.datetime(2015, 12,  7, 11, 16, 34),
                                         dt.datetime(2015, 12,  7, 11, 53,  8),
                                         dt.datetime(2015, 12,  7, 12, 29, 25),
                                         dt.datetime(2015, 12,  7, 14,  2, 37),
                                         dt.datetime(2015, 12,  7, 14, 39,  4),
                                         dt.datetime(2015, 12,  8,  9, 39, 35),
                                         dt.datetime(2015, 12,  8, 10, 53, 28),
                                         dt.datetime(2015, 12,  8, 12, 52, 22),
                                         dt.datetime(2015, 12,  8, 13, 31, 42),
                                         dt.datetime(2015, 12,  8, 14,  8,  5),
                                         dt.datetime(2015, 12,  8, 14, 44,  2),
                                         dt.datetime(2015, 12,  8, 15, 26,  5),
                                         dt.datetime(2015, 12,  8, 16,  4, 36),
                                         dt.datetime(2015, 12,  8, 16, 40, 55),
                                         dt.datetime(2015, 12,  9,  9,  6, 39),
                                         dt.datetime(2015, 12,  9,  9, 42, 49),
                                         dt.datetime(2015, 12,  9, 10, 20,  2),
                                         dt.datetime(2015, 12,  9, 10, 56, 27),
                                         dt.datetime(2015, 12,  9, 11, 32, 37)])  
    
    elif experiment_name == '':
        scan_start_times = None
        scan_end_times = None
        pass
    
    else:
        scan_start_times = None
        scan_end_times = None
        print "Can't find time stamps for this experiment!"
        
    return scan_start_times, scan_end_times