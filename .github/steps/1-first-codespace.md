<!--
  <<< Author notes: Step 1 >>>
  Choose 3-5 steps for your course.
  The first step is always the hardest, so pick something easy!
  Link to docs.github.com for further explanations.
  Encourage users to open new tabs for steps!
-->

## Step 1: Create your first codespace and push code

_Welcome to "Develop code using GitHub Codespaces and Visual Studio Code"! :wave:_

**What's the big deal about using a codespace for software development?** A codespace is a development environment that's hosted in the cloud. You can customize your project for GitHub Codespaces by committing configuration files to your repository (also known as configuration-as-code), which creates a repeatable codespace configuration for all users of your project. Each codespace you create is hosted by GitHub in a Docker container that runs on a virtual machine. You can choose the type of machine you want to use depending on the resources you need.

GitHub offers a range of features to help your development team customize a codespace to reach peak configuration and performance needs. For example, you can:

- Create a codespace from your repository.
- Push code from the codespace to your repository.
- Use VS Code to develop code.
- Customize the codespace with custom images.
- Manage the codespace.

To begin developing using GitHub Codespaces, you can create a codespace from a template or from any branch or commit in a repository. When you create a codespace from a template, you can start from a blank template or choose a template suitable for the work you're doing.

### :keyboard: Activity: Start a codespace

**We recommend opening another browser tab to work through the following activities so you can keep these instructions open for reference.**

1. Start from the landing page of your repository.
1. Click the green **Code** button located in the middle of the page.
1. Select the **Codespaces** tab in the box that pops up and then click the **Create codespace on main** button.

   > Wait about 2 minutes for the codespace to spin itself up.
   > **Note**: It's a virtual machine spinning up in the background.

1. Verify your codespace is running. The browser should contain a VS Code web-based editor and a terminal should be present such as the below:
   ![codespace1](https://user-images.githubusercontent.com/26442605/207355196-71aab43f-35a9-495b-bcfe-bf3773c2f1b3.png)

### :keyboard: Activity: Push code to your repository from the codespace

1. From inside the codespace in the VS Code explorer window, select the `index.html` file.
1. Replace the **h1** header with the below:

   ```html
   <h1>Hello from the codespace!</h1>
   ```

1. Save the file.
   > **Note**: The file should autosave.
1. Use the VS Code terminal to commit the file change by entering the following commit message:

   ```shell
   git commit -a -m "Adding hello from the codespace!"
   ```

1. Push the changes back to your repository. From the VS Code terminal, enter:

   ```shell
   git push
   ```

1. Your code has been pushed to your repository!
1. Switch back to the homepage of your repository and view the `index.html` to verify the new code was pushed to your repository.
1. Wait about 20 seconds then refresh this page (the one you're following instructions from). [GitHub Actions](https://docs.github.com/en/actions) will automatically update to the next step.
