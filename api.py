import pymysql
import subprocess

class Data:
    def __init__(self):
        self.file_path = '/Volumes/Data-Resource/R-Book-ZLibrary'
        self.connection = pymysql.connect(
            host='10.10.5.6',
            user=subprocess.getoutput('op read op://private/MySQL-DSM/username'),
            password=subprocess.getoutput('op read op://private/MySQL-DSM/password'),
            database='zlibrary',
        )

    def get(self, id):
        with self.connection.cursor() as cursor:
            sql = 'SELECT * FROM `book` WHERE `id` = %s'
            cursor.execute(sql, (id,))
            sql_result = cursor.fetchone()

        info = {
            'id': sql_result[0],
            'title': sql_result[1],
            'author': sql_result[2],
            'language': sql_result[3],
            'year': sql_result[4],
            'extension': sql_result[5],
            'source': sql_result[6],
        }
        return info




if __name__ == '__main__':
    data = Data()
    print(data.get_sql('z0000001'))