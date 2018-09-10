from rmon.models import Server

class TestServer:
    """
        test Server's functions
    """

    def test_save(self, db):
        """
            test Server.save
        """
        # ��ʼ״̬�����ݿ�û�б���Redis�����Դ�ʱ����Ϊ0

        assert Server.query.count() == 0
        server = Server(name='test', host='127.0.0.1')
        server.save()
        # �������ݿ������Ϊ1
        assert Server.query.count() == 1
        # �����ݿ�ļ�¼����֮ǰ�����ļ�¼
        assert Server.query.first() == server

    def test_delete(self, db, server):
        """
            test Server.delete
        """

        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0
