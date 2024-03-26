# vibraniumdome-sdk

## Overview

Client SDK to send LLM interactions to the [Vibranium Dome System](https://github.com/genia-dev/vibraniumdome).

## Getting Started 

### Install the PiPY package

https://pypi.org/project/vibraniumdome-sdk/

```
pip3 install vibraniumdome-sdk
```

### Run sample
To start trace your OpenAI, you need to define `VIBRANIUM_DOME_BASE_URL` environment variable to point Vibranium Dome service, and to set `VIBRANIUM_DOME_API_KEY` from [Vibranium Dome System](https://github.com/genia-dev/vibraniumdome); Run it locally via the basic installation:

```
export VIBRANIUM_DOME_BASE_URL=http://localhost:5001
export VIBRANIUM_DOME_API_KEY=vibranium...
```

Code sample:
```python
import os
import openai

from vibraniumdome_sdk import VibraniumDome

openai.api_key = os.getenv("OPENAI_API_KEY")

VibraniumDome.init(app_name="openai_test_app")

def main():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ],
    temperature=0,
    request_timeout=5,
    user="user-123456",
    headers={"x-session-id": "abcd-1234-cdef"},)

    print(response)


if __name__ == "__main__":
    main()
```


For more details please see [documentation here](https://docs.vibraniumdome.com/quickstart)

## Contributing

We would appreciate your contributions! 🙌🌟💖
👩‍💻➕👨‍💻 Fork repository, make your changes, and submit a pull request!
More details can be found [here](./CONTRIBUTING.md).

## License

MIT License.

See [LICENSE](./LICENSE) to see the full text.

## Contact

Got an idea to improve our project? We'd love to hear it and collaborate with you. Don't hesitate to reach out to us! Just open an [issue](https://github.com/genia-dev/vibraniumdome-sdk/issues) and we will respond to you 🦸‍♀️🦸‍♂️ !
You can see details [here](./.github/ISSUE_TEMPLATE/submit-a-request.md).

## Documentation

https://docs.vibraniumdome.com
