# import uuid
# import hashlib
#
# def get_unique_str():
#     uuid_str = str(uuid.uuid4()).encode("utf-8")
#     md5 = hashlib.md5()
#     md5.update(uuid_str)
#     return md5.hexdigest()