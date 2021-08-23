from AllNeo_Code.Helper.logger import NeoLogger as NL

Logger = NL.getLogger("Whatever")
Logger.warning("Test Warning")
Logger.error("Test Error")
Logger.exception("Test Exception")
Logger.debug("Test Debug")
Logger.info("Test Infos")