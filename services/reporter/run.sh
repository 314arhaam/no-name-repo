docker run \
    --network analytics_network \
    --env-file .env \
    --volume ./data/:data/
    reporter:latest