#!/usr/bin/env bash

NAME="derpace.designs"

docker build -t "$NAME" "`dirname $0`

docker run -d -p 8000:80 \
	--name "$NAME" \
	--restart unless-stopped \
	--mount type=bind,source=`pwd`/options,target=/usr/src/app/options,readonly \
	--mount type=bind,source=`pwd`/votes.json,target=/usr/src/app/votes.json \
	-t "$NAME" \
