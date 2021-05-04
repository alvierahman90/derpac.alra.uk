# derpac.designs

vote for your favorite [derpac](https://github.com/derpac/) design!

1. Install docker
2. 
    ```bash
    $ git clone https://github.com/alvierahman90/derpac.designs
    $ cd derpac.designs
    $ mkdir options && echo '{}' > votes.json
    $ ./buildandrun.sh
    ```
3. Place images in `options` directory
4. Point [nginx](http://nginx.org/en/docs/install.html) (or equivalent) to docker container.
   nginx example:

   ```
   server {
      root /var/www/html;
      location /designs {
         proxy_pass http://localhost:8000;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwaded-For $remote_addr;
         proxy_set_header X-Forwaded-Proto $scheme;
      }

      listen 80;
   }
   ```

## features

- sad faces
- not using a real database
- doughnuts
