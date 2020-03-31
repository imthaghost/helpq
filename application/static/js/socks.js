var socket = io.connect(
    'http://' + document.domain + ':' + location.port + '/test'
);
$(document).ready(function() {
    socket.on('connect', function() {
        socket.send('Connected');
    });
    socket.on('message', function(msg) {
        var html = `
    <div class="card card-task">
    <div class="progress">
      <div class="progress-bar bg-danger" role="progressbar" style="width: 75%" aria-valuenow="25"
        aria-valuemin="0" aria-valuemax="100"></div>
    </div>
    <div class="card-body">
      <div class="card-title">
        <a href="{{url_for('message.root')}}">
          <h6 id="messages" data-filter-by="text">Lamo</h6>
        </a>
        <span class="text-small">Today</span>
      </div>
      <div class="card-meta">
        <ul class="avatars">

          <li>
            <a href="#" data-toggle="tooltip" title="Kenny">
              <img alt="Kenny Tran" class="avatar" src="static/img/avatar-male-6.jpg" />
            </a>
          </li>

          <li>
            <a href="#" data-toggle="tooltip" title="David">
              <img alt="David Whittaker" class="avatar" src="static/img/avatar-male-4.jpg" />
            </a>
          </li>

          <li>
            <a href="#" data-toggle="tooltip" title="Sally">
              <img alt="Sally Harper" class="avatar" src="static/img/avatar-female-3.jpg" />
            </a>
          </li>

          <li>
            <a href="#" data-toggle="tooltip" title="Kristina">
              <img alt="Kristina Van Der Stroem" class="avatar"
                src="static/img/avatar-female-4.jpg" />
            </a>
          </li>

          <li>
            <a href="#" data-toggle="tooltip" title="Claire">
              <img alt="Claire Connors" class="avatar" src="static/img/avatar-female-1.jpg" />
            </a>
          </li>

          <li>
            <a href="#" data-toggle="tooltip" title="Marcus">
              <img alt="Marcus Simmons" class="avatar" src="static/img/avatar-male-1.jpg" />
            </a>
          </li>

        </ul>
        <!-- <div class="d-flex align-items-center">
          <i class="material-icons">playlist_add_check</i>
          <span>3/4</span>
        </div> -->
        <div class="dropdown card-options">
          <button class="btn-options" type="button" id="task-dropdown-button-1"
            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="material-icons">more_vert</i>
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            <a class="dropdown-item" href="#">Mark as done</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item text-danger" href="#">Archive</a>
          </div>
        </div>
      </div>
    </div>
  </div>
`;
        $('messages').append(msg);
    });
});

function wtf() {
    var formData = new FormData(document.querySelector('#task-add-modal'));
    name = formData.get('task-name');
    description = formData.get('task-description');
    thename = String(name);
    event.preventDefault();
}
