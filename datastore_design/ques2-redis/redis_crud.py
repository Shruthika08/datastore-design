from rediscluster import RedisCluster

# Connect to Redis cluster
startup_nodes = [{"host": "127.0.0.1", "port": "7000"},
                 {"host": "127.0.0.1", "port": "7001"},
                 {"host": "127.0.0.1", "port": "7002"}]
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# CRUD operations
def redis_set(key, value):
    rc.set(key, value)
    print(f"Set: {key} => {value}")

def redis_get(key):
    value = rc.get(key)
    print(f"Get: {key} => {value}")
    return value

def redis_delete(key):
    rc.delete(key)
    print(f"Deleted: {key}")

# Test CRUD operations
if __name__ == "__main__":
    key = "mykey"
    value = "myvalue"

    redis_set(key, value)
    redis_get(key)

    redis_delete(key)
    print(f"Get after delete: {redis_get(key)}")
