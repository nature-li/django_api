from multiprocessing import process

reload = True
threads = 1
preload_app = True


def post_worker_init(worker):
    for child in process.active_children():
        if child.name == 'AsyncLogger':
            process._children.remove(child)


def on_exit(server):
    application = server.app.callable
    application.stop_logger()
