# llm-eval-harness

A Python harness for testing LLM outputs: it sends test cases to Claude, checks the responses, and reports what passed and what failed.

I'm a QA automation engineer, and I'm building this to apply proper testing practice to AI features: deterministic checks, regression detection, LLM-as-judge scoring, and an eval gate in CI.

## Status

Work in progress, built in public.

- [x] Project setup with uv
- [ ] Call the Claude API and get structured output with Pydantic
- [ ] Deterministic checks across a set of test cases
- [ ] pytest suite with concurrent (async) API calls and retries
- [ ] LLM-as-judge for faithfulness, compared against hand-labelled cases
- [ ] Eval gate in GitHub Actions that fails the build if quality drops
- [ ] Red-team tests for prompt injection and system-prompt leaks

## Setup

Requires [uv](https://docs.astral.sh/uv/) and an Anthropic API key.

```bash
git clone https://github.com/<your-username>/llm-eval-harness.git
cd llm-eval-harness
uv sync
```

Set your API key as an environment variable:

```powershell
# Windows (then reopen PowerShell)
setx ANTHROPIC_API_KEY "your-key-here"
```

```bash
# macOS / Linux
export ANTHROPIC_API_KEY="your-key-here"
```

## Usage

_Coming soon._

## Test data

All test cases use made-up data. No real user data is used anywhere in this project.

## What I've learned

A running log of what broke and how I fixed it.

-