from AllNeo_Code.Helper.logger import NeoLogger as NL

Logger = NL.NeoLogger.getLogger("TestLog")
Logger.warning("Test Warning")
Logger.error("Test Error")