# Twitter Bot for Tech-Related Tweets

This Python script automates the process of tweeting tech-related content using the Twitter API and OpenAI's powerful language models. It periodically generates tweets about JavaScript, HTML, CSS, ReactJS, or NextJS and posts them to your Twitter account.

## Features

- **Automatic Tweeting**: Tweets are generated and posted automatically based on a schedule.
- **OpenAI Integration**: Uses OpenAI's API (`gpt-3.5-turbo`) to generate diverse and relevant tweet content.
- **Customizable**: Easily modify the script to adjust tweet frequency, content generation parameters, and more.

## Setup

### Prerequisites

1. **Python 3.6+**: Ensure Python is installed on your system.
2. **Python Packages**: Install required packages using:

3. **Twitter Developer Account**: Obtain Twitter API credentials (consumer key and secret).
4. **OpenAI API Key**: Obtain an API key from OpenAI to use their language models.

### Installation

1. Clone the repository:
git clone https://github.com/Faizee095/twitter_bot.git
cd repository

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. Install dependencies:

4. Set up configuration:
- Replace `consumer_key`, `consumer_secret`, and `openai.api_key` with your actual API keys in the script.

### Usage

Run the script:
python tweet_bot.py


The bot will start running, generating and posting tech-related tweets based on the specified schedule (every 2 hours by default).

### Configuration

- **Tweet Schedule**: Adjust tweet frequency and timing by modifying `schedule.every(2).hours.do(post_tweet, oauth_session)` in `tweet_bot.py`.
- **Tweet Content**: Customize tweet prompts and generation settings by editing the `generate_tech_tweet()` function in `tweet_bot.py`.

### Contributions

Contributions are welcome! If you find issues or have improvements, feel free to fork the repository and submit pull requests.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

