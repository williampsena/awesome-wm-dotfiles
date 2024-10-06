import subprocess
from string import Template
from ebenezer.core.files import resolve_file_path


def build_shell_command(raw_cmd: str, **kwargs: dict[str, str]) -> str:
    cmd_template = Template(resolve_file_path(raw_cmd))

    return cmd_template.safe_substitute(kwargs).strip()


def run_shell_command(
    raw_cmd: str, **kwargs: dict[str, str]
) -> subprocess.CompletedProcess:
    return subprocess.run(build_shell_command(raw_cmd, **kwargs), shell=True)