from redis import Redis

def main():
    test_redis_connection()

def test_redis_connection():
    try:
        # Create a redis client
        redis_client = Redis(host='localhost', port=6379, db=0)

        # Set a value
        redis_client.set('test_key', 'test_value')

        # Retrieve the value
        value = redis_client.get('test_key')
        
        if value.decode('utf-8') == 'test_value':
            print("Redis connection test passed!")
        else:
            print("Redis connection test failed - Could not retrieve the correct value.")
        
    except Exception as e:
        print(f"Redis connection test failed - Exception: {e}")

if __name__ == "__main__":
    main()
