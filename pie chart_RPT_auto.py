# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:43:31 2019

@author: FS122322
"""

from fleet_performance import Site, Fleet
import fleet_performance.data_acquisition_toolbox as dat

import pandas as pd
import numpy as np
from datetime import timedelta
import matplotlib.pyplot as plt

site = Site('Topaz')
site.SiteAssetID
start = '2019-01-01 00:00'
stop = '2019-01-31 23:59'

func = dat.get_operator_logs(site.SiteAssetID,start,stop)

operator_log_outage_filtered = func[['EventClassification', 'TotalLostkWh', 'TotalTODLostkWh']]

FO = operator_log_outage_filtered.loc[:,'EventClassification'] == 'Downtime - Forced Outage (FO)'

Lost_Energy_FO = operator_log_outage_filtered.TotalLostkWh.loc[FO].sum()

operator_log_outage_filtered.EventClassification.unique()

MO = operator_log_outage_filtered.loc[:,'EventClassification'] == 'Downtime - Maintenance Outage (MO)'

Lost_Energy_MO = operator_log_outage_filtered.TotalLostkWh.loc[MO].sum()

OMC_curt = operator_log_outage_filtered.loc[:,'EventClassification'] == 'Downtime - Outside Management Control (OMC) Curtailment'

Lost_Energy_OMC_curt = operator_log_outage_filtered.TotalLostkWh.loc[OMC_curt].sum()

OMC = operator_log_outage_filtered.loc[:,'EventClassification'] == 'Downtime - Outside Management Control (OMC)'

Lost_Energy_OMC = operator_log_outage_filtered.TotalLostkWh.loc[OMC].sum()

Labels = 'Downtime - Forced Outage (FO)', 'Downtime - Maintenance Outage (MO)', 'Downtime - Outside Management Control (OMC) Curtailment', 'Downtime - Outside Management Control (OMC)'
Colors = ['red','blue','lightgreen','yellow']

figAC, ax = plt.subplots()
ax.pie([Lost_Energy_FO, Lost_Energy_MO, Lost_Energy_OMC_curt, Lost_Energy_OMC], labels = Labels, autopct='%1.1f%%', colors = Colors)
ax.set_title('Outages by Classification (this month)')


