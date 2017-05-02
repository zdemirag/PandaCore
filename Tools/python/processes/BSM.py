#!/usr/bin/env python
'''@package docstring
Just a giant list of processes and properties
'''

processes =	{

'TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('TTbarDM','MC',1),


'thq':('thq','MC',0.7927),
'thw':('thw','MC',0.147),

'GluGlu_HToInvisible_M125_13TeV_powheg_pythia8':('ggFHinv','MC',48.6),
'Glu_HToInvisible_M125_13TeV_powheg_pythia8':('ggf-m125','MC',48.6),
'VBF_HToInvisible_M125_13TeV_powheg_pythia8':('vbf-m125','MC',3.78),
'VBF_HToInvisible_M1000_13TeV_powheg_pythia8':('vbf-m1000','MC',1),
'VBF_HToInvisible_M110_13TeV_powheg_pythia8':('vbf-m110','MC',1),
'VBF_HToInvisible_M150_13TeV_powheg_pythia8':('vbf-m150','MC',1),
'VBF_HToInvisible_M200_13TeV_powheg_pythia8':('vbf-m200','MC',1),
'VBF_HToInvisible_M300_13TeV_powheg_pythia8':('vbf-m300','MC',1),
'VBF_HToInvisible_M500_13TeV_powheg_pythia8':('vbf-m500','MC',1),
'VBF_HToInvisible_M600_13TeV_powheg_pythia8':('vbf-m600','MC',1),
'VBF_HToInvisible_M800_13TeV_powheg_pythia8':('vbf-m800','MC',1),

'ZprimeToTTJet_M-500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-500','MC',1),
'ZprimeToTTJet_M-750_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-750','MC',1),
'ZprimeToTTJet_M-1000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1000','MC',1),
'ZprimeToTTJet_M-1250_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1250','MC',1),
'ZprimeToTTJet_M-1500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1500','MC',1),
'ZprimeToTTJet_M-2000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-2000','MC',1),
'ZprimeToTTJet_M-2500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-2500','MC',1),
'ZprimeToTTJet_M-3000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-3000','MC',1),
'ZprimeToTTJet_M-3500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-3500','MC',1),
'ZprimeToTTJet_M-4000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-4000','MC',1),

'ZprimeToWW_narrow_M-800_13TeV-madgraph':('ZpWW_med-800','MC',1),
'ZprimeToWW_narrow_M-1000_13TeV-madgraph':('ZpWW_med-1000','MC',1),
'ZprimeToWW_narrow_M-1200_13TeV-madgraph':('ZpWW_med-1200','MC',1),
'ZprimeToWW_narrow_M-1400_13TeV-madgraph':('ZpWW_med-1400','MC',1),
'ZprimeToWW_narrow_M-1600_13TeV-madgraph':('ZpWW_med-1600','MC',1),
'ZprimeToWW_narrow_M-1800_13TeV-madgraph':('ZpWW_med-1800','MC',1),
'ZprimeToWW_narrow_M-2000_13TeV-madgraph':('ZpWW_med-2000','MC',1),
'ZprimeToWW_narrow_M-2500_13TeV-madgraph':('ZpWW_med-2500','MC',1),

'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph':('ZpA0h_med-800','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph':('ZpA0h_med-1000','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph':('twohdm_med-1200','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph':('ZpA0h_med-1400','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph':('ZpA0h_med-1700','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph':('ZpA0h_med-2000','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph':('ZpA0h_med-2500','MC',1),

'MonoHbb_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10_dm-1000','MC',1),
'MonoHbb_ZpBaryonic_MZp-15_MChi-10_13TeV-madgraph':('ZpBaryonic_med-15_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph':('ZpBaryonic_med-20_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph':('ZpBaryonic_med-50_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-50_MChi-10_13TeV-madgraph':('ZpBaryonic_med-50_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-50_MChi-50_13TeV-madgraph':('ZpBaryonic_med-50_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-95_MChi-50_13TeV-madgraph':('ZpBaryonic_med-95_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph':('ZpBaryonic_med-100_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-100_MChi-10_13TeV-madgraph':('ZpBaryonic_med-100_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph':('ZpBaryonic_med-200_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-200_MChi-50_13TeV-madgraph':('ZpBaryonic_med-200_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph':('ZpBaryonic_med-200_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-295_MChi-150_13TeV-madgraph':('ZpBaryonic_med-295_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph':('ZpBaryonic_med-300_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-300_MChi-50_13TeV-madgraph':('ZpBaryonic_med-300_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph':('ZpBaryonic_med-500_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-500_MChi-150_13TeV-madgraph':('ZpBaryonic_med-500_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-500_MChi-500_13TeV-madgraph':('ZpBaryonic_med-500_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-995_MChi-500_13TeV-madgraph':('ZpBaryonic_med-995_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-1000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-1000_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-1000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1000','MC',1),
'MonoHbb_ZpBaryonic_MZp-1995_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1995_dm-1000','MC',1),
'MonoHbb_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-2000_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-2000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-2000_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10000_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10000_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10000_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10000_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1000','MC',1),

'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph':('ZpA0h_med-2500_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph':('ZpA0h_med-1400_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph':('ZpA0h_med-800_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph':('ZpA0h_med-800_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph':('ZpA0h_med-800_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph':('ZpA0h_med-800_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph':('ZpA0h_med-600_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph':('ZpA0h_med-600_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph':('ZpA0h_med-2500_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph':('ZpA0h_med-2500_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph':('ZpA0h_med-2500_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph':('ZpA0h_med-2500_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph':('ZpA0h_med-2500_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph':('ZpA0h_med-2000_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph':('ZpA0h_med-2000_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-600_13TeV-madgraph':('ZpA0h_med-2000_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph':('ZpA0h_med-2000_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph':('ZpA0h_med-2000_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph':('ZpA0h_med-2000_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph':('ZpA0h_med-1700_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph':('ZpA0h_med-1700_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph':('ZpA0h_med-1700_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph':('ZpA0h_med-1700_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph':('ZpA0h_med-1700_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph':('ZpA0h_med-1400_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph':('ZpA0h_med-1400_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph':('ZpA0h_med-1400_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph':('ZpA0h_med-1400_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph':('ZpA0h_med-1400_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph':('ZpA0h_med-1200_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph':('ZpA0h_med-1200_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph':('ZpA0h_med-1200_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph':('ZpA0h_med-1200_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph':('ZpA0h_med-1200_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph':('ZpA0h_med-1000_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph':('ZpA0h_med-1000_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph':('ZpA0h_med-1000_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph':('ZpA0h_med-1000_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph':('ZpA0h_med-1000_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph':('ZpA0h_med-1000_dm-300','MC',1),


'ST_tch_DM-scalar_LO-100_1-13_TeV':('ST_tch_DM-scalar_LO-100_1-13_TeV','MC',0.293*0.68),
'ST_tch_DM-scalar_LO-300_1-13_TeV':('ST_tch_DM-scalar_LO-300_1-13_TeV','MC',0.03202*0.68),
'ST_tch_DM-scalar_LO-500_1-13_TeV':('ST_tch_DM-scalar_LO-500_1-13_TeV','MC',0.004996*0.68),
'ST_tch_DM-scalar_LO-1000_1-13_TeV':('ST_tch_DM-scalar_LO-1000_1-13_TeV','MC',0.0003009*0.68),

'TT_DM-scalar_LO-300_1-13_TeV':('TT_DM-scalar_LO-300_1-13_TeV','MC',0.03045),
'TT_DM-scalar_LO-500_1-13_TeV':('TT_DM-scalar_LO-500_1-13_TeV','MC',0.004947),
'TT_DM-scalar_LO-1000_1-13_TeV':('TT_DM-scalar_LO-1000_1-13_TeV','MC',0.000736),

'TTbarDMJets_scalar_Mchi-10_Mphi-100' : ('TTbarDMJets_scalar_Mchi-10_Mphi-100','MC',1),
'TTbarDMJets_scalar_Mchi-10_Mphi-10' : ('TTbarDMJets_scalar_Mchi-10_Mphi-10','MC',1),
'TTbarDMJets_scalar_Mchi-10_Mphi-15' : ('TTbarDMJets_scalar_Mchi-10_Mphi-15','MC',1),
'TTbarDMJets_scalar_Mchi-10_Mphi-50' : ('TTbarDMJets_scalar_Mchi-10_Mphi-50','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-10000' : ('TTbarDMJets_scalar_Mchi-1_Mphi-10000','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-100' : ('TTbarDMJets_scalar_Mchi-1_Mphi-100','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-10' : ('TTbarDMJets_scalar_Mchi-1_Mphi-10','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-200' : ('TTbarDMJets_scalar_Mchi-1_Mphi-200','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-20' : ('TTbarDMJets_scalar_Mchi-1_Mphi-20','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-300' : ('TTbarDMJets_scalar_Mchi-1_Mphi-300','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-500' : ('TTbarDMJets_scalar_Mchi-1_Mphi-500','MC',1),
'TTbarDMJets_scalar_Mchi-1_Mphi-50' : ('TTbarDMJets_scalar_Mchi-1_Mphi-50','MC',1),
'TTbarDMJets_scalar_Mchi-50_Mphi-10' : ('TTbarDMJets_scalar_Mchi-50_Mphi-10','MC',1),
'TTbarDMJets_scalar_Mchi-50_Mphi-200' : ('TTbarDMJets_scalar_Mchi-50_Mphi-200','MC',1),
'TTbarDMJets_scalar_Mchi-50_Mphi-300' : ('TTbarDMJets_scalar_Mchi-50_Mphi-300','MC',1),
'TTbarDMJets_scalar_Mchi-50_Mphi-50' : ('TTbarDMJets_scalar_Mchi-50_Mphi-50','MC',1),
'TTbarDMJets_scalar_Mchi-50_Mphi-95' : ('TTbarDMJets_scalar_Mchi-50_Mphi-95','MC',1),


						}