## Step 2: Add a custom image to your codespace!

_Nice work! :tada: You created your first codespace and pushed code using VS Code!_

You can configure the development container for a repository so that any codespace created for that repository will give you a tailored development environment, complete with all the tools and runtimes you need to work on a specific project.

**What are development containers?** Development containers, or dev containers, are Docker containers that are specifically configured to provide a fully featured development environment. Whenever you work in a codespace, you are using a dev container on a virtual machine.

A dev container file is a JSON file that lets you customize the default image that runs your codespace, VS code settings, run custom code, forward ports and much more!

Let's add a `devcontainer.json` file and add a custom image.

### :keyboard: Activity: Add a .devcontainer.json file to customize your codespace

1. Navigating back to your **Code** tab of your repository, click the **Add file** drop-down button, and then click `Create new file`.
1. Type or paste the following in the empty text field prompt to name your file.

   ```txt
   .devcontainer/devcontainer.json
   ```

1. In the body of the new **.devcontainer/devcontainer.json** file, add the following content:

   ```jsonc
   {
     // Name this configuration
     "name": "Codespace for Skills!",
     // Use the base codespace image
     "image": "mcr.microsoft.com/vscode/devcontainers/universal:latest",

     "remoteUser": "codespace",
     "overrideCommand": false
   }
   ```

1. Click **Commit changes** and then select **Commit changes directly to the `main` branch**.
1. Create a new codespace by navigating back to the **Code** tab of your repository.
1. Click the green **Code** button located in the middle of the page.
1. Click the **Codespaces** tab on the box that pops up.

   > Notice that our recently codespace is listed.

1. Click the `+` sign on the tab to start another one which is now using our configuration file.

   > Wait about **2 minutes** for the codespace to spin itself up.

1. Verify that your new codespace is running, as you did previously.

   Note the image being used is the default image provided for GitHub Codespaces. It includes runtimes and tools for Python, Node.js, Docker, and more. See the full list here: https://aka.ms/ghcs-default-image. Your development team can use any custom image that has the necessary prerequisites installed. For more information, see [codespace image](https://aka.ms/configure-codespace).

1. With our dev container configuration committed, Mona will begin checking your work. Give her a moment to provide feedback and the next learning steps.
