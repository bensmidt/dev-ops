from tasks import reverse 

def main(): 
    result = reverse.delay('celery example')
    print(result.get(timeout=10))

if __name__ == '__main__':
    main()