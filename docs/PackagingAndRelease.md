# Packaging and Release

We have a guideline for you to package and release your Python projects in JQ.
Please checkout [this document](https://v9kg4fi819.feishu.cn/docx/LNE7dBRWVoCAXPxz8OucfBmennh?from=from_copylink)
before you begins and make sure you follow the guidelines.

The packaging requires the `build` tool which can be installed via `pip`:

```bash
pip install build
```

## Packaging

You can package your project by simply running the following command:

```bash
python3 -m build --wheel
```

> [!IMPORTANT]
> In JQ, we always use the wheel format to package Python project. Please make
> sure the `--wheel` flag is always specified when running the `build` tool.

## Release

### Pre-Release Tests

Once you have packaged your project, it's time for releasing your package to
your downstream users. Before releasing, you need to get in touch with your user
and figure out what environment they use. You need a checklist to be filled by
your user's requirements:

- What is the operating system? What exact version is the operatin system?
- What is the Python version?

Besides, you also need to fill the following checklist according to the
requirements of your project:

- If your project depends on other 3rd-party Python packages, what are the
  versions of those Python packages?
- If your project contains C++ code, and the C++ code depends on 3rd-party
  libraries and Python packages, what are the versions of those libraries and
  Python pacakges?

For `jsda`, the answers might be:

- The users use Ubuntu 22.04 LTS as their operating system.
- The users use CPython 3.10 as their Python environment.
- The `jsda` Python package depends on `pyarrow==8.0.1` and `pandas` to work.
- The C++ code in `jsda` depends on `pyarrow==8.0.1` to work.

Based on the answers you collected, before releasing your project, you need to
package your project under the exact environment described by the above answers.
For `jsda`, this means you have to package your project:

- Under Ubuntu 22.04 LTS;
- With CPython 3.10 installed;
- With `pyarrow==8.0.1` and the latest `pandas` installed.

And then you need to test your package to make sure that your code works under
such an environment. The typical way to do this is run all unit tests and make
sure all tests pass.

If your users work under multiple environments, you need to package and test
your project against each environment individually before releasing.

### Releasing through Artifactory

After you have tested your package under all possible environments, you can now
release your package to your user. In JQ, we release all Python packages through
the Artifactory platform. See [this document](https://v9kg4fi819.feishu.cn/docx/LNE7dBRWVoCAXPxz8OucfBmennh?from=from_copylink)
for how to use this platform and how to upload your package onto this platform.
