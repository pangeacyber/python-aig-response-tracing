# AI Guard Response Tracing in Python

An example Python app demonstrating how to integrate Pangea's [AI Guard][]
service into a Python app to monitor and sanitize LLM generations.

## Prerequisites

- Python v3.12 or greater.
- pip v24.2 or [uv][] v0.5.11.
- A [Pangea account][Pangea signup] with AI Guard enabled.
- An [OpenAI API key][OpenAI API keys].

## Setup

```shell
git clone https://github.com/pangeacyber/python-aig-response-tracing.git
cd python-aig-response-tracing
```

If using pip:

```shell
python -m venv .venv
source .venv/bin/activate
pip install .
```

Or, if using uv:

```shell
uv sync
source .venv/bin/activate
```

Then the app can be executed with:

```shell
python aig_response_tracing.py "What is MFA?"
```

## Usage

```
Usage: aig_response_tracing.py [OPTIONS] PROMPT

Options:
  --model TEXT           OpenAI model.  [default: gpt-4o-mini; required]
  --ai-guard-token TEXT  Pangea AI Guard API token. May also be set via the
                         `PANGEA_AI_GUARD_TOKEN` environment variable.
                         [required]
  --pangea-domain TEXT   Pangea API domain. May also be set via the
                         `PANGEA_DOMAIN` environment variable.  [default:
                         aws.us.pangea.cloud; required]
  --openai-api-key TEXT  OpenAI API key. May also be set via the
                         `OPENAI_API_KEY` environment variable.  [required]
  --help                 Show this message and exit.
```

## Example

AI Guard will protect against leaking credentials like Pangea API tokens. The
easiest way to demonstrate this would be to have the LLM repeat a given (fake)
API token:

```shell
python aig_response_tracing.py "Echo 'pts_testtesttesttesttesttesttesttest' back."
```

The output after AI Guard is:

```
************************************
```

Audit logs can be viewed at the [Secure Audit Log Viewer][].

[AI Guard]: https://pangea.cloud/docs/ai-guard/
[Secure Audit Log Viewer]: https://console.pangea.cloud/service/audit/logs
[Pangea signup]: https://pangea.cloud/signup
[OpenAI API keys]: https://platform.openai.com/api-keys
[uv]: https://docs.astral.sh/uv/
