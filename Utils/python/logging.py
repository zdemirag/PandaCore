from root import root 
root.gSystem.Load("libPandaCoreUtils.so")

Logger = root.Logger
logger = Logger()

# for backwards-compatibility
def PInfo(*args):
    logger.info(*args)
def PDebug(*args):
    logger.debug(*args)
def PWarning(*args):
    logger.warning(*args)
def PError(*args):
    logger.error(*args)
