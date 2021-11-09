# GanonymizerV3 App

## OVERVIEW
Smart devices including a camera module are used currently by people all over the world, for example, Smartphones, Go Pro, and so on.  
People can take a photo easily in all situations, and they can upload it to the internet too by using Social Networking Services. (Facebook, Instagram, Twitter, etc.)  
Like that, this culture is used for a city to improve the quality of life for everyone there.   
For example, it can automatically detect illegal garbages, aged wanderers, and accidents on the road by using a vehicle and a drive recorder.  
At this background, we need to think about people's privacy, because an auto-sensing module has a possibility that gets private information of people.  
  
Therefore, we developed the new system "Ganonymizer" to solve the privacy problem.  
Ganonymizer could realize masking private information such as people and cars on a photo.  
The following image is an example by using a ganonymizer. This system can hide private information.
![ganonymize_image](https://user-images.githubusercontent.com/13267712/140917165-b802e2ce-4933-4eaa-a519-0aa9d2cc0e76.png)


## System Architecture
Ganonymizer performs as Web API, so if you want to do this, you run this system on your server.  
Ganonymizer doesn't have the especially requirements to run.
you install this program where you want this system to run, and you execute the "run" command.

The following image is the system architecture.
![ganonymizer_system](https://user-images.githubusercontent.com/13267712/140919796-00331bb2-31ef-4e5e-9561-37485c6843a0.png)


The ganonymizer server returns the processed image after you just post a photo included private information to it.
the Usage shows the next section.

## Usage

host: https://notus.ht.sfc.keio.ac.jp

### GANonymize

`POST /image`

Request

- Authorization
  - Basic Auth (ht standard)

- Headers
  - Content-Type: application/json

- Body (json)
```
{
  "image": "${base64 encoded image}"
}
```

Response (json)
```
{
  "image": "${base64 encoded image}"
}
```

## Development

### Setup
```
$ copy .env.default .env

# set variables in .env
```

### Start service (stg)
```
$ bash ./scripts/run.sh
```

### Start service (prod)

Create ssl with Let's Encrypt.

```
$ bash ./scripts/run.sh prod
```
