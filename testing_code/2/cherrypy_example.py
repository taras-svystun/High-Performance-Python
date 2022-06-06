def lanch_memory_usage_server(port=8080):
    import cherrypy
    import dowser

    cherrypy.tree.mount(dowser.Root())
    cherrypy.config.update({
        'environment': 'embedded',
        'server.socket_port': port
    })

    cherrypy.engine.start()

if __name__ == '__main__':
    lst1 = [i for i in range(10 ** 6) if not i % 7]
    lanch_memory_usage_server()
    lst2 = [i for i in range(10 ** 6) if i % 7]