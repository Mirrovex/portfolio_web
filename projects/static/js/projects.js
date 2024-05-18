var tag_filter = "";
var name_filter = "";

function get_projects(page=null) {
    const url = page ? page : `/projects/list/?name=${name_filter}&tag=${tag_filter}`;
    fetch(url)
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Error connecting to /projects/list/', response.status);
    })
    .then(data => {
        const projectsList = document.querySelector('.project-list');
        const paginationNav = document.querySelector('.pagination-nav');
        projectsList.innerHTML = '';
        paginationNav.innerHTML = '';
        data.results.forEach(project => {

            const card = `
                <div class="card-container project" data-name="${project.title.toLowerCase()}">
                     <div class="card">
                        <a href="${project.project_url}">
                            <img src="${project.image_url}" class="card-img-top">
                        </a>
                        <div class="card-body">
                            <h5 class="card-title">
                                <a href="${project.project_url}">${project.title}</a>
                            </h5>
                            <p class="card-text">${project.description}</p>
                            <footer class="tags">Tags: ${project.tags.join(', ')}</footer>
                        </div>
                    </div>
                </div>`

            projectsList.insertAdjacentHTML('beforeend', card);
        });

        const pagination = `
            <ul class="pagination">
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Previous" onclick="get_projects('${data.previous}')">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
                <li class="page-item"><a class="page-link" href="#">#</a></li>
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Next" onclick="get_projects('${data.next}')">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            </ul>`

        paginationNav.insertAdjacentHTML('beforeend', pagination);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}


document.addEventListener("DOMContentLoaded", function () {
    const nameSearch = document.getElementById("name-search")
    const tags = document.querySelectorAll(".tag")

    get_projects();


    function filterProject() {
        const nameQuery = nameSearch.value.toLowerCase();
        /* const projects = document.querySelectorAll(".project")

        projects.forEach((project) => {
            const name = project.getAttribute('data-name');

            if (name.includes(nameQuery)) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        }) */
        name_filter = nameQuery;
        get_projects();
    }

    tags.forEach((tag) => {
        tag.addEventListener("click", function () {
            var selectedTag = "";
            if (this.classList.contains("active")) {
                this.classList.remove("active");
            } else {
                tags.forEach((tag) => {
                    tag.classList.remove("active");
                })
                selectedTag = this.getAttribute("data-tag");
                this.classList.add("active");
            }
            
            tag_filter = selectedTag;
            get_projects();
        })
    })

    nameSearch.addEventListener("input", filterProject)

})