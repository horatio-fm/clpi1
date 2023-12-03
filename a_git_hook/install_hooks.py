import os

hook_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".git", "hooks")

orig_hook = "post-commit"

hook_text_list = """
post-commit
post-checkout
post-receive
post-merge
post-update
push-to-checkout
push-to-deploy
"""

if __name__ == '__main__':

    hook_files = list(map(str.strip, hook_text_list.split("\n")[1:-1]))

    file_content = r"""
#!/bin/sh
python -m a_git_hook.update_version
    """.lstrip()

    for file in hook_files:
        with open(os.path.join(hook_dir, file), "w") as fp:
            fp.write(file_content)
