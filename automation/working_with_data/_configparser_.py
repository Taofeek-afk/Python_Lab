import configparser

config_parser = configparser.ConfigParser();

config_parser.read("settings.ini")

port = config_parser.getint("Server", "port", fallback=8080);

back_up = config_parser.has_section("Backup");
compress = config_parser.has_option("Backup", "compress");

print(config_parser.sections())
print(config_parser.options("Backup"))

config_parser["User"] = {
    "name": "Taofeek",
}

with open("config.ini", "w") as file_obj:
    config_parser.write(file_obj)
