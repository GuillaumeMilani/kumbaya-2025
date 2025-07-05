# Chansonnier LaTeX Project

This repository contains the LaTeX source code for the Chansonnier project. The main file to compile is `chansonnier.tex`. This README provides instructions on how to build the project locally and using GitHub Actions.

## Requirements

To build the LaTeX project locally, you need to have the following software installed:

- [TeX Live](https://www.tug.org/texlive/) or [MikTeX](https://miktex.org/)
- [latexmk](https://ctan.org/pkg/latexmk)

## Building Locally

To build the `chansonnier.tex` file into a PDF, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/GuillaumeMilani/kumbaya-2025.git
   cd kumbaya-2025
   ```

2. Use `latexmk` to compile the LaTeX file:
   ```bash
   latexmk -pdf chansonnier.tex
   ```

3. The output PDF file (`chansonnier.pdf`) will be generated in the same directory.

## Building with GitHub Actions

You can also use GitHub Actions to automatically build the PDF whenever you push changes to the repository or create a new tag.

### GitHub Actions Workflow

A sample GitHub Actions workflow is provided in `.github/workflows/build-latex.yml`. This workflow is triggered on new tags.

### How to Trigger the Workflow

To trigger the workflow, you can create a new tag:

1. Push changes to the `main` branch:
   ```bash
   git add .
   git commit -m "Update LaTeX source"
   git push origin main
   ```

2. Create a new tag:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

The GitHub Actions workflow will automatically start, compile the LaTeX file, and upload the resulting PDF as an artifact.

# Generate the indexes
```bash
texlua songidx.lua content/allsongs.sxd content/allsongs.sbx
texlua songidx.lua content/bans.sxd content/bans.sbx
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.