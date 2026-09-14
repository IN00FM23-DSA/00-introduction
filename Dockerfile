# Minimal, disposable sandbox for running a single student's exercise
# code against the canonical tests. See organization/RISKS.md #10/#11.
#
# Deliberately NOT given anything beyond pytest — no network access at
# build *usage* time (the container itself is always run with
# --network none), no extra packages, non-root user, so even a fully
# compromised process inside it has nothing useful to reach.

FROM python:3.12-slim

RUN pip install --no-cache-dir pytest>=8.0 \
    && useradd --no-create-home --uid 65532 --shell /usr/sbin/nologin grader

USER grader
WORKDIR /work

ENTRYPOINT ["python", "-m", "pytest"]
