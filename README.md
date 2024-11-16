# KeepAlive Bot

A simple Python-based bot designed to prevent free server hosting platforms from entering sleep mode by periodically sending requests to a specific URI. This ensures consistent server responsiveness and eliminates delays caused by server wake-ups.


## 📝 Motivation

I created this small bot because I host my backend project on a free server. If no requests are sent to the server within 15 minutes, the server goes into sleep mode, causing requests to be delayed by up to a minute. This bot sends a GET request to a specific public URI every 10 minutes, keeping the server awake and preventing these delays.


## 🚀 Features

- Sends periodic GET requests to a specified URI.
- Highly customizable request intervals.
- Easy-to-use, lightweight Docker deployment.
- Securely loads configuration from a `.env` file.


## 🛠️ Requirements

- **Docker**
- (Optional) Python 3.9+ (if running locally)


## 📦 Installation and Usage

Follow these steps to clone and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/CAPELLAX02/keep-alive-bot.git
cd keep-alive-bot
```

### 2. Set Up Environment Variables

Create a `.env` file in the project directory with the following content:

```bash
BACKEND_URL=https://your-backend-url.com
```
Replace `https://your-backend-url.com` with your server's public URI that you want to send a request.

### 3. Build and Run the Docker Container

Build the Docker image:

```bash
sudo docker build -t keepalive-bot .
```

Run the Docker container:

```bash
sudo docker run -d --name keepalive-bot --restart always keepalive-bot
```

### 4. Verify the Logs

Check the container's logs to ensure the bot is working correctly:

```bash
sudo docker logs keepalive-bot -f
```
You should see output like this:

```bash
Bot started. Sending GET request every 10 minutes...
Sending GET request...
GET request successful: {...response.json data...}
```

## ⚙️ Configuration

The bot uses the `schedule` library to send requests at regular intervals. By default, it sends a request every 10 minutes. To change this interval, update the following line in `bot.py`:

```bash
schedule.every(10).minutes.do(fetch_data)
```

For testing purposes , you can set it to a shorter interval:

```bash
schedule.every(5).seconds.do(fetch_data)
```

## 🐞 Troubleshooting

### Logs are empty or not updating:

- Ensure the Docker container is running:

```bash
sudo docker ps
```

- Check the `.env` file for correct configuration.

### GET requests fail:

- Ensure the server URL is correct and reachable by using curl to test it:

```bash
curl https://your-backend-url.com
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make changes, and submit a pull request. Alternatively, you can open an issue for discussion.