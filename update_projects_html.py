import re

def extract_projects_from_readme(readme_path):
    """
    Extract project details from README.md file.
    Each project should follow a specific format:
    ### <Project Title>
    - **Description**: <Description>
    - **Technologies**: <Technologies>
    - **GitHub Link**: <Link>
    """
    projects = []
    with open(readme_path, 'r') as file:
        content = file.read()
    
    # Regular expression to match project details
    project_pattern = re.compile(
        r"###\s+(.*?)\n- \*\*Description\*\*: (.*?)\n- \*\*Technologies\*\*: (.*?)\n- \*\*GitHub Link\*\*: \[(.*?)\]\((.*?)\)",
        re.DOTALL
    )
    
    matches = project_pattern.findall(content)
    for match in matches:
        projects.append({
            "title": match[0],
            "description": match[1],
            "technologies": match[2],
            "link_text": match[3],
            "link_url": match[4]
        })
    return projects

def update_projects_html(html_path, projects):
    """
    Update the projects section in projects.html with new project details.
    """
    with open(html_path, 'r') as file:
        html_content = file.read()
    
    # Template for each project card
    project_card_template = """
    <div class="card overflow-hidden shadow rounded-4 border-0 mb-5">
        <div class="card-body p-0">
            <div class="d-flex align-items-center">
                <div class="p-5">
                    <h2 class="fw-bolder">{title}</h2>
                    <p>{description}</p>
                    <p><strong>Technologies:</strong> {technologies}</p>
                    <a class="btn btn-primary btn-sm" href="{link_url}" target="_blank">{link_text}</a>
                </div>
                <img class="img-fluid" src="https://dummyimage.com/300x400/343a40/6c757d" alt="{title}" />
            </div>
        </div>
    </div>
    """
    
    # Generate the new projects section
    new_projects_section = "\n".join([
        project_card_template.format(**project) for project in projects
    ])
    
    # Replace the existing projects section in the HTML
    new_html_content = re.sub(
        r"<!-- Projects Section Start -->.*<!-- Projects Section End -->",
        f"<!-- Projects Section Start -->\n{new_projects_section}\n<!-- Projects Section End -->",
        html_content,
        flags=re.DOTALL
    )
    
    # Write the updated HTML back to the file
    with open(html_path, 'w') as file:
        file.write(new_html_content)

def main():
    readme_path = "README.md"
    html_path = "projects.html"
    
    print("Extracting projects from README.md...")
    projects = extract_projects_from_readme(readme_path)
    print(f"Found {len(projects)} projects.")
    
    print("Updating projects.html with new projects...")
    update_projects_html(html_path, projects)
    print("projects.html has been updated successfully!")

if __name__ == "__main__":
    main()
