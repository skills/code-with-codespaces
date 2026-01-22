## Step 3: Add Features

You can further customize your codespace by adding container feature, VS Code extensions, VS Code settings, host requirements, and much more.

Let's add the GitHub CLI, extensions to run the python program using VS Code, and a custom script to install some packages when first creating the Codespace.

### ⌨️ Activity: Add support for the Python

1. In VS Code, open the Command Palette (`CTRL`+`SHIFT`+`P`) and select the below command.

   ```txt
   Codespaces: Add Dev Container Configuration Files...
   ```

   <img width="350" alt="vs code configure dev container command" src="https://github.com/user-attachments/assets/38265419-47bf-4ac8-a0fd-71ea67e2d6eb" />

1. Select the option `Modify your active configuration...`.

1. In the list of features, search for and select `Python` from `devcontainers`.

   - Instead of the defaults, pick `Configure Options`.
   - Leave `Install Tools` set to `true`.
   - Select Python version: `3.10`

1. Navigate to and open the `.devcontainer/devcontainer.json` file.

1. Verify a new entry similar to the below was added.

   ```json
   "features": {
      "ghcr.io/devcontainers/features/python:1": {
         "installTools": true,
         "version": "3.10"
      }
   },
   ```

### ⌨️ Activity: Add VS Code extensions

1. In the left navigation, select the **Extension** tab.

   <img width="200" alt="vs code extensions tab" src="https://github.com/user-attachments/assets/d7941711-e5a9-4871-83f3-c723c203bc70" />

1. Search for `python` and find entries for `Python` and `Python Debugger`.

   <img width="250" alt="python extensions for vs code" src="https://github.com/user-attachments/assets/b34ef808-2023-41f2-8963-85ba04d5684b" />

1. Right click on each entry and select the `Add to devcontainer.json` option.

   <img width="250" alt="add to devcontainer config button" src="https://github.com/user-attachments/assets/30ada390-c8a7-4175-9d83-dfa17fc83de3" />

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

The Dev Container specification provides multiple locations to run [lifecycle scripts](https://containers.dev/implementors/json_reference/#lifecycle-scripts) to further customize your Codespace. Let's add the `postCreateCommand` which runs one time after initial build (or rebuild).

1. Use the VS Code file explorer to create a script file with the below name.

   ```txt
   .devcontainer/postCreate.sh
   ```

   Alternately, run the below terminal command to create it.

   ```bash
   touch .devcontainer/postCreate.sh
   ```

1. Make the script executable by running the below terminal command.

   ```bash
   chmod +x .devcontainer/postCreate.sh
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

1. Create the `postCreateCommand` entry at the same level (_top level_) as `features`, and `customizations`.

   ```json
   "postCreateCommand": ".devcontainer/postCreate.sh"
   ```

1. With our new configuration finished, let's commit the changes. Use VS Code's source control tools or the below terminal command.

   ```shell
   git add '.devcontainer/devcontainer.json'
   git add '.devcontainer/postCreate.sh'
   git commit -m 'feat: Add features, extensions, and postCreate script'
   git push
   ```

1. Open the VS Code Command Palette (`CTRL`+`Shift`+`P`) and run the `Codespaces: Rebuild Container` command. Select the **Rebuild** option. A full build is not necessary.

   <img width="350" alt="rebuild codespace command" src="https://github.com/user-attachments/assets/2b72e1a7-68c4-4c8d-8bf1-5727a520fd0e"/>

1. Wait a few minutes for the Codespace to rebuild and VS Code to reconnect.

1. With the customizations committed, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.

> [!TIP]
> You can also configure your account to [install dotfiles](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account), allowing you to combine personal configurations with the project's configuration.

### ⌨️ Activity: (optional) Verify our customizations

Now that you've rebuilt the codespace, let's verify the python extension, python version, and custom script were adjusted correctly in the Codespace.

1. Ensure you are in the Codespace.

1. In the left sidebar, click the extensions tab and verify that the Python extensions are installed and enabled.

   <img width="250" alt="python extensions for vs code" src="https://github.com/user-attachments/assets/b34ef808-2023-41f2-8963-85ba04d5684b" />

1. In the left sidebar, select **Run and Debug** tab and then press the **Start Debugging** icon. VS Code will open the lower panel and show the run logs.

   <img width="250" alt="run and debug tab pointing to start button" src="https://github.com/user-attachments/assets/63327b56-b033-4ca1-aa83-93ec076389f5"/>

1. In the lower panel, switch to the **TERMINAL** tab.

1. Run the following command to show the installed version of Python. Notice the others are not installed.

   ```bash
   node --version
   dotnet --version
   python --version
   gh --version
   ```

1. Run the following command to show the steam locomotive animation.

   ```bash
   sl
   ```
