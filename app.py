import sys
import threading
from datetime import datetime
import flask

# TODO import all apps with sys path append
# TODO use relative paths
sys.path.append("/home/sasha/workspace/iot-dataset/generated-api-clients/smarttv-api-client/")
sys.path.append("/home/sasha/workspace/iot-dataset/generated-api-clients/windwow-api-client/")

# Import all the apps 
import app_smarttv
import windwow

# app_smarttv.smarttv_api_instance.add_channel_username_canal_post(app_smarttv.username, app_smarttv.canal)

# Create an object that will describe current environment values
class general_environment:
    now = 0

    def __init__(self):
        # Var init
        self.now = datetime.now()

        # Proceses init
        self.set_time()
        
    def set_time(self):
        threading.Timer(1.0, self.set_time).start()
        self.now = datetime.now()
    
    def print_env_values(self):
        return "Current Time =" + self.now.strftime("%H:%M:%S")

# Instance of environment values
env = general_environment();

# Starting the Hub Server
app = flask.Flask(__name__)


#windwow.api_instance.settings_setting_name_get("luminosity")

# Route to print all the environment variables 
@app.route("/")
def print_env():
    return env.print_env_values()



# CLI code to generate the api-client for an app.
# java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate -i ../../WindWow/openapi.yaml -g python -o ../windwow-api-client
        
