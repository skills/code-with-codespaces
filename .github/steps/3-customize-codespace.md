## Step 3: Add Features

You can further customize your codespace by adding feature layers, VS Code extensions, VS Code settings, host requirements, and much more.

Let's add the GitHub CLI, extensions to run the python program using VS Code, and a custom script to install some packages when first creating the Codespace.

[understanding the codespace lifecycle](https://docs.github.com/en/codespaces/getting-started/understanding-the-codespace-lifecycle)

### ⌨️ Activity: Add the GitHub CLI

1. In VS Code, open the Command Palette (`CTRL`+`SHIFT`+`P`) and run the below command.

   ```txt
   CodeSpaces: Add Dev Container Configuration Files...
   ```

1. Select the option `Modify Active Configuration...`.

1. In the list of features, search for and select `GitHub CLI`. Accept the default options.

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Verify a new entry similar to the below was added.

   ```json
   "features": {
      "ghcr.io/devcontainers/features/github-cli:1": {}
   },
   ```

### ⌨️ Activity: Add VS Code extensions

1. In the left navigation, select the **Extension** tab.

1. Search for `python` and find the below entries.

1. Right click on each entry and select the `Add to devcontainer.json` option.

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Verify a new entry similar to the below was added.

   ```json
   "customizations": {
      "vscode": {
         "extensions": [
            "ms-python.python",
            "ms-python.debugpy"
         ]
      }
   },
   ```

### ⌨️ Activity: Add a custom script

The Dev Container specification provides multiple locations to run [life cycle](https://containers.dev/implementors/json_reference/#lifecycle-scripts) scripts to further customize your Codespace.

Let's add the `postCreateCommand` which runs one time after initial build (or rebuild).

1. Use the VS Code file explorer to create a script file with the below name.

   ```txt
   .devcontainer/postCreate.sh
   ```

   Alternately, run the below terminal command to create it.

   ```bash
   mkdir -p .devcontainer
   echo "" > .devcontainer/postCreate.sh
   ```

1. Open the `.devcontainer/postCreate.sh` file and add the following code, which will install an animation of a steam locomotive.

   ```bash
   #!/bin/bash

   sudo apt-get update
   sudo apt-get install sl
   echo "export PATH=\$PATH:/usr/games" >> ~/.bashrc
   echo "export PATH=\$PATH:/usr/games" >> ~/.zshrc
   ```

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Add the below entry to call the script.

   ```json
   "postCreateCommand": "bash .devcontainer/postCreate.sh"
   ```

1. Run the below command to allow running the script as an executable, and pushing the changes.

   ```shell
   git add '.devcontainer/postCreate.sh' --chmod=+x
   git add '.devcontainer/devcontainer.json'
   git commit -m 'feat: Add postCreate script'
   git push
   ```

1. Open the VS Code Command Palette (`CTRL`+`Shift`+`P`) and run the command `Codespaces: Rebuild Container` with a normal "not full" rebuild.

1. Wait a few minutes for the Codespace to rebuild and VS Code to reconnect.

1. With the customizations committed, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.

> [!TIP]
> You can also configure your account to [install dotfiles](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account), allowing you to combine personal configurations with the project's configuration.

### ⌨️ Activity: (optional) Verify our customizations

Let's verify our python extension, github CLI, and custom script were installed correctly in the Codespace.

1. Ensure you are in VS Code (Codespace).

1. In the left sidebar, click the extensions tab and verify that the Python extensions are installed and enabled.

   <img width="350" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. In the left sidebar, select **Run and Debug** tab and then press the **Start Debugging** icon. VS Code will open the lower panel and switch to the **DEBUG CONSOLE** tab to show the run logs.

   <img alt="run and debug tab pointing to start button" src="" width="350"/>

1. In the lower panel, switch to the **TERMINAL** tab.

1. Run the following command to show the version of the installed GitHub CLI.

   ```bash
   gh --version
   ```

1. Run the following command to show the steam locomotive animation.

   ```bash
   sl
   ```
