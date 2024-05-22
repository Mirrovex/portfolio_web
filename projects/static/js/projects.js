var tag_filter = "";
var name_filter = "";

function get_projects(page=null) {
    const projectsList = document.querySelector('.project-list');
    const paginationNav = document.querySelector('.pagination-nav');
    projectsList.innerHTML = `
        <div class="d-flex align-items-center loading">
            <strong role="status">Ładowanie...</strong>
            <div class="spinner-border ms-auto" aria-hidden="true"></div>
        </div>`;
    paginationNav.innerHTML = '';

    const url = page ? page : `/projects/list/?name=${name_filter}&tag=${tag_filter}`;
    fetch(url)
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Error connecting to /projects/list/', response.status);
    })
    .then(data => {
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
                            <footer class="tags">Tagi: ${project.tags.join(', ')}</footer>
                        </div>
                    </div>
                </div>`

            projectsList.insertAdjacentHTML('beforeend', card);
        });

        var previous_btn = "";
        if (data.previous) {
            previous_btn = `
            <a class="page-link" href="#" aria-label="Previous" onclick="get_projects('${data.previous}')">
                <span aria-hidden="true">&laquo;</span>
            </a>`;
        } else {
            previous_btn = `
            <a class="page-link disabled" href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>`;
        }
        
        var next_btn = "";
        if (data.next) {
            next_btn = `
            <a class="page-link" href="#" aria-label="Next" onclick="get_projects('${data.next}')">
                <span aria-hidden="true">&raquo;</span>
            </a>`;
        } else {
            next_btn = `
            <a class="page-link disabled" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>`;
        }

        const pagination = `
            <ul class="pagination">
                <li class="page-item">
                    ${previous_btn}
                </li>
                <li class="page-item"><a class="page-link" href="#">#</a></li>
                <li class="page-item">
                    ${next_btn}
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
    const buttonSearch = document.querySelector(".search-button")
    const tags = document.querySelectorAll(".tag")

    get_projects();

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


    nameSearch.addEventListener("input", function filterProject() {
        if (!nameSearch.value) {
            buttonSearch.disabled = true;
            name_filter = nameSearch.value.toLowerCase();
            get_projects();
        } else {
            buttonSearch.disabled = false;
        }
    })
    buttonSearch.addEventListener("click", function filterProject() {
        if (nameSearch.value) {
            name_filter = nameSearch.value.toLowerCase();
            get_projects();
        } else {

        }
    })
})