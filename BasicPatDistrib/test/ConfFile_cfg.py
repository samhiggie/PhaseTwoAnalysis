import FWCore.ParameterSet.Config as cms

process = cms.Process("MyAna")

process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '91X_upgrade2023_realistic_v1', '')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('MyAna')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) ) 

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    #fileNames = cms.untracked.vstring(
    #    '/store/user/ebouvier/RelValTTbar_14TeV/crab_UPG_CheckPat_miniAOD-prod_RelValTTbar/170612_140401/0000/miniAOD-prod_PAT_1.root',
    #)
    #fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/PhaseIITDRSpring17MiniAOD/GluGluToHHTo2B2G_node_SM_14TeV-madgraph/MINIAODSIM/PU200_91X_upgrade2023_realistic_v3-v1/90000/0036BF3F-5A5A-E711-A084-B499BAAB50A0.root')
    #fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA1000-v1/00000/1E0B06B1-F969-E711-BE53-0CC47A4D75F2.root')
    #300HGG125
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA300-v1/00000/A4E21AF4-FD69-E711-82F5-0CC47A78A45A.root','/store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA300-v1/00000/C005D5C8-FD69-E711-BBBF-0025905B85BE.root')
    #1000HGG125
    #fileNames = cms.untracked.vstring('/store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA1000-v1/00000/C47CAAA4-F969-E711-BD09-0025905A48B2.root','/store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA1000-v1/00000/1E0B06B1-F969-E711-BE53-0CC47A4D75F2.root')
    #3000HGG125
    #fileNames = cms.untracked.vstring('/store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA3000Ultimate-v1/00000/7E0FED53-FC69-E711-898B-0CC47A4C8EE8.root','/store/relval/CMSSW_9_1_1_patch3/RelValH125GGgluonfusion_14/MINIAODSIM/91X_upgrade2023_realistic_v3_D17noPUEA3000Ultimate-v1/00000/D2BB8F51-FC69-E711-9EE9-0025905B85AE.root')
)

process.myana = cms.EDAnalyzer('BasicPatDistrib')
process.load("PhaseTwoAnalysis.BasicPatDistrib.CfiFile_cfi")
process.myana.useDeepCSV = True

process.TFileService = cms.Service("TFileService",
        fileName = cms.string('HGG125RelVal_TEST_300.root') 
)

process.p = cms.Path(process.myana)
