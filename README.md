# DiscordLLM 🤖💬

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Discord.py](https://img.shields.io/badge/discord-py-blue.svg)](https://discordpy.readthedocs.io/en/stable/)
[![Ollama](https://img.shields.io/badge/Ollama-Powered-orange)](https://ollama.ai/)

DiscordLLM is a powerful Discord bot that brings the capabilities of large language models right to your server, running entirely on your local machine. No cloud services, no API costs – just pure, home-brewed local AI at your fingertips.

## 🌟 Features

- Run state-of-the-art language models locally
- Interact with AI using simple Discord slash commands
- Zero cloud dependency, complete privacy
- Customizable and expandable
- Supports multiple LLM models (currently showcasing Qwen2 1.5B)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Discord Developer Account](https://discord.com/developers/applications)
- [Ollama](https://ollama.ai/) installed on your local machine

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/boshyxd/DiscordLLM.git
   cd DiscordLLM
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Discord bot:
   - Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications)
   - Add a bot to your application
   - Copy the bot token

4. Configure the bot:
   - Replace `YOUR_BOT_TOKEN` with your actual bot token

5. Install and run Ollama:
   ```
   ollama run qwen2:1.5b
   ```

6. Start the bot:
   ```
   python bot.py
   ```

## 💬 Usage

Once the bot is running and invited to your server, you can interact with it using slash commands:

- `/ask <your question>`: Ask the AI a question
- `/help`: Display help information about the bot

Example:
```
/ask What is the capital of France?
```

## 🧠 Supported Models

Currently, DiscordLLM is configured to use the Qwen2 1.5B model, but it can be easily adapted to use any model supported by Ollama. To use a different model:

1. Download the model using Ollama:
   ```
   ollama pull model_name
   ```
2. Update the `default_model` in `config.json`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

Angus Bailey - AngusB@techie.com

Project Link: [https://github.com/boshyxd/DiscordLLM](https://github.com/boshyxd/DiscordLLM)

## 🙏 Acknowledgements

- [Discord.py](https://discordpy.readthedocs.io/)
- [Ollama](https://ollama.ai/)
- [Qwen2](https://huggingface.co/Qwen/Qwen1.5-0.5B)
