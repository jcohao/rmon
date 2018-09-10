from rmon.models import Server

class TestServer:
    """
        test Server's functions
    """

    def test_save(self, db):
        """
            test Server.save
        """
        # 初始状态下数据库没有保存Redis，所以此时数量为0

        assert Server.query.count() == 0
        server = Server(name='test', host='127.0.0.1')
        server.save()
        # 现在数据库的数量为1
        assert Server.query.count() == 1
        # 且数据库的记录就是之前创建的记录
        assert Server.query.first() == server

    def test_delete(self, db, server):
        """
            test Server.delete
        """

        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0

    def test_ping_success(self, db, server):

        assert server.ping() is True

    def test_ping_failed(self, db):
        # 没有服务器监听在6399上，所以访问将失败
        server = Server(name='test', host='127.0.0.1', port=6399)
        
        try:
            server.ping()
        except RestException as e:
            assert e.code == 400
            assert e.message == 'redis server %s can not connected' % server.host

