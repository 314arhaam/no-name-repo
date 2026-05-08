import redis, dotenv, argparse, os

dotenv.load_dotenv()

if __name__ == '__main__':
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=os.getenv("REDIS_PORT", "6379")
    )
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    # Subcommand 1
    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("--dep", required=True)
    start_parser.add_argument("--job", required=True)
    # Subcommand 2
    finish_parser = subparsers.add_parser("finish")
    finish_parser.add_argument("--dep", required=True)
    finish_parser.add_argument("--job", required=True)
    # ping
    ping_parser = subparsers.add_parser("ping")
    # list
    term_parser = subparsers.add_parser("term")
    term_parser.add_argument("--dep", required=True)
    args = parser.parse_args()
    #
    if args.command == "start":
        r.sadd(args.dep, args.job)
    elif args.command == "finish":
        r.srem(args.dep, args.job)
    elif args.command == "ping":
        if r.ping() != True:
            raise ValueError("Redis not ready")
    elif args.command == "term":
        if r.smembers(args.dep) != set():
            raise ValueError("Cannot terminate the infra job")