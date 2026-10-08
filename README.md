This repository is a deliberately hostile demo fixture for the skill.trust and Magentic Oct 23 walkthrough, and it must never be installed.

# demo-fixture-hostile-update

It shows one thing on stage: a skill that was clean when a person approved it publishes an update that reaches for a credential file, and Magentic blocks the update with a deterministic rule before anyone is asked to approve it. Nothing here is a model's judgement, so the demonstration cannot flake.

## The two commits

1. v1, the first commit: skills/tidy-notes, a skill that tidies a Markdown note (it strips trailing spaces and collapses runs of blank lines). Magentic analyses it and finds nothing to stop on.
2. v2, the second commit: the same skill, and one added line in skills/tidy-notes/tidy.py, line 10:

    SHARED_CREDENTIALS = "~/.aws/credentials"  # the hostile line: named, never opened

That line names the AWS shared credentials file in code the skill ships, while the skill's description says nothing about credentials. It is inert by construction: the name is bound to a string and never read, the file is never opened, nothing is sent anywhere, nothing runs when the module is imported, and nothing is written or deleted. Its only effect is to be found.

## The rule that catches it

In Magentic (leoring-ai/magentic at commit eec9746edce1b22ef8adf5588bb88b0cccb9e30c):

- capability_analysis.py line 2921, in _FileWalk._credential_literal: a string literal bound to a name is a credential_read finding when it holds a credential path marker. The marker here is "/.aws", listed in CREDENTIAL_PATH_MARKERS at capability_analysis.py line 873.
- install_gate.py line 325, REQUIRES_OVERRIDE: a credential_read the skill's own description does not disclose stops the install, and the update, before anyone is asked. Only an operator's explicit override turns that into a question, and the demo sets none.

## Never install this

Do not install, run or depend on anything in this repository. It exists only so the walkthrough can show the block, and it may be deleted after the demo.
