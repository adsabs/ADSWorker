from .models import KeyValue
from adsputils import get_date, ADSCelery




def create_app(app_name='ADSWorker',
               **local_config):
    """Builds and initializes the Celery application."""
    
    app = ADSWorkerCelery(app_name, **local_config)
    return app



class ADSWorkerCelery(ADSCelery):
    
    def hello_world(self, message):            
        return 'Hello world {}'.format(message)
