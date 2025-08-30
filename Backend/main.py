import modal
import os
app = modal.App("moon-tune")
image = (
    modal.Image.debian_slim()
    .apt_install("git")
    . pip_install_from_requirements("requirements.txt")
    .run_commands(["git clone https://github.com/ace-step/ACE-Step.git /tmp/ACE-Step", "cd /tmp/ACE-Step && pip install ."])
    .env({"HF_HOME": "/.cache/huggingface"})
    .add_local_python_source("prompts")
)
music_gen_secrets = modal.Secret.from_name("music-gen-secret")

@app.function(image=image,secrets=[modal.Secret.from_name("music-gen-secret")])
def function_test():
    print("hello")
    print(os.environ["test"])


@app.local_entrypoint()
def main():
    function_test.remote()