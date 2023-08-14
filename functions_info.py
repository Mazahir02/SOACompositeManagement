Offline Mode
=============

sca_listDeployedComposites('localhost','7004','<username>','<password>')
sca_undeployComposite('http://localhost:7004','HelloProject','1.0')
sca_undeployComposite('http://localhost:7004','HelloProject','1.0',user='<username>',password='<password>',partition='default')
sca_deployComposite('http://localhost:7004','<mention your path>/sca_HelloProject.jar',user='<username>',password='<password>',partition='default')
sca_stopComposite('localhost','7004','<username>','<password>','HelloProject','1.0',partition='default')
sca_startComposite('localhost','7004','<username>','<password>','HelloProject','1.0',partition='default')
sca_retireComposite('localhost','7004','<username>','<password>','HelloProject','1.0',partition='default')
sca_activateComposite('localhost','7004','<username>','<password>','HelloProject','1.0',partition='default')
sca_exportComposite('http://localhost:7004','all','<mention your path>/sca_HelloProject_rev1.0.jar','HelloProject','1.0',user='<username>',password='<password>',partition='default')

all = All Post Deployment Changes
property = Property related post deployment changes
runtime = Only runtime related changes like metadata
none = Exports only original and excludes Post Deployment Changes

sca_exportUpdates('http://localhost:7004','all','<mention your path>/updates_sca_HelloProject_rev1.0.jar','HelloProject','1.0',user='<username>',password='<password>',partition='default')
sca_importUpdates('http://localhost:7004','<mention your path>/updates_sca_HelloProject_rev1.0.jar','HelloProject','1.0',user='<username>',password='<password>',partition='default')



Online Mode
============
sca_createPartition('New')
sca_deletePartition('New')
sca_stopCompositesInPartition('default')
sca_startCompositesInPartition('default')
sca_retireCompositesInPartition('default')
sca_activateCompositesInPartition('default')
sca_listPartitions()
