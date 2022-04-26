var course1 = document.getElementById(1);
var course2 = document.getElementById(2);
var course3 = document.getElementById(3);
var loader = document.getElementById('loader');
loader.style.opacity = 1;

function fill_course(course, data) {
    const title = course.children[0];
    const score = course.children[1].children[0];
    const detail = course.children[2];
    const id = data.id;

    title.innerText = data.title;
    score.innerText = data.score;
    detail.innerText = data.detail;
    course.style.display = "block";
    course.parentElement.href = "show/course?id=" + id;
    course.parentElement.display = "flex";
    // alert(data.id)
}

function get_data() {
    //获取后端搜索的结果
    const res = document.getElementById('res').innerText.replace(/'/g, '"');
    const obj = JSON.parse(res);
    const hits = obj['hits']['hits'];
    var re = [];
    for (let i = 0; i < 3; i++) {
        var h = hits[i];
        if (h === undefined) {

        } else {
            var title = h['_source']['name'];
            var score = h['_score'];
            var description = h['_source']['description'];
            var id = h['_source']['course_id'];
            var data = {"title": title, "score": Math.round(score * 100) / 100, "detail": description, 'id': id};
            re.push(data);
        }
    }
    return re;
}

const data = get_data();
const courses = [course1, course2, course3];
for (let i = 0; i < data.length; i++) {
    var d = data[i];
    var c = courses[i];
    fill_course(c, d);
}

function wipe() {
    var x = document.getElementById('loader')
    x.style.display = 'none';
}

setTimeout(wipe, 3000);