from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import subprocess
import re
import cgi

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['POST'])
@cross_origin()
def hello():
	if(request.method=='POST'):
		headerdata=request.get_data()
     	filename = re.search("filename=(\S+)", headerdata)
     	print filename.group(0)
     	pattern = r'"([A-Za-z0-9_\./\\-]*)"'
     	m=re.search(pattern,filename.group(0))
     	imagepath=m.group(0).lstrip('"').rstrip('"')
     	a=subprocess.check_output(['bash','-c',"python  /home/prateekvishnu/tensorflow/lib/python2.7/site-packages/tensorflow/models/image/imagenet/classify_image.py --image /var/www/html/data_css/uploads/"+imagepath])
     	return a


if __name__ == "__main__":
    app.run()
