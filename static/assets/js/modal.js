document.addEventListener('DOMContentLoaded', function() {
    var courseModal = document.getElementById('courseModal');
    courseModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var courseTitle = button.getAttribute('data-course-title');
        var courseDescription = button.getAttribute('data-course-description');
        var modalTitle = courseModal.querySelector('#modalCourseTitle');
        var modalDescription = courseModal.querySelector('#modalCourseDescription');
        modalTitle.textContent = courseTitle;
        modalDescription.textContent = courseDescription;
    });
});