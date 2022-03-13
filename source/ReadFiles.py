
class ReadFiles():
    CONF_LOGGINS_FILE = "confs/loggins.conf"
    CONF_FORWARDING_FILE = "confs/forwarding.conf"

    def getForwadingConf(self):
        conf_dic = {}
        conf_file = open(self.CONF_FORWARDING_FILE, "r")
        lines = conf_file.readlines()
        for line in lines:
            line_splited = line.split(",")
            conf_dic[line_splited[0]] = line_splited[1]
        return conf_dic

    def getTelegramConf(self):
        conf_dic = {}
        conf_file = open(self.CONF_LOGGINS_FILE, "r")
        lines = conf_file.readlines()
        for line in lines:
            line_splited = line.split("=")
            if line_splited[0] == "telegram_api_id":
                conf_dic["telegram_api_id"] = line_splited[1]
            if line_splited[0] == "telegram_api_hash":
                conf_dic["telegram_api_hash"] = line_splited[1]
        return conf_dic

    def getDiscordConf(self):
        conf_dic = {}
        conf_file = open(self.CONF_LOGGINS_FILE, "r")
        lines = conf_file.readlines()
        for line in lines:
            line_splited = line.split("=")
            if line_splited[0] == "discord_token":
                conf_dic["discord_token"] = line_splited[1]
        return conf_dic

    def getFileContent(self, file):
        message_file = open(file, "r")
        message = ""
        lines = message_file.readlines()
        for line in lines:
            message += line
        message_file.close()
        return message
