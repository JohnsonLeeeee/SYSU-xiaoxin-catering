# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename
from ..Model.base import db
from ..libs.web_help import getCurrentDate
import datetime
import  os,stat,uuid
from ..Model.Image import Image


UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/static/upload/',
    'prefix_url':'/static/upload/'
}

class UploadService():
	@staticmethod
	def uploadByFile( file ):
		config_upload = UPLOAD
		resp = { 'code':200,'msg':'操作成功~~','data':{} }
		print(file.filename)
		filename = secure_filename( file.filename )
		print(filename)
		ext = filename.rsplit(".",1)[1]
		if ext not in config_upload['ext']:
			resp['code'] = -1
			resp['msg'] = "不允许的扩展类型文件"
			return resp

		tmp = os.getcwd().replace('\\','/') + "/Backend"
		root_path = tmp + config_upload['prefix_path']
		#不使用getCurrentDate创建目录，为了保证其他写的可以用，这里改掉，服务器上好像对时间不兼容
		file_dir = datetime.datetime.now().strftime("%Y%m%d")
		save_dir = root_path + file_dir
		if not os.path.exists( save_dir ):
			os.mkdir( save_dir )
			os.chmod( save_dir,stat.S_IRWXU | stat.S_IRGRP |  stat.S_IRWXO )

		file_name = str( uuid.uuid4() ).replace("-","") + "." + ext
		file.save( "{0}/{1}".format( save_dir,file_name ) )

		model_image = Image()
		model_image.file_key = file_dir + "/" + file_name
		model_image.create_time = getCurrentDate()
		db.session.add( model_image)
		db.session.commit()

		resp['data'] = {
			'file_key': model_image.file_key
		}
		return resp