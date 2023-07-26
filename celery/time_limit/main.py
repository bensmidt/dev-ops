from celery_worker import app, sleeptask

def main(): 
    sleeptask.delay()

if __name__ == '__main__':
    main()