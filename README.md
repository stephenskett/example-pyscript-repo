# Example of a Repository to Manage a Simple Python Script

Here, we have a very simple Python script in the `src` folder ("test-script.py"), with a single package dependency (`NumPy`), which we want a user to be able to run in a Python virtual-environment in a single step. In this case, we can use the "entrypoint.sh" script to achieve this, which will create the required Python-venv, install the dependencies, and run the script with a single shell-command, i.e.

```shell{:copy}
source entrypoint.sh
```

(N.B. This assumes a Linux/MacOS enironment with an `sh`-based terminal. See comments in entry-point script file for ideas on what to do in Windows.)

All your Python code (incl. any bundled function-modules, Jupyter Notebook folders, etc.) would go in `src`.

If you want to have additional 'entry-points' to add different possible actions your user might want to do, you can make a shell-script (similar to "entrypoint.sh") for each.

## Sharing your code

Ideally, your user will already have git version control available on their system. In which case, all they need to do to make their own copy of your code is 'clone' this repository using:

```shell{:copy}
git clone https://github.com/stephenskett/example-pyscript-repo.git {path/to/local/repo/copy}
```

If your user(s) don't have/use Git version-control (or an equivalent of your choice), you can clone the repo yourself, zip it up into a single file, and distribute!
