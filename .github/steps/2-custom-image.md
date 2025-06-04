## Step 2: Use a custom image in your codespace

The didn't specify any configuration for the codespace we just created, so GitHub used a default Docker image. While this is very useful, it won't be consistent and it doesn't version lock our runtime environment. Specifying the configuration is important to keep the development environment repeatable.

Let's do that now by providing a specific docker container image.

### How to configure a Codespace?

Configuration is provided directly in the repository via the `.devcontainer/devcontainer.json`. You can even add multiple configurations!

Let's create this file and set a few of the most common settings. For other options like setting configuring VS Code, forwarding ports, and running lifecycle scripts, see the [Codespaces documentation](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces) on GitHub.

### ⌨️ Activity: Customize the codespace

1. Ensure you are in the VS Code Codespace.

1. Use the VS Code file explorer to create the configuration file.

   ```txt
   .devcontainer/devcontainer.json
   ```

   Alternately, run the below terminal command to create it.

   ```bash
   mkdir -p .devcontainer
   touch .devcontainer/devcontainer.json
   ```

1. Open the `.devcontainer/devcontainer.json` file and add the following content.

   ```json
   {
     "name": "Python 3.10",
     "image": "mcr.microsoft.com/vscode/devcontainers/python:3.10"
   }
   ```

   > 💡 **Tip**: The name is optional but it will help identify the configuration when creating a codespace on GitHub, if there are multiple options.

1. After saving, VS Code likely popped up a notification that it detected a configuration change. You can **Accept** that option to rebuild the development container or manually use the Command Palette (`CTRL`+`Shift`+`P`) and run the command `Codespaces: Rebuild Container`. Select the **Rebuild** option. A full build is not necessary.

   <img width="350" alt="rebuild codespace command" src="https://github.com/user-attachments/assets/2b72e1a7-68c4-4c8d-8bf1-5727a520fd0e"/>

1. Wait a few minutes for the Codespace to rebuild and VS Code to reconnect.

1. Expand the lower panel and select the **TERMINAL** tab.

1. Paste the following command to view the installed version of Python.

   ```bash
   python --version
   ```

   > Notice it is different from the previous step.

1. With our new configuration verified, let's commit the changes. Use VS Code's source control tools or the below terminal command.

   ```bash
   git add '.devcontainer/devcontainer.json'
   git commit -m 'feat: Add codespace configuration'
   git push
   ```

1. With our dev container configuration committed, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.
