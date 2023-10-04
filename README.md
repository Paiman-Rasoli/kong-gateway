## Django app and Kong CDN prototype demo app.

- First of all make sure you have installed django. and also install django_cloudinary_storage
  in this example I use cloudinary as image provider.

- open the project and run the `py manage.py migrate` in order to create migrations. A sqlite file will be create.
- run django app in port `9000` using this command `py manage.py runserver 9000`
- The run `docker-compose up` to run the `Kong` gateway and make sure you have `Kong` image in your docker.
- For uploading image use this proxy url
`http://localhost:8000/media/upload/` and in body of request add `file_path`.
- For retrieving the image use this proxy url `http://localhost:8000/media/retrieve?file_name=nameOfFile`
and in the params give the file name which already has been uploaded.