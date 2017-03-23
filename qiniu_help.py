# coding=utf8

from qiniu import Auth, put_file, etag, urlsafe_base64_encode, BucketManager
import utils
import ConfigParser
import requests

access_key = 'Access_Key'
secret_key = 'Secret_Key'
bucket_name = 'easy-pass'
bucket_domain = ''


def init_data():
        global access_key, secret_key, bucket_domain

        cf = ConfigParser.ConfigParser()
        cf.read('./config.ini')
        access_key = cf.get('qiniu', 'app_key')
        secret_key = cf.get('qiniu', 'app_secret')
        bucket_domain = cf.get('qiniu', 'bucket_domain')


def upload_file(file_path, save_name):
        init_data()

        q = Auth(access_key, secret_key)
        token = q.upload_token(bucket_name, save_name, 3600)
        ret, info = put_file(token, save_name, file_path)
        if info.status_code == 200:
                utils.record_log("qiniu upload file_path success")
        else:
                utils.record_log("qiniu upload file_path failed")


def down_file(key, save_name=''):
        init_data()
        q = Auth(access_key, secret_key)
        base_url = 'http://%(domain)s/%(key)s' % {"domain": bucket_domain, "key": key}
        private_url = q.private_download_url(base_url, expires=3600)

        r = requests.get(private_url)
        if r.status_code == 200:
                msg = private_url + " download success"
                utils.record_log(msg)
                if not save_name:
                        save_name = key

                f = open("Shot/" + save_name, 'wb')
                f.write(r.content)
                f.close()
        else:
                msg = private_url + " download failed"
                utils.record_log(msg)


def get_file_stat(key):
        init_data()
        q = Auth(access_key, secret_key)
        bucket = BucketManager(q)
        ret, info = bucket.stat(bucket_name, key)
        return info


def get_list_files():
        init_data()
        q = Auth(access_key, secret_key)
        bucket = BucketManager(q)
        ret, eof, file_infos = bucket.list(bucket_name)
        return ret['items']
