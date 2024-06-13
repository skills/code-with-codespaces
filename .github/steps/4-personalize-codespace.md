<!--
  <<< Author notes: Step 4 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

## Step 4: Personalize your codespace!

_Nicely done customizing your codespace!_ :partying_face:

When using any development environment, customizing the settings and tools to your preferences and workflows is an important step. GitHub Codespaces offers two main ways of personalizing your codespace: `Settings Sync` with VS Code and `dotfiles`.

`Dotfiles` will be the focus of this activity.

**What are `dotfiles`?** Dotfiles are files and folders on Unix-like systems starting with . that control the configuration of applications and shells on your system. You can store and manage your dotfiles in a repository on GitHub.

Let's see how this works!

### :keyboard: Activity: Enable a `dotfile` for your codespace

1. Start from the landing page of your repository.
1. In the upper-right corner of any page, click your profile photo, and then click **Settings**.
1. In the **Code, planning, and automation** section of the sidebar, click **Codespaces**.
1. Under **Dotfiles**, select **Automatically install dotfiles** so that GitHub Codespaces automatically installs your dotfiles into every new codespace you create.
1. Click **Select repository** and then choose your current skills working repository as the repository from which to install dotfiles.

### :keyboard: Activity: Add a `dotfile` to your repository and run your codespace

1. Start from the landing page of your repository.
1. Click the **Code** button located in the middle of the page.
1. Click the **Codespaces** tab on the box that pops up.
1. Click the **Create codespace on main** button.

   > Wait about **2 minutes** for the codespace to spin itself up.

1. Verify your codespace is running. The browser should contain a VS Code web-based editor and a terminal should be present such as the below:

   ![codespace1](https://user-images.githubusercontent.com/26442605/207355196-71aab43f-35a9-495b-bcfe-bf3773c2f1b3.png)

1. From inside the codespace in the VS Code explorer window, create a new file `setup.sh`.
1. Add the following code inside of the file:

   ```bash
   #!/bin/bash

   sudo apt-get update
   sudo apt-get install sl
   alias sl="/usr/games/sl"
   ```

1. Save the file.
   > **Note**: The file should autosave.
1. Commit the file changes. From the VS Code terminal enter:

   ```shell
   git add setup.sh --chmod=+x
   git commit -m "Adding setup.sh from the codespace!"
   ```

1. Push the changes back to your repository. From the VS Code terminal, enter:

   ```shell
   git push
   ```

1. Switch back to the homepage of your repository and view the `setup.sh` to verify the new code was pushed to your repository.
1. Close the codespace web browser tab.
1. Click the **Create codespace on main** button.

   > Wait about **2 minutes** for the codespace to spin itself up.

1. Verify your codespace is running, as you did previously.
1. Verify the `setup.sh` file is present in your VS Code editor.
1. From the VS Code terminal, type or paste:

   ```shell
   sl
   ```

1. Enjoy the show!
1. Wait about 20 seconds then refresh this page (the one you're following instructions from). [GitHub Actions](https://docs.github.com/en/actions) will automatically update to the next step.
