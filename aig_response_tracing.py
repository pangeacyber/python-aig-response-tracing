from __future__ import annotations

import click
from openai import OpenAI
from pangea import PangeaConfig
from pangea.services import AIGuard


@click.command()
@click.option("--model", default="gpt-4o-mini", show_default=True, required=True, help="OpenAI model.")
@click.option(
    "--ai-guard-token",
    envvar="PANGEA_AI_GUARD_TOKEN",
    required=True,
    help="Pangea AI Guard API token. May also be set via the `PANGEA_AI_GUARD_TOKEN` environment variable.",
)
@click.option(
    "--pangea-domain",
    envvar="PANGEA_DOMAIN",
    default="aws.us.pangea.cloud",
    show_default=True,
    required=True,
    help="Pangea API domain. May also be set via the `PANGEA_DOMAIN` environment variable.",
)
@click.option(
    "--openai-api-key",
    envvar="OPENAI_API_KEY",
    required=True,
    help="OpenAI API key. May also be set via the `OPENAI_API_KEY` environment variable.",
)
@click.argument("prompt")
def main(
    *,
    prompt: str,
    model: str,
    ai_guard_token: str,
    pangea_domain: str,
    openai_api_key: str,
) -> None:
    # Generate chat completions.
    completion = OpenAI(api_key=openai_api_key).chat.completions.create(
        messages=[{"role": "user", "content": prompt}], model=model, stream=False
    )

    # Guard the LLM's response.
    config = PangeaConfig(domain=pangea_domain)
    ai_guard = AIGuard(token=ai_guard_token, config=config)

    for x in completion.choices:
        if not x.message.content:
            continue

        guarded = ai_guard.guard_text(x.message.content, recipe="pangea_llm_response_guard")
        assert guarded.result

        click.echo(guarded.result.prompt_text or x.message.content)


if __name__ == "__main__":
    main()
