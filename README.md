# vibraniumdome-sdk

## Overview

Client SDK to send LLM interactions to the [Vibranium Dome System](https://github.com/genia-dev/vibraniumdome).
Supports both the deprecated version of OpenAI Python SDK 0.28.1, and the new version 1.*

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
from openai import OpenAI

from vibraniumdome_sdk import VibraniumDome

VibraniumDome.init(app_name="vibraniumdome_sdk_openai_test_app")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],
    user="user-123456",
    extra_headers={"x-session-id": "abcd-1234-cdef"},
)

print(completion.choices[0].message.content)
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