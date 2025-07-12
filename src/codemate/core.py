def create_readme(tmp_path):
    readme_path = tmp_path / "README.md"
    with open(readme_path, "w") as file:
        file.write("# Project Title \n")
    return readme_path
